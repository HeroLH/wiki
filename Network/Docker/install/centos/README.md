----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Centos 下安装 Docker {#index}

[TOC]











## 环境查看

```shell
uname -r					# 查看系统内核
cat /etc/os-release 		# 查看系统版本
```



## 安装

> [官方帮助文档](https://docs.docker.com/engine/install/centos/)

```shell
" 1、卸载旧的版本
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
                  
" 2、需要的安装包
sudo yum install -y yum-utils

" 3、设置镜像的仓库
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

" 更新yum软件包索引
yum makecache fast

" 4、安装docker相关的源 docker-ce 社区 ee 企业版
yum install docker-ce docker-ce-cli containerd.io

" 5、启动docker
systemctl start docker

" 6、使用 docker version 查看是否安装成功
docker version

" 7、下载运行镜像
docker run hello-world

" 8、查看下载的这个 hello-world 镜像
docker images
```



## 卸载 docker

```shell
" 1、依赖卸载
yum remove docker-ce docker-ce-cli containerd.io

" 2、删除资源
rm -rf /var/lib/docker
" /var/lib/docker docker 的默认工作路径
```

