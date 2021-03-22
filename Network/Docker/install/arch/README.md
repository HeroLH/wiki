----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











# 安装

> [Arch 系 Linux 中安装 Docker](https://www.cnblogs.com/kainhuck/p/12292767.html)
> [Archlinux下安装docker、docker-compose、TiDB](https://www.jianshu.com/p/1edc97bfbaa6)



## 下载最新版 docker

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

    

## 配置 docker 国内镜像

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



更新源

```shell
sudo systemctl daemon-reload
sudo systemctl restart docker
```



## 安装docker-compose

```shell
sudo pacman -S docker-compose
```





# Arch 下面删除 Docker

```shell
" 删除Docker包，同时删除其依赖的包。
sudo pacman -Rns docker

" 删除Docker运行过程中产生的镜像、容器等文件。用户生成的配置文件需要手工删除。
rm -rf /var/lib/docker
```







