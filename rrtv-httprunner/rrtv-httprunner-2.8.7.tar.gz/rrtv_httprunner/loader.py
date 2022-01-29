import csv
import importlib
import json
import os
import sys
import types
from typing import Tuple, Dict, Union, Text, List, Callable

import yaml
from loguru import logger
from pydantic import ValidationError

from rrtv_httprunner import builtin, utils
from rrtv_httprunner import exceptions
from rrtv_httprunner.models import TestCase, ProjectMeta, TestSuite, GlobalConfig
from rrtv_httprunner.utils import loads_json

try:
    # PyYAML version >= 5.1
    # ref: https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
    yaml.warnings({"YAMLLoadWarning": False})
except AttributeError:
    pass

project_meta: Union[ProjectMeta, None] = None


def _load_yaml_file(yaml_file: Text) -> Dict:
    """ load yaml file and check file content format
    """
    with open(yaml_file, mode="rb") as stream:
        try:
            yaml_content = yaml.load(stream)
        except yaml.YAMLError as ex:
            err_msg = f"YAMLError:\nfile: {yaml_file}\nerror: {ex}"
            logger.error(err_msg)
            raise exceptions.FileFormatError

        return yaml_content


def _load_json_file(json_file: Text) -> Dict:
    """ load json file and check file content format
    """
    with open(json_file, mode="rb") as data_file:
        try:
            json_content = json.load(data_file)
        except json.JSONDecodeError as ex:
            err_msg = f"JSONDecodeError:\nfile: {json_file}\nerror: {ex}"
            raise exceptions.FileFormatError(err_msg)

        return json_content


def load_test_file(test_file: Text) -> Dict:
    """load testcase/testsuite file content"""
    if not os.path.isfile(test_file):
        raise exceptions.FileNotFound(f"test file not exists: {test_file}")

    file_suffix = os.path.splitext(test_file)[1].lower()
    if file_suffix == ".json":
        test_file_content = _load_json_file(test_file)
    elif file_suffix in [".yaml", ".yml"]:
        test_file_content = _load_yaml_file(test_file)
    else:
        # '' or other suffix
        raise exceptions.FileFormatError(
            f"testcase/testsuite file should be YAML/JSON format, invalid format file: {test_file}"
        )

    return test_file_content


def load_testcase(testcase: Dict) -> TestCase:
    try:
        # validate with pydantic TestCase model
        testcase_obj = TestCase.parse_obj(testcase)
    except ValidationError as ex:
        err_msg = f"TestCase ValidationError:\nerror: {ex}\ncontent: {testcase}"
        raise exceptions.TestCaseFormatError(err_msg)

    return testcase_obj


def load_testcase_file(testcase_file: Text) -> TestCase:
    """load testcase file and validate with pydantic model"""
    testcase_content = load_test_file(testcase_file)
    testcase_obj = load_testcase(testcase_content)
    testcase_obj.config.path = testcase_file
    return testcase_obj


def load_testsuite(testsuite: Dict) -> TestSuite:
    path = testsuite["config"]["path"]
    try:
        # validate with pydantic TestCase model
        testsuite_obj = TestSuite.parse_obj(testsuite)
    except ValidationError as ex:
        err_msg = f"TestSuite ValidationError:\nfile: {path}\nerror: {ex}"
        raise exceptions.TestSuiteFormatError(err_msg)

    return testsuite_obj


def load_dot_env_file(dot_env_path: Text) -> Dict:
    """ load .env file.

    Args:
        dot_env_path (str): .env file path

    Returns:
        dict: environment variables mapping

            {
                "UserName": "debugtalk",
                "Password": "123456",
                "PROJECT_KEY": "ABCDEFGH"
            }

    Raises:
        exceptions.FileFormatError: If .env file format is invalid.

    """
    if not os.path.isfile(dot_env_path):
        return {}

    logger.info(f"Loading environment variables from {dot_env_path}")
    env_variables_mapping = {}

    with open(dot_env_path, mode="rb") as fp:
        for line in fp:
            # maxsplit=1
            if b"=" in line:
                variable, value = line.split(b"=", 1)
            elif b":" in line:
                variable, value = line.split(b":", 1)
            else:
                raise exceptions.FileFormatError(".env format error")

            env_variables_mapping[
                variable.strip().decode("utf-8")
            ] = value.strip().decode("utf-8")

    utils.set_os_environ(env_variables_mapping)
    return env_variables_mapping


