import os
import platform
from dataclasses import dataclass


# 加载平台路径分隔符
def load_platform_path_delimiter():
    if platform.system().lower() == 'windows':
        return "\\"
    elif platform.system().lower() == 'linux':
        return "/"


@dataclass
class FileInfoDto:
    name: str  # 文件名
    is_dir: bool  # 是否目录
    relative_path: str  # 相对路径
    has_child_folder: bool = False  # 是否有子文件
    child_node: list = None  # 子文件


def scan_files(directory, skip: list = []) -> FileInfoDto:
    path_delimiter = load_platform_path_delimiter()
    file_name_list = directory.split(path_delimiter)
    file_name = file_name_list[-1] if len(file_name_list) >= 2 else ""

    root_node = FileInfoDto(name=file_name, is_dir=True, relative_path=directory)
    file_node_list, has_child_folder = list(), False
    files = os.listdir(directory)
    for f in files:
        if f in skip:
            continue

        if os.path.isfile(directory + path_delimiter + f):
            file_node = FileInfoDto(name=f, is_dir=False, relative_path=directory, child_node=[])
        else:
            has_child_folder = True
            file_node = scan_files(directory + path_delimiter + f, skip)

        file_node_list.append(file_node)
    root_node.child_node = file_node_list
    root_node.has_child_folder = has_child_folder

    return root_node


file_tree = scan_files("..", [".git", ".idea", ".docsify", ".github", ".gitignore", ".nojekyll", "index.html", "file template.md",
                              "README.en.md", ".assets"])


def build_navbar(file_node: FileInfoDto):
    if len(file_node.child_node) <= 0:
        return
    if file_node.has_child_folder:
        mkdoc = ""
        for f in file_node.child_node:
            title = f.name
            link = f.relative_path.replace(" ", "%20") + load_platform_path_delimiter()
            if f.is_dir:
                if f.has_child_folder:
                    link = link[2:] + "_navbar"
                else:
                    link = link[2:] + "README"
            else:
                link = link[2:] + f.name
                title = title.split(".")[0]
            if title == "_navbar":
                continue

            mkdoc += "* [**{title}**]({link})  \n".format(title=title, link=link)
            build_navbar(f)

        with open(file_node.relative_path+load_platform_path_delimiter()+"_navbar.md", "w", encoding="utf8") as f_io:
            f_io.write(mkdoc)

build_navbar(file_tree)

readme = "## 目录\n"
for f in file_tree.child_node:
    title = f.name
    link = f.relative_path.replace(" ", "%20") + load_platform_path_delimiter()
    if f.is_dir:
        if f.has_child_folder:
            link = link[2:] + "_navbar"
        else:
            link = link[2:] + "README"
    else:
        link = link[2:] + f.name
        title = title.split(".")[0]
    if title == "_navbar":
        continue

    readme += "* [{title}]({link})  \n".format(title=title, link=link)

with open(file_tree.relative_path + load_platform_path_delimiter() + "README.md", "w", encoding="utf8") as f_io:
    f_io.write(readme)
