from setuptools import setup

with open('README.md') as f:
    desc = f.read()

with open('CHANGELOG.md') as f2:
    log = f2.read()

setup(
    name = 'randcoor',
    version = '0.1.1',
    description = 'Tools for creating random coordinates and using them',
    author = 'FromHumansImportDevs',
    author_email = 'randcoor@msgsafe.io',
    url = 'https://pypi.org/project/randcoor',
    license = 'Public Domain',
    py_modules = ['randcoor'],
    package_dir = {'': 'src'},
    classifiers = [
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Operating System :: OS Independent',
    ],
    long_description = desc + '\n\n' + log,
    long_description_content_type = 'text/markdown',
)
