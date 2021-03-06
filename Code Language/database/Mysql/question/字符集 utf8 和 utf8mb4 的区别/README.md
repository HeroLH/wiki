----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# MySQL 数据库字符集 utf8 和 utf8mb4 的区别 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-08-12 | Herolh | 文档创建 |
|            |        |          |



## 简介

> [博客园 - 一线大码 - MySQL 数据库字符集 utf8 和 utf8mb4 的区别](https://www.cnblogs.com/wbxk/p/10785517.html)



## 字符集选择

> **utf8mb4 的最低 mysql 版本支持版本为 5.5.3+**

![img](https://img2018.cnblogs.com/blog/1001886/201904/1001886-20190428173534265-70386776.png)

&emsp;&emsp;==MySQL 的 utf8 实际上不是真正的 UTF-8。utf8 只支持每个字符最多三个字节，而真正的 UTF-8 是每个字符最多四个字节。==
&emsp;&emsp;MySQL 一直没有修复这个 bug，他们在 2010 年发布了一个叫作 utf8mb4 的字符集，绕过了这个问题。当然，他们并没有对新的字符集广而告之（可能是因为这个 bug 让他们觉得很尴尬），以致于现在网络上仍然在建议开发者使用 utf8，但这些建议都是错误的。

简单概括如下：
- MySQL 的 utf8mb4 是真正的 UTF-8。
- MySQL 的 utf8 是一种专属的编码，它能够编码的 Unicode 字符并不多。

所有在使用 utf8 的 MySQL 和 MariaDB 用户都应该改用 utf8mb4，永远都不要再使用 utf8。
[这里](https://mathiasbynens.be/notes/mysql-utf8mb4#utf8-to-utf8mb4)提供了一个指南用于将现有数据库的字符编码从 utf8 转成 utf8mb4。



## 历史原因
&emsp;&emsp;为什么 MySQL 开发者会让“utf8”失效？我们或许可以从提交日志中寻找答案。

&emsp;&emsp;MySQL 从 4.1 版本开始支持 UTF-8，也就是 2003 年，而今天使用的 UTF-8 标准（RFC 3629）是随后才出现的。
&emsp;&emsp;旧版的 UTF-8 标准（RFC 2279）最多支持每个字符 6 个字节。2002 年 3 月 28 日，MySQL 开发者在第一个 MySQL 4.1 预览版中使用了 RFC 2279。
&emsp;&emsp;同年 9 月，他们对 MySQL 源代码进行了一次调整：“UTF8 现在最多只支持 3 个字节的序列”。

&emsp;&emsp;是谁提交了这些代码？他为什么要这样做？这个问题不得而知。在迁移到 Git 后（MySQL 最开始使用的是 BitKeeper），MySQL 代码库中的很多提交者的名字都丢失了。2003 年 9 月的邮件列表中也找不到可以解释这一变更的线索。
不过我可以试着猜测一下。

&emsp;&emsp;2002 年，MySQL 做出了一个决定：如果用户可以保证数据表的每一行都使用相同的字节数，那么 MySQL 就可以在性能方面来一个大提升。为此，用户需要将文本列定义为“CHAR”，每个“CHAR”列总是拥有相同数量的字符。如果插入的字符少于定义的数量，MySQL 就会在后面填充空格，如果插入的字符超过了定义的数量，后面超出部分会被截断。
&emsp;&emsp;MySQL 开发者在最开始尝试 UTF-8 时使用了每个字符 6 个字节，CHAR(1) 使用 6 个字节，CHAR(2) 使用 12 个字节，并以此类推。
&emsp;&emsp;应该说，他们最初的行为才是正确的，可惜这一版本一直没有发布。但是文档上却这么写了，而且广为流传，所有了解 UTF-8 的人都认同文档里写的东西。

不过很显然，MySQL 开发者或厂商担心会有用户做这两件事：
- 使用 CHAR 定义列（在现在看来，CHAR 已经是老古董了，但在那时，在 MySQL 中使用 CHAR 会更快，不过从 2005 年以后就不是这样子了）。
- 将 CHAR 列的编码设置为“utf8”。

我的猜测是 MySQL 开发者本来想帮助那些希望在空间和速度上双赢的用户，但他们搞砸了“utf8”编码。
&emsp;&emsp;所以结果就是没有赢家。那些希望在空间和速度上双赢的用户，当他们在使用“utf8”的 CHAR 列时，实际上使用的空间比预期的更大，速度也比预期的慢。而想要正确性的用户，当他们使用“utf8”编码时，却无法保存像“”这样的字符。
&emsp;&emsp;在这个不合法的字符集发布了之后，MySQL 就无法修复它，因为这样需要要求所有用户重新构建他们的数据库。最终，MySQL 在 2010 年重新发布了“utf8mb4”来支持真正的 UTF-8。