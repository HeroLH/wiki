----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Mysql 的安装 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-09-15 | Herolh | 文档创建 |
|            |        |          |



## 简介





## 安装

### Docker 下

> [参考教程原文地址](https://www.cnblogs.com/sablier/p/11605606.html)

#### 建立镜像

[DockerHub MySQL 文档地址](https://hub.docker.com/_/mysql/)

- 拉取官方镜像（我们这里选择5.7，如果不写后面的版本号则会自动拉取最新版）

    ```shell
    docker pull mysql:5.7   # 拉取 mysql 5.7
    docker pull mysql       # 拉取最新版mysql镜像
    ```

- 检查是否拉取成功

    ```shell
    sudo docker images
    ```

- 运行容器

    ```shell
    sudo docker run -p 3306:3306 --name mysql57 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
    
    # –name：容器名，此处命名为mysql
    # -e：配置信息，此处配置mysql的root用户的登陆密码
    # -p：端口映射，此处映射 主机3306端口 到 容器的3306端口
    # -d：后台运行容器，保证在退出终端后容器继续运行
    ```

    一般来说数据库容器不需要建立目录映射，如果要建立目录映射：

    ```shell
    duso docker run -p 3306:3306 --name mysql57 \
    -v /usr/local/docker/mysql/conf:/etc/mysql \
    -v /usr/local/docker/mysql/logs:/var/log/mysql \
    -v /usr/local/docker/mysql/data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=123456 \
    -d mysql:5.7
    
    # -v：主机和容器的目录映射关系，":"前为主机目录，之后为容器目录
    ```

- 检查容器是否正确运行

    ```shell
    docker container ls
    ```



#### 连接 mysql

- 进入 docker 本地连接 mysql 客户端

    ```shell
    sudo docker exec -it mysql57 bash
    mysql -uroot -p123456
    ```

- 使用远程连接软件时要注意一个问题, 我们在创建容器的时候已经将容器的3306端口和主机的3306端口映射到一起，所以我们应该访问：

    ```shell
    host: 127.0.0.1
    port: 3306
    user: root
    password: 123456
    ```

- 如果你的容器运行正常，但是无法访问到MySQL，一般有以下几个可能的原因：

    - 防火墙阻拦

        ```shell
        # 开放端口：
        $ systemctl status firewalld
        $ firewall-cmd  --zone=public --add-port=3306/tcp -permanent
        $ firewall-cmd  --reload
        # 关闭防火墙：
        $ sudo systemctl stop firewalld
        ```

    - 需要进入 docker 本地客户端设置远程访问账号

        ```shell
        $ sudo docker exec -it mysql57 bash
        $ mysql -uroot -p123456
        mysql> grant all privileges on *.* to root@'%' identified by "password";
        ```

        

#### 出现问题

###### `/var/lib/mysql` 权限问题

> mysqld: Can't create/write to file '/var/lib/mysql/is_writable' (Errcode: 13 - Permission denied)

创建容器改为

```shell
sudo docker run -p 3306:3306 --name mysql5 -v /data/mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7

# cd /data 中添加权限
chomd -R 777 mysql-data/
```

