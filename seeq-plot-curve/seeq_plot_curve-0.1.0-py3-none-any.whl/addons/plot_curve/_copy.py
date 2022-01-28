import os
from pathlib import Path
from distutils import dir_util
import shutil
from typeguard import typechecked

directory = Path(__file__).resolve().parent


@typechecked
def copy_notebooks(des_folder: str = None, src_folder: str = None, *,
                   overwrite_folder: bool = None, overwrite_contents: bool = None):
    """
    Copies the files on the src_folder to a des_folder in the current working directory.
    Parameters
    ----------
    des_folder : str
        The destination folder. By default it will be copied to a 'deployment_notebook' folder
         in the current working directory.

    src_folder : str
        Name of the folder that contains the documentation to be copied

    overwrite_folder : bool
        If True, any existing files in the specified folder will be deleted before the documentation is copied in.

    overwrite_contents : bool
        If True, files in the specified folder will be overwriting if necessary when the documentation is copied in.
    """

    root_src_dir = os.path.dirname(__file__)

    if not des_folder:
        des_folder = 'deployment'
    des_folder_path = Path.cwd().joinpath(des_folder)

    if not src_folder:
        src_folder = 'deployment_notebook'
    src_folder_path = directory.joinpath(src_folder)

    if des_folder_path.exists():
        if not overwrite_folder and not overwrite_contents:
            raise RuntimeError(
                f"The {des_folder_path} directory already exists. If you would like to overwrite it, supply the "
                f"overwrite_folder=True parameter to clean up the folder or overwrite_contents=True to keep the "
                f"current files but overwrite them with the contents of {src_folder_path}. ")
        if overwrite_folder:
            dir_util.remove_tree(str(des_folder_path))
            dir_util.copy_tree(str(src_folder_path), str(des_folder_path))
            print(f'Copied My Add-on notebook to {des_folder_path}')
        if overwrite_contents:
            if not os.path.exists(des_folder_path):
                os.makedirs(des_folder_path)
            for src_dir, dirs, files in os.walk(src_folder_path):
                for file_ in files:
                    src_file = os.path.join(src_dir, file_)
                    dst_file = os.path.join(des_folder_path, file_)
                    if os.path.exists(dst_file):
                        # in case of the src and dst are the same file
                        if os.path.samefile(src_file, dst_file):
                            continue
                        os.remove(dst_file)
                    shutil.copy(src_file, des_folder_path)

    else:
        dir_util.copy_tree(src_folder_path, str(des_folder_path))
        print(f'Copied My Add-on notebook to {des_folder_path}')

