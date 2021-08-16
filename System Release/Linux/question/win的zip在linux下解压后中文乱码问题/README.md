----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 解决 win 的 zip 在 linux 下解压后中文乱码问题 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-08-16 | Herolh | 文档创建 |
|            |        |          |



## 简介

&emsp;&emsp;由于 zip 在压缩时并没有指定编码格式，win 下生成的 zip 文件中的编码是 GBK/GB2312 等，而 Linux 下的默认编码是 UTF8 因此，导致这些 zip 文件在 Linux 下解压时出现中文乱码问题。



## 解决方案

### 解决方案一： CP936

&emsp;&emsp;解决的方法是 加上 CP936 选项，这里的 CP936 , 有些人可能不明白，其实最早的 GBK 编码，就是 IBM 定制的 MBCS 字符集，汉字编码正好在整个字符集中的 936 页，因此好多地方其实都是用 CP936 来代表 GBK。

```shell
unzip -O CP936 xxx.zip
```

但是，有些发行版所带的 unzip 没有这个参数，比如 ArchLinux 就需要安装 unzip-iconv。Ubuntu 12.04 里面的 unzip 是有这个参数的。



### 解决方案二： 7Z解压

安装 7zip 和 convmv

```shell
# Arch 下
sudo pacman -S p7zip 
sudo pacman -S convmv

# ubuntu 下
sudo apt-get install p7zip convmv
```

安装完之后，就可以用 7za 和 convmv 两个命令完成解压缩任务。

```shell
# 解压缩，LANG=C 表示以 US-ASCII 这样的编码输出文件名，如果没有这个语言设置，它同样会输出乱码，只不过是UTF8格式的乱码(convmv 会忽略这样的乱码)
LANG=C 7za x your-zip-file.zip

# 将GBK编码的文件名转化为UTF8编码，-r 表示递归访问目录，即对当前目录中所有文件进行转换
convmv -f GBK -t utf8 --notest -r .
```



### 解决方案三: python 脚本

此方案目前来看非常完美。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import zipfile

#print "Processing File " + sys.argv[1]

file=zipfile.ZipFile(sys.argv[1],"r");
for name in file.namelist():
    utf8name=name.decode('gbk')
#    print "Extracting " + utf8name
    pathname = os.path.dirname(utf8name)
    if not os.path.exists(pathname) and pathname!= "":
        os.makedirs(pathname)
    data = file.read(name)
    if not os.path.exists(utf8name):
        fo = open(utf8name, "w")
        fo.write(data)
        fo.close()
file.close()
```

 Windows 用户屏蔽两条 print 语句，Linux 用户不用屏蔽





## 参考
- [博客园 - jihite - Linux 下 zip 文件解压乱码如何解决](https://www.cnblogs.com/kaituorensheng/p/12296439.html)
- [知乎 - Linux 下 zip 文件解压乱码如何解决？](https://www.zhihu.com/question/20523036)
- [博客园 - CarsonFan - 解决Linux下zip文件解压乱码问题](https://www.cnblogs.com/xmzncc/p/6060185.html)

