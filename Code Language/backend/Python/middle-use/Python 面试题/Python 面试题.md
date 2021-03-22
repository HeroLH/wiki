----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

## 装饰器（什么是AOP/面向切面编程）

> 面向切面编程（AOP）是一种编程思想，与OOP并不矛盾，只是他们的关注点不同。面向对象的目的在于**抽象和管理**，而面向切面的目的在于**解耦和复用**

### 作用:

- 使得功能逻辑和业务逻辑解耦，更能和业务的修改完全独立，代码结构清晰，开发方便

- 一键注入，代码复用程度高，扩展方便

### 装饰器

#### 原理

&emsp;&emsp;python 中的装饰器就是设计来实现切面注入功能的，较为经典的有插入日志、性能测试、事务处理等。装饰器式解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数本身无关的雷同代码并继续复用。类如，Django 中就大量使用装饰器去完成一下切面需求，如权限控制，内容过滤，请求管理等等。

```python
def w1(func):
    def inner():
        # 代码块 1
        # 代码块 2
        # 代码块 3
        return func()
    return inner
 
@w1
def f1():
    print 'f1'
```

&emsp;&emsp;当写完这段代码后( 函数未被执行、未被执行、未被执行 )，python 解释器就会从上到下解释代码，步骤如下：
> def w1(func):  ==>将w1函数加载到内存
> @w1

&emsp;&emsp;从表面上看解释器仅仅会解释这两句代码，因为函数在**没有被调用之前**其内部代码不会被执行。但是 @w1 这一句代码里却有大文章，**@函数名** 是python的一种语法糖。

如上例@w1内部会执行w1函数，并将 @w1 下面的 **函数** 作为w1函数的参数，即：`@w1 等价于 w1(f1)`。所以，内部就会去执行：

```python
def inner():
	# 代码块 1
    # 代码块 2
    # 代码块 3
	return f1()   # func是参数，此时 func 等于 f1
return inner     # 返回的 inner，inner代表的是函数，非执行函数
```

其实就是将原来的 f1 函数塞进另外一个函数中( 闭包 )



#### 有参数的装饰器

```python
# 一个参数的
def w1(func):
    def inner(arg):
        # 验证1
        # 验证2
        # 验证3
        return func(arg)
    return inner

@w1
def f1(arg):
    print 'f1'
```


```python
# 两个或三个参数的
def w1(func):
    def inner(arg1,arg2,arg3):
        # 验证1
        # 验证2
        # 验证3
        return func(arg1,arg2,arg3)
    return inner

@w1
def f1(arg1,arg2,arg3):
    print 'f1'
```

```python
# n 个参数的
def w1(func):
    def inner(*args,**kwargs):
        # 验证1
        # 验证2
        # 验证3
        return func(*args,**kwargs)
    return inner
 
@w1
def f1(arg1,arg2,arg3):
    print 'f1'
```







# 你的写的类都继承过哪些类？

class View(object):

class APIView(View):

class GenericAPIView(views.APIView):

class GenericViewSet(ViewSetMixin, generics.GenericAPIView)

class ModelViewSet(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin,
            mixins.ListModelMixin,
            GenericViewSet):























