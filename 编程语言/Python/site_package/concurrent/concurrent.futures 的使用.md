----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# concurrent.futures

&emsp;&emsp;`concurrent.futures` 是 python 3.2 中引入的新模块，它为异步执行可调用对象提供了高层接口。可以使用 `ThreadPoolExecutor` 来进行多线程编程，`ProcessPoolExecutor` 进行多进程编程，两者实现了同样的接口，这些接口由抽象类 `Executor `定义。这个模块提供了两大类型，一个是 Executor 执行器类，另一个是 Future 类。
&emsp;&emsp;执行器用来管理工作池，future 用来管理工作计算出来的结果，通常不用直接操作 future 对象，因为有丰富的 API。







##  ThreadPoolExecutor 线程池执行器

> &emsp;&emsp;`ThreadPoolExecutor` 线程池执行器是 `Executor` 执行器的子类，通过线程池来执行异步调用。它管理一组工作线程，当工作线程有富余的时候，给它们传递任务。
> 当属于一个 Future 对象的可调用对象等待另一个 Future 的返回时，会发生死锁 deadlock。

```python
ThreadPoolExecutor(self, max_workers=None, thread_name_prefix='', initializer=None, initargs=())
```

构造实例的时候，传入`max_workers`参数来设置线程池中最多能同时运行的线程数目。这个 Executor 子类最多用 max_workers 个线程来异步执行调用。
initializer 是一个可选的可调用对象，会在每个 worker 线程启动之前调用。
initargs 是传递给 initializer 的参数元组。
如果 initializer 抛出了异常，那么当前所有等待的任务都会抛出 BrokenThreadPool 异常，继续提交 submit 任务也会抛出此异常。

> 3.5 的变化：如果 `max_worker` 没有指定或者为 None，则默认为本机处理器数量乘以 5。
> 3.6 新特性：添加了 `thread_name_prefix` 参数，可以控制由线程池创建的工作线程名称，便于调试。
> 3.7 的变化：添加了 `initializer` 和 `initargs` 参数。



### 简单使用

```python
from concurrent.futures import ThreadPoolExecutor
import time


def get_html(times):
    time.sleep(times)                               # 参数times用来模拟网络请求的时间
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

# done方法用于判定某个任务是否完成
print(task1.done())

# cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功, 这个例子中，线程池的大小设置为2，任务已经在运行了，所以取消失败。如果改变线程池的大小为1，那么先提交的是task1，task2还在排队等候，这是时候就可以成功取消。
print(task2.cancel())
time.sleep(4)
print(task1.done())

# result方法可以获取task的执行结果. 查看内部代码，发现这个方法是阻塞的。
print(task1.result())
```

> 执行结果：
>
> ```shell
> 
> False  		# 表明task1未执行完成
> False  		# 表明task2取消失败，因为已经放入了线程池中
> get page 2s finished
> get page 3s finished
> True  		# 由于在get page 3s finished之后才打印，所以此时task1必然完成了
> 3     		# 得到task1的任务返回值
> ```





#### as_completed()

> 上面虽然提供了判断任务是否结束的方法，但是不能在主线程中一直判断啊。有时候我们是得知某个任务结束了，就去获取结果，而不是一直判断每个任务有没有结束。这是就可以使用 `as_completed` 方法一次取出所有任务的结果。

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4] # 并不是真的url
all_task = [executor.submit(get_html, (url)) for url in urls]

for future in as_completed(all_task):
    data = future.result()
    print("in main: get page {}s success".format(data))

# 执行结果
# get page 2s finished
# in main: get page 2s success
# get page 3s finished
# in main: get page 3s success
# get page 4s finished
# in main: get page 4s success
```

&emsp;&emsp;`as_completed()`方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会`yield`这个任务，就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，**先完成的任务会先通知主线程**。



#### map()
> 除了上面的`as_completed`方法，还可以使用`executor.map`方法，但是有一点不同。
> 使用`map`方法，无需提前使用`submit`方法，`map`方法与`python`标准库中的`map`含义相同，都是将序列中的每个元素都执行同一个函数。

```python
from concurrent.futures import ThreadPoolExecutor
import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4] # 并不是真的url

