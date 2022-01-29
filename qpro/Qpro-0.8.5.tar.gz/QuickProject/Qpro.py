from . import *
from . import _ask
from QuickProject import __sub_path
from rich.prompt import Prompt


templateProjectUrls_not_CN = {
    'c': ['https://github.com/Rhythmicc/QproCTemplate.git', 'QproCTemplate'],
    'cpp': ['https://github.com/Rhythmicc/QproCppTemplate.git', 'QproCppTemplate'],
    'java': ['https://github.com/Rhythmicc/QproJavaTemplate.git', 'QproJavaTemplate'],
    'python3': ['https://github.com/Rhythmicc/QproPython3Template.git', 'QproPython3Template'],
    'python': ['https://github.com/Rhythmicc/QproPythonTemplate.git', 'QproPythonTemplate']
}

templateProjectUrls_is_CN = {
    'c': ['https://gitee.com/RhythmLian/QproCTemplate.git', 'QproCTemplate'],
    'cpp': ['https://gitee.com/RhythmLian/QproCppTemplate.git', 'QproCppTemplate'],
    'java': ['https://gitee.com/RhythmLian/QproJavaTemplate.git', 'QproJavaTemplate'],
    'python3': ['https://gitee.com/RhythmLian/QproPython3Template.git', 'QproPython3Template'],
    'python': ['https://gitee.com/RhythmLian/QproPythonTemplate.git', 'QproPythonTemplate']
}


def __format_json(info, path: str):
    """
    回写配置表

    :param info: 列表格式或字典格式
    :param path: 路径
    :return:
    """
    import json
    with open(path, 'w') as f:
        if isinstance(info, list):
            config = {}
            for line in info:
                config[line[0]] = line[1] if line[0] != 'server_target' else line[1:]
            json.dump(config, f, indent=1)
        elif isinstance(info, dict):
            json.dump(info, f, indent=1)


def __findAndReplace(dirPath, fo, to):
    """
    替换模板项目中的指定字段

    :param dirPath: 项目路径
    :param fo: 识别
    :param to: 替换
    :return:
    """
    for rt, son_dir, son_files in os.walk(dirPath):
        for file in son_files:
            with open(rt + dir_char + file, 'r') as f:
                ct = f.read()
            with open(rt + dir_char + file, 'w') as f:
                f.write(ct.replace(fo, to))


def remove(path):
    """
    删除文件或目录

    :param path: 路径
    :return:
    """
    import shutil
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def scp_init(server_target: list):
    if server_target:
        server, target, port = get_server_target(server_target)
        user, ip = server.split('@') if '@' in server else [None, server]
        st = SshProtocol.post_all_in_folder(user, ip, target, port, '')
        if st:
            QproDefaultConsole.print(QproErrorString, "upload project failed!" if user_lang != 'zh' else '上传项目失败!')


def _external_create(project_name: str, key: str = ''):
    from git import Repo
    if key:
        if key in ['empty', '空项目']:
            __format_json([
                ['compile_tool', ''],
                ['compile_filename', ''],
                ['executable_filename', ''],
                ['input_file', ''],
                ['template_root', ''],
                ['server_target', '', '']
            ], project_name + dir_char + configure_name)
            return

        with QproDefaultConsole.status(('Cloning Qpro {} Template to {}' if user_lang != 'zh' else '正在克隆Qpro {} 模板为 {}').format(key, project_name)):
            try:
                from QuickStart_Rhy.API.alapi import ip_info
                is_CN = ip_info('')['ad_info']['nation'].startswith('中国')
            except:
                is_CN = False
            templateProjectUrls = templateProjectUrls_is_CN if is_CN else templateProjectUrls_not_CN
            Repo.clone_from(templateProjectUrls[key][0], project_name)
    else:
        templateProjectUrls = _ask({
            'type': 'input',
            'message': 'GIT ' + ('URL' if user_lang != 'zh' else '链接') + ':',
            'name': 'url'
        })
        with QproDefaultConsole.status(('Cloning External Template to {}' if user_lang != 'zh' else '正在克隆Qpro 外部模板为 {}').format(project_name)):
            Repo.clone_from(templateProjectUrls, project_name)
    os.chdir(project_name)
    try:
        remove('.git')
    except Exception as e:
        QproDefaultConsole.print(QproErrorString, repr(e))
    if key:
        __findAndReplace(os.getcwd(), templateProjectUrls[key][1], project_name)


