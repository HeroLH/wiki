----------------------------------------------
> *Made By {Author}*
----------------------------------------------

# SSH 基础使用 {#index}

[TOC]











--------------------------------------------

## 基础知识

> https://wangdoc.com/ssh/basic.html



### 介绍
#### What is SSH?

> SSH（Secure Shell 的缩写）是一种网络协议，用于加密两台计算机之间的通信，并且支持各种身份验证机制。
> 实务中，它主要用于保证远程登录和远程通信的安全，任何网络服务都可以用这个协议来加密。

&emsp;&emsp;历史上，网络主机之间的通信是不加密的，属于明文通信。这使得通信很不安全，一个典型的例子就是服务器登录。登录远程服务器的时候，需要将用户输入的密码传给服务器，如果这个过程是明文通信，就意味着传递过程中，线路经过的中间计算机都能看到密码，这是很可怕的。

&emsp;&emsp;SSH 就是为了解决这个问题而诞生的，它能够加密计算机之间的通信，保证不被窃听或篡改。它还能对操作者进行认证（authentication）和授权（authorization）。明文的网络协议可以套用在它里面，从而实现加密。



### 历史

- 1995 年，芬兰赫尔辛基工业大学的研究员 Tatu Ylönen 设计了 SSH 协议的第一个版本（现称为 SSH 1），同时写出了第一个实现（称为 SSH1）。

    > 当时，他所在的大学网络一直发生密码嗅探攻击，他不得不为服务器设计一个更安全的登录方式。写完以后，他就把这个工具公开了，允许其他人免费使用。
    >
    > SSH 可以替换 rlogin、TELNET、FTP 和 rsh 这些不安全的协议，所以大受欢迎，用户快速增长，1995 年底已经发展到五十个国家的 20,000 个用户。SSH 1 协议也变成 IETF 的标准文档。
    >
    > 1995 年 12 月，由于客服需求越来越大，Tatu Ylönen 就成立了一家公司 SCS，专门销售和开发 SSH。这个软件的后续版本，逐渐从免费软件变成了专有的商业软件。

- 1996~1998年

    > SSH 1 协议存在一些安全漏洞，所以 1996 年又提出了 SSH 2 协议（或者称为 SSH 2.0）。这个协议与 1.0 版不兼容，在 1997 年进行了标准化，1998 年推出了软件实现 SSH2。但是，官方的 SSH2 软件是一个专有软件，不能免费使用，而且 SSH1 的有些功能也没有提供。

- 1999 年，OpenBSD 的开发人员决定写一个 SSH 2 协议的开源实现，这就是 OpenSSH 项目。

    > 该项目最初是基于 SSH 1.2.12 版本，那是当时 SSH1 最后一个开源版本。但是，OpenSSH 很快就完全摆脱了原始的官方代码，在许多开发者的参与下，按照自己的路线发展。OpenSSH 随 OpenBSD 2.6 版本一起提供，以后又移植到其他操作系统，成为最流行的 SSH 实现。目前，Linux 的所有发行版几乎都自带 OpenSSH。



### SSH 架构

>  SSH 的软件架构是服务器 - 客户端模式（Server - Client）。

&emsp;&emsp;在这个架构中，SSH 软件分成两个部分：向服务器发出请求的部分，称为客户端（client），OpenSSH 的实现为 ssh；接收客户端发出的请求的部分，称为服务器（server），OpenSSH 的实现为 sshd。
&emsp;&emsp;另外，OpenSSH 还提供一些辅助工具软件（比如 ssh-keygen 、ssh-agent）和专门的客户端工具（比如 scp 和 sftp），这个教程也会予以介绍。





## SSH 客户端

OpenSSH 的客户端是二进制程序 ssh。它在 Linux/Unix 系统的位置是 `/usr/local/bin/ssh`，Windows 系统的位置是 `\Program Files\OpenSSH\bin\ssh.exe`。



## 基础使用

### 登录服务器

&emsp;&emsp;ssh 最常见的用途就是登录服务器，这要求服务器安装并正在运行 SSH 服务器软件。ssh 登录服务器的命令如下:

```shell
ssh hostname
```

上面命令中，`hostname` 是主机名，它可以是域名，也可能是 IP 地址或局域网内部的主机名。不指定用户名的情况下，将使用客户端的当前用户名，作为远程服务器的登录用户名。如果要指定用户名，可以采用下面的语法:

```shell
ssh user@hostname
```

用户名也可以使用 `ssh` 的 `-l` 参数指定，这样的话，用户名和主机名就不用写在一起了:

```shell
ssh -l username host
```

ssh 默认连接服务器的 22 端口，`-p` 参数可以指定其他端口。

```shell
ssh -p 8821 host
```



