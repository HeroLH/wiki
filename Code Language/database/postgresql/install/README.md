----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Postgresql 的安装 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-07-26 | Herolh | 文档创建 |
|            |        |          |



## Arch 下安装

> [wiki](https://wiki.archlinux.org/title/PostgreSQL_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
> [博客园 - Lemo_wd - archlinux 使用 postgresql](https://www.cnblogs.com/lemos/p/11605557.html)

```shell
sudo pacman -S postgresql
```



### 初始化数据目录

- 切换到 postgres 用户

  ```shell
  sudo -iu postgres
  ```

- 数据目录初始化

  ```shell
  initdb --locale=zh_CN.UTF-8 -E UTF8 -D/var/lib/postgres/data
  ```

- 退出此用户，启动服务 `postgresql.service`

  ```shell
  systemctl enable postgresql.service
  systemctl start postgresql.service
  ```



### 创建用户与数据库

> **提示：** 如果创建一个与你的 Arch 用户 ($USER) 同名的数据库用户，并允许其访问 PostgreSQL 数据库的 shell，那么在使用PostgreSQL 数据库 shell 的时候无需指定用户登录（这样做会比较方便）。

再次进入 `sudo -iu postgres`

- 添加新的数据库用户

  ```shell
  createuser --interactive
  ```

- 创建数据库

  ```shell
  createdb --username=root --owner=root myDatabaseName
  ```

  

