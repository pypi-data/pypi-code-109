#!/usr/bin/env python3


# pip install --user python-redmine click


import configparser
import glob
import os
import re
import subprocess
import tempfile
from datetime import datetime, timedelta

import click
import git
import unidecode
from redminelib import Redmine
from requests.adapters import HTTPAdapter

MARKER = '# Everything below is ignored\n'


def slugify(title):
    title = unidecode.unidecode(title)
    title = re.sub('[^a-zA-Z]+', '-', title)
    return title


def get_repo():
    return git.Repo(search_parent_directories=True)


def get_config(name, default=Ellipsis):
    repo = get_repo()
    reader = repo.config_reader()
    if not reader.has_section('redmine'):
        raise click.UsageError('Please add a redmine section to your git configuration')
    if default is Ellipsis:
        return reader.get('redmine', name)
    else:
        return reader.get('redmine', name, fallback=default)


def get_main_branch_name():
    # try to get local default
    try:
        return get_config('main')
    except configparser.NoOptionError:
        pass

    # or guess...
    repo = get_repo()
    reader = repo.config_reader()
    default = reader.get('init', 'defaultBranch', fallback='main')
    for branch_name in [default, 'master', 'main']:
        if branch_name in repo.branches:
            return branch_name


def get_redmine_api():
    url = get_config('url')
    key = get_config('key', None)
    username = get_config('username', None)
    password = get_config('password', None)
    if not key and (not username or not password):
        raise click.UsageError('Please add a redmine\'s key or username/password')
    if key:
        kwargs = dict(key=key)
    else:
        kwargs = dict(username=username, password=password)
    redmine = Redmine(url, **kwargs)
    redmine.engine.session.mount('http://', HTTPAdapter(max_retries=3))
    redmine.engine.session.mount('https://', HTTPAdapter(max_retries=3))
    redmine.statuses = {status.name: status for status in redmine.issue_status.all()}
    redmine.nouveau = redmine.statuses['Nouveau']
    redmine.solution = redmine.statuses['Solution proposée']
    redmine.resolu_a_deployer = redmine.statuses['Résolu (à déployer)']
    redmine.developpement = [tr for tr in redmine.tracker.all() if tr.name == 'Développement'][0]
    redmine.rustine = [cf for cf in redmine.custom_field.all() if cf.name == 'Rustine proposée'][0]
    return redmine


def set_redmine(repo, section, option, value):
    with repo.config_writer() as config_writer:
        if not config_writer.has_section(section):
            config_writer.add_section(section)
        config_writer.set(section, option, value)


def set_branch_option(repo, branch, option, value):
    set_redmine(repo, 'branch "%s"' % branch.name, option, value)


def get_issue(issue_number=None):
    if not issue_number:
        issue_number = get_current_issue()
    api = get_redmine_api()
    try:
        issue = api.issue.get(issue_number)
    except Exception:
        raise click.UsageError('Cannot find issue %s' % issue_number)
    return issue


def get_current_issue():
    repo = get_repo()
    branch_name = repo.head.reference.name
    splitted = branch_name.rsplit('/', 1)
    issue_number = splitted[-1].split('-')[0]
    try:
        issue_number = int(issue_number)
    except Exception:
        raise click.UsageError('Cannot find an issue number in current branch name %s' % branch_name)
    return issue_number


def get_current_project():
    project_id = get_config('project', None)
    if not project_id:
        raise click.UsageError('No default project is set')
    api = get_redmine_api()
    return api.project.get(project_id)


def get_patches(number_of_commits=0, ref=None):
    repo = get_repo()
    tempdir = tempfile.mkdtemp()
    if number_of_commits:
        ref = 'HEAD' + '~' * number_of_commits
    elif not ref:
        ref = '@{upstream}'
    repo.git.format_patch(ref, o=tempdir)

    def helper():
        for path in glob.glob(os.path.join(tempdir, '*.patch')):
            yield {
                'path': path,
                'filename': os.path.basename(path),
            }

    return list(helper())


