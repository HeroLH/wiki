----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# SQLAlchemy 介绍

> &emsp;&emsp;SQLAlchemy 是一个基于 Python 实现的 ORM 框架。该框架建立在 DB API 之上，使用关系对象映射进行数据库操作，简言之便是：将类和对象转换成 SQL，然后使用数据 API 执行 SQL 并获取执行结果。
> 作用：帮助我们使用类和对象快速实现数据库操作。



## 安装

```python
pip3 install sqlalchemy -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```









# SQLAlchemy 基本使用

## 数据表的增删

> SQLalchemy 默认不能**修改**表结构，如果需要必须由第三方模块进行

```python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    password = Column(String(32), index=True, nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)



def create_all(
        username,password,database,
        db_engine="mysql",engine_module="pymysql",
        host="127.0.0.1",port=3306,charset="utf8"
):
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "{sql}+{engine_module}://{user}:{pwd}@{host}:{port}/{db}?charset={charset}".format(
            sql=db_engine,engine_module=engine_module,user=username,pwd=password,
            host=host,port=port,db=database,charset=charset
        ),
        max_overflow=0,  	# 超过连接池大小外最多创建的连接
        pool_size=5,  		# 连接池大小
        pool_timeout=30,  	# 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  	# 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.create_all(engine)

def drop_all(
        username,password,database,
        db_engine="mysql",engine_module="pymysql",
        host="127.0.0.1",port=3306,charset="utf8"
):
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        "{sql}+{engine_module}://{user}:{pwd}@{host}:{port}/{db}?charset={charset}".format(
            sql=db_engine,engine_module=engine_module,user=username,pwd=password,
            host=host,port=port,db=database,charset=charset
        ),
        max_overflow=0,  	# 超过连接池大小外最多创建的连接
        pool_size=5,  		# 连接池大小
        pool_timeout=30,  	# 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  	# 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    create_all(
        username="root",
        password="root@133",
        database="sqlalchemy_test"
    )
    # drop_all(
    #     username="root",
    #     password="root@133",
    #     database="sqlalchemy_test"
    # )
```





## 数据行的增删改查

```python
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from T1_create_detele_db import Users		# 要导入修改的数据表 源类

engine = create_engine(
    "mysql+pymysql://root:root@133@127.0.0.1:3306/sqlalchemy_test",
    max_overflow=0,
    pool_size=5
)
SessionFactory = sessionmaker(bind=engine)

# ORM 操作

# 关闭session
session.close()
```

### 增

```python
############# 单个增 #############
obj1 = Users(name="user1",password="1")
session.add(obj1)
# 提交事务
session.commit()

############# 多个增 #############
session.add_all([
    Users(name="user2",password="2"),
    Users(name="user3",password="3")
])
session.commit()
```

### 删

```python
session.query(Users).filter(Users.id > 2).delete()
session.commit()
```

### 改

```python
# ############# 修改 #############
session.query(Users).filter(Users.id == 1).update({
    Users.name: "user111"
    # "name":"user111"              # 这样也是可以
})
session.commit()

# 参数 synchronize_session
session.query(Users).filter(Users.id > 0).update({
    Users.name: Users.name + "099"},
    synchronize_session=False           
    # 默认进行的是数字的加减，需要字符串拼接的要改成 False
)
session.commit()
```

### 查

```python
# 查看 sqlalchemy 执行的 sql 语句
query = session.query(Users.id,Users.name)
print(query)
# SELECT users.id AS users_id, users.name AS users_name
# FROM users

# 想要什么查什么
result = session.query(Users.id,Users.name).all()
print(result)   				# [(1, 'user111099'), (2, 'user2099')]
for item in result:
    print(item[0], item.name)	# 1 user111099
    
# as name   起别名
result = session.query(Users.id,Users.name.label("username")).all()
for item in result:
    # print(item[0], item.name)       # 因为取完别名就要用别名，否则会报错 
    # AttributeError: 'result' object has no attribute 'name'
    print(item[0], item.username)
```