def load_csv_file(csv_file: Text) -> List[Dict]:
    """ load csv file and check file content format

    Args:
        csv_file (str): csv file path, csv file content is like below:

    Returns:
        list: list of parameters, each parameter is in dict format

    Examples:
        >>> cat csv_file
        username,password
        test1,111111
        test2,222222
        test3,333333

        >>> load_csv_file(csv_file)
        [
            {'username': 'test1', 'password': '111111'},
            {'username': 'test2', 'password': '222222'},
            {'username': 'test3', 'password': '333333'}
        ]

    """
    if not os.path.isabs(csv_file):
        global project_meta
        if project_meta is None:
            raise exceptions.MyBaseFailure("load_project_meta() has not been called!")

        # make compatible with Windows/Linux
        csv_file = os.path.join(project_meta.RootDir, *csv_file.split("/"))

    if not os.path.isfile(csv_file):
        # file path not exist
        raise exceptions.CSVNotFound(csv_file)

    csv_content_list = []

    with open(csv_file, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list


def load_folder_files(folder_path: Text, recursive: bool = True) -> List:
    """ load folder path, return all files endswith .yml/.yaml/.json/_test.py in list.

    Args:
        folder_path (str): specified folder path to load
        recursive (bool): load files recursively if True

    Returns:
        list: files endswith yml/yaml/json
    """
    if isinstance(folder_path, (list, set)):
        files = []
        for path in set(folder_path):
            files.extend(load_folder_files(path, recursive))

        return files

    if not os.path.exists(folder_path):
        return []

    file_list = []

    for dirpath, dirnames, filenames in os.walk(folder_path):
        filenames_list = []

        for filename in filenames:
            if not filename.lower().endswith((".yml", ".yaml", ".json", "_test.py")):
                continue

            filenames_list.append(filename)

        for filename in filenames_list:
            file_path = os.path.join(dirpath, filename)
            file_list.append(file_path)

        if not recursive:
            break

    return file_list


def load_module_functions(module) -> Dict[Text, Callable]:
    """ load python module functions.

    Args:
        module: python module

    Returns:
        dict: functions mapping for specified python module

            {
                "func1_name": func1,
                "func2_name": func2
            }

    """
    module_functions = {}

    for name, item in vars(module).items():
        if isinstance(item, types.FunctionType):
            module_functions[name] = item

    return module_functions


def load_builtin_functions() -> Dict[Text, Callable]:
    """ load builtin module functions
    """
    return load_module_functions(builtin)


def locate_file(start_path: Text, file_name: Text) -> Text:
    """ locate filename and return absolute file path.
        searching will be recursive upward until system root dir.

    Args:
        file_name (str): target locate file name
        start_path (str): start locating path, maybe file path or directory path

    Returns:
        str: located file path. None if file not found.

    Raises:
        exceptions.FileNotFound: If failed to locate file.

    """
    if os.path.isfile(start_path):
        start_dir_path = os.path.dirname(start_path)
    elif os.path.isdir(start_path):
        start_dir_path = start_path
    else:
        raise exceptions.FileNotFound(f"invalid path: {start_path}")

    file_path = os.path.join(start_dir_path, file_name)
    if os.path.isfile(file_path):
        # ensure absolute
        return os.path.abspath(file_path)

    # system root dir
    # Windows, e.g. 'E:\\'
    # Linux/Darwin, '/'
    parent_dir = os.path.dirname(start_dir_path)
    if parent_dir == start_dir_path:
        raise exceptions.FileNotFound(f"{file_name} not found in {start_path}")

    # locate recursive upward
    return locate_file(parent_dir, file_name)


def locate_debugtalk_py(start_path: Text) -> Text:
    """ locate debugtalk.py file

    Args:
        start_path (str): start locating path,
            maybe testcase file path or directory path

    Returns:
        str: debugtalk.py file path, None if not found

    """
    try:
        # locate debugtalk.py file.
        debugtalk_path = locate_file(start_path, "debugtalk.py")
    except exceptions.FileNotFound:
        debugtalk_path = None

    return debugtalk_path


def locate_custom_py(start_path: Text, project_root_directory: Text) -> Text:
    """ locate {custom}.py file

    Args:
        start_path (str): start locating path,
            maybe testcase file path or directory path

    Returns:
        str: {custom}.py file path, None if not found

    """
    try:
        # locate {custom}.py file.
        start_dir_path = os.path.dirname(start_path)
        custom_dir_name = start_dir_path.split("/")[-1]
        custom_dir_path = os.path.join(project_root_directory, "hooks")
        custom_path = os.path.join(custom_dir_path, custom_dir_name + ".py")
    except exceptions.FileNotFound:
        custom_path = None

    return custom_path


def locate_project_root_directory(test_path: Text) -> Tuple[str, str]:
    """ locate debugtalk.py path as project root directory

    Args:
        test_path: specified testfile path

    Returns:
        (str, str): debugtalk.py path, project_root_directory

    """

    def prepare_path(path):
        if not os.path.exists(path):
            err_msg = f"path not exist: {path}"
            logger.error(err_msg)
            raise exceptions.FileNotFound(err_msg)

        if not os.path.isabs(path):
            path = os.path.join(os.getcwd(), path)

        return path

    test_path = prepare_path(test_path)

    # locate debugtalk.py file
    debugtalk_path = locate_debugtalk_py(test_path)

    if debugtalk_path:
        # The folder contains debugtalk.py will be treated as project RootDir.
        project_root_directory = os.path.dirname(debugtalk_path)
    else:
        # debugtalk.py not found, use os.getcwd() as project RootDir.
        project_root_directory = os.getcwd()
    # custom_path = locate_custom_py(test_path, project_root_directory)
    return debugtalk_path, project_root_directory


def load_debugtalk_functions() -> Dict[Text, Callable]:
    """ load project debugtalk.py module functions
        debugtalk.py should be located in project root directory.

    Returns:
        dict: debugtalk module functions mapping
            {
                "func1_name": func1,
                "func2_name": func2
            }

    """
    # load debugtalk.py module
    try:
        imported_module = importlib.import_module("debugtalk")
    except Exception as ex:
        logger.error(f"error occurred in debugtalk.py: {ex}")
        sys.exit(1)

    # reload to refresh previously loaded module
    imported_module = importlib.reload(imported_module)
    return load_module_functions(imported_module)


def load_hooks_functions_by_path(hooks_paths: List = None) -> Dict[Text, Callable]:
    """ load project hooks module functions
    """
    try:
        batch_hooks_functions = {}
        if hooks_paths:
            for path in hooks_paths:
                if path != "":
                    path = path.replace("/", ".").split(".py")[0]
                    imported_module = importlib.import_module(path)
                    batch_hooks_functions.update(load_module_functions(imported_module))
    except Exception as ex:
        logger.error(f"error occurred in hooks.py: {ex}")
        sys.exit(1)
    return batch_hooks_functions


def load_hooks_functions_default(start_path: Text = None) -> Dict[Text, Callable]:
    """ load project hooks module functions default
    默认会在hooks目录下读取testcases下根目录名文件夹名的py文件
    """
    try:
        batch_hooks_functions = {}
        file_path = os.path.join(start_path, "hooks")
        if os.path.exists(file_path):
            file_path_list = os.listdir(file_path)
            for i in range(0, len(file_path_list)):
                path = os.path.join(file_path, file_path_list[i])
                if os.path.isfile(path):
                    hooks_py_name = file_path_list[i].split(".py")[0]
                    # reload to refresh previously loaded module
                    imported_module = importlib.import_module(f"hooks.{hooks_py_name}")
                    batch_hooks_functions.update(load_module_functions(imported_module))
    except Exception as ex:
        logger.error(f"error occurred in hooks.py: {ex}")
        sys.exit(1)
    return batch_hooks_functions


def load_self_functions_default(start_path: Text = None, test_path: Text = None) -> Dict[Text, Callable]:
    """
    load project self module functions
    默认会把自身py文件中写的函数加载进来
    """
    try:
        separator = "/"
        if sys.platform.startswith("win"):
            separator = "\\"
        if os.path.isabs(test_path) is False:
            test_path = os.path.abspath(test_path)
        if os.path.exists(test_path) and test_path.endswith(".py"):
            batch_self_functions = {}
            if start_path[-1] != separator:
                start_path = start_path + separator
            self_py_dir = test_path.split(start_path)[1]
            path = self_py_dir.replace(separator, ".").split(".py")[0]
            imported_module = importlib.import_module(path)
            batch_self_functions.update(load_module_functions(imported_module))
            return batch_self_functions
    except Exception as ex:
        logger.error(f"error occurred in {test_path}: {ex}")
        sys.exit(1)
    return {}


def load_project_meta(test_path: Text, reload: bool = False) -> ProjectMeta:
    """ load testcases, .env, debugtalk.py functions.
        testcases folder is relative to project_root_directory
        by default, project_meta will be loaded only once, unless set reload to true.

    Args:
        test_path (str): test file/folder path, locate project RootDir from this path.
        reload: reload project meta if set true, default to false

    Returns:
        project loaded api/testcases definitions,
            environments and debugtalk.py functions.

    """
    global project_meta
    if project_meta and (not reload):
        if not test_path:
            return project_meta
        debugtalk_path, project_root_directory = locate_project_root_directory(test_path)
        self_functions = load_self_functions_default(project_root_directory, test_path)
        project_meta.functions.update(self_functions)
        return project_meta

    project_meta = ProjectMeta()

    if not test_path:
        return project_meta

    if sys.platform.startswith("win"):
        test_path = test_path.replace("/", "\\")

    debugtalk_path, project_root_directory = locate_project_root_directory(test_path)

    # add project RootDir to sys.path
    sys.path.insert(0, project_root_directory)

    # load .env file
    # NOTICE:
    # environment variable maybe loaded in debugtalk.py
    # thus .env file should be loaded before loading debugtalk.py
    dot_env_path = os.path.join(project_root_directory, ".env")
    dot_env = load_dot_env_file(dot_env_path)
    global_config_path = os.path.join(project_root_directory, "config.json")
    global_config = loads_json(global_config_path)
    hooks_functions = {}
    hooks_path = None
    datasource = {}
    if dot_env:
        project_meta.env = dot_env
        project_meta.dot_env_path = dot_env_path

    if global_config:
        if "hooks" in global_config:
            if "paths" in global_config["hooks"]:
                hooks_path = global_config["hooks"]["paths"]
                hooks_functions = load_hooks_functions_by_path(hooks_path)

        if "middleware" in global_config:
            if "datasource" in global_config["middleware"]:
                datasource = global_config["middleware"]["datasource"]

    # load {hooks}.py functions
    if hooks_functions == {}:
        hooks_functions = load_hooks_functions_default(project_root_directory)
    else:
        hooks_functions.update(load_hooks_functions_default(project_root_directory))

    if debugtalk_path:
        # load debugtalk.py functions
        debugtalk_functions = load_debugtalk_functions()
    else:
        debugtalk_functions = {}

    self_functions = load_self_functions_default(project_root_directory, test_path)

    # locate project RootDir and load debugtalk.py functions
    project_meta.RootDir = project_root_directory
    project_meta.functions = debugtalk_functions
    project_meta.functions.update(hooks_functions)
    project_meta.functions.update(self_functions)
    project_meta.debugtalk_path = debugtalk_path
    project_meta.custom_path = hooks_path
    project_meta.self_path = test_path
    project_meta.datasource = datasource
    return project_meta


def convert_relative_project_root_dir(abs_path: Text) -> Text:
    """ convert absolute path to relative path, based on project_meta.RootDir

    Args:
        abs_path: absolute path

    Returns: relative path based on project_meta.RootDir

    """
    _project_meta = load_project_meta(abs_path)
    if not abs_path.startswith(_project_meta.RootDir):
        raise exceptions.ParamsError(
            f"failed to convert absolute path to relative path based on project_meta.RootDir\n"
            f"abs_path: {abs_path}\n"
            f"project_meta.RootDir: {_project_meta.RootDir}"
        )

    return abs_path[len(_project_meta.RootDir) + 1:]
