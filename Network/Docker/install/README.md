----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Docker 安装文档 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-06-28 | Herolh | 文档创建 |
|            |        |          |



## 安装

帮助文档：https://docs.docker.com/engine/install/





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

" 4、安装docker相关的源，docker-ce 是社区版，docker-ee 企业版
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





### ubuntu 下

#### 前期准备

- 由于apt官方库里的docker版本可能比较旧，所以先卸载可能存在的旧版本：

    ```shell
    sudo apt-get remove docker docker-engine docker-ce docker.io
    # 更新apt包索引
    sudo apt-get update
    ```

- 安装以下包以使 apt 可以通过 HTTP S使用存储库（repository）：

    ```shell
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    ```

- 添加Docker官方的GPG密钥：

    ```shell
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```

- 使用下面的命令来设置stable存储库：

    ```shell
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```

- 再更新一下apt包索引：

    ```shell
    sudo apt-get update
    ```



#### 安装

- 安装最新版本的Docker CE：

    ```shell
    sudo apt-get install -y docker-ce
    ```

- 在生产系统上，可能会需要应该安装一个特定版本的Docker CE，而不是总是使用最新版本：

    - 列出可用的版本：

        ```shell
        apt-cache madison docker-ce
        ```

    - 选择要安装的特定版本，第二列是版本字符串，第三列是存储库名称，它指示包来自哪个存储库，以及扩展它的稳定性级别。要安装一个特定的版本，将版本字符串附加到包名中，并通过等号(=)分隔它们：

        ```shell
        sudo apt-get install docker-ce=<VERSION>
        ```

    

####  验证docker

- 查看docker服务是否启动：

    ```shell
    systemctl status docker
    ```

- 若未启动，则启动docker服务：

    ```shell
    sudo systemctl start docker
    ```

- 经典的hello world：

    ```shell
    sudo docker run hello-world
    ```

    



### Mac 下

- [官网下载](https://docs.docker.com/desktop/mac/install/).
-  [阿里云镜像源](http://mirrors.aliyun.com/docker-toolbox/mac/docker-for-mac/) 

下载成功后双击打开安装, 打开docker，在终端输入 `docker info`、`docker version` 可查看基本信息。



### Window 下



## 常见问题

### 修改Docker数据目录位置，包含镜像位置

[修改Docker数据目录位置，包含镜像位置](https://www.cnblogs.com/hellxz/p/docker-change-data-root.html)



#### 为啥要改？

Docker 安装后默认下载的位置在 `/var/lib/docker` ，如果 `/var` 分区没有独立分出来，Linux下默认是与 `/` 根分区在一起。一般我们装 Linux 系统的时候，除了做邮件服务器外，都不会把 /var分区独立分出来，而且 `/` 分区一般不会太大，比如我现在用的这台根分区30G的，在拉镜像的时候提示硬盘空间不足的问题，而其它分区还有很大空间。基于此情此景，我们都要把这个目录改一下。



#### 查看当前Docker目录位置

```shell
#展示当前docker的配置信息
docker info
-------------------------------------------------------------------
#在信息找到Docker Root Dir，对应的就是了，默认为：
Docker Root Dir: /var/lib/docker
```



#### 修改 `/etc/docker/daemon.json`

```shell
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"],
  "data-root": "/home/hellxz/docker-home"
}
```

保存退出，重启 docker 服务

```shell
sudo systemctl restart docker
```



#### 验证

查看 `docker info`

![img](.assets/1149398-20190704161019154-2144727749.png)



