def create():
    try:
        project_name = sys.argv[sys.argv.index('-c') + 1]
    except IndexError:
        return QproDefaultConsole.print(QproWarnString, 'usage: Qpro -c <project>' if user_lang != 'zh' else '使用: Qpro -c <项目>')
    else:
        if os.path.exists(project_name) and os.path.isdir(project_name):
            return QproDefaultConsole.print(QproErrorString, '"%s" is exist!' % (os.path.abspath(project_name)))

        lang = _ask({
            'type': 'list',
            'name': 'lang_name',
            'message': 'Choose Lang | 选择语言:',
            'choices': [
                'c', 'cpp', 'java', 'python3', 'python',
                'empty' if user_lang != 'zh' else '空项目',
                'external' if user_lang != 'zh' else '外部项目'
            ]
        })

        if lang in ['external', '外部项目']:
            _external_create(project_name)
        else:
            _external_create(project_name, lang)

        server_target = Prompt.ask(
            'input user@ip:dir_path if you need scp' if user_lang != 'zh' else '输入 用户@IP:路径 如果你打算使用SSH'
        ).strip().replace(dir_char, '/')
        if server_target and not server_target.endswith('/'):
            if not server_target.endswith(':'):
                server_target += '/'
            else:
                server_target += '~/'
        config = get_config()
        config['server_target'] = [server_target, '22']
        __format_json(config, configure_name)

        if _ask({
            'type': 'confirm',
            'message': 'Open it with VS Code?' if user_lang != 'zh' else '是否现在使用VS Code打开?',
            'name': 'open',
            'default': True
        }):
            if sys.platform == 'darwin':
                os.system(f'open -a "Visual Studio Code" .')
            else:
                os.system('code .')


def scp():
    try:
        path = sys.argv[sys.argv.index('-scp') + 1]
        sub_path = __sub_path(path)
    except IndexError:
        return QproDefaultConsole.print(
            QproWarnString, 'usage: Qpro -scp <path>' if user_lang != 'zh' else '使用: Qpro -scp <路径>'
        )
    else:
        if not sub_path:
            return \
                QproDefaultConsole.print(
                    QproErrorString,
                    (f"{path} is not in this Qpro project!" if os.path.exists(path) else f'No such file named: {path}')
                    if user_lang != 'zh' else
                    (f"{path} 不在当前 Qpro 项目中!" if os.path.exists(path) else f'该路径不存在: {path}')
                )
        server, target, port = get_server_target()
        user, ip = server.split('@') if '@' in server else [None, server]
        if os.path.isdir(path):
            SshProtocol.post_folder(user, ip, target, port, path, sub_path)
        else:
            SshProtocol.post_file(user, ip, target, port, path, sub_path)


def get():
    try:
        path = sys.argv[sys.argv.index('-get') + 1]
        sub_path = __sub_path(path, isExist=False)
    except IndexError:
        return QproDefaultConsole.print(
            QproWarnString, 'usage: Qpro -get <path>' if user_lang != 'zh' else '使用: Qpro -get <路径>'
        )
    else:
        if not sub_path:
            return QproDefaultConsole.print(QproErrorString, f"{path} is not in this Qpro project!" if user_lang != 'zh' else f'{path} 不在当前 Qpro 项目中!')
        server, target, port = get_server_target()
        user, ip = server.split('@') if '@' in server else [None, server]
        SshProtocol.get_file_or_folder(user, ip, target, port, sub_path, path)


