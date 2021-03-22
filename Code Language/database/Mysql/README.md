----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# 一、MySQL是什么：
服务端
客户端

## Mysql数据库

> Mysql 是最流行的关系型数据库管理系统，在 WEB 应用方面 MySQL 是最好的RDBMS(Relational Database Management System：关系数据库管理系统)应用软件之一。
> 由瑞典 MySQL AB 公司开发，目前属于Oracle公司。



### 什么是数据库

> 数据库（Database）是按照数据结构来组织、存储和管理数据的仓库 
> 我们也可以将数据存储在文件中，但是在文件中读写数据速度相对较慢。
> 所以，现在我们使用关系型数据库管理系统(RDBMS)来存储和管理的大数据量。所谓的**关系型数据库，是建立在关系模型基础上的数据库**，借助于集合代数等数学概念和方法来处理数据库中的数据。
> 每个数据库都有一个或多个不同的API用于创建，访问，管理，搜索和复制所保存的数据。

### 关系型数据库的特点
> RDBMS即关系数据库管理系统(Relational Database Management System)的特点：
- 数据以表格的形式出现
- 每行为各种记录名称
- 每列为记录名称所对应的数据域
- 许多的行和列组成一张表单
- 若干的表单组成database

```mysql
-- 关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。
```



### MySQL 数据库的优势
- Mysql是开源的，所以你不需要支付额外的费用。
- Mysql支持大型的数据库。可以处理拥有上千万条记录的大型数据库。
- MySQL使用标准的SQL数据语言形式。
- Mysql可以允许于多个系统上，并且对多种语言有很好支持。这些编程语言包括C、C++、Python、Java、Perl、PHP、Eiffel、Ruby和 Tcl 等。
- MySQL支持大型数据库，支持5000万条记录的数据仓库，32位系统表文件最大可支持4GB，64位系统支持最大的表文件为8TB。
- Mysql是可以定制的，采用了 GPL 协议，你可以修改源码来开发自己的 Mysql 系统。




## 技能

### 安装
- 源码安装/exe
- 初始化
    - 启动服务端
    - 客户端连接
        - 发送指令
    - 环境变量

## 连接：

```shell
mysql -u root [-h 主机] -p
```

```shell
# 查看mysql的进程(LINUX下)
ps -ef |grep mysql 	
```





## 数据库操作

### 数据库级别操作：

```mysql
status：	查看默认设置
desc 表名;  查看表结构
```

### 数据表操作：

- 数据类型
    - 约束
        - 唯一索引
        - 主键约束
        - 外键
            - 一对一
            - 一对多
            - 多对多
    - 自增

### 数据行操作：

- 增删改查
    - 排序
    - 分组
    - 条件
    - 临时表
    - 联表
    - 通配符
    - 分页
    - 组合

### 视图

### 触发器

### 函数

### 存储过程

- 游标
- 事务逻辑：

### pymysql

- 连接 conect()
    - 操作（游标）
        - 增删改 ：commit
        - 查	   ：fetchone，fetchall,fatchany
    - 存储过程调用方式
        - callproc("名",参数)
        - select @_存储过程名称_0
    - SQL注入
        - 关闭游标
        - 关闭连接



# 二、MySQL操作
## 创建用户
```mysql
create user ‘username’@'pasword' *identified by* 'password'	
```

### 语法代码

```mysql
use mysql;
grant create,delete,drop,update,insert,select   # 或者直接写grant all
	on TUTORIALS.*                  # 所有数据库.所有表
	to 'username'@'localhost'  
	# 用户名@ 从哪台机子登陆  '%' 代表任意主机登陆
	IDENTIFIED by 'password'        # 登陆密码
	;
```

### 授权
```mysql
grant all privileges *on 库名.表名 to*  'username'@'%' 	
```

### 取消授权
```mysql
revoke al privileges on 库名.表名 *from* 'username'@'%'
```

### 查看用户权限

```mysql
show grants for 用户名;
```







## 字符编码

```mysql
charset = GBK;
create 库名 default charset = utf8;
```

### 查看字符集：