for data in executor.map(get_html, urls):
    print("in main: get page {}s success".format(data))

# 执行结果
# get page 2s finished
# get page 3s finished
# in main: get page 3s success
# in main: get page 2s success
# get page 4s finished
# in main: get page 4s success
```

&emsp;&emsp;上面的代码就是对`urls`的每个元素都执行`get_html`函数，并分配各线程池。可以看到执行结果与上面的`as_completed`方法的结果不同，**输出顺序和`urls`列表的顺序相同**，就算2s的任务先执行完成，也会先打印出3s的任务先完成，再打印2s的任务完成。



#### wait

> `wait`方法可以让主线程阻塞，直到满足设定的要求。

```python
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4] # 并不是真的url
all_task = [executor.submit(get_html, (url)) for url in urls]
wait(all_task, return_when=ALL_COMPLETED)
print("main")
# 执行结果 
# get page 2s finished
# get page 3s finished
# get page 4s finished
# main
```

`wait` 方法接收 3 个参数，等待的任务序列、超时时间以及等待条件。等待条件 `return_when` 默认为`ALL_COMPLETED`，表明要等待所有的任务都结束。可以看到运行结果中，确实是所有任务都完成了，主线程才打印出 `main`。等待条件还可以设置为 `FIRST_COMPLETED`，表示第一个任务完成就停止等待。





## ProcessPoolExecutor 进程池执行器

> `ProcessPoolExecutor` 进程池执行器类是 `Executor` 执行器类的子类，使用进程池来异步执行调用。
> `ProcessPoolExecutor` 使用了` multiprocessing` 模块，这允许它可以规避 Global Interpreter Lock，但是也意味着只能执行和返回可序列化的（picklable）对象。

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4] # 并不是真的url
all_task = [executor.submit(get_html, (url)) for url in urls]

for future in as_completed(all_task):
    data = future.result()
    print("in main: get page {}s success".format(data))

# 执行结果
# get page 2s finished
# in main: get page 2s success
# get page 3s finished
# in main: get page 3s success
# get page 4s finished
# in main: get page 4s success
```

`as_completed()`方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会`yield`这个任务，就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，**先完成的任务会先通知主线程**。





# 源码分析

