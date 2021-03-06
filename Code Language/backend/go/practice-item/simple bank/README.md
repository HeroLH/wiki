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



## Lesson 7 DB 事务锁 & 如何处理 Golang 的死锁

> 修复由外键引起的死锁 => `FOR NO KEY UPDATE`

```sql
BEGIN;

INSERT INTO transfers (from_account_id,to_account_id,amount) VALUES (1, 2, 10) RETURNING *;

INSERT INTO entries (account_id, amount) VALUES (1, -10) RETURNING *;
INSERT INTO entries (account_id, amount) VALUES (2, 10) RETURNING *;

SELECT * FROM accounts WHERE id = 1 LIMIT 1 FOR UPDATE;
UPDATE accounts SET balance = 90 WHERE id = 1 RETURNING *;

SELECT * FROM accounts WHERE id = 2 LIMIT 1 FOR UPDATE;
UPDATE accounts SET balance = 90 WHERE id = 2 RETURNING *;

ROLLBACK;
```

查看 postgresql 锁

```shell
  SELECT blocked_locks.pid     AS blocked_pid,
         blocked_activity.usename  AS blocked_user,
         blocking_locks.pid     AS blocking_pid,
         blocking_activity.usename AS blocking_user,
         blocked_activity.query    AS blocked_statement,
         blocking_activity.query   AS current_statement_in_blocking_process
   FROM  pg_catalog.pg_locks         blocked_locks
    JOIN pg_catalog.pg_stat_activity blocked_activity  ON blocked_activity.pid = blocked_locks.pid
    JOIN pg_catalog.pg_locks         blocking_locks 
        ON blocking_locks.locktype = blocked_locks.locktype
        AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
        AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
        AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
        AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
        AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
        AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
        AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
        AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
        AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
        AND blocking_locks.pid != blocked_locks.pid

    JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
   WHERE NOT blocked_locks.granted;
```



查看进程

```shell
SELECT
	pa.datname,      						-- 数据库名称
	pa.pid,											-- 
	pa.application_name,				-- 哪个进程在使用
	pa.usename,									-- 运行查询的用户名
	l.relation :: regclass,			-- 表的名称
	l.transactionid,						-- 交易 ID
	l.MODE,											-- 锁的 mod
	l.locktype,									-- 锁的类型
	l.GRANTED,									-- 锁的类新
	pa.query,										-- 持有或试图获取锁的查询
	pa.query_start, 						-- 锁开始的时间
	age(now(), pa.query_start) as "age" 			-- 持有锁的时间
FROM
	pg_stat_activity pa
	JOIN pg_locks l ON l.pid = pa.pid 
ORDER BY
	pa.pid
```





## Lesson 8 如何避免 DB 事务中的死锁？查询顺序问题

> 防止死锁最好的方法是通过确保我们的应用程序总是以一致的顺序获得锁.

会导致死锁

```sql
-- Tx1: transfer $10 from account1 to account2
BEGIN;		-- 1
UPDATE accounts SET balance = balance - 10 WHERE id = 1 RETURNING *; -- 2
UPDATE accounts SET balance = balance + 10 WHERE id = 2 RETURNING *; -- 5 死锁
ROLLBACK;


-- Tx2: transfer $10 from account2 to account1
BEGIN;  -- 3
UPDATE accounts SET balance = balance - 10 WHERE id = 2 RETURNING *; -- 4
UPDATE accounts SET balance = balance + 10 WHERE id = 1 RETURNING *;
ROLLBACK;
```



解死锁

```sql
-- Tx1: transfer $10 from account1 to account2
BEGIN; -- 1
UPDATE accounts SET balance = balance - 10 WHERE id = 1 RETURNING *; -- 2
UPDATE accounts SET balance = balance + 10 WHERE id = 2 RETURNING *; -- 5
ROLLBACK; -- 6


-- Tx2: transfer $10 from account2 to account1
BEGIN; -- 3
UPDATE accounts SET balance = balance + 10 WHERE id = 1 RETURNING *; -- 4, 锁住
UPDATE accounts SET balance = balance - 10 WHERE id = 2 RETURNING *; -- 7, 解锁
ROLLBACK; -- 8
```



## Lesson 9 深入理解 MySQL 和 PostgreSQL 中的事务隔离级别和读现象

