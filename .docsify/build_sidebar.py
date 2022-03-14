import os
import platform

# 加载平台路径分隔符
from dataclasses import dataclass


def load_platform_path_delimiter():
    if platform.system().lower() == 'windows':
        return "\\"
    elif platform.system().lower() == 'linux':
        return "/"


def scan_files(directory, prefix=None, postfix=None):
    child_file_list = list()

    files_list = []
    path_delimiter = load_platform_path_delimiter()

    for root, sub_dirs, files in os.walk(directory):
        print(root, sub_dirs, files)
        rootList = root.split(path_delimiter)
        if len(rootList) >= 2:
            if rootList[1] in [".git", ".docsify", ".assets"]:
                continue
        if rootList[-1] in [".assets", "assets"]:
            continue

        if len(files) == 0:
            continue

        for special_file in files:
            file_path = os.path.join(root, special_file)
            is_dir = os.path.isdir(file_path)
            file_info = FileInfoDto(name=special_file, is_dir=is_dir, relative_path=file_path)
            filetree[special_file] = file_info
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list


def create_dir(root_dir, path_list):
    if len(path_list) <= 1 and type(root_dir) == dict:
        return path_list[0]
    else:
        root_dir = dict()
        root_dir[root_dir] = root_dir
    if path_list[0] not in root_dir:
        root_dir[path_list[0]] = create_dir({}, path_list[1:])
    else:
        root_dir[path_list[0]] = create_dir(root_dir[path_list[0]], path_list[1:])

    return root_dir


md_file_list = scan_files("..", "", ".md")

print("-" * 30)