引用： [博客园 - naralv - Python线程池ThreadPoolExecutor源码分析](https://www.cnblogs.com/naralv/p/11190602.html)

## Executor Object 执行器对象

> `concurrent.futures.Executor` 类
> 这个抽象类提供了一系列方法，可以用于异步执行调用。
> 它不能直接使用，只能通过子类化出来的具体类来使用。



### 定义的方法

#### `submit(self, fn, *args, **kwargs)`

```python
def submit(self, fn, *args, **kwargs):
    """Submits a callable to be executed with the given arguments.

        Schedules the callable to be executed as fn(*args, **kwargs) and returns
        a Future instance representing the execution of the callable.

        Returns:
            A Future representing the given call.
        """
    raise NotImplementedError()
```



#### `map(func, *iterables, timeout=None, chunksize=1)`

> 类似内置函数 `map(func, *iterables)`，但是有两点不同：
>
> 1. 立即获取 `iterables` 而不会惰性获取；
> 2. 异步执行 `func`，并支持多次并发调用。

```python
def map(self, fn, *iterables, timeout=None, chunksize=1):
    """Returns an iterator equivalent to map(fn, iter).

    Args:
        fn: A callable that will take as many arguments as there are
            passed iterables.
        timeout: The maximum number of seconds to wait. If None, then there
            is no limit on the wait time.
        chunksize: The size of the chunks the iterable will be broken into
            before being passed to a child process. This argument is only
            used by ProcessPoolExecutor; it is ignored by
            ThreadPoolExecutor.

    Returns:
        An iterator equivalent to: map(func, *iterables) but the calls may
        be evaluated out-of-order.

    Raises:
        TimeoutError: If the entire result iterator could not be generated
            before the given timeout.
        Exception: If fn(*args) raises for any values.
    """
    if timeout is not None:
        end_time = timeout + time.monotonic()

    fs = [self.submit(fn, *args) for args in zip(*iterables)]

    # Yield must be hidden in closure so that the futures are submitted
    # before the first iterator value is required.
    def result_iterator():
        try:
            # reverse to keep finishing order
            fs.reverse()
            while fs:
                # Careful not to keep a reference to the popped future
                if timeout is None:
                    yield fs.pop().result()
                else:
                    yield fs.pop().result(end_time - time.monotonic())
        finally:
            for future in fs:
                future.cancel()

    return result_iterator()

```

它返回一个迭代器。
从调用 `Executor.map()` 开始的 timeout 秒之后，如果在迭代器上调用了 `__next__()` 并且无可用结果的话，迭代器会抛出 `concurrent.futures.TimeoutError` 异常。
timeout 秒数可以是浮点数或者整数，如果设置为 None 或者不指定，则不限制等待时间。

如果 func 调用抛出了异常，那么该异常会在从迭代器获取值的时候抛出。

当使用 `ProcessPoolExecutor` 的时候，这个方法会把 iterables 划分成多个块，作为独立的任务提交到进程池。这些块的近似大小可以通过给 chunksize 指定一个正整数。对于很长的 iterables，使用较大的 chunksize 而不是采用默认值 1，可以显著提高性能。对于 `ThreadPoolExecutor`，chunksize 不起作用。

```shell
# chunksize 是 3.5 加入的新参数。
```

**注意**：

&emsp;&emsp;不管并发任务的执行次序如何，`map` 总是基于输入顺序来返回值。`map` 返回的迭代器，在主程序迭代的时候，会等待每一项的响应。





#### `shutdown(self, wait=True)`

> 告诉执行器 executor 在当前所有等待的 future 对象运行完毕后，应该释放执行器用到的所有资源。

```python
def shutdown(self, wait=True):
    """Clean-up the resources associated with the Executor.

    It is safe to call this method several times. Otherwise, no other
    methods can be called after this one.

    Args:
        wait: If True then shutdown will not return until all running
            futures have finished executing and the resources used by the
            executor have been reclaimed.
    """
    pass
```

&emsp;&emsp;在 shutdown 之后再调用 Executor.submit() 和 Executor.map() 会报运行时错误 RuntimeError。
如果 wait 为 True，那么这个方法会在所有等待的 future 都执行完毕，并且属于执行器 executor 的资源都释放完之后才会返回。
&emsp;&emsp;如果 wait 为 False，本方法会立即返回。属于执行器的资源会在所有等待的 future 执行完毕之后释放。
不管 wait 取值如何，整个 Python 程序在等待的 future 执行完毕之前不会退出。你可以通过 with 语句来避免显式调用本方法。with 语句会用 `wait=True` 的默认参数调用 `Executor.shutdown()`方法





## ThreadPoolExecutor

### `__init__`

> `_init__`方法中主要重要的就是任务队列和线程集合，在其他方法中需要使用到。

```python
def __init__(self, max_workers=None, thread_name_prefix=''):
    """初始化一个新的ThreadPoolExecutor实例。
     参数：
         max_workers：		可用于执行以下操作的最大线程数执行给定的调用。
         thread_name_prefix：提供我们的线程的可选名称前缀。
    """
    if max_workers is None:
        # 如果没有设置最大值，则默认为 cpu 核心数的 5 倍
        max_workers = (os.cpu_count() or 1) * 5
    if max_workers <= 0:
        raise ValueError("max_workers must be greater than 0")

    self._max_workers = max_workers
    # 任务队列， 每次提交就将 task 放入队列中
    self._work_queue = queue.Queue()
    # 启动线程的集合
    self._threads = set()
    self._shutdown = False
    # submit 和 shutdown 的互斥锁
    self._shutdown_lock = threading.Lock()
    self._thread_name_prefix = (thread_name_prefix or
                                ("ThreadPoolExecutor-%d" % self._counter()))

```



### `submit()`
> 把worker放入queue中
> 开启一个新线程不断从queue中取出woker，执行woker.run()，即执行func()

```python
def submit(self, fn, *args, **kwargs):
    with self._shutdown_lock:
        if self._shutdown:
            raise RuntimeError('cannot schedule new futures after shutdown')

        f = _base.Future()                  # 核心, 未来对象，负责接收 task 状态和结果
        # 把目标函数f包装成worker对象，执行worker.run()会调用f()
        w = _WorkItem(f, fn, args, kwargs)  # 任务对象，接收未来对象以及 task 的函数名和参数， 任务执行通过该对象的 run 方法
        
        self._work_queue.put(w)             # 将worker任务对象放到任务队列中
        self._adjust_thread_count()         # 根据设置的最大线程数创建线程， 不断的从 queue 中获取 worke r对象，获取到则调用 worker.run()
        return f                            # 返回未来对象，让主线程能够获得 task 的结果

submit.__doc__ = _base.Executor.submit.__doc__
```

`submit`中有两个重要的对象，`_base.Future()`和`_WorkItem()`对象，`_WorkItem()`对象负责运行任务和对`future`对象进行设置，最后会将`future`对象返回，可以看到整个过程是立即返回的，没有阻塞。



### `_adjust_thread_count()`
> 开启一个新线程执行 _worker 函数，这个函数的作用就是不断去 queue 中取出 worker， 执行 `woker.run()`，即执行 `func()`
> 把新线程跟队列 queue 绑定，防止线程被 `join(0)` 强制中断。

```python
def _adjust_thread_count(self):
    # 当执行del executor时，这个回调方法会被调用，也就是说当executor对象被垃圾回收时调用
    def weakref_cb(_, q=self._work_queue):
        q.put(None)

    # TODO(bquinlan): 如果有更多线程，应避免创建新线程
    # 空闲线程数大于工作队列中的项目数。
    num_threads = len(self._threads)
    if num_threads < self._max_workers:
        # 如果启动的线程数小于最大线程数就创建线程
        # 线程使用的函数是 _worker, 传入的参数是一个弱引用和 task 队列
        thread_name = '%s_%d' % (self._thread_name_prefix or self,
                                 num_threads)
        # 把_worker函数作为新线程的执行函数
        t = threading.Thread(name=thread_name, target=_worker,
                             args=(weakref.ref(self, weakref_cb),
                                   self._work_queue))
        t.daemon = True
        t.start()
        self._threads.add(t)
        # 这一步很重要，是确保该线程t不被t.join(0)强制中断的关键。具体查看_python_exit 函数
        _threads_queues[t] = self._work_queue
```



### shutdown()

> `shutdown(wait=True)` 方法默认阻塞当前线程，等待子线程执行完毕。即使 `shutdown(wait=Fasle)` 也只是非阻塞的关闭线程池，线程池中正在执行任务的子线程并不会被马上停止，而是会继续执行直到执行完毕。

```python
def shutdown(self, wait=True):
    with self._shutdown_lock:
        self._shutdown = True
        self._work_queue.put(None)
    if wait:
        for t in self._threads:
            t.join()

shutdown.__doc__ = _base.Executor.shutdown.__doc__
```





### _WorkItem 对象

> `_WorkItem`对象的职责就是执行任务和设置结果。这里面主要复杂的还是`self.future.set_result(result)`。

```python
class _WorkItem(object):
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn            # 执行的 task函数
        self.args = args
        self.kwargs = kwargs

    def run(self):
        if not self.future.set_running_or_notify_cancel():
            return

        try:
            # 执行任务
            result = self.fn(*self.args, **self.kwargs)
        except BaseException as exc:
            self.future.set_exception(exc)
            # Break a reference cycle with the exception 'exc'
            self = None
        else:
            # 对 future 对象设置结果
            self.future.set_result(result)

```



### 线程执行函数--_worker

> 这是线程池创建线程时指定的函数入口，主要是在新线程中不断获得 queue 中的 worker 对象，执行 `worker.run()` 方法，执行完毕后通过放入 None 到 queue 队列的方式来通知其他线程结束。

```python
def _worker(executor_reference, work_queue):
    """
    这是线程池中线程执行的函数，线程池中的所有线程创建的时候都是使用此函数
    :param executor_reference:
    :param work_queue:
    :return:
    """
    try:
        while True:			# 不断从queue中取出 worker对象
            # 从 task 队列中获取一个 task (是 _WorkItem 对象)
            work_item = work_queue.get(block=True)
            if work_item is not None:
                work_item.run()					# 执行func()
                # Delete references to object. See issue16284
                del work_item
                continue
            # 从弱引用对象中返回executor
            executor = executor_reference()
            # Exit if:
            #   - The interpreter is shutting down OR
            #   - The executor that owns the worker has been collected OR
            #   - The executor that owns the worker has been shutdown.
            
            # 当executor执行shutdown()方法时executor._shutdown为True，同时会放入None到队列，
            # 当work_item.run()执行完毕时，又会进入到下一轮循环从queue中获取worker对象，但是由于shutdown()放入了None到queue，因此取出的对象是None，从而判断这里的if条件分支
            # 发现executor._shutdown是True，又放入一个None到queue中，是来通知其他线程跳出while循环的
            # shutdown()中的添加None到队列是用来结束线程池中的某一个线程的，这个if分支中的添加None
            # 队列是用来通知其他线程中的某一个线程结束的，这样连锁反应使得所有线程执行完func中的逻辑后都会结束
            if _shutdown or executor is None or executor._shutdown:
                # Notice other workers
                work_queue.put(None)
                return
            del executor
    except BaseException:
        _base.LOGGER.critical('Exception in worker', exc_info=True)

```



### _python_exit()

> 用来注册一个函数，当 MainThread 中的逻辑执行完毕时，会执行注册的这个 `_python_exit` 函数。然后执行 `_python_exit` 中的逻辑，也就是说 `t.join()` 会被执行，强制阻塞。这里好奇，既然是在 MainThread 结束后执行，那这个 `t.join()` 是在什么线程中被执行的呢。其实是一个叫 `_DummyThread` 线程的虚拟线程中执行的。

```python
import atexit


_threads_queues = weakref.WeakKeyDictionary()
_shutdown = False

def _python_exit():
    global _shutdown
    _shutdown = True
    items = list(_threads_queues.items())
    for t, q in items:
        q.put(None)
	# 取出_threads_queues中的线程t，执行t.join()强制等待子线程完成
    for t, q in items:
        t.join()

atexit.register(_python_exit)
```

示例：

```python
import atexit
import threading
import weakref
import time

threads_queues = weakref.WeakKeyDictionary()

def foo():
    print('enter at {} ...'.format(time.strftime('%X')))
    time.sleep(5)
    print('exit  at {} ...'.format(time.strftime('%X')))

def _python_exit():
    items = list(threads_queues.items())
    print('current thread in _python_exit --> ', threading.current_thread())
    for t, _ in items:
        t.join()

atexit.register(_python_exit)

if __name__ == '__main__':

    t = threading.Thread(target=foo)
    t.setDaemon(True)
    t.start()

    threads_queues[t] = foo

    print(time.strftime('%X'))
    t.join(timeout=2)
    print(time.strftime('%X'))
    t.join(timeout=2)
    print(time.strftime('%X'))
    print('current thread in main -->', threading.current_thread())
    print(threading.current_thread(), 'end')
```

&emsp;&emsp;从这个例子可以看到，当线程 t 开启时 foo 函数阻塞 5 秒，在 MainThread 中 2 次调用`t.join(timeout=2)`，分别的等待了 2 秒，总等待时间是 4 秒，但是当执行第二个`t.join(timeout=2)` 后，线程 t 依然没有被强制停止，然后主线执行完毕，然后 `_python_exit` 方法被调用，在 _DummyThread 线程中由调用 `t.join()`，继续等待子线程 t 的执行完毕，直到线程t打印`exit at 17:13:49 ...`才执行完毕。

总结：

&emsp;&emsp;`join()` 是可以被一个线程多次调用的，相当是多次等待的叠加。把 `_python_exit` 函数注册到 atexit 模块后，其他线程即使企图调用 `t.jion(timeout)` 来终止线程 t 也不起作用，因为`_python_exit` 总是在最后执行时调用 `t.jion()` 来保证让线程t执行完毕，而不是被中途强制停止。







## Future 对象

> `Future` 类封装了可调用对象的异步执行。
> `Future` 实例通过 `Executor.submit()` 创建，除非用于测试，不应该直接手动创建。













