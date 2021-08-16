----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# sqlc 的使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2020-07-28 | Herolh | 文档创建 |
|            |        |          |



## 简介

![image-20210801161001819](.assets/image-20210801161001819.png)

[官网](https://sqlc.dev/)

[github 仓库](https://github.com/kyleconroy/sqlc)

sqlc generates fully-type safe idiomatic Go code from SQL.

> Sqlc 从 SQL 生成完全类型的安全地址转换代码。

1. You write SQL queries 

   >  编写 SQL 查询

2. You run sqlc to generate Go code that presents type-safe interfaces to those queries 

   >  您可以运行 sqlc 来生成 Go 代码，该代码为这些查询提供类型安全的接口

3. You write application code that calls the methods sqlc generated. 

   > 您编写调用生成的 sqlc 方法的应用程序代码

Seriously, it's that easy. You don't have to write any boilerplate SQL querying code ever again. Read more in the [introduction](https://conroy.org/introducing-sqlc).

说真的，就这么简单。您不必再编写任何样板化 SQL 查询代码。更多内容请参阅介绍。



## 安装

[官方安装文档](https://docs.sqlc.dev/en/latest/overview/install.html)

### LInux 

#### arch 下安装

```shell
go get github.com/kyleconroy/sqlc/cmd/sqlc
```

加入环境变量:

```shell
# 根据实际情况
export PATH=$PATH:/usr/local/go/bin
export PATH=$PATH:/usr/local/go/project/bin
```



#### debian 系列

```shell
sudo snap install sqlc
```





### macOS

```shell
brew install sqlc
```



### windows 

> 因为 `sqlc` 用到了一个 linux 下的库，在 windows 上无法正常编译。在 windows 上我们可以使用 docker 镜像 `kjconroy/sqlc`。

```shell
docker pull kjconroy/sqlc
```

Run `sqlc` using `docker run`:

```shell
docker run --rm -v $(pwd):/src -w /src kjconroy/sqlc generate
```





## 使用

[Go 每日一库之 sqlc](https://darjun.github.io/2020/04/28/godailylib/sqlc/)

```shell
# 查看帮助
sqlc help
Usage:
  sqlc [command]

Available Commands:
  compile     Statically check SQL for syntax and type errors	# 检查 SQL 语法和类型错误
  generate    Generate Go code from SQL							# 错误减价并根据 SQL 生成 golang 代码
  help        Help about any command							# 查看帮助
  init        Create an empty sqlc.yaml settings file			# 创建一个空的 sqlc.yaml 代码
  version     Print the sqlc version number						# 查看版本

Flags:
  -x, --experimental   enable experimental features (default: false)
  -f, --file string    specify an alternate config file (default: sqlc.yaml)
  -h, --help           help for sqlc

Use "sqlc [command] --help" for more information about a command.
```



### 初始化 配置

> [配置相关文档](https://docs.sqlc.dev/en/latest/reference/config.html)

```shell
sqlc init
```

生成的文件

```yaml
version: "1"
packages: []
```



#### 可配置项