def adjust():
    config = get_config()
    if not config:
        return QproDefaultConsole.print(QproErrorString, 'Get Qpro config failed!')

    import tkinter as tk
    win = tk.Tk()
    win.title('Qpro项目调整器')
    key_to_name = {
        'compile_tool': '编译指令:' if user_lang == 'zh' else 'Compile',
        'compile_filename': '源程序:' if user_lang == 'zh' else 'Source',
        'executable_filename': '运行指令:' if user_lang == 'zh' else 'Run',
        'input_file': '输入文件:' if user_lang == 'zh' else 'Input',
        'template_root': '模板目录:' if user_lang == 'zh' else 'Template',
        'server_target': '远程映射:' if user_lang == 'zh' else 'Server'
    }
    if 'enable_complete' in config:
        key_to_name.update({'enable_complete': '自动补全:' if user_lang == 'zh' else 'Complete'})
    all_dt = {}
    for i, v in enumerate(config):
        tk.Label(win, text='%12s' % key_to_name[v]).grid(row=i, column=0)
        if v == 'server_target':
            stringvar1 = tk.Variable()
            stringvar1.set(config[v][0])
            stringvar2 = tk.Variable()
            stringvar2.set(config[v][1])
            tk.Entry(win, textvariable=stringvar1, width=20).grid(row=i, column=1)
            tk.Entry(win, textvariable=stringvar2, width=19).grid(row=i, column=2)
            all_dt[v] = [stringvar1, stringvar2]
        else:
            stringvar1 = tk.Variable()
            stringvar1.set(config[v])
            tk.Entry(win, textvariable=stringvar1, width=40).grid(row=i, column=1, columnspan=2)
            all_dt[v] = stringvar1

    def deal_config():
        for dt in all_dt:
            if dt == 'server_target':
                config[dt] = [all_dt[dt][0].get(), all_dt[dt][1].get()]
                if config[dt][0]:
                    try:
                        if ':' in config[dt][0]:
                            if config[dt][0].count(':') not in [1, 8]:
                                raise Exception(
                                    '%s: not a legal server target' % config[dt][0]
                                    if user_lang != 'zh' else
                                    '%s: 不是合法的远程映射' % config[dt][0]
                                )
                            if not config[dt][0].endswith(dir_char) and config[dt][0].endswith(':'):
                                config[dt][0] += '/'
                        else:
                            raise Exception(
                                '%s: not a legal server target' % config[dt][0]
                                if user_lang != 'zh' else
                                '%s: 不是合法的远程映射' % config[dt][0]
                            )
                    except Exception as e:
                        QproDefaultConsole.print(QproErrorString, repr(e))
                        QproDefaultConsole.print(
                            QproWarnString, 'Legal server target:\n'
                                            '        addr1: <username>@<ipv4 | ipv6 | domain>:</path/to/project/>\n'
                                            '        addr2: <configured name>:</path/to/project/>\n'
                                            '        port : <ssh port>, default 22') \
                        if user_lang != 'zh' else \
                        QproDefaultConsole.print(
                            QproWarnString, '合法的远程映射:\n'
                                            '        地址1: <用户名>@<ipv4 | ipv6 | 域名>:</项目/路径/>\n'
                                            '        地址2: <SSH配置表中项目>:</项目/路径/>\n'
                                            '        端口 : <SSH 端口>, 默认 22')
            else:
                config[dt] = all_dt[dt].get()
        if not config['template_root'].endswith(dir_char):
            config['template_root'] += dir_char
        if 'enable_complete' in config:
            config['enable_complete'] = True if config['enable_complete'] not in ['0', 'false', 'False'] else False
        win.destroy()
        __format_json(config, project_configure_path)

    tk.Button(win, text='确认', command=deal_config, width=10).grid(row=7 if 'enable_complete' in config else 6, column=0, columnspan=3)
    tk.mainloop()