- 查看查看MySQL数据库服务器和数据库MySQL字符集。

    ```mysql
    show variables like '%char%'; 
    ```

    ```mysql
    # 输出结果
    +--------------------------+----------------------------+
    | Variable_name            | Value                      |
    +--------------------------+----------------------------+
    | character_set_client     | utf8     (客户端字符集)      |
    | character_set_connection | utf8                       |
    | character_set_database   | latin1   (数据库字符集)      |
    | character_set_filesystem | binary                     |
    | character_set_results    | utf8                       |
    | character_set_server     | latin1   (服务器字符集)      |
    | character_set_system     | utf8                       |
    | character_sets_dir       | /usr/share/mysql/charsets/ |
    +--------------------------+----------------------------+
    ```

- 查看MySQL数据表（table）的MySQL字符集。

    ```mysql
    show table status from sqlstudy_db like '%countries%'; 
    ```

    ```mysql
    # 输出结果
    +---------+--------+--------+------------+------+-----------------+ 
    | Name    | Engine | Version| Row_format | Rows | Collation       | 
    +---------+--------+--------+------------+------+-----------------+
    |countries| InnoDB |     10 | Compact    |   11 | utf8_general_ci | 
    +---------+--------+--------+------------+------+-----------------+
    ```

- 查看MySQL数据列（column）的MySQL字符集。

    ```mysql
    show full columns from countries;  
    ```

    ```mysql
    +----------------------+-------------+-----------------+
    | Field                | Type        | Collation       | 
    +----------------------+-------------+-----------------+ 
    | countries_id         | int(11)     | NULL            | 
    | countries_name       | varchar(64) | utf8_general_ci | 
    | countries_iso_code_2 | char(2)     | utf8_general_ci |
    | countries_iso_code_3 | char(3)     | utf8_general_ci |  
    | address_format_id    | int(11)     | NULL            | 
    +----------------------+-------------+-----------------+
    ```



### 修改字符集

#### 暂时修改

##### 修改全局字符集

```mysql
/*建立连接使用的编码*/
set character_set_connection=utf8;
/*数据库的编码*/
set character_set_database=utf8;
/*结果集的编码*/
set character_set_results=utf8;
/*数据库服务器的编码*/
set character_set_server=utf8;
```

##### 修改库的字符集

```mysql
alter database 库名 default character set 字符集;
```

##### 修改表的字符集

```mysql
alter table 表名 convert to character set 字符集;
```

##### 修改字段的字符集

```mysql
alter table 表名 modify 字段名 字段属性 character set gbk；
```



#### 永久修改
- 修改 mysql 配置文件
    ```shell
    sudo vi /etc/my.cnf
    ```

- 在 `[mysqld]` 上方添加以下设置：

    ```mysql
    default-character-set=utf8
    ```

- 在[mysqld]下方添加以下设置：

    ```mysql
    character-set-server=utf8
    collation-server=utf8_general_ci
    ```

    

## 原子性操作

```mysql
engine = inodb
```



## 数据库操作

### 查看数据库

```mysql
show databases;
```

### 创建数据库

```mysql
create database 库名;         # 这么写默认不能处理中文
create database 库名 charset utf8;	# 解决中文字符处理问题：
```

### 删除数据库  

```mysql
drop database 库名;
```

### 进入数据库

```mysql
use 数据库名;
```

### 查看所有表

```mysql
show tables;
```

### 查看表结构

```mysql
desc 表名;
-- 或
show colums from 表名;
```





## 增删改查

### 创建数据表

```mysql
CREATE TABLE table_name (column_name column_type);
```

### 插入数据

```mysql
INSERT INTO table_name ( field1, field2,...fieldN )
VALUES ( value1, value2,...valueN );
```

### 查询数据

```mysql
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[OFFSET M ][LIMIT N]
```

### UPDATE 更新数据

