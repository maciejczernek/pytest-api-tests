import os
import shutil


def copy_dir(f_path, target_path):
    shutil.copytree(f_path, target_path, dirs_exist_ok=True)


def create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
