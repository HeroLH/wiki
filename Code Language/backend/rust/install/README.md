----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Rust 的安装 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2022-02-16 | Herolh | 文档创建 |
|            |        |          |



## 简介

&emsp;&emsp;我们通过 `rustup` 下载 Rust，这是一个管理 Rust 版本和相关工具的命令行工具。如果你出于某些理由倾向于不使用 `rustup`，请到 [Rust 的其他安装方法页面](https://forge.rust-lang.org/infra/other-installation-methods.html) 查看其它安装选项。



## 安装 rust

### Linux 下

#### 通用

```shell
curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
```

此命令下载一个脚本并开始安装 `rustup` 工具，这会安装最新稳定版 Rust。过程中可能会提示你输入密码。如果安装成功，将会出现如下内容：

> Rust is installed now. Great!



#### Arch

```shell
sudo pacman -Ss rustup

# 通过 rustup 安装 stable版本的
rustup install stable

# 设置stable为默认的版本
rustup default stable
```



### Windows 下

&emsp;&emsp;在 Windows 上，前往 [官方下载地址](https://www.rust-lang.org/tools/install) 并按照说明安装 Rust。在安装过程的某个步骤，你会收到一个信息说明为什么需要安装 Visual Studio 2013 或更新版本的 C++ build tools。获取这些 build tools 最方便的方法是安装 [Build Tools for Visual Studio 2019](https://visualstudio.microsoft.com/visual-cpp-build-tools/)。当被问及需要安装什么的时候请确保选择 ”C++ build tools“，并确保包括了 Windows 10 SDK 和英文语言包（English language pack）组件。



### 更新与卸载 rust

通过 `rustup` 安装了 Rust 之后，很容易更新到最新版本。在 shell 中运行如下更新脚本：

```shell
rustup update
```

为了卸载 Rust 和 `rustup`，在 shell 中运行如下卸载脚本:

```shell
rustup self uninstall
```



### 故障排除

要检查是否正确安装了 Rust，打开 shell 并运行如下行：

```console
$ rustc --version
```

你应能看到已发布的最新稳定版的版本号、提交哈希和提交日期，显示为如下格式：

```text
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

如果出现这些内容，Rust 就安装成功了！如果并没有看到这些信息，并且使用的是 Windows，请检查 Rust 是否位于 `%PATH%` 系统变量中。如果一切正确但 Rust 仍不能使用，有许多地方可以求助。最简单的是 [位于 Rust 官方 Discord](https://discord.gg/rust-lang) 上的 #beginners 频道。在这里你可以和其他 Rustacean（Rust 用户的称号，有自嘲意味）聊天并寻求帮助。其它给力的资源包括[用户论坛](https://users.rust-lang.org/)和 [Stack Overflow](https://stackoverflow.com/questions/tagged/rust)。



### 本地文档

&emsp;&emsp;安装程序也自带一份文档的本地拷贝，可以离线阅读。运行 `rustup doc` 在浏览器中查看本地文档。任何时候，如果你拿不准标准库中的类型或函数的用途和用法，请查阅应用程序接口（application programming interface，API）文档！