```mysql
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

### DELETE 语句

```mysql
DELETE FROM table_name [WHERE Clause]
```



## 数据类型
int
decimal
datatime
char，text

```mysql
性别 enum（ ‘','’ ） username char
set()
```



### String类型：

| **数据类型：** | **描述**                                                     | **存储**                  |
| -------------- | ------------------------------------------------------------ | ------------------------- |
| char(n)        | 固定长度的字符串。最多 8,000 个字符。<br/>定义类型为char(5)，那么就表示该类型可以存储5个字符<br/>即使存入2个字符，剩余的3个字符也会用空格补齐。 | Defined width             |
| varchar(n)     | 可变长度的字符串。最多 8,000 个字符。<br/>定义类型为varchar(5)，那么就表示该类型可以存储5个字符<br/>如果存入 2 个字符，字符长度就是 2 而不是 5 | 2 bytes + number of chars |
| varchar(max)   | 可变长度的字符串。最多 $1,073,741,824$  个字符。             | 2 bytes + number of chars |
| text           | 可变长度的字符串。最多 2GB 文本数据。                        | 4 bytes + number of chars |
| nchar          | 固定长度的 Unicode 字符串。最多 4,000 个字符。               | Defined width x 2         |
| nvarchar       | 可变长度的 Unicode 字符串。最多 4,000 个字符。               |                           |
| nvarchar(max)  | 可变长度的 Unicode 字符串。最多 536,870,912 个字符。         |                           |
| ntext          | 可变长度的 Unicode 字符串。最多 2GB 文本数据。               |                           |
| bit            | 允许 0、1 或 NULL<br/>如果表中的列为8bit，则这些列作为一个字节存储<br/>如果列为9-16bit，这这些列作为2个字节存储，以此类推 |                           |
| binary(n)      | 固定长度的二进制字符串。最多 8,000 字节。                    |                           |
| varbinary      | 可变长度的二进制字符串。最多 8,000 字节。                    |                           |
| varbinary(max) | 可变长度的二进制字符串。最多 2GB。                           |                           |
| image          | 可变长度的二进制字符串。最多 2GB。                           |                           |



### Number类型

| **数据类型** | 描述                                                         | 存储        |
| ------------ | ------------------------------------------------------------ | ----------- |
| tinyint      | 允许从 $0$ 到 $255$ 的所有数字。                             | 1 字节      |
| smallint     | 允许介于 $-32,768$ 与 $32,767$ 的所有数字。                  | 2 字节      |
| int          | 允许介于 $-2,147,483,648$ 与 $2,147,483,647$ 的所有数字。    | 4 字节      |
| bigint       | 允许介于 $-9,223,372,036,854,775,808$ ~ $9,223,372,036,854,775,807​$ 之间的所有数字。 | 8 字节      |
| decimal(p,s) | 固定精度和比例的数字。<br/>允许从 $-10^{38} +1$ 到 $10^{38} -1​$ 之间的数字。<br/>p 参数指示可以存储的最大位数（小数点左侧和右侧）。<br/>p 必须是 1 到 38 之间的值。默认是 18。<br/>s 参数指示小数点右侧存储的最大位数。s 必须是 0 到 p 之间的值。默认是 0。 | 5-17 字节   |
| numeric(p,s) | 固定精度和比例的数字。<br/>允许从 $-10^{38} +1$ 到 $10^{38} -1$ 之间的数字。<br/>p 参数指示可以存储的最大位数（小数点左侧和右侧）。<br/>p 必须是 1 到 38 之间的值。默认是 18。<br/>s 参数指示小数点右侧存储的最大位数。s 必须是 0 到 p 之间的值。默认是 0。 | 5-17 字节   |
| smallmoney   | 介于 $-214,748.3648$ 与 $214,748.3647$ 之间的货币数据。      | 4 字节      |
| money        | 介于 $-922,337,203,685,477.5808$ ~ $922,337,203,685,477.5807​$ 之间的货币数据。 | 8 字节      |
| float(n)     | 从 $-1.79E + 308$ 到 $1.79E + 308$ 的浮动精度数字数据。<br/>n 参数指示该字段保存 4 字节还是 8 字节。float(24) 保存 4 字节，而 float(53) 保存 8 字节。n 的默认值是 53。 | 4 或 8 字节 |
| real         | 从 $-3.40E + 38$ 到 $3.40E + 38$ 的浮动精度数字数据。        | 4 或 8 字节 |



### Date 类型

| 数据类型       | 描述                                                         | 存储      |
| -------------- | ------------------------------------------------------------ | --------- |
| datetime       | 从 1753 年 1 月 1 日 到 9999 年 12 月 31 日，精度为 3.33 毫秒。 | 8 字节    |
| datetime2      | 从 1753 年 1 月 1 日 到 9999 年 12 月 31 日，精度为 100 纳秒。 | 6-8 字节  |
| smalldatetime  | 从 1900 年 1 月 1 日 到 2079 年 6 月 6 日，精度为 1 分钟。   | 4 字节    |
| date           | 仅存储日期。从 0001 年 1 月 1 日 到 9999 年 12 月 31 日。    | 3 bytes   |
| time           | 仅存储时间。精度为 100 纳秒。                                | 3-5 字节  |
| datetimeoffset | 与 datetime2 相同，外加时区偏移。                            | 8-10 字节 |
| timestamp      | 存储唯一的数字，每当创建或修改某行时，该数字会更新。<br/>timestamp 值基于内部时钟，不对应真实时间。<br/>每个表只能有一个 timestamp 变量。 |           |



### 其他数据类型

| **数据类型**     | **描述**                                                     |
| ---------------- | ------------------------------------------------------------ |
| sql_variant      | 存储最多 8,000 字节不同数据类型的数据，除了 text、ntext 以及 timestamp。 |
| uniqueidentifier | 存储全局唯一标识符 (GUID)。                                  |
| xml              | 存储 XML 格式化数据。最多 2GB。                              |
| cursor           | 存储对用于数据库操作的指针的引用。                           |
| table            | 存储结果集，供稍后处理。                                     |

 



## 约束

- 唯一约束 unique
- 主键约束 primary key
- 外键约束 constraint 外键名 foreign key（ 列名 ） references 外表（ 列名 ）



## 自动递增

```mysql
*auto_increment
```



## 通配符

- %

- _



## 算数、逻辑、比较运算符



## 排序( order by )

- asc
- desc



## 分组( group by )
- 多表连接

- 左右联表 : join

- 上下联表 : union

    - 自动去重：

        ```mysql
        select * from 表1		（假设十条）
        union
        select * from 表2		（假设十条）
        (返回二十条)
        ```

    - 不去重

        ```mysql
        select * from 表1		（假设十条）
        union
        select * from 表1		
        (返回二十条)
        ```



## 分页(limit)

```mysql
select * from 表名 limit 0,10;
```

（ 翻的页越大越慢 ）---> 加速方法：只对索引进行扫描



### 加速方式一：索引加速

```mysql
# 覆盖索引，但是快不了多少
select * from userinfo3 where uid in ( select uid from limit 20000,10)
```

### 最佳方法加速方式：

> 记录当前页最大值最小值ID：

```mysql
# 当前页后十条
select * from userinfo3 where uid > 20000 limit 10;					
# 当前页前十条
select * from userinfo3 where uid < 20000 order by id desc limit 10;
```



### 分页方式：

#### 页面只有上一页和下一页：

```mysql
# 上一页：
select * from userinfo3 where uid > max_id limit 10;
# 下一页：
select * from userinfo3 where uid < min_id order by id desc limit 10;
```



#### 上一页 192 193  [196]  197  198  199 下一页

```mysql
# 上一页：
select * from userinfo3 where id in (
select id from (select id from userinfo3 where id > max_id limit 30) as N order by N.id desc limit 10
)
```





# 三、MySQL 高级编程
## 视图

### 创建视图( 临时表的反复使用 )
```mysql
create views 视图名称 as SQL语句( select ....)				# 从真实表动态获取数据
```
使用视图时，将其当作表进行操作即可，由于视图是虚拟表，所以无法使用其对真实表进行创建、更新和删除操作，仅能做查询用。

### 修改视图：

```mysql
alter views 视图名称 as SQL语句( select ....)
```

删除视图：

```mysql
 drop views 视图名称
