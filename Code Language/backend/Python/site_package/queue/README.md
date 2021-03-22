> *Made By Herolh*

----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# 初识 queue

## queue 的基本介绍

### 什么是 queue

> Python 的 Queue 模块中提供了同步的、线程安全的队列类，包括 FIFO（先入先出)队列Queue，LIFO（后入先出）队列 LifoQueue，和优先级队列 PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。



## queue 的初步使用

### queue 的常用方法

|             方法              |                             说明                             |
| :---------------------------: | :----------------------------------------------------------: |
|         Queue.qsize()         |                        返回队列的大小                        |
|         Queue.empty()         |              如果队列为空，返回 True,反之 False              |
|         Queue.full()          | 如果队列满了，返回 True,反之False,<br />Queue.full 与 maxsize 大小对应 |
| Queue.get([block[, timeout]]) |                  获取队列，timeout等待时间                   |
|      Queue.get_nowait()       |              相当于Queue.get(False)，非阻塞方法              |
|        Queue.put(item)        |                  写入队列，timeout等待时间                   |
|       Queue.task_done()       | 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号。每个get()调用得到一个任务，接下来task_done()调用告诉队列该任务已经处理完毕。 |
|         Queue.join()          |           实际上意味着等到队列为空，再执行别的操作           |







### queue 语法

> 对语法进行由浅入深的归纳分类



### queue 模拟场景





# queue 进阶

> 中高级的应用



# queue 源码分析





# queue 注意事项





# queue 思考

