----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

## 多进程中 APScheduler 重复运行

引用：[解决多进程中APScheduler重复运行的问题](https://blog.csdn.net/misayaaaaa/article/details/102684649)

> **问题：**
> &emsp;&emsp;在一个 python web 应用中需要定时执行一些任务，所以用了 [APScheduler](https://apscheduler.readthedocs.io/en/latest/)，非常轻巧： 这个库。又因为是用 flask 这个 web 框架，所以用了 flask-apscheduler 这个插件（本质上与直接用 APScheduler 一样，这里不作区分）  
> 在开发中直接测试运行是没有问题的，但是用 gunicorn 或 uwsgi 部署以后发生了重复运行的问题：
> 每个任务在时间到的时刻会同时执行好几遍。  
> 注意了一下重复的数量，恰恰是 gunicorn/uwsgi 里配置的 worker 进程数量，显然是每个 worker 进程都启动了一份 scheduler 造成。  
>
> **解决方案：**  
> - 用 `--preload` 启动 gunicorn，确保 scheduler 只在 loader 的时候创建一次  
> - 另外创建一个单独的定时任务项目，单独以一个进程运行  
> - 用全局锁确保scheduler只运行一次    
> 经过实践，只有第三个方案比较好。



### 方案一：用 `--preload` 启动
&emsp;&emsp;虽然这样可以使用 scheduler 创建代码只执行一次，但是问题也在于它只执行一次，重新部署以后如果用 `kill -HUP` 重启 gunicorn，它并不会重启，甚至整个项目都不会更新。这是 preload 的副作用，除非重写部署脚本，完全重启应用。



### 方案二：单独进程
&emsp;&emsp;也是因为部署麻烦，需要多一套部署方案，虽然用 Docker 会比较方便，但仍然不喜欢，而且同时维护两个项目也多出很多不必要的事情。



### 方案三：全局锁
&emsp;&emsp;全局锁是一个较好的方案，但问题在于找一个合适的锁。
&emsp;&emsp;python 自带的多进程多线程锁方案都需要一个共享变量来维护，但是因为 worker 进程是被 gunicorn 的主进程启动的，并不方便自己维护，所以需要一个系统级的锁。
&emsp;&emsp;在 Stackoverflow上看到有人是用了一个 socket 端口来做锁实现这个方案，但是我也不喜欢这样浪费一个宝贵的端口资源。不过这倒给了我一个启发：可以用**文件锁**！

```python
import atexit
import fcntl
from flask_apscheduler import APScheduler
 
def init(app):
    f = open("scheduler.lock", "wb")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        scheduler = APScheduler()
        scheduler.init_app(app)
        scheduler.start()
    except:
        pass
    def unlock():
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()
    atexit.register(unlock)
```

**原理：**
> init 函数为 flask 项目初始化所调用，这里为 scheduler 模块的初始化部分。
> 首先打开（或创建）一个 `scheduler.lock` 文件，并加上非阻塞互斥锁。成功后创建  scheduler 并启动。
> 如果加文件锁失败，说明 scheduler 已经创建，就略过创建 scheduler 的部分。
> 最后注册一个退出事件，如果这个 flask 项目退出，则解锁并关闭 `scheduler.lock` 文件的锁。

```python
from . import sche
from web_app.scheduler.jobs import add_jobs
import platform, atexit
job_list = []

def sche_run():
    """
    保证系统只启动一次定时任务
    :param app:
    :return:
    """
    if platform.system() != 'Windows':
        fcntl = __import__("fcntl")
        f = open('scheduler.lock', 'wb')
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            job_init()
        except:
            pass

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

        atexit.register(unlock)
    else:
        msvcrt = __import__('msvcrt')
        f = open('scheduler.lock', 'wb')
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            job_init()
        except:
            pass

        def _unlock_file():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                pass

        atexit.register(_unlock_file)


def job_init():
    # 定时任务初始化
    print('sche start')
    sche.start(paused=True)
    jobs = sche.get_jobs()
    job_list = [job_.id for job_ in jobs]
    add_jobs(job_list)
    sche.resume()
```