```



## 触发器( 数据库级别操作 )

> 当对某张表做增删改操作时，可以使用触发器自定义关联行为

### 创建触发器

```mysql
create trigger 触发器名称 before/after (SQL行为语句) ON 表、库
```

eg:

```mysql
create trigger tri_before_insert before insert ON tb1 [For EACH ROW 每插入一行就会触发 ]
begin
	...;
end

create trigger tri_before_insert after insert ON tb1 For EACH ROW
begin
	...;
end
```

### 注意:

```markdown
# 查询不会触发触发器
```





## 函数( 性能低 )

### 执行函数：

```mysql
select 函数名();
```

### 内置函数：

#### 聚合函数

```mysql
select CURDATE();			# 2018-05-15				年-月-日
select CURRENT_TIMESTAMP();	#  2018-05-15 20:53:36		年-月-日 时:分:秒
select CHAR_LENGTH(str);	# 字符串str长度
select CONCAT(str1,str2)	# 字符串拼接
```



#### 自定义函数：

```mysql
delimiter //
create function f1(
	i1 int,		--传入参数
	i2 int 
)
return int
begin
	-- 不能写 select * from 表名 等SQL行为
	declare num int default 0;	# 定义临时变量
	set num = i1 + i2;
	return(num);
END//
delimiter ;
```





## 存储过程( 更为重要 )
>  mysql 前几年还没有这个
> 保存在 MySQL 上的一个别名 => 一坨SQL语句	



### 1.创建存储过程
#### 无参存储过程

```mysql
delimiter //
create procedure p1()
begin
	INSERT INTO userinfo(username,password) VALUES("user5","pd5");
	SELECT *  FROM userinfo;