def pro_init():
    work_project = ''
    while not work_project:
        work_project = Prompt.ask('You need to set project name' if user_lang != 'zh' else '请设置项目名').strip()
    lang_tool_exe = {
        'c': ['gcc -std=c11 --source_file-- -o --execute--', '', '.c'],
        'cpp': ['g++ -std=c++11 --source_file-- -o --execute--', '', '.cpp'],
        'java': ['javac -d dist --source_file--', 'java -classpath dist ', '.java'],
        'python3': ['', 'python3 ', '.py'],
        'python': ['', 'python ', '.py'],
        'empty': ['', '', '']
    }

    lang_name = _ask({
        'type': 'list',
        'name': 'lang_name',
        'message': 'Choose Lang | 选择语言:',
        'choices': lang_tool_exe.keys()
    })

    lang = lang_tool_exe[lang_name]
    source_file = ''
    if lang_name != 'empty':
        source_file = ('main' + lang[-1]) if lang[0] != 'javac' else work_project + lang[-1]
        while not os.path.exists(source_file):
            source_file = Prompt.ask((
                            'Not found "%s", set compile_filename'
                            if user_lang != 'zh' else
                            '没有找到 "%s", 请设置源文件'
                            ) % source_file).strip()
    server_target = Prompt.ask(
        'input user@ip:dir_path if you need scp' if user_lang != 'zh' else '输入 用户@IP:路径 如果你打算使用SSH'
    ).strip().replace(dir_char, '/')
    if ':' in server_target and not server_target.endswith('/'):
        if not server_target.endswith(':'):
            server_target += '/'
        else:
            server_target += '~/'
    if lang[0] != 'javac':
        execute = lang[1] + 'dist' + dir_char + work_project if lang[0] else lang[1] + source_file
    elif lang_name != 'empty':
        work_project = source_file.split(dir_char)[-1].split('.')[0]
        execute = lang[1] + work_project
    else:
        execute = ''
    if (not os.path.exists('dist') or not os.path.isdir('dist')) and lang_name != 'empty':
        os.mkdir('dist')
    info = [
        ['compile_tool', lang[0].replace('--source_file--', source_file).replace('--execute--', execute)],
        ['compile_filename', source_file],
        ['executable_filename', execute],
        ['input_file', 'dist' + dir_char + 'input.txt' if lang_name != 'empty' else ''],
        ['template_root', 'template' + dir_char if lang_name != 'empty' else ''],
        ['server_target', server_target, '22' if server_target else '']
    ]
    __format_json(info, configure_name)
    if lang_name and lang_name == 'empty':
        scp_init(info[-1][1:] if server_target else None)
        return
    with open(info[3][-1], 'w') as f:
        f.write('edit this file to make input' if user_lang != 'zh' else '编辑此文件作为程序输入')
    if not os.path.exists('template') or not os.path.isdir('template'):
        os.mkdir('template')
    try:
        with open(info[1][-1], 'r') as f:
            main_cont = f.read()
        with open('template' + dir_char + 'main', 'w') as f:
            f.write(main_cont)
    except Exception as e:
        QproDefaultConsole.print(
            QproErrorString, "make backup failed with error: %s, you need backup code by yourself!" % e)
    scp_init(info[-1][1:] if server_target else None)


def ssh():
    server, target, port = get_server_target()
    os.system("ssh -p %s -t %s 'cd %s ; exec $SHELL -l'" % (port, server, target))


def delete_all():
    config = get_config()
    if ':' in config['server_target'][0]:
        server, target, port = get_server_target()
        user, ip = server.split('@') if '@' in server else [None, server]
        st = SshProtocol.command(user, ip, target, port, 'rm -rf .')
        # st = os.system("ssh -p %s %s 'rm -rf %s'" % (port, server, target))
        if st:
            return
    remove(os.getcwd())


def delete():
    try:
        path = os.path.abspath(sys.argv[sys.argv.index('-del') + 1])
        sub_path = __sub_path(path)
    except IndexError:
        return QproDefaultConsole.print(
            QproWarnString, 'usage: Qpro -del <path>' if user_lang != 'zh' else '使用: Qpro -del <路径>'
        )
    else:
        if not sub_path:
            return \
                QproDefaultConsole.print(
                    QproErrorString,
                    (f"{path} is not in this Qpro project!" if os.path.exists(path) else f'No such file named: {path}')
                    if user_lang != 'zh' else
                    (f"{path} 不在当前 Qpro 项目中!" if os.path.exists(path) else f'该路径不存在: {path}')
                )
        config = get_config()
        if ':' in config['server_target'][0]:
            server, target, port = get_server_target()
            user, ip = server.split('@') if '@' in server else [None, server]
            st = SshProtocol.command(user, ip, target, port, f'rm -rf {sub_path}')
            # st = os.system("ssh -p %s %s 'rm -rf %s'" % (port, server, target + sub_path))
            if st:
                return
        remove(path)