@click.group()
def redmine():
    """Integrate git branch with redmine, you must configure your .config/git/config file
    with a [redmine] section and keys: url, key or username/password.
    """
    pass


@redmine.command()
def main_branch():
    print(get_main_branch_name())


@redmine.command()
def shell():
    import IPython

    api = get_redmine_api()
    repo = get_repo()
    IPython.embed()


@redmine.group()
def issue():
    pass


@redmine.group(invoke_without_command=True)
@click.pass_context
def project(ctx):
    if ctx.invoked_subcommand is None:
        project = get_current_project()
        click.echo('Current project %s' % project)


def apply_attachments(repo, issue):
    if not issue.attachments.total_count:
        return
    print('Currently attached patches')
    attachments = sorted(issue.attachments, key=lambda a: a.id)
    for i, attachment in enumerate(attachments):
        print(i, attachment.created_on, '%6d bytes' % attachment.filesize, attachment.filename)
    while True:
        indexes = click.prompt(
            'Which patch would you like to apply (id separated by spaces) ?', type=str, default=''
        )
        try:
            indexes = indexes.strip()
            if not indexes:
                break
            indexes = list(map(int, indexes.split()))
            if not all(i < len(attachments) for i in indexes):
                raise ValueError('invalid values', indexes)
        except Exception as e:
            print('error:', e)
            continue
        else:
            break
    for index in indexes:
        attachment = attachments[index]
        content = attachment.download().content
        try:
            p = repo.git.execute(['git', 'am', '-3'], istream=subprocess.PIPE, as_process=True)
            p.communicate(content)
        except Exception as e:
            print(e)
            print('Applying patch', index, attachment.filename, 'failed, please fix it.')
            break


@issue.command()
@click.argument('issue_number')
@click.option('--reference', default=None)
def take(issue_number, reference):
    '''Create or switch to a branch to fix an issue'''
    api = get_redmine_api()
    issue = api.issue.get(issue_number, include='attachments')
    repo = get_repo()
    new = False
    for head in repo.heads:
        if '/%s-' % issue_number in head.name:
            branch_name = head.name
            branch = head
            if click.confirm('Do you want to move to branch « %s » ?' % branch_name, default=True):
                break
    else:
        new = True
        default_branch_name = 'wip/%s-%s' % (issue_number, slugify(issue.subject)[:32])
        click.confirm(
            'Do you want to create a branch tracking %s ?'
            % (reference or 'origin/%s' % get_main_branch_name()),
            default=True,
            abort=True,
        )
        branch_name = click.prompt('Branch name', default=default_branch_name)
        branch = repo.create_head(branch_name, commit=reference or 'origin/%s' % get_main_branch_name())
        set_branch_option(repo, branch, 'merge', 'refs/heads/%s' % get_main_branch_name())
        set_branch_option(repo, branch, 'remote', '.')
    if repo.head.reference == branch:
        click.echo('Already on branch %s' % branch_name)
    else:
        branch.checkout()
        click.echo('Moved to branch %s' % branch_name)
    current_user = api.user.get('current')
    if (not hasattr(issue, 'assigned_to') or issue.assigned_to.id != current_user.id) and click.confirm(
        'Do you want to assign the issue to yourself ?',
        default=not hasattr(issue, 'assigned_to') and issue.status == api.nouveau,
    ):
        issue.assigned_to_id = current_user.id
        issue.save()
    if new:
        apply_attachments(repo, issue)


@issue.command()
@click.option('--issue', default=None, type=int)
def apply(issue):
    issue = get_issue(issue)
    repo = get_repo()
    apply_attachments(repo, issue)


@issue.command()
@click.option('--issue', default=None, type=int)
def show(issue):
    issue = get_issue(issue)
    click.echo('URL: %s' % issue.url)
    click.echo('Subject: %s' % issue.subject)
    click.echo('Description: %s' % issue.description)
    click.echo('')
    journals = list(issue.journals)
    if journals:
        click.echo('Last note by %s: ' % journals[-1].user)
        click.echo('%s' % journals[-1].notes)