end//
delimiter ;
```



#### 有参数存储过程：( 关键字：in\out\inout )

```mysql
delimiter //
create procedure p2(
	in n1 int,
	in n2 int
)
begin
	select * from userinfo where id > n1;
end//
delimiter ;
```

- 存储过程没有返回值的概念，out 是传进一个变量，然后你可以在存储过程中改变该变量的值

- out 不往里面传值，也就是虽然在外面 `@var=1`，实际上 p3 里使用不了 `@var` 的值

    ```mysql
    delimiter //
    create procedure p3(
    	in n1 int,
    	out n2 int
    )
    begin
    	set n2 = 123123;
    	select * from userinfo where id > n1;
    end//
    delimiter ;
    
    set @var = 1;			# 定义一个变量@var = 0
    call p3(8,@var );
    select @var				# @var = 123123
    ```


- inout：即可往存储过程里面传值，也可以往外传值

#### ！注意：
- 为什么要有结果集，又要有out伪造的的返回值？

    > out用于设置一个值，标识存储过程的执行结果



### 2.调用存储过程：

```mysql
call p1();
```



### 存储过程的优缺点
#### 好处：
>  网络传的数据就少了

#### 坏处：
> 存储过程如果改了，程序就GG了

#### 以后工作的方式：
##### 方式一：存储过程
MySQL: 存储过程
程序：调用存储过程

##### 方式二：SQL语句
MySQL：。。
程序：SQL语句

##### 方式三：ORM 框架
MySQL：。。
程序：类和对象（SQL语句）



## 事务（ 性能不高 ）

### 事务逻辑：

```mysql
delimiter //
create procedure p4(
	out status int
)
BEGIN
	# 声明如果出现异常则执行
	{
		set status = 1;
		rollback;
	}

	#开始事务
	SQL;
	commit;

	# 结束
	set status = 2;
END //
delimiter ;
```

语法代码

```mysql
delimiter \\
create PROCEDURE p5(
	OUT p_return_code tinyint
)
BEGIN 
	DECLARE exit handler for sqlexception 		--声明如果出现异常则执行
	BEGIN 
		-- ERROR 
		set p_return_code = 1; 
		rollback; 
	END; 

	START TRANSACTION; 							--开始事务
		DELETE from tb1;
		insert into tb2(name)values('seven');
	COMMIT; 

	-- SUCCESS 
	set p_return_code = 2; 