[数据库事务隔离级别](https://blog.csdn.net/jim_cainiaoxiaolang/article/details/72832217)

&emsp;&emsp;**事务隔离（isolation）**定义了数据库系统中一个操作产生的影响什么时候以哪种方式可以对其他并发操作可见。隔离是事务 ACID (原子性、一致性性、隔离性、持久性) 四大属性中的一个重要属性。



### 读现象

![image-20210803213336558](.assets/image-20210803213336558.png)

- **脏读**

    > 事务1 读到其他尚未提交的并发事务2 写入的数据(其他事务2 可能被回滚)

- **不可重复读**

    > 一个事务两次读取同一条记录并看到不同的值时

- **幻影读**

    > 影响搜索多行而不是一行的查询. 重复执行相同的查询,但返回一组不同的行

- **序列化异常**

    > 当一组并发提交事务的结果无法实现时, 如果我们尝试以任何顺序依次运行他们而不互相重叠.



### 事务隔离等级

![image-20210808113313093](.assets/image-20210808113313093.png)

#### 读取未提交

> 可以看到其他未提交事务写入的数据，从而允许脏读现象

- 事务一

    ```sql
    -- 1: 开启事务
    begin；
    
    -- 3: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 5： 更新表数据
    update account set balance = balance - 10 where id = 1;
    
    -- 6: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    ```

- 事务二

    ```sql
    -- 2: 开启事务
    begin;
    
    -- 4: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    
    -- 7: 查询数据(脏读)
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    ```



#### 读提交

> 只能看到其他事务已提交的数据

- 事务一

    ```sql
    -- 1: 开启事务
    begin；
    
    -- 3: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 5： 更新表数据
    update account set balance = balance - 10 where id = 1;
    
    -- 6: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    
    -- 8: 提交事务
    commit;
    
    -- 9: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    ```

- 事务二

    ```sql
    -- 2: 开启事务
    begin;
    
    -- 4: 查询数据
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    
    -- 7: 查询数据(脏读不存在)
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 10: 查询数据（不可重复读）
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    
    -- 11: 查询数据（幻读）
    select * from account where balance = 100;
    -- 之前返回 1 条， 现在返回 0 条
    ```

    



#### 可重复读取

> 相同的选择查询将始终返回相同的结果，无论执行了多少次，即使一些并发事务的新更改满足查询

- 事务一

    ```sql
    -- 1: 开启事务
    begin；
    
    -- 3: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 5： 更新表数据
    update account set balance = balance - 10 where id = 1;
    
    -- 6: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    
    -- 8: 提交事务
    commit;
    
    -- 9: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    ```

- 事务二

    ```sql
    -- 2: 开启事务
    begin;
    
    -- 4: 查询数据
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    
    -- 7: 查询数据(脏读不存在)
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 10: 查询数据（可重复读）
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 11: 查询数据（幻读不存在）
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 12： 更新表数据
    update account set balance = balance - 10 where id = 1;
    -- 更新数据后可重复性消失
    
    -- 13： 查询数据（不可重复读）
    -- | 1  | one   |  80      | USD      | 2021-08-10 22:42:21 |
    
    -- 14: 查询数据（存在幻读）
    select * from account where balance = 100;
    -- 之前返回 1 条， 现在返回 0 条
    ```

    

#### 序列化

保证产生相同的结果，就好像它们以某种顺序依次执行，一个接着一个没有重叠。

- 事务一

    ```sql
    -- 1: 开启事务
    begin；
    
    -- 3: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 5： 更新表数据
    update account set balance = balance - 10 where id = 1;
    -- 阻塞中...
    -- mysql 将所有的普通 select 查询隐式转换成 select for share 以及一个持有 select for share 的交易
    -- 只允许其他事务读取行，不允许更新或删除它们
    -- 此锁具有超时持续时间，如果第二个事务没有提交或回滚，会报错
    -- (1205, 'Lock wait timeout exceeded; try restarting transaction')
    
    ```

- 事务二

    ```sql
    -- 2: 开启事务
    begin;
    
    -- 4: 查询数据
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 6： 结束事务
    commit;
    -- 事务一的阻塞结束，更新成功
    ```

    



### 查看数据库事务隔离级别

#### mysql

> 默认为可重复读( repeatable read )

- 开启事务

    ```sql
    -- 开启事务
    start transaction;
    begin;
    ```

- 查看数据隔离级别

    ```sql
    -- 该会话下的隔离级别
    select @@transaction_isolation;
    
    -- 全局的隔离级别
    select @@global.transaction_isolation;
    ```

- 修改事务隔离级别

    ```sql
    -- 改为读取未提交
    set session transaction isolation level read uncommitted;
    
    -- 改为读取已提交
    set session transaction isolation level read committed;
    
    -- 改为可重复读取
    set session transaction isolation level repeatable read;
    
    -- 改为序列化
    set session transaction isolation level serializable;
    ```



#### mariaDB

> 默认为可重复读( repeatable read )

- 开启事务

    ```sql
    -- 开启事务
    start transaction;
    begin;
    ```

- 查看数据隔离级别

    ```sql
    -- 该会话下的隔离级别
    select @@tx_isolation;
    
    -- 全局的隔离级别
    select @@global.tx_isolation;
    ```

- 修改事务隔离级别

    ```sql
    -- 改为读取未提交
    set session transaction isolation level read uncommitted;
    
    -- 改为读取已提交
    set session transaction isolation level read committed;
    
    -- 改为可重复读取
    set session transaction isolation level repeatable read;
    
    -- 改为序列化
    set session transaction isolation level serializable;
    ```

    

#### postgres

> 默认为读取已提交( read committed )
>
> 在 Mysql 中， 我们在启动事务之前设置了整个会话的隔离级别， 但是在 pg 中我们只能在事务内部设置隔离级别，它只会对那一个特定交易产生影响。

- 查看数据隔离级别

    ```sql
    show transaction isolation level;
    ```



##### 读取未提交

> PG 中的读取未提交( read uncommitted ) 和读取已提交是完全相同的( read committed )，所以基本上我们可以说 PG 只有 3 个隔离级别，最低级别是读取已提交。这是合理的，因为通常我们永远不想在任何情况下使用 read-uncommitted。

- 事务一

    ```sql
    -- 1: 开启事务
    begin；
    
    -- 3： 改为读取未提交
    set session transaction isolation level read uncommitted;
    
    -- 5: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 7： 更新表数据
    update account set balance = balance - 10 where id = 1 returning *;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    
    -- 9: 提交事务
    commit;
    ```

- 事务二

    ```sql
    -- 2: 开启事务
    begin;
    
    -- 4： 改为读取未提交
    set session transaction isolation level read uncommitted;
    
    -- 6: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    
    -- 8: 查询数据(脏读不存在)
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 10: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    ```



##### 读取已提交

> 和 mysql 一致





##### 可重复读

- 事务一

    ```sql
    -- 1: 开启事务
    begin；
    
    -- 3： 改为读取未提交
    set session transaction isolation level repeatable read;
    
    -- 5: 查询数据
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 7： 更新表数据
    update account set balance = balance - 10 where id = 1 returning;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    
    -- 9: 提交事务
    commit;
    
    -- 10: 查询数据
    select * from account;
    -- | 1  | one   |  90      | USD      | 2021-08-10 22:42:21 |
    ```

- 事务二

    ```sql
    -- 2: 开启事务
    begin;
    
    -- 4： 改为读取未提交
    set session transaction isolation level repeatable read;
    
    -- 6: 查询数据
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    
    -- 8: 查询数据(脏读不存在)
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 11: 查询数据（可重复读）
    select * from account;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 12: 查询数据（幻读不存在）
    select * from account where balance = 100;
    -- | 1  | one   | 100      | USD      | 2021-08-10 22:42:21 |
    
    -- 13： 更新表数据
    update account set balance = balance - 10 where id = 1 returning *;
    -- 报错： Error: could not access due to concurrent update
    ```

    

序列化异常 



## Lesson 10 设置 Github Actions 以运行自动化测试

```shell
mkdir .github/workflows
vim test.yml
```

```yaml
name: Run unit tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    name: Test
    runs-on: ubuntu-latest

    # 指定外部服务列表
    services:
      postgres:
        image: postgres:12-alpine
        env:
          POSTGRES_USER: root
          POSTGRES_PASSWORD: secret
          POSTGRES_DB: simple_bank
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - name: Set up Go 1.x
        uses: actions/setup-go@v2
        with:
          go-version: ^1.16
        id: go

      - name: Check out code into the Go module directory
        uses: actions/checkout@v2

      # 数据库迁移
      - name: Install golang-migrate
        # 垂直管道符执行多行命令
        run: |
          curl -L https://github.com/golang-migrate/migrate/releases/download/v4.14.1/migrate.linux-amd64.tar.gz | tar xvz
          sudo mv migrate.linux-amd64 /usr/bin/migrate
          which migrate

      - name: Run migrations
        run: make migrateup

      - name: Test
        run: make test
```





## Lesson 11 使用 Gin 在 Go 中实现 RESTful HTTP API





## Lesson 13 Mock DB 用于在 Go 中测试 HTTP API 并实现 100% 覆盖

### mock 的优势

- 帮助我们更轻松地编写独立的测试

    > 每个测试都会使用自己单独的模拟数据库来存储数据,所以他们之间不会有冲突.如果使用真实的数据库,所有的车市都会把数据写到同一个地方, 很难避免冲突.

- 测试会运行的很快

    > 因为他们不必花时间与数据库沟通并等待查询运行, 所有的操作都将在内存中执行， 并在同一进程中执行。

- 允许我们编写实现 100% 覆盖率的测试

    > 使用 mock 数据库，我们可以轻松设置和测试一些边缘情况。例如意外错误与连接丢失。如果使用真正的数据库这是不可能实现的。