@issue.command()
@click.option('--issue', default=None, type=int)
@click.option('--no-rebase', default=False, type=bool)
@click.argument('number_of_commits', default=0)
@click.pass_context
def submit(ctx, issue, no_rebase, number_of_commits):
    '''Submit current patch from this issue branch to Redmine'''
    if not no_rebase:
        ctx.invoke(rebase)
    issue = get_issue(issue)
    patches = get_patches(number_of_commits)
    message = '\n\n' + MARKER
    for patch in patches:
        message += '\n%s' % patch['filename']
    message = click.edit(message)
    if message is not None:
        message = message.split(MARKER, 1)[0].rstrip('\n')
    api = get_redmine_api()
    kwargs = {}
    repo = get_repo()
    for commit in list(get_commits(repo, get_main_branch_name()))[:number_of_commits]:
        if ('#%s' % get_current_issue()) not in commit.message:
            click.echo(click.style('Missing commit number in commit message', fg='red'))
            click.echo()
            click.echo(commit.message)
            raise click.Abort()
    if click.confirm('Push -f this branch to origin ?', default=True):
        origin = repo.remote()
        for pi in origin.push(f=True):
            if pi.flags & pi.ERROR:
                click.echo(
                    click.style(
                        'Push from « %s » to « %s » failed.'
                        % (pi.local_ref.name, pi.remote_ref.name, pi.summary),
                        fg='red',
                    )
                )

    if click.confirm('Propose this patch as a solution ?', default=True):
        current_user = api.user.get('current')
        if not hasattr(issue, 'assigned_to'):
            issue.assigned_to_id = current_user.id
            issue.save()
        elif issue.assigned_to.id != current_user.id:
            if click.confirm(
                'Issue is currently assigned to %s, do you want '
                'to assign the issue to yourself ?' % issue.assigned_to.name
            ):
                issue.assigned_to_id = current_user.id
                issue.save()
        kwargs['tracker_id'] = api.developpement.id
        kwargs['status_id'] = api.solution.id
    api.issue.update(
        issue.id,
        notes=message,
        uploads=patches,
        custom_fields=[{'id': api.rustine.id, 'value': '1'}],
        **kwargs,
    )


@issue.command()
@click.argument('issue', default=0, type=int)
def comment(issue):
    '''Add a comment to the current issue or a chosen one'''
    issue = get_issue(issue or None)
    message = click.edit('')
    api = get_redmine_api()
    api.issue.update(issue.id, notes=message)


@issue.command()
@click.option('--reference', default=None)
@click.pass_context
def new(ctx, reference):
    '''Create a new issue in the default project of this repository'''
    project = get_current_project()
    api = get_redmine_api()
    subject_and_description = click.edit('Enter subject on first line\n\nand notes after.')
    if not subject_and_description:
        raise click.UsageError('No subject and description')
    subject_and_description = subject_and_description.splitlines()
    subject, description = subject_and_description[0], '\n'.join(subject_and_description[1:])
    subject = subject.strip()
    if not subject:
        raise click.UsageError('No subject')
    description = description.strip()
    current_user = api.user.get('current')
    click.echo('Project: %s' % project)
    click.echo('Subject: %s' % subject)
    click.echo('Description: %s' % description)
    click.echo('Assigned to: %s' % current_user)
    if click.confirm('Create issue ?', default=True):
        issue = api.issue.create(
            project_id=project.id,
            subject=subject,
            tracker_id=api.developpement.id,
            description=description,
            assigned_to_id=current_user.id,
        )
        click.echo('Created issue %s' % issue.url)
        ctx.invoke(take, issue_number=issue.id, reference=reference)