END\\
delimiter ;
```



## 游标( 性能不高 )

### 创建游标

```mysql
declare my_cursor CURSOR FOR [SQL语句]select * from A；
```

### 使用游标

```mysql
fetch my_cursor into row_namename,row_psd;
```

### 一个循环的例子：

```mysql
delimiter \\
create procedure p6()
BEGIN
	DECLARE row_name varchar(20);		-- 自定义一个变量1
	DECLARE row_psd varchar(50);		-- 自定义一个变量2
	declare done int default False;		-- 自定义循环结束标志

	declare my_cursor CURSOR FOR select username,password from userinfo;
	declare CONTINUE HANDLER FOR NOT FOUND set done = TRUE;				
	-- 当游标为空时改变循环结束标志

	open my_cursor;						-- 打开游标
		SIGN:LOOP						-- 开始循环标志
			fetch my_cursor into row_namename,row_psd;	-- 获取游标内容
				if done then 				
					leave SIGN;				-- breake
				end if;
				insert into userinfo2( row_namename,row_psd) values( row_name,row_psd);
		end loop SIGN;					-- 关闭循环标志
	close my_cursor;					-- 关闭游标
END\\
delimiter ;
```



## 动态执行SQL语句：( 防SQL注入 )
### 伪代码：

```mysql
delimiter \\
create procedure p7(
	in str varchar(255),			# 放要执行的SQL语句
	in arg int
)
begin 
	1. 预检测某个东西 SQL语句合法性
	2. SQL =格式化 tpl + arg 
	3. 执行SQL语句
end
```

### 语法代码

```mysql
delimiter \\
CREATE PROCEDURE p7(
	in nid int
)
BEGIN
	set @nid = nid;				-- 因为 execute 只能使用@ 所以要给他赋值
	PREPARE prod FROM 'select * from student where sid > ?';		
	-- 预检测SQL语句
	EXECUTE prod USING @nid;										
	-- 拼接
	DEALLOCATE prepare prod; 
