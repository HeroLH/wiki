----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# pages

> [CSDN - git bash 下 pacman 环境配置](https://blog.csdn.net/zhouguoqionghai/article/details/111143869)



## 步骤

```shell
# 安装 pacman
tar xvf pacman-5.2.2-4-x86_64.pkg.tar.xz
# 安装软件源 mirrors
tar -xvf pacman-mirrors-20201208-1-any.pkg.tar.xz
# 安装 keyring
tar -xvf msys2-keyring-1~20201002-1-any.pkg.tar.xz

pacman-key --init
pacman-key --populate msys2
pacman -Sy
```





## 实际环境尝试

### 安装 pacman

下载 [pacman](https://mirrors.tuna.tsinghua.edu.cn/msys2/msys/x86_64/pacman-5.2.2-4-x86_64.pkg.tar.xz)，解压到 git 的安装目录。

> `C:\Program Files\Git`，一定要是 git 的安装根目录，这样解压出来的目录结构和安装 git 时的层次保持一致

```shell
tar xvf pacman-5.2.2-4-x86_64.pkg.tar.xz
```

此时在 git bash 里运行 `pacman` 会提示没有软件源相关的配置文件。

> error: config file /etc/pacman.d/mirrorlist.mingw32 could not be read: No such file or directory



### 安装软件源 mirrors

下载源配置包[mirrors](http://repo.msys2.org/msys/x86_64/pacman-mirrors-20201208-1-any.pkg.tar.xz)，一样的，要放到 git 安装的根目录下解压。

```shell
tar -xvf pacman-mirrors-20201208-1-any.pkg.tar.xz
```

修改相关的配置，使用[清华的软件源](https://mirrors.tuna.tsinghua.edu.cn/help/msys2/)，重启 git bash，再次运行，提示没有数据库。

```shell
pacman
```

> warning: database file for ‘mingw32’ does not exist (use ‘-Sy’ to download)
> warning: database file for ‘mingw64’ does not exist (use ‘-Sy’ to download)
> warning: database file for ‘msys’ does not exist (use ‘-Sy’ to download)
> error: no operation specified (use -h for help)



```shell
pacman -Sy
```

> :: Synchronizing package databases…
> mingw32 760.3 KiB 2.40 MiB/s 00:00 [###################################################################################] 100%
> mingw32.sig 438.0 B 428 KiB/s 00:00 [###################################################################################] 100%
> warning: Public keyring not found; have you run **‘pacman-key --init’**?
> error: mingw32: key “4A6129F4E4B84AE46ED7F635628F528CF3053E04” is unknown
> error: keyring is not writable
> error: failed to update mingw32 (invalid or corrupted database (PGP signature))
> mingw64 761.9 KiB 2.21 MiB/s 00:00 [###################################################################################] 100%
> mingw64.sig 438.0 B 0.00 B/s 00:00 [###################################################################################] 100%
> error: mingw64: key “4A6129F4E4B84AE46ED7F635628F528CF3053E04” is unknown
> error: keyring is not writable
> error: failed to update mingw64 (invalid or corrupted database (PGP signature))
> msys 273.5 KiB 1581 KiB/s 00:00 [###################################################################################] 100%
> msys.sig 438.0 B 428 KiB/s 00:00 [###################################################################################] 100%
> error: msys: key “4A6129F4E4B84AE46ED7F635628F528CF3053E04” is unknown
> error: keyring is not writable
> error: failed to update msys (invalid or corrupted database (PGP signature))
> error: failed to synchronize all databases



按提示，先进行初始化。

```shell
pacman-key --init
```

再次更新：

```shell
pacman -Sy
```

会卡主：

> error: mingw32: key “4A6129F4E4B84AE46ED7F635628F528CF3053E04” is unknown
> :: Import PGP key 4A6129F4E4B84AE46ED7F635628F528CF3053E04? [Y/n] y

`ctrl + c` 终止之后，使用 pacman-key 更新 key

```shell
pacman-key --populate msys2
```

提示：
> ==> 错误： 密匙环文件 /usr/share/pacman/keyrings/msys2.gpg 不存在



### 安装 keyring

下载[keyring](http://repo.msys2.org/msys/x86_64/msys2-keyring-1~20201002-1-any.pkg.tar.xz)数据库包，同样的解压。

```shell
tar -xvf msys2-keyring-1~20201002-1-any.pkg.tar.xz
```

再次:

```shell
pacman-key --populate msys2
```

最后成功。

```shell
pacman -Sy
```

> :: 正在同步软件包数据库…
> mingw32 已经是最新版本
> mingw64 已经是最新版本
> msys 已经是最新版本



### 最后

如果上述方法还不行，可尝试更新 pacman 所有包的数据库。

```shell
pacman -S --dbonly pacman 
```

> pacman has a record of only some of the contents of the pacman package.
> Try the following to fix the databse entry for the pacman package.