@issue.command()
@click.argument('issue', type=int)
def link(issue):
    '''Create link with another issue'''
    api = get_redmine_api()
    current_issue = get_issue()
    try:
        target_issue = api.issue.get(issue)
    except Exception:
        raise click.UsageError('Cannot find issue %s' % issue)
    if len(api.issue_relation.filter(issue_id=current_issue.id, issue_to_id=target_issue.id)):
        click.echo(click.style('Already linked.', fg='green'))
        return
    if click.confirm(
        f'Link issue {current_issue.id } - « {current_issue.subject} » to {target_issue.id} - « {target_issue.subject} »',
        default=False,
        abort=True,
    ):
        api.issue_relation.create(
            issue_id=current_issue.id, issue_to_id=target_issue.id, relation_type='relates'
        )
        click.echo(click.style('Linked.', fg='green'))


class MyProgressPrinter(git.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")


def get_commits(repo, ref):
    yield from git.Commit.iter_items(repo, '%s..' % ref)


@redmine.command(name='merge-and-push')
@click.option('--issue', default=None, type=int)
@click.option('--validate-msg/--no-validate-msg', default=True)
@click.argument('target_branch', default=get_main_branch_name())
def merge_and_push(issue, validate_msg, target_branch):
    issue = get_issue(issue or None)
    repo = get_repo()
    origin = repo.remote()

    if repo.head.is_detached:
        raise click.UsageError('Your cannot merge from a detached HEAD.')

    if repo.is_dirty():
        raise click.UsageError('Your cannot merge, your repo is dirty.')

    current_head = repo.head.ref.name

    if current_head == target_branch:
        raise click.UsageError('Your cannot merge on %s as your are already on it.')

    try:
        repo.branches[target_branch]
    except IndexError:
        raise click.UsageError('%r is not a local branch.' % target_branch)

    notes = '<pre>%s</pre>' % repo.git.log('%s..' % target_branch)

    if validate_msg:
        for commit in get_commits(repo, target_branch):
            if ('#%s' % get_current_issue()) not in commit.message:
                click.echo(click.style('Missing commit number in commit message', fg='red'))
                click.echo()
                click.echo(commit.message)
                raise click.Abort()
            if 'rebase' in commit.message:
                click.echo()
                click.echo('Commit %s contains the word "rebase" :' % commit.hexsha[:8])
                click.echo()
                click.echo(''.join(['  ' + line for line in commit.message.splitlines()]))
                click.echo()
                click.confirm('Continue ?', abort=True)

    try:
        click.echo('Checking-out branch « %s » ... ' % target_branch, nl=False)
        repo.branches[target_branch].checkout()
        click.echo(click.style('Done.', fg='green'))
        click.echo(
            'Pull-rebasing from remote « %s » onto branch « %s » ... ' % (origin.name, target_branch),
            nl=False,
        )
        failure = False
        for pi in origin.pull(rebase=True):
            if pi.flags & pi.ERROR:
                failure = True
                click.echo(
                    click.style('Pull-rebase from « %s » failed: %s.' % (pi.ref.name, pi.note), fg='red')
                )
        click.echo(click.style('Done.', fg='green'))
        if failure:
            raise click.ClickException('Pull rebase failed.')
    finally:
        click.echo('Checking-out branch « %s »... ' % current_head, nl=False)
        repo.branches[current_head].checkout()
        click.echo(click.style('Done.', fg='green'))

    try:
        click.echo('Rebasing branch « %s » onto branch « %s » ... ' % (current_head, target_branch), nl=False)
        repo.git.rebase(target_branch)
    except git.GitCommandError as e:
        click.echo(click.style('command %r failed, aborting.' % e.command, fg='red'))
        try:
            repo.git.rebase(abort=True)
        except git.GitCommandError as e:
            click.echo(click.style('rebase abort failed, %s\n%s.' % (e.stdout, e.stderr), fg='red'))
        raise click.Abort()
    click.echo(click.style('Done.', fg='green'))
    try:
        click.echo('Checking-out to %s... ' % target_branch, nl=False)
        repo.branches[target_branch].checkout()
        click.echo(click.style('Done.', fg='green'))
        click.echo('Merging branch « %s » into « %s » ... ' % (current_head, target_branch), nl=False)
        try:
            repo.git.merge(current_head, ff=True)
        except git.GitCommandError as e:
            click.echo(click.style('command %r failed, aborting.' % e.command, fg='red'))
            try:
                repo.git.merge(abort=True)
            except git.GitCommandError as e:
                click.echo(click.style('merge abort failed, %s\n%s.' % (e.stdout, e.stderr), fg='red'))
            raise click.Abort()

        click.echo(click.style('Done.', fg='green'))
        try:
            origin.refs[current_head]
        except IndexError:
            pass
        else:
            if click.confirm(
                'Do you want to delete feature branch « %s » on remote « %s » ?'
                % (current_head, origin.name),
                default=True,
            ):
                for pi in origin.push(refspec=':%s' % current_head):
                    if pi.flags & pi.ERROR:
                        click.echo(
                            click.style(
                                'Push from « %s » to « %s » failed.'
                                % (pi.local_ref.name, pi.remote_ref.name, pi.summary),
                                fg='red',
                            )
                        )
        if click.confirm(
            'Do you want to push « %s » on remote « %s » ?' % (target_branch, repo.remote().name),
            default=True,
        ):
            for pi in origin.push():
                if pi.flags & pi.ERROR:
                    click.echo(
                        click.style(
                            'Push from « %s » to « %s » failed: %s.'
                            % (pi.local_ref.name, pi.remote_ref.name, pi.summary),
                            fg='red',
                        )
                    )
        if click.confirm('Do you want to delete feature branch « %s » ?' % current_head, default=True):
            repo.delete_head(repo.branches[current_head])
        else:
            repo.branches[current_head].checkout()
    except Exception:
        click.echo(click.style('\nFailure going back to branch « %s ».' % current_head, fg='red'))
        repo.branches[current_head].checkout()
        raise
    if click.confirm('Set issue status to solved ?', default=True):
        api = get_redmine_api()
        current_user = api.user.get('current')
        kwargs = {}
        if not hasattr(issue, 'assigned_to'):
            issue.assigned_to_id = current_user.id
            issue.save()
        elif issue.assigned_to.id != current_user.id:
            if click.confirm(
                'Issue is currently assigned to %s, do you want '
                'to assign the issue to yourself ?' % issue.assigned_to.name
            ):
                issue.assigned_to_id = current_user.id
                issue.save()
        kwargs['status_id'] = api.resolu_a_deployer.id
        api.issue.update(issue.id, notes=notes, **kwargs)


@redmine.command(name='rebase')
@click.argument('target_branch', default=get_main_branch_name())
def rebase(target_branch):
    repo = get_repo()
    origin = repo.remote()

    if repo.head.is_detached:
        raise click.UsageError('Your cannot rebase from a detached HEAD.')

    if repo.is_dirty():
        raise click.UsageError('Your cannot rebase, your repo is dirty.')

    current_head = repo.head.ref.name

    if current_head == target_branch:
        raise click.UsageError('Your cannot rebase on « %s » as your are already on it.' % target_branch)

    try:
        repo.branches[target_branch]
    except IndexError:
        raise click.UsageError('%r is not a local branch.' % target_branch)

    try:
        click.echo('Checking-out branch « %s » ... ' % target_branch, nl=False)
        repo.branches[target_branch].checkout()
        click.echo(click.style('Done.', fg='green'))
        click.echo(
            'Pull-rebasing from remote « %s » onto branch « %s » ... ' % (origin.name, target_branch),
            nl=False,
        )
        failure = False
        for pi in origin.pull(rebase=True):
            if pi.flags & pi.ERROR:
                failure = True
                click.echo(
                    click.style('Pull-rebase from « %s » failed: %s.' % (pi.ref.name, pi.note), fg='red')
                )
        click.echo(click.style('Done.', fg='green'))
        if failure:
            raise click.ClickException('Pull rebase failed.')
    finally:
        click.echo('Checking-out branch « %s »... ' % current_head, nl=False)
        repo.branches[current_head].checkout()
        click.echo(click.style('Done.', fg='green'))

    try:
        click.echo('Rebasing branch « %s » onto branch « %s » ... ' % (current_head, target_branch), nl=False)
        repo.git.rebase(target_branch)
    except git.GitCommandError as e:
        click.echo(click.style('command %r failed, aborting.' % e.command, fg='red'))
        try:
            repo.git.rebase(abort=True)
        except git.GitCommandError as e:
            click.echo(click.style('rebase abort failed, %s\n%s.' % (e.stdout, e.stderr), fg='red'))
        raise click.Abort()
    click.echo(click.style('Done.', fg='green'))


@issue.command(name='open')
@click.option('--issue', default=None, type=int)
def _open(issue):
    issue = get_issue(issue)
    subprocess.call(['xdg-open', issue.url])


@project.command()
@click.argument('project_id')
def set(project_id):
    '''Set default redmine project for this git repository'''
    api = get_redmine_api()
    try:
        api.project.get(project_id)
    except Exception:
        raise click.UsageError('Project %s is unknown' % project_id)
    repo = get_repo()
    config_writer = repo.config_writer()
    if not config_writer.has_section('redmine'):
        config_writer.add_section('redmine')
    config_writer.set('redmine', 'project', project_id)
    config_writer.write()


@redmine.command()
@click.option('--local/--no-local', default=False)
def clean(local):
    repo = get_repo()
    repo.git.fetch(prune=True)
    api = get_redmine_api()
    api.engine.chunk = 10
    issue_re = re.compile(r'wip/([0-9]+)')
    issues_to_branch = {}

    origin = repo.remote()
    for ref in origin.refs:
        m = issue_re.search(ref.name)
        if not m:
            continue
        issues_to_branch[m.group(1)] = ref.name.lstrip('origin/')
    if not issues_to_branch:
        return

    issues_to_delete = []
    temp_issues_to_branch = list(issues_to_branch)
    while temp_issues_to_branch:
        issue_ids = ','.join(temp_issues_to_branch[:30])
        issues = api.issue.filter(issue_id=issue_ids, status_id='closed', include=['journals'])
        for issue in issues:
            journals = list(issue.journals)
            last_journal = len(journals) and journals[len(journals) - 1]
            if last_journal.created_on < datetime.now() - timedelta(days=21):
                issues_to_delete.append((issue.id, issue.subject))
        temp_issues_to_branch = temp_issues_to_branch[30:]

    if not local:
        for _id, _subject in issues_to_delete:
            print('%5s | %60s | %s' % (_id, issues_to_branch[str(_id)][:60], _subject))
        if issues_to_delete and click.confirm('Remove theses remote branches ?'):
            for _id, _subject in issues_to_delete:
                ref = issues_to_branch[str(_id)]
                click.echo('Deleting origin/%s... ' % ref, nl=False)
                try:
                    origin.push(refspec=':%s' % ref)
                except git.GitCommandError as e:
                    click.echo(click.style('Failed(%s).' % e, fg='red'))
                else:
                    click.echo(click.style('Done.', fg='green'))

    issues_to_branch = {}
    for ref in repo.branches:
        m = issue_re.search(ref.name)
        if not m:
            continue
        issues_to_branch[m.group(1)] = ref.name
    issues = api.issue.filter(issue_id=','.join(issues_to_branch), status_id='closed')
    issues_to_delete = list(issues.values_list('id', 'subject'))
    for _id, _subject in issues_to_delete:
        print('%5s | %60s | %s' % (_id, issues_to_branch[str(_id)][:60], _subject))
    if issues_to_delete and click.confirm('Remove theses branches ?'):
        for _id, _subject in issues_to_delete:
            ref = issues_to_branch[str(_id)]
            click.echo('Deleting %s... ' % ref, nl=False)
            repo.delete_head(ref, force=True)
            click.echo(click.style('Done.', fg='green'))


if __name__ == '__main__':
    redmine()