END\\
delimiter ;
```



## 索引( 加速查找 )
> 对于频繁查找的列要创建索引

### 作用：

#### 约束

#### 加速查找

##### 慢速查找：

```mysql
select * from tb where 列名="...”
```

**快速查找：**

```mysql
select * from tb where id = 65
```

#### 无索引：

> 从前往后依次查询

#### 有索引：

- 创建额外文件( 某种格式存储)，保存特殊的数据结构
- 查询快，插入更新删除慢
- 命中索引( 版本和版本，数据库和数据库也有不同标准 )



### 索引类别

#### 按作用分类

- 主键索引：加速查找 + 不能为空 + 不能重复
- 普通索引：加速查找
- 唯一索引：加速查找 + 不能重复
- 联合索引（多列）：
  - 联合主键索引
  - 联合唯一索引
  - 联合普通索引

##### 特殊

>  以下并非真实索引

- **覆盖索引：**			

    ```mysql
    --在索引文件中直接获取数据
    select id from userinfo3 where email = ".....";
    ```
- **索引合并：**		

    ```mysql
    --把多个单列索引合并使用
    select id from userinfo3 where email = "....." and pd = ”...“;	
    ```

    
#### 按实现方法

##### hash索引

- 单值快
- 范围慢

##### btree索引（ 默认下 ）

- 按二叉树查
- 快



### 索引的创建
#### 普通索引：

```mysql
create index 索引名 on 表名( 列名 );
```

#### 唯一索引：

```mysql
create unique index 索引名 on 表名( 列名 );
```

#### 联合索引：

```mysql
create unique index 索引名 on 表名( 列名1，列名2 );
```

##### 最左前缀匹配：

```mysql
select * from 表名 where 列名1 = xxx and 列名2 = xxx;		-- 走索引
select * from 表名 where 列名2 = xxx;					  -- 不走索引
-- 联合索引的效率大于索引合并
```

#### 短索引：

```mysql
create index 索引名 on 表名( 列名(16) )  -- 对列名1的16个字节之后的数据建立索引
```

> **注意:** 在 Mysql 里 TEXT 类型要想建立索引必须建立短索引，否则报错





## ORM 框架操作 ( 关系对象映射 )	
> 如 SQLAlchmy
- 当一类函数公用同样参数时候，可以转变成类进行 - 分类
- 面向对象： 数据和逻辑（属性和行为）组合在一起
  函数编程： 数据和逻辑分离

- 模板“约束”

    > 提取共性
    > 一类事物共同具有：属性和行为

### 作用
- 提供简单的规
- 自动转换成SQL语句
- 

### ORM框架类别：

- DB first: 

    ```mermaid
    graph LR
    A(手动创建数据库以及表) --> B(ORM框架 )
    B --> C(自动生成类)
    ```

- code first： 

    > SQLAlchmy 属于该类

    ```mermaid
    graph LR
    A(手动创建类和数据库) -->B(ORM框架)
    B -->C(以及表)
    ```

    





### 注意事项

#### 不用 like

>  不用like,用 like 永远也命中不了索引

#### 避免使用函数

#### 避免使用 or

特别的：当or条件中有未建立索引的列才失效，以下会走索引

```mysql
select * from tb1 where nid = 1 or name = 'seven';
select * from tb1 where nid = 1 or name = 'seven@live.com' and email = 'alex'
```

#### 类型要一致，类型不一致也会使用类型转化函数

#### 普通索引不走以下语法

##### !=：

```mysql
select * from tb1 where email != '...'
-- 特别的：如果是主键，则还是会走索引
select * from tb1 where nid != 123
```

##### >：

```mysql
select * from tb1 where email > 'alex'
-- 特别的：如果是主键或索引是整数类型，则还是会走索引
select * from tb1 where nid > 123
select * from tb1 where num > 123	
```

##### order by

```mysql
select name from tb1 order by email desc;( 前后不一致不走索引 )
-- 当根据索引排序时候，选择的映射如果不是索引，则不走索引
-- 特别的：如果对主键排序，则还是走索引：
select * from tb1 order by nid desc;
```






# 四、MySQL 注意事项
- 避免使用select * 

- count(1)或count(列) 代替 count(*)

- 创建表时尽量时 char 代替 varchar	

- 表的字段顺序固定长度的字段优先

- 组合索引代替多个单列索引（经常使用多个条件查询时）

- 尽量使用短索引

- 使用连接（JOIN）来代替子查询(Sub-Queries)

    ```mysql
    -- MYSQL里已经没有区别了
    ```

- 连表时注意条件类型需一致

- 索引散列值（重复少）不适合建索引，例：性别不适合


- 因为mysql默认;为语句结束符，所以当执行复合语句内部[begin...end]时会出错,解决如下：

    ```mysql
    delimiter //					修改语句结束符为 //
    create trigger tri_before_insert after insert ON tb1 For EACH ROW
    begin
    ...;
    end//
    delimiter ;						还原，避免其他语句被干扰
    补充：
    -- NEW,代指新数据（添加的时候有）
    insert into tb() values( NEW.user );
    -- OLD,代指老数据( 删除的时候有 ) 
    ```

    

补充：

- NEW,代指新数据（添加的时候有）

    ```mysql
    insert into tb() values( NEW.user );
    ```

- OLD,代指老数据( 删除的时候有 ) 



# 五、DBA工作
## 慢日志

- 执行时间 > 10
- 未命中索引
- 日志文件路径

### 配置：

#### 方式一：内存

```mysql
show variables like '%query%'
set global 变量名 = 值
set global slow_query_log = ON;			--开启慢日志，默认关闭
```

#### 方式二：指定配置文件

```shell
mysqld --defaults-file='E:\wupeiqi\mysql-5.7.16-winx64\mysql-5.7.16-winx64\my-default.ini'
```

**my.conf内容：**

```mysql
slow_query_log = ON
slow_query_log_file = D:/....
```

#### 方式三：Mysql的配置文件里修改

> 注意：修改配置文件之后，需要重启服务。修改配置文件之前，需要备份配置文件


​	



## 数据库优化

- 避免使用select * 

- 固定长度在前面

    > 表的字段顺序固定长度的字段优先

- 内存代替表，如：性别等
- 读写分离
- 分库
- 分表
  - 水平分表
  - 垂直分表



[公司内部mysql使用规范分享](https://www.studytime.xin/article/mysql-internal-specifications.html?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)





















































































































