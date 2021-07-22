----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Locust 的安装{#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-07-16 | Herolh | 文档创建 |
|            |        |          |





## 前期准备

支持的python版本：2.7、3.4、3.5、3.6；



## Windows 下安装

### 直接通过命令安装

```shell
pip install locustio
```



### 源码安装

通过为pyzmq、gevent和greenlet安装预先构建的二进制包，然后在[这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/)找到非官方的预制包，下载.whl文件后，使用 pip install name-of-file.whl 命令安装；

安装成功后可以输入 pip show locust 命令查看是否安装成功，以及通过 locust -help 命令查看帮助信息。

**PS**：运行大规模测试时，建议在 Linux 机器上执行此操作，因为gevent在 Windows 下的性能很差。



## Arch 下安装

```shell
sudo pip in
```