```python
# ############# 查 #############
result = session.query(Users).all()     # 查全部
for row in result:
    print(row.id,row.name,row.password )

result = session.query(Users).first()   # 取第一个
print(result)

# 限制
ret = session.query(Users)[1:2]
```



#### filter()

> 可以传表达式

```python
result = session.query(Users).filter(Users.id <= 2)	
print(result)							# 条件查，可加多个参数，默认关系为 and 

# between 
ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()

# in
ret = session.query(Users).filter(Users.id.in_([1,3,4])).all()

# not in
ret = session.query(Users).filter(~Users.id.in_([1,3,4])).all()

# 子查询
session.query(Users).filter(
    Users.id.in_(session.query(Users.id).filter_by(name='eric'))
).all()

# add 和 or 
from sqlalchemy import and_, or_
ret = session.query(Users).filter(
    and_(Users.id > 3, Users.name == 'eric')		# fiflter 默认也是 and
).all()
ret = session.query(Users).filter(
    or_(Users.id < 2, Users.name == 'eric')
).all()
# 组合拳
ret = session.query(Users).filter(
    or_(
        Users.id < 2,
        and_(Users.name == 'eric', Users.id > 3),
        Users.extra != ""
    )).all()

# 通配符
ret = session.query(Users).filter(Users.name.like('e%')).all()
ret = session.query(Users).filter(~Users.name.like('e%')).all()
```



#### filter_by()

> 传参数

```python
result = session.query(Users).filter_by(id = 2)	
```

> 本质上 filter_by 内部执行的也是 filter()



#### order_by()

```python
# 排序
ret = session.query(Users).order_by(Users.name.desc()).all()
ret = session.query(Users).order_by(
    Users.name.desc(), Users.id.asc()
).all()		# 先按 name 从大到小排，如果同名则按id从小到大排
```



#### group_by()

```python
# 分组
from sqlalchemy.sql import func

ret = session.query(Users).group_by(Users.id).all()
# 分组后同一组的只能出现一个，而且该语句在 sqlserver 是会报错的 

ret = session.query(
    func.max(Users.id),				# 取最大的 id
    func.count(Users.id),			# 统计 id 个数
    func.sum(Users.id),				# 
    func.min(Users.id)
).group_by(Users.name).all()

ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).having(func.count(Users.id) >2).all()
```



### 组合

> union 是上下进行拼接，而join 是左右进行拼接

```python
# 组合
q1 = session.query(Users.name).filter(Users.id > 2)
q2 = session.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union(q2).all()			# 重复的去重，相当于：
"""
select id,name from users
UNION
select id,name from users;
"""

q1 = session.query(Users.name).filter(Users.id > 2)
q2 = session.query(Favor.caption).filter(Favor.nid < 2)
ret = q1.union_all(q2).all()		# 重复的不去重，相当于：
"""
select id,name from users
UNION ALL
select id,name from users;
"""
```





## 多表结构

### 一对多

```python
from sqlalchemy import ForeignKey
depart_id = Column(Integer, ForeignKey("depart.id") )
```



#### join



#### relationship

```python
from sqlalchemy.orm import relationship
dp = relationship("Depart", backref="pers")     # 该字段不会在数据库出现
# 与 Depart 表做关联,帮助我们自动跨表
# backref 表示反向关联
```





### 多对多

> flask 里没有一个字段 manytoMany 帮你去自动创建第三张表，还是

#### rqalationship





## 多线程

> 推荐 scoped_session

```python
# 每次执行数据库操作时，都需要创建一个session
from sqlalchemy.orm import scoped_session
SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)

session.remove()
```

```mermaid
graph LR
A[scoped_session] -->B("__init__()")
B --> C(self.regestry)
C --> D["ThreadLocalRegistry()"]
D --> E("threading.local()")
```





## 执行原生 sql

```python
# 查询
# cursor = session.execute('select * from users')
# result = cursor.fetchall()

# 添加
cursor = session.execute('insert into users(name) values(:value)',params={"value":'wupeiqi'})
session.commit()
print(cursor.lastrowid)
```



























