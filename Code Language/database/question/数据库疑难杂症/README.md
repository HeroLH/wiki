----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# 数据库左连接、右连接、内连接、全连接笔记

## 基本定义：

- **left join （左连接）**：返回包括左表中的所有记录和右表中连接字段相等的记录。
- **right join （右连接）**：返回包括右表中的所有记录和左表中连接字段相等的记录。
- **inner join （等值连接或者叫内连接）**：只返回两个表中连接字段相等的行。
- **full join （全外连接）**：返回左右表中所有的记录和左右表中连接字段相等的记录



A 表 

|  id  | name |
| :--: | :--: |
|  1   | 小王 |
|  2   | 小李 |
|  3   | 小刘 |

B 表

|  id  | A_id |  job   |
| :--: | :--: | :----: |
|  1   |  2   |  老师  |
|  2   |  4   | 程序员 |



### 内连接

> 只有2张表匹配的行才能显示

```mysql
select a.name,b.job from A as a  
inner join B as b 
on a.id=b.A_id

# 只能得到一条记录 
#　　小李　　老师
```



### 左连接

> 左边的表不加限制

```mysql
select a.name,b.job from A as a  
left join B as b 
on a.id=b.A_id

# 三条记录
#　　小王　　null
#　　小李　　老师
#　　小刘　　null
```



### 右连接

> 右边的表不加限制

```mysql
select a.name,b.job from A a  
right join B b 
on a.id=b.A_id
 
# 两条记录
#　　小李　　老师 
#　　null　　程序员
```



### 全外连接：

> 左右2张表都不加限制

```mysql
select a.name,b.job from A a  
full join B b 
on a.id=b.A_id
 
# 四条数据
#　　小王　　null
#　　小李　　老师 
#　　小刘　　null 
#　　null　　程序员
```



### 注意：

&emsp;&emsp;在sql中l外连接包括左连接（left join ）和右连接（right join），全外连接（full join），等值连接（inner join）又叫内连接。



#### 参考文章

[左连接 ，右连接，内连接和全外连接的4者区别](https://blog.csdn.net/weixin_39220472/article/details/81193617)





# 数据库事务,原子性、一致性、隔离性、持久性

## 原子性

> &emsp;&emsp;表示组成一个事务的多个数据库操作是一个不可分割的原子单元，只有所有的操作执行成功，整个事务才提交。事务中的任何一个数据库操作失败，已经执行的任何操作都必须被撤销，让数据库返回初始状态。

## 一致性

>&emsp;&emsp;事务操作成功后，数据库所处的状态和他的业务规则是一致的，即数据不会被破坏。如A账户转账100元到B账户，不管操作成功与否，A和B账户的存款总额是不变的。

## 隔离性

> &emsp;&emsp;在并发数据操作时，不同的事务拥有各自的数据空间，他们的操作不会对对方产生敢逃。准确地说，并非要求做到完全无干扰。数据库规定了多种事务隔离界别，不同的隔离级别对应不用的干扰成都，隔离级别越高，数据一致性越好，但并发行越弱。

## 持久性

> &emsp;&emsp;一旦事务提交成功后，事务中所有的数据操作都必须被持久化到数据库中。即使在事务提交后，数据库马上崩溃，在数据库重启时，也必须保证能够通过某种机制恢复数据。

```markdown
# 在这些事务特性中，数据“一致性”时最终目标，其他特性都是为达到这个目标而采取的措施、要求或手段。
```



















