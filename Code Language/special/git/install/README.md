> *Made By Herolh*

----------------------------------------------

# 安装与升级 {#index}

[TOC]











--------------------------------------------

## Centos 7

### Centos 下升级 git 版本

> [Centos下升级git版本](https://blog.csdn.net/qq_28903377/article/details/86148687)

centos7.5一般自带的git都是1.8.3.1版本的，比较老了，所以有时候需要升级一下git版本



#### 安装依赖软件

```shell
yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel asciidoc
yum install  gcc perl-ExtUtils-MakeMaker
```



#### 卸载系统自带的低版本git

```shell
yum remove git
```



#### 编译安装最新的git版本

```shell
cd /usr/local/src/

wget https://www.kernel.org/pub/software/scm/git/git-2.15.1.tar.xz

tar -vxf git-2.15.1.tar.xz

cd git-2.15.1

make prefix=/usr/local/git all
make prefix=/usr/local/git install

echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/profile

source /etc/profile
git --version
```