def tele_ls():
    try:
        path = sys.argv[sys.argv.index('-ls') + 1]
        sub_path = __sub_path(path, False)
    except IndexError:
        sub_path = ''
    config = get_config()
    if ':' in config['server_target'][0]:
        from . import SshProtocol
        server, target, port = get_server_target()
        user, ip = server.split('@') if '@' in server else [None, server]
        SshProtocol.command(user, ip, target, port, f'ls {sub_path}')


def template_format():
    config = {}
    with open('project_configure.csv', 'r') as f:
        for row in f.read().strip().split('\n'):
            row = row.replace('\,', '--QPRO-IS-SPLIT--')
            row = [i.replace('--QPRO-IS-SPLIT--', ',') for i in row.split(',')]
            config[row[0]] = [i.strip() for i in row[1:]]
        for i in config:
            if i in ['server_target']:
                continue
            config[i] = config[i][0]
    __format_json(config, 'project_configure.json')
    remove('project_configure.csv')


def enable_complete():
    config = get_config()
    config['enable_complete'] = True
    __format_json(config, project_configure_path)


func = {
    '-c': create,
    '-scp': scp,
    '-get': get,
    '-adjust': adjust,
    '-ssh': ssh,
    '-del-all': delete_all,
    '-del': delete,
    '-ls': tele_ls,
    '-csv': template_format,
    '-enable-complete': enable_complete
}


def main():
    if len(sys.argv) < 2 or '-h' == sys.argv[1]:
        menu_output({'title': 'Qpro usage\n' if user_lang != 'zh' else 'Qpro 菜单\n',
                     'lines': [
                        ('-init', 'let current dir be a Qpro project!' if user_lang != 'zh' else '使当前目录成为Qpro项目'),
                        ('-h', 'help' if user_lang != 'zh' else '帮助'),
                        ('-c   [bold magenta]<name>', 'create a Qpro project' if user_lang != 'zh' else '创建Qpro项目'),
                        ('-update', 'update Qpro' if user_lang != 'zh' else '更新Qpro'),
                        ('-adjust', 'adjust configure' if user_lang != 'zh' else '调整配置表'),
                        ('-ssh', 'login server by ssh' if user_lang != 'zh' else '通过SSH登录远程映射'),
                        (
                            '-scp [bold magenta]<path>',
                            'upload path to default server target' if user_lang != 'zh' else '上传路径到默认的远程映射对应位置'
                        ),
                        (
                            '-scp-init',
                            'upload all of project to server target' if user_lang != 'zh' else '上传当前全部内容到远程映射'
                        ),
                        (
                            '-get [bold magenta]<path>',
                            'download file from server target' if user_lang != 'zh' else '从远程映射下载'
                        ),
                        (
                            '-del [bold magenta]<path>',
                            'delete path in project' if user_lang != 'zh' else '同时删除本地及远程映射文件或目录'
                        ),
                        ('-del-all', 'delete Qpro project' if user_lang != 'zh' else '销毁当前Qpro项目(本地+远程)'),
                        ('-ls  [bold magenta]<path>', 'list element in path' if user_lang != 'zh' else '展示路径中的子项'),
                        ('tmpm *', 'manage your template' if user_lang != 'zh' else '模板管理器'),
                        ('qrun *', 'run your Qpro project' if user_lang != 'zh' else '运行器'),
                        (
                            'detector -<p/f><p/f>',
                            'run beat detector for two source files' if user_lang != 'zh' else '对拍器'
                        )],
                     'prefix': 'Qpro'})
    elif '-update' == sys.argv[1]:
        os.system('pip3 install Qpro --upgrade')
    elif sys.argv[1] in func:
        func[sys.argv[1]]()
    elif sys.argv[1] == '-scp-init':
        scp_init(get_config()['server_target'])
    elif '-init' not in sys.argv:
        QproDefaultConsole.print(
            QproErrorString, 'wrong usage! Run "Qpro -h" for help!' if user_lang != 'zh' else '请运行 "Qpro -h" 查看帮助!'
        )
    elif not os.path.exists(configure_name):
        pro_init()
    else:
        QproDefaultConsole.print(
            f"You have configured your project, see {project_configure_path} to adjust your configure!"
            if user_lang != 'zh' else
            f"你已经配置过这个项目啦, 查看配置表({project_configure_path})来调整它吧!"
        )


if __name__ == '__main__':
    main()
