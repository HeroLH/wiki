----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# {Title} {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-06-28 | Herolh | 文档创建 |
|            |        |          |



## 安装

### Arch 下

> [Arch 系 Linux 中安装 Docker](https://www.cnblogs.com/kainhuck/p/12292767.html)
> [Archlinux下安装docker、docker-compose、TiDB](https://www.jianshu.com/p/1edc97bfbaa6)



#### 下载最新版 docker

```shell
sudo pacman -S docker
```

- 免 sudo 执行 docker

  ```shell
  sudo gpasswd -a ${USER} docker		# 将当前用户添加至docker用户组
  newgrp docker                 		# 更新docker用户组
  
  " 需重启docker
  sudo systemctl restart docker
  
  " 开机自起docker(可选)
  sudo systemctl enable docker
  ```

  

#### 配置 docker 国内镜像

​	在 `/etc/docker` 目录下新建 `daemon.json` 文件,写入下面内容(网易镜像)

```shell
{
	"registry-mirrors": ["http://hub-mirror.c.163.com"]
}
```

其他源：

```shell
{
   "registry-mirrors":["https://zyojraje.mirror.aliyuncs.com"]
}
```



##### 更新源

```shell
sudo systemctl daemon-reload
sudo systemctl restart docker
```



#### 安装docker-compose

```shell
sudo pacman -S docker-compose
```





#### Arch 下面删除 Docker

```shell
" 删除Docker包，同时删除其依赖的包。
sudo pacman -Rns docker

" 删除Docker运行过程中产生的镜像、容器等文件。用户生成的配置文件需要手工删除。
rm -rf /var/lib/docker
```







### Centos 下

#### 环境查看

```shell
uname -r					# 查看系统内核
cat /etc/os-release 		# 查看系统版本
```



#### 安装

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



#### 卸载 docker

```shell
" 1、依赖卸载
yum remove docker-ce docker-ce-cli containerd.io

" 2、删除资源
rm -rf /var/lib/docker
" /var/lib/docker docker 的默认工作路径
```



### Mac 下

- [官网下载](https://docs.docker.com/desktop/mac/install/).
-  [阿里云镜像源](http://mirrors.aliyun.com/docker-toolbox/mac/docker-for-mac/) 

下载成功后双击打开安装, 打开docker，在终端输入 `docker info`、`docker version` 可查看基本信息。



### Window 下





















