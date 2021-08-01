----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# golang-migrate 的使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-08-01 | Herolh | 文档创建 |
|            |        |          |



## 简介

> **Database migrations written in Go. Use as [CLI](https://github.com/golang-migrate/migrate#cli-usage) or import as [library](https://github.com/golang-migrate/migrate#use-in-your-go-project).**  
> 用 Go 编写的数据库迁移。作为 CLI 使用或作为库导入。



## 安装

[github 仓库](https://github.com/golang-migrate/migrate/tree/master/cmd/migrate)

### linux 系列

#### arch 下

```shell
yay -S migrate
```



#### debian 系列

```shell
curl -L https://packagecloud.io/golang-migrate/migrate/gpgkey | apt-key add -
echo "deb https://packagecloud.io/golang-migrate/migrate/ubuntu/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/migrate.list
apt-get update
apt-get install -y migrate
```





### MacOS

```
$ brew install golang-migrate
```



### Windows

Using [scoop](https://scoop.sh/)

```
$ scoop install migrate
```



## 使用

```shell
migrate help

Options:
  -source          Location of the migrations (driver://url)
  -path            Shorthand for -source=file://path
  -database        Run migrations against this database (driver://url)
  -prefetch N      Number of migrations to load in advance before executing (default 10)
  -lock-timeout N  Allow N seconds to acquire database lock (default 15)
  -verbose         Print verbose logging
  -version         Print version
  -help            Print usage

Commands:
  create [-ext E] [-dir D] [-seq] [-digits N] [-format] NAME
           Create a set of timestamped up/down migrations titled NAME, in directory D with extension E.
           Use -seq option to generate sequential up/down migrations with N digits.
           Use -format option to specify a Go time format string. Note: migrations with the same time cause "duplicate
migration version" error.

  goto V       Migrate to version V
  up [N]       Apply all or N up migrations
  down [N]     Apply all or N down migrations
  drop [-f] [-all]    Drop everything inside database
        Use -f to bypass confirmation
        Use -all to apply all down migrations
  force V      Set version V but don't run migration (ignores dirty state)
  version      Print current migration version

Source drivers: go-bindata, gcs, s3, github, github-ee, gitlab, godoc-vfs, file, bitbucket
Database drivers: mysql, spanner, sqlserver, stub, clickhouse, mongodb, mongodb+srv, firebird, neo4j, redshift, cassandra, cockroach, postgresql, postgres, cockroachdb, crdb-postgres, firebirdsql
```































