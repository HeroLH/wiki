----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# {Title} {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-07-30 | Herolh | 文档创建 |
|            |        |          |





## 简介

[Github](https://github.com/kyleconroy/sqlc)

[Go 每日一库之 sqlc](https://darjun.github.io/2020/04/28/godailylib/sqlc/)

`sqlc`可以根据我们编写的 SQL 语句生成类型安全的、地道的 Go 接口代码，我们要做的只是调用这些方法。





## 安装

### arch 下

- 安装 sqlc

    ```shell
    go get github.com/kyleconroy/sqlc/cmd/sqlc
    
    # 上面代码会将可执行程序 sqlc 放到 $GOPATH/bin 目录下。我习惯把 $GOPATH/bin 目录加入到系统 PATH 中。如果没有的可以执行第三步
    ```

- 安装对应的数据库驱动

    ```shell
    # postgresql 驱动
    go get github.com/lib/pq
    # mysql 驱动
    go get github.com/go-sql-driver/mysql
    ```

- 将 sqlc 加入环境变量

    ```shell
    vim /etc/profile
    
    # 追加内容， ~/project/go/bin 根据情况更改
    export PATH=$PATH:~/project/go/bin
     
    # 生效：
    source /etc/profile
    ```





### window 下

因为 sqlc 用到了一个 linux 下的库，在 windows 上无法正常编译。在 windows 上我们可以使用 docker 镜像`kjconroy/sqlc`。拉取镜像：

```shell
docker pull kjconroy/sqlc
```





## 使用