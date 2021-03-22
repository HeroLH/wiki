[TOC]



# 什么是Shell？

&emsp;&emsp;相对于内核来说，Shell 是 Linux/Unix 的一个外壳，它负责外界与 Linux 内核的交互，接收用户或其他应用程序的命令，然后把这些命令转化成内核能理解的语言，传给内核，内核是真正干活的，干完之后再把结果返回用户或应用程序。
&emsp;&emsp;简单的说，shell就是那“黑乎乎”的命令行。



# Shell的分类
&emsp;&emsp;Linux/Unix 提供了很多种 Shell，不同的 shell 具备不同的功能，shell 还决定了脚本中函数的语法，Linux中默认的shell是 `/bin/bash`；
&emsp;&emsp;想知道你的系统有几种shell，可以通过以下命令查看：

```shell
cat /etc/shells
```

显示如下：

```
/bin/bash  
/bin/csh
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
```

&emsp;&emsp;**bash**这个是目前大多数 Linux 系统默认使用的 shell，全名是 BourneAgain Shell，一共有40个命令。包含的功能几乎可以涵盖shell所具有的功能，所以一般的shell脚本都会指定它为执行路径。在 Linux 里执行这个命令和 Mac 略有不同，你会发现 Mac 多了一个 zsh，也就是说 OS X 系统预装了个 zsh，它是什么呢？



# zsh介绍

&emsp;&emsp;zsh 是一款功能强大的 shell 软件，它可以兼容 bash，并且提供了很多高效的改进。它是Linux里最庞大的一种shell，它有84个内部命令，也提供了更为强大的功能:

- 更好的自动补全
- 更好的文件名展开
- 丰富的插件 
- 强大的定制性

但是由于配置过于复杂，一般情况下，我们不会使用该 shell，直到「oh my zsh」的出现。



# oh my zsh

&emsp;&emsp;[Oh My Zsh](http://ohmyz.sh/) 是一款社区驱动的命令行工具，正如它的主页上说的，`Oh My Zsh` 是一种生活方式。它基于zsh命令行，提供了主题配置，插件机制，已经内置的便捷操作。给我们一种全新的方式使用命令行。`Oh My Zsh`只是一个对 zsh 命令行环境的配置包装框架，但它不提供命令行窗口，更不是一个独立的 APP。