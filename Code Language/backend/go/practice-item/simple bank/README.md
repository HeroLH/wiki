----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Go + Postgres + Docker 实现银行转账功能 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-07-29 | Herolh | 文档创建 |
|            |        |          |



## 简介

[github 仓库](https://github.com/techschool/simplebank)

[youtube 视频教程](https://www.youtube.com/playlist?list=PLy_6D98if3ULEtXtNSY_2qN21VCKgoQAE)

> In this backend master class, we’re going to learn everything about how to design, develop, and deploy a complete backend system from scratch using Golang, PostgreSQL, and Docker.
>
> 在这个后端大师课程中，我们将学习如何使用 Golang、 PostgreSQL 和 Docker 从头开始设计、开发和部署一个完整的后端系统。

![Backend master class](.assets/backend-master.png)

The service that we’re going to build is a simple bank. It will provide APIs for the frontend to do following things:
> 我们要建立的服务是一个简单的银行。它将为前端提供以下功能的 api:

1. Create and manage bank accounts, which are composed of owner’s name, balance, and currency. 
   
   > 创建和管理银行账户，这些账户由所有者的姓名、余额和货币组成
   
2. Record all balance changes to each of the account. So every time some money is added to or subtracted from the account, an account entry record will be created. 
   
   >  记录每个账户的所有余额变化。因此，每当一些钱被添加或减去的帐户，一个帐户分录记录将被创建
   
3. Perform a money transfer between 2 accounts. This should happen within a transaction, so that either both accounts’ balance are updated successfully or none of them are. 
   
   >  在两个账户之间进行转账。这应该发生在一个事务中，这样，要么两个账户的余额都更新成功，要么它们都不更新



## Lesson 1 数据库设计

[数据库设计工具 dbdiagram](https://dbdiagram.io)



### 设计语言:

```sql
// 创建帐户
Table account as A {
  id bigint [pk, increment] // auto-increment
  owner varchar [not null]
  balance bigint [not null]
  currency varchar [not null]
  created_at timestamptz [not null, default: `now()`] 

  Indexes {
    owner
  }
}

// 创建条目
Table entries {
  id bigint [pk]
  account_id bigint [ref: > A.id]
  amount bigint [not null, note: 'can be negative or positive'] // +/-
  created_at timestamptz [not null, default: `now()`] 
  
  Indexes {
    account_id
  }
}

// 转移表
Table transfers {
  id bigint [pk]
  from_account_id bigint [ref: > A.id]
  to_account_id bigint [ref: > A.id]
  amount bigint [not null,note: 'must be positive'] // must +
  created_at timestamptz [not null, default: `now()`] 

  Indexes {
    from_account_id
    to_account_id
    (from_account_id, to_account_id)
  }
}

Enum currency {
  USD // 美元
  EUR // 欧元
  RMB // 人民币
}

```



### 表展示

https://dbdiagram.io/embed/60feb50328da596eb54d9cc5

![image-20210731231527171](.assets/image-20210731231527171.png)



### 导出 sql 文件

略



## Lesson 2 使用 Docker + Postgres 创建 DB 

- **docker 的安装(略)**

- **拉取 postgresql 镜像**

  ```shell
  docker pull postgres:12-alpine
  ```

- **启动 postgresql 容器**

  ```shell
  docker run --name postgres12 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:12-alpine
  ```

  - 进入 postgres 控制台

    ```shell
    docker exec -it postgres12 psql -U root 
    # 默认情况下, Postgres 容器在本地设置信任身份验证, 所以冲本地主机连接时不需要密码
    ```

  - 遇到问题可查看容器日志排错

    ```shell
    docker logs postgres12
    ```

- **使用工具链接 postsgres**

  ![image-20210801000542462](.assets/image-20210801000542462.png)

- **执行导出的 sql 语句创建表**

  ![image-20210801000727613](.assets/image-20210801000727613.png)





## Lesson 3 为 Go 编写和运行数据库迁移

[goland-migrate 的 github 仓库](https://github.com/golang-migrate/migrate)

![image-20210801144223383](.assets/image-20210801144223383.png)

- **项目创建迁移文件**

  ```shell
  migrate create -ext sql --dir db/migration -seq init_schema
  ```

  生成两个文件: `000001_init_schema.up.sql`, `000001_init_schema.down.sql`

- **填入迁移文件内容**

  - x.up.sql

    ```sql
    CREATE TABLE "accounts" (
                               "id" BIGSERIAL PRIMARY KEY,
                               "owner" varchar NOT NULL,
                               "balance" bigint NOT NULL,
                               "currency" varchar NOT NULL,
                               "created_at" timestamptz NOT NULL DEFAULT (now())
    );
    
    CREATE TABLE "entries" (
                               "id" bigint PRIMARY KEY,
                               "account_id" bigint,
                               "amount" bigint NOT NULL,
                               "created_at" timestamptz NOT NULL DEFAULT (now())
    );
    
    CREATE TABLE "transfers" (
                                 "id" bigint PRIMARY KEY,
                                 "from_account_id" bigint,
                                 "to_account_id" bigint,
                                 "amount" bigint NOT NULL,
                                 "created_at" timestamptz NOT NULL DEFAULT (now())
    );
    
    ...
    ```

  - x.down.sql

    ```sql
    DROP table if exists entries;
    DROP table if exists transfers;
    -- 外键关联,需最后删除
    DROP table if exists accounts;
    ```

- **执行迁移脚本**

  ```shell
  # migrate up
  migrate -path db/migration -database "postgresql://root:secret@localhost:5432/simple_bank?sslmode=disable" -verbose up
  
  # migrate down
  migrate -path db/migration -database "postgresql://root:secret@localhost:5432/simple_bank?sslmode=disable" -verbose down
  ```

  

为方便执行命令, 创建 Makefile 文件

```shell
postgres:
	docker run --name postgres12 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -d postgres:12-alpine

createdb:
	docker exec -it postgres12 createdb --username=root --owner=root simple_bank

dropdb:
	docker exec -it postgres12 dropdb simple_bank

migrateup:
	migrate -path db/migration -database "postgresql://root:secret@localhost:5432/simple_bank?sslmode=disable" -verbose up

migratedown:
	migrate -path db/migration -database "postgresql://root:secret@localhost:5432/simple_bank?sslmode=disable" -verbose down


.PHONY: postgres createdb dropdb migrateup migratedown
```



## Lesson 4 使用 sqlc 从 SQL 生成 crud 代码 

### 比较 db/SQL，gorm，sqlx & sqlc

![image-20210801153738512](.assets/image-20210801153738512.png)



#### database/sql

[goland 官方包文档](https://pkg.go.dev/database/sql#section-documentation)

##### 优点

- 运行十分快 & 编写代码十分简单.

##### 缺点

- 必须手动将 SQL 字段映射到变量,这很无聊也很容易出错.
- 出问题只能在运行时报错.



#### GORM

[官方使用文档](https://gorm.io/docs/)

##### 优点

- 使用方便,所有的 CRUD 操作都已经实现, 生产代码会很短, 只需要声明模型, 并调用 gorm 提供的函数

##### 缺点

- 必须学习如何使用 gorm 提供的函数编写查询,有一定学习成本.

- 当流量很高时, 它运行很慢, 比标准库慢 3-5 倍



#### sqlx

[goland 官方包文档](https://pkg.go.dev/github.com/jmoiron/sqlx)

##### 优点

- 运行速度几乎和标准库一样快
- 有字段映射,通过查询文本或结构体标签来完成, 提供蓝一些函数将结果自动扫描到结构体字段中

- 比 database/sql 代码更短,减少了部分的潜在错误

##### 缺点

- 要写的代码还是很长
- 查询中的任何错误只会在运行时被捕获



#### sqlc

![image-20210801160906392](.assets/image-20210801160906392.png)

[官网](https://sqlc.dev/)

[官方文档](https://docs.sqlc.dev/en/latest/index.html)

##### 优点

- 运行速度几乎和标准库一样快,易于使用
- 只需要编写 SQL 查询, golang CRUD 代码会自动为我们生成
- 任何错误会被发现并立刻报告

##### 缺点

- 只完全支持 Postgres, Mysql 仍处于试验阶段(2021-02-01)



### 使用

![image-20210801174914961](.assets/image-20210801174914961.png)

- **初始化 sqlc 配置**

  ```shell
  sqlc init
  ```

- **写入项目配置**

  ```yaml
  version: "1"
  packages:
    - name: "db"
      path: "./db/sqlc/db"
      queries: "./db/sqlc/sql/"
      schema: "./db/migration/"
      engine: "postgresql"
      emit_json_tags: true
      emit_prepared_queries: false
      emit_exact_table_names: false
      emit_interface: true
      emit_empty_slices: true
  ```

  | 字段                   |      名称      | 描述                                                         |
  | ---------------------- | :------------: | ------------------------------------------------------------ |
  | name                   |                | 要用于生成代码的包名。默认为 `path` 的基础包名               |
  | path                   |                | 生成代码的输出目录                                           |
  | queries                |                | SQL 查询目录或单个 SQL 文件的路径；或路径列表                |
  | schema                 |                | SQL 迁移目录或单个 SQL 文件的路径；或路径列表                |
  | engine                 |                | 默认支持 postgresql, MySQL 是实验性的                        |
  | emit_db_tags           |      标签      | 如果为 true，则向生成的结构添加 DB 标记。默认值为 false      |
  | emit_prepared_queries  |  生成预备查询  | 如果为真，则包含对生成已准备好的查询的支持。默认为 false     |
  | emit_interface         |      接口      | 如果为真，则在生成的包中输出一个 Querier 接口。默认为 false  |
  | emit_exact_table_names | 输出精确的表名 | 如果为真，则 struct names 将镜像表名。<br />否则，sqlc 将尝试单数化复数表名。默认值为 false |
  | emit_empty_slices      |     空切片     | 如果为 true，由 `:many` 返回的片将为空列表，而不是 nil。默认值为 false |
  | emit_json_tags         |   json 标签    | 如果为 true，则向生成的结构添加 JSON 标记。默认为 false      |
  | json_tags_case_style   | 标签大小写样式 | camelCase 使用 camel，<br />PascalCase 使用 pascal，<br />snake 使用 snake _ case，<br />或者在 DB 中不使用列名。默认为零。 |

- **编写 SQL**

  ```shell
  -- name: CreateAccount :one
  INSERT INTO accounts (owner, balance, currency)
  VALUES ($1, $2, $3) RETURNING *;
  
  -- name: UpdateAccount :one
  UPDATE accounts
  SET balance = $2
  WHERE id = $1
  RETURNING *;
  
  -- name: DeleteAccount :exec
  DELETE FROM accounts
  WHERE id = $1;
  
  -- name: GetAccount :one
  SELECT *
  FROM accounts
  WHERE id = $1 LIMIT 1;
  
  -- name: ListAccounts :many
  SELECT *
  FROM accounts
  WHERE owner = $1
  ORDER BY id LIMIT $2
  OFFSET $3;
  ```

- **生成 CRUD 代码**

  ```shell
  sqlc generate
  ```





## Lesson 5 为数据库 CRUD 编写单元测试

使用到的库:

```shell
github.com/stretchr/testify/require
```





## Lesson 6 在 Golang 实现数据库事务的干净方法

![image-20210801214556336](.assets/image-20210801214556336.png)

![image-20210801214709678](.assets/image-20210801214709678.png)

在上面的代码中, 查询结构( Queries ) 仅对一个特定表执行 1 次操作, 所以查询结构不支持事务, 所以我们需要扩展其功能:

























