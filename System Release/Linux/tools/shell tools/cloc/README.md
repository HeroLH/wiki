----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 代码统计  {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | /修改人 | 内容     |
| :--------: | :-----: | :------- |
| 2021-06-17 | Herolh  | 文档创建 |
|            |         |          |



## 简介

> [cloc 官网](https://github.com/AlDanial/cloc)



### 安装

> 根据您的操作系统，这些安装方法中的一种可能适合您(除了 Windows 的最后两个条目以外，其他所有条目都需要一个 Perl 解释器) :

```shell
npm install -g cloc              # https://www.npmjs.com/package/cloc
sudo apt install cloc            # Debian, Ubuntu
sudo yum install cloc            # Red Hat, Fedora
sudo dnf install cloc            # Fedora 22 or later
sudo pacman -S cloc              # Arch
sudo emerge -av dev-util/cloc    # Gentoo https://packages.gentoo.org/packages/dev-util/cloc
sudo apk add cloc                # Alpine Linux
doas pkg_add cloc                # OpenBSD
sudo pkg install cloc            # FreeBSD
sudo port install cloc           # macOS with MacPorts
brew install cloc                # macOS with Homebrew
choco install cloc               # Windows with Chocolatey
scoop install cloc               # Windows with Scoop
```





## 使用

```shell
# 计算目录中的所有代码行
cloc path/to/directory

# 统计一个目录中的所有代码行，在统计过程中显示一个进度条：
cloc --progress=1 path/to/directory

# 比较 2 个目录结构并计算它们之间的差异：
cloc --diff path/to/directory/one path/to/directory/two

# 忽略 VCS 忽略的文件，例如 `.gitignore` 中指定的文件：
cloc --vcs git path/to/directory

# 计算目录中的所有代码行数，显示每个文件而不是每种语言的结果：
cloc --by-file path/to/directory
```