### 连接流程

ssh 连接远程服务器后，首先有一个验证过程，验证远程服务器是否为陌生地址。

如果是第一次连接某一台服务器，命令行会显示一段文字，表示不认识这台机器，提醒用户确认是否需要连接:

```shell
The authenticity of host 'foo.com (192.168.121.111)' can't be established.
ECDSA key fingerprint is SHA256:Vybt22mVXuNuB5unE++yowF7lgA/9/2bLSiO3qmYWBY.
Are you sure you want to continue connecting (yes/no)?
```

上面这段文字告诉用户，`foo.com` 这台服务器的指纹是陌生的，让用户选择是否要继续连接（输入 yes 或 no）。

所谓 “服务器指纹”，指的是 SSH 服务器公钥的哈希值。每台 SSH 服务器都有唯一一对密钥，用于跟客户端通信，其中公钥的哈希值就可以用来识别服务器。下面的命令可以查看某个公钥的指纹:

```shell
ssh-keygen -l -f /etc/ssh/ssh_host_ecdsa_key.pub

# 256 da:24:43:0b:2e:c1:3f:a1:84:13:92:01:52:b4:84:ff   (ECDSA)
```

上面的例子中，`ssh-keygen -l -f` 命令会输出公钥 `/etc/ssh/ssh_host_ecdsa_key.pub` 的指纹。

ssh 会将本机连接过的所有服务器公钥的指纹，都储存在本机的 `~/.ssh/known_hosts` 文件中。每次连接服务器时，通过该文件判断是否为陌生主机（陌生公钥）。

在上面这段文字后面，输入 `yes`，就可以将当前服务器的指纹也储存在本机 `~/.ssh/known_hosts` 文件中，并显示下面的提示。以后再连接的时候，就不会再出现警告了。

```shell
Warning: Permanently added 'foo.com (192.168.121.111)' (RSA) to the list of known hosts
```

然后，客户端就会跟服务器建立连接。接着，ssh 就会要求用户输入所要登录账户的密码。用户输入并验证密码正确以后，就能登录远程服务器的 Shell 了。



### 服务器密钥变更

服务器指纹可以防止有人恶意冒充远程主机。如果服务器的密钥发生变更（比如重装了 SSH 服务器），客户端再次连接时，就会发生公钥指纹不吻合的情况。这时，客户端就会中断连接，并显示一段警告信息。

```shell
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
77:a5:69:81:9b:eb:40:76:7b:13:04:a9:6c:f4:9c:5d.
Please contact your system administrator.
Add correct host key in /home/me/.ssh/known_hosts to get rid of this message.
Offending key in /home/me/.ssh/known_hosts:36
```

上面这段文字的意思是，该主机的公钥指纹跟 `~/.ssh/known_hosts` 文件储存的不一样，必须处理以后才能连接。这时，你需要确认是什么原因，使得公钥指纹发生变更，到底是恶意劫持，还是管理员变更了 SSH 服务器公钥。

如果新的公钥确认可以信任，需要继续执行连接，你可以执行下面的命令，将原来的公钥指纹从 `~/.ssh/known_hosts` 文件删除。

```shell
ssh-keygen -R hostname
```

上面命令中，`hostname` 是发生公钥变更的主机名。

除了使用上面的命令，你也可以手工修改 `known_hosts` 文件，将公钥指纹删除。

删除了原来的公钥指纹以后，重新执行 ssh 命令连接远程服务器，将新的指纹加入 `known_hosts` 文件，就可以顺利连接了。





### 执行远程命令

SSH 登录成功后，用户就进入了远程主机的命令行环境，所看到的提示符，就是远程主机的提示符。这时，你就可以输入想要在远程主机执行的命令。

另一种执行远程命令的方法，是将命令直接写在 `ssh` 命令的后面。

```shell
ssh username@hostname command
```

上面的命令会使得 SSH 在登录成功后，立刻在远程主机上执行命令 `command`。

采用这种语法执行命令时，ssh 客户端不会提供互动式的 Shell 环境，而是直接远程命令的执行结果输出在命令行。但是，有些命令需要互动式的 Shell 环境，这时就要使用 `-t` 参数。

```shell
# 报错
ssh remote.server.com emacs
# emacs: standard input is not a tty

# 不报错
ssh -t server.example.com emacs
```

上面代码中，`emacs` 命令需要一个互动式 Shell，所以报错。只有加上 `-t` 参数，ssh 才会分配一个互动式 Shell。





### SSH 密钥登录

SSH 默认采用密码登录，这种方法有很多缺点，简单的密码不安全，复杂的密码不容易记忆，每次手动输入也很麻烦。密钥登录是比密码登录更好的解决方案。