----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# 了解 flask

&emsp;&emsp;Flask是一个基于 Python 开发并且依赖 jinja2 模板和 Werkzeug WSGI 服务的一个微型框架。

> 对于 Werkzeug 本质是 Socket 服务端，其用于接收 http 请求并对请求进行预处理，然后触发 Flask 框架，开发人员基于 Flask 框架提供的功能对请求进行相应的处理，并返回给用户；

> 如果要返回给用户复杂的内容时，需要借助jinja2模板来实现对模板的处理，即：将模板和数据进行渲染，将渲染后的字符串返回给用户浏览器。

&emsp;&emsp;微框架中的“微”意味着 Flask 旨在保持核心简单而易于扩展。Flask 不会替你做出太多决策——比如使用何种数据库。而那些 Flask 所选择的——比如使用何种模板引擎——则很容易替换。

&emsp;&emsp;默认情况下，Flask 不包含数据库抽象层、表单验证，或是其它任何已有多种库可以胜任的功能。然而，Flask 支持用扩展来给应用添加这些功能，众多的扩展提供了数据库集成、表单验证、上传处理、各种各样的开放认证技术等功能。

```shell
# 短小精悍、可扩展强 的一个Web框架。
# 注意：**上下文管理机制**
```





## 	django和flask的认识

&emsp;&emsp;django 是一个大而全的 web 框架，内部提供了很多组件，比如 orm、admin、form、分页、缓存等等，我们只需要在配置文件中修改就能将其应用起来

&emsp;&emsp;flask 是一个轻量级的，短小精悍，可扩展性强的一个扩展，适合用来快速开发小型项目。但是用来开发大型项目也可以，它也提供了很多第三方组件，我们可以把 falsk 跟第三方组件结合起来也可以创建一个跟 django 类似的集成很多功能的web框架，这也体现了它的可定制性比 django 强。





## flask和django最大的不同点：request/session

django 的 session 是依附于 request，request.session



## 3.flask知识点

- 模板+静态文件

    ```shell
    app= Flask(__name__,....)
    ```

- 路由 

  ```python
  @app.route('/index',methods=["GET"])
  ```

  

  

  

- 响应 

- session 
  session['xx'] = 123
  session.get('xx')



如果遇到一个没看过的web 框架，第一念头去找它的路由，通过路由找到它的视图，视图里面就是写着它的业务逻辑





# flask 快速上手

## flask 的安装

### Python 版本

> 我们推荐使用最新版本的 Python 3 。 Flask 支持 Python 3.4 及更高版本的 Python 3 、 Python 2.7 和 PyPy 。



### 依赖

当安装 Flask 时，以下配套软件会被自动安装。

- [Werkzeug](https://palletsprojects.com/p/werkzeug/) 用于实现 WSGI ，应用和服务之间的标准 Python 接口。
- [Jinja](https://palletsprojects.com/p/jinja/) 用于渲染页面的模板语言。
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/) 与 Jinja 共用，在渲染页面时用于避免不可信的输入，防止注入攻击。
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) 保证数据完整性的安全标志数据，用于保护 Flask 的 session cookie.
- [Click](https://palletsprojects.com/p/click/) 是一个命令行应用的框架。用于提供 `flask` 命令，并允许添加自定义 管理命令。



#### 可选依赖

以下配套软件不会被自动安装。如果安装了，那么 Flask 会检测到这些软件。

- [Blinker](https://pythonhosted.org/blinker/) 为 [信号](https://dormousehole.readthedocs.io/en/latest/signals.html#signals) 提供支持。
- [SimpleJSON](https://simplejson.readthedocs.io/) 是一个快速的 JSON 实现，兼容 Python’s `json` 模块。如果安装 了这个软件，那么会优先使用这个软件来进行 JSON 操作。
- [python-dotenv](https://github.com/theskumar/python-dotenv#readme) 当运行 `flask` 命令时为 [通过 dotenv 设置环境变量](https://dormousehole.readthedocs.io/en/latest/cli.html#dotenv) 提供支持。
- [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供快速高效的重载。



### 虚拟环境

- 建议在开发环境和生产环境下都使用虚拟环境来管理项目的依赖。
- 为什么要使用虚拟环境？
    > &emsp;&emsp;随着你的 Python 项目越来越多，你会发现不同的项目会需要 不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。
    > &emsp;&emsp;虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。

- Python 3 内置了用于创建虚拟环境的 [`venv`](https://docs.python.org/3/library/venv.html#module-venv) 模块。如果你使用的是较新的 Python 版本，那么请接着阅读本文下面的内容。
- 如果你使用 Python 2 ，请首先参阅 [安装 virtualenv](https://dormousehole.readthedocs.io/en/latest/installation.html#install-install-virtualenv) 。



#### 创建一个虚拟环境

- 创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 `venv` 文件夹：

    ```shell
    mkdir myproject
    cd myproject
    python3 -m venv ./venv
    ```

    



#### 激活虚拟环境

- 在开始工作前，先要激活相应的虚拟环境：

    ```shell
    venv/bin/activate
    ```

- 在 Windows 下：

    ```shell
    venv\Scripts\activate
    ```

激活后，你的终端提示符会显示虚拟环境的名称。



### 安装 Flask

- 在已激活的虚拟环境中可以使用如下命令安装 Flask：

    ```shell
    pip install Flask
    ```

Flask 现在已经安装完毕。请阅读 [快速上手](https://dormousehole.readthedocs.io/en/latest/quickstart.html) 或者 [文档目录](https://dormousehole.readthedocs.io/en/latest/index.html) 。



#### 与时俱进

- 如果想要在正式发行之前使用最新的 Flask 开发版本，可以使用如下命令从主分支 安装或者更新代码：

    ```shell
    pip install -U https://github.com/pallets/flask/archive/master.tar.gz
    ```

    



## 依赖wsgi：werkzeug
> 安装 flask 的时候会自动安装 werkzurg

### 什么是wsgi？
> web服务网关接口，wsgi是一个协议
>
> 实现其协议的模块本质上就是socket服务端用于接收用户请求，并处理。
> 一般web框架基于 wsgi 实现，这样实现关注点分离



### 第一个 werkzeug 应用

```python
from werkzeug.wrappers import Response		# 导入模块
from werkzeug.serving import run_simple

def hello(environ, start_response):
    # environ		：请求相关的所有数据(由 wsgi 做初步封装)
    # start_response：用于设置响应相关的数据
    response = Response('Hello World!')
    return response(environ, start_response)	# 返回 Response 对象

if __name__ == '__main__':
    run_simple('localhost', 4000, hello)
```



### 与 wsgiref 应用进行对比

```python
# python 标准库提供的独立 WSGI 服务器 wsgiref。
from wsgiref.simple_server import make_server		

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]
	# 返回字节
 
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
```



## 一个最小 flask 应用

### 半个 flask 应用

```python
from flask import Flask		# 导入 Flask 类,该类的实例将会成为我们的 WSGI 应用。
app = Flask(__name__)		# 实例化 Flask 类
# Flask 第一个参数只是给对象起一个名，并不一定要用 __name__
# 第一个参数是应用模块或者包的名称。如果你使用一个单一模块（就像本例），那么应当使用 `__name__` 
# 因为名称会根据这个模块是按应用方式使用还是作为一个模块导入而发生变化。
#	（可能是 ‘__main__’ ， 也可能是实际导入的名称）
# 这个参数是必需的，这样 Flask 才能知道在哪里可以找到模板和静态文件等东西。

app.run()
```

> **会报错 404 not found！**
> 因为我们只写了访问，并没有接受处理函数



### 最小 flask 应用

```python
from flask import Flask				
# 1、实例化 Flask 对象，所有的功能都是从 Falsk 对象出发的的
app = Flask(__name__)

# 2、设置路由
@app.route('/index')				# 使用 route() 装饰器来告诉 Flask 触发函数的 URL 
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # 3、启动 socket 服务端
    app.run()
```



## 程序运行流程图

```mermaid
graph LR
A["app.run()"] -->B("run_simple()")
B --> C((死循环,等待客户端响应))
C --> D("__call__()")
D --> E(" wsgi_app()")
```









## 示例：用户登录应用

> 新建一个项目文件夹 user_login

### 登录页面的展示

#### 视图 app.py

&emsp;&emsp;在项目文件夹 user_login 下新建一个 app.py 文件

```python
from flask import Flask,render_template		
app = Flask(__name__)

@app.route("/login")						# 默认只接受 GET 请求
def login():
	return render_template("login.html")	# 相当于 django 中的 render()
	# 会自动去同一级文件下找 templates 文件夹
    # 如果要改默认文件夹可以在 Flask 实例化时指定Flask(__name__,template_folder="")

    # return "Login"                        # 相当于 Django 中的 HttpRespose

if __name__ == "__main__":
    app.run()
```

#### 模版 templates

&emsp;&emsp;在项目文件夹 user_login 下新建一个 templates 文件夹；在 template 文件夹新建一个login.html 文件：

```html
<body>
    <h1 align="center">用户登录</h1>
    <form method="post" action="">
        <input type="text" name="user">
        <input type="password" name="passwd">
        <input type="submit">
    </form>
</body>
```

> **!attention!**：
> 此处文件夹名称一定得是 templates 否则会找不到 login.html
> 当然你可以在 Flask 实例化的时候改变它，如：
>
> ```
> app = Flask(__name__, template_folder="templates_folder" )
> ```

#### 效果展示

![1582610255100](assets/1582610255100.png)



### 登录页面的表单

#### 视图 app.py

```python
from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])	# 允许 GET 和 POST 方法
def login():
    print( request )                        
    # <Request 'http://127.0.0.1:5000/login' [POST]>
    print( request.method )                 # 答应请求方法，如 POST
    print( request.args )					# 对应 GET 请求体
    print( request.form )					# 对应 POST 请求体
    
    if request.method == 'GET':
        return render_template("login.html")

    user = request.form.get("user")
    pwd = request.form.get("passwd")
    if user == "admin" and pwd == "123":
        return redirect("/index")           # redirect() 方法也是需要导入的
    return render_template('login.html', error="用户名或密码错误！")

@app.route("/index",methods=["GET","POST"])
def index():
    # flask 也支持字典传值，不过需要在字典前加 **
    return render_template('index.html', **{ "msg":"登录成功！"})

if __name__ == "__main__":
    app.run()
```

**!attention!**：
> - 路由默认只允许 `get` 请求，要在路由里加上 `methods` 参数指定方法才能接受其他：
>  ```python
> @app.route("/login",methods=["GET","POST"])
>  ```


> - flask 也支持字典传值，不过需要在字典前加 `**`
> ```python
> return render_template('index.html', **{ "msg":"登录成功！"})
> ```


> - 获取请求体的方法：
> ```
> GET 请求：		request.args	( django 中是 request.GET  )
> POST 请求：	request.form	( django 中是 request.POST )
> ```



#### 模版 templates

##### login.html

```html
<body>
    <h1 align="center">用户登录</h1>
    <form method="post" action="">
        <input type="text" name="user">
        <input type="password" name="passwd">
        <input type="submit">
    </form>
    <p style="color: red;">{{ error }}</p>
</body>
```



##### index.html

&emsp;&emsp;在项目文件夹下新建一个 static 文件夹，在该文件夹下存放静态文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    <h1>欢迎使用</h1>
    <p style="color: green;">{{ msg }}</p>
    <img src="/static/test_img.gif">
</body>
</html>
```

#### 效果展示

![1582612175643](assets/1582612175643.png)







# Flask 基础
## 1 配置文件
flask中 的配置文件是一个 `flask.config.Config` 对象（继承字典）,默认配置为：

```python
{
    'DEBUG':        get_debug_flag(default=False),  # 是否开启 Debug 模式
    'TESTING':                              False,  # 是否开启测试模式
    'PROPAGATE_EXCEPTIONS':                 None,                         
    'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
    'SECRET_KEY':                           None,
    # 默认 session 超时时间：31 天
    'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
    'USE_X_SENDFILE':                       False,
    'LOGGER_NAME':                          None,
    'LOGGER_HANDLER_POLICY':               'always',
    'SERVER_NAME':                          None,
    'APPLICATION_ROOT':                     None,
     'SESSION_COOKIE_NAME':                  'session',	# 写到cookie里的名称
    'SESSION_COOKIE_DOMAIN':                None,		# 域名
    'SESSION_COOKIE_PATH':                  None,		# 路径
    'SESSION_COOKIE_HTTPONLY':              True,		#是否只设置为http读取
    'SESSION_COOKIE_SECURE':                False,		# 是否
    'SESSION_REFRESH_EACH_REQUEST':         True,
    'MAX_CONTENT_LENGTH':                   None,
    'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
    'TRAP_BAD_REQUEST_ERRORS':              False,
    'TRAP_HTTP_EXCEPTIONS':                 False,
    'EXPLAIN_TEMPLATE_LOADING':             False,
    'PREFERRED_URL_SCHEME':                 'http',
    'JSON_AS_ASCII':                        True,
    'JSON_SORT_KEYS':                       True,
    'JSONIFY_PRETTYPRINT_REGULAR':          True,
    'JSONIFY_MIMETYPE':                     'application/json',
    'TEMPLATES_AUTO_RELOAD':                None,
}
```



### 使用方式

#### 方式一：直接引用修改

```python
from flask import  Flask
app = Flask(__name__)
print( app.config )             		# 封装了全部的默認配置文件
app.config["DEBUG"] = True				# 找到并修改

if __name__ == "__main__":
    app.run()
```





#### 方式二：类文件调用

> 底层是通过类的反射实现的，dir() 和 getattr() 和 importlib
>
> ```
> 但凡可扩展性强的地方都会这么玩，比如：
> django 中间件
> django rest framework 全局配置
> ```
>
> 

- **config.py**

    ```python
    from flask import  Flask
    app = Flask(__name__)
    print( app.config )
    
    app.config.from_object("settings.Foo")	# 从sys.path 中已经存在路径开始
    print( app.config )
    
    if __name__ == "__main__":
        app.run()
    ```

- **settings.py**

    ```python
    # settings.py 文件默认路径要放在程序 root_path 目录，如果instance_relative_config 为T rue，则就是instance_path目录
    class Foo:
        DEBUG = True
    ```

    > !attention!：配置文件中不能有逗号，否则会报错

##### 不同环境下使用不同的配置文件

- **config.py**

    ```python
    from flask import  Flask
    app = Flask(__name__)
    
    app.config.from_object("settings.Pro")		
    
    if __name__ == "__main__":
        app.run()
    ```

- **settings.py**

    ```python
    class Config( object ):
        DEBUG = False
        TESTING = False
        SECRET_KEY = "asdf"							# 共同的配置
    
    class ProductionConfig( Config ):				# 稳定版
        DATABASE_URL = "mysql://user@localhost/foo"
    
    class DevelopmentConfig( Config ):	    		# 开发版
        DEBUG = True
    
    class TestingConfig( Config ):					# 测试版
    	TESTING = True
    ```



#### 方式三 其他导入格式

##### 导入文件
```
app.config.from_pyfile("python文件名称")
```
> 文件的格式
> ```python
> DEBUG = True
> ```



##### 导入 Json
> JSON文件名称，必须是 json 格式，因为内部会执行 `json.loads`
```python
app.config.from_json("json文件名称")
```



##### 导入字典
```python
app.config.from_mapping({'DEBUG':True})
```



##### 导入环境变量
> 环境变量的值为python文件名称名称，内部调用from_pyfile方法
```python
app.config.from_envvar("环境变量名称")
```





### 配置文件导入原理

> 底层是通过类的反射实现的，dir() 和 getattr() 和 importlib

只要给一个路径 “config.Foo”，可以找到类并获取去其中的大写的静态字段。
新建两个 py 文件：settings.py 和 config.py

#### 原理实现

##### Setting.py

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws

import importlib
path = "config.Foo"
p,c = path.rsplit( ".",maxsplit=1 )     # 从右边第一个 . 开始切分
m = importlib.import_module( p )
cls = getattr( m,c )                    # 找到该类
print( p )                              # config
print( c )                              # Foo
print( m )                              # 类详细模块信息
print( cls )                            # <class 'config.Foo'>
print( dir( cls ) )                     # ['DEBUG', 'TEST', '__class__', ...

for key in dir( cls ):
    if key.isupper():
        print( key ,getattr(cls,key) )
        # getattr(object, name[, default])
        # 函数功能是从对象object 中获取名称为 name的属性，等效与调用 object.name。
```

##### config.py

```python
class Foo:
    DEBUG = True
    TEST = True
    # 必须要大写，否则读不到
```



#### Falsk 源码实现

```mermaid
graph LR
    a3-->b1
    b2-->c1
    
    subgraph Flask 类
    a1(app.config)-->|=|a2("make_config()")
    a2 -->|return|a3(config_class)
    end
    
    subgraph config.py 模块
    b1(Config类)-->b2("from_object(obj)")
    end
    
    subgraph utils.py 模块
    c1("import_string(import_name)")-->c2(getattr)
    end
```

![1582788823956](assets/1582788823956.png)





## 2 路由系统

> flask 的路由通过装饰器实现

### 装饰器的复习

```python
def auth(func):
    # 装饰器
    def inner(*args,**kwargs):
        print("前")
        ret = func( *args, **kwargs )
        print("后")
        return ret
    return inner

@auth
def index():
    pass

print(index)
# 没加装饰器之前，输出为 <function index at 0x0000020F21E2AC80>
# 加了装饰器之后，输出为 <function auth.<locals>.inner at 0x0000021F531FAD08>

print(index.__name__)
# 没加装饰器之前，输出为 index
# 加了装饰器之后，输出为 inner
```



#### 更彻底的装饰器

```python
# 为防止上述情况发生，装饰器可以这么写;
import functools
def auth2(func):
    @functools.wraps(func)					# 会将原函数信息带过来
    def inner(*args,**kwargs):
        ret = func( *args, **kwargs )
        return ret
    return inner

@auth2
def index2():
    pass

print( index2 )         # <function index2 at 0x000001617753E730>
print(index2.__name__)  # index2
```



#### 装饰器的先后顺序

> 自下而上顺序执行

##### 装饰器在路由上（X）

> 不应该这么做！装饰器的执行顺序是自下而上的

```python
def auth(func):
    def inner(*args,**kwargs):
        ret = func( *args, **kwargs )
        return ret
    return inner

@auth					# 原来是想装饰 login 的，结果却没装饰上
@app.route("/login")	# 先执行这一个装饰器，再将整体给 auth
def login():
    ...
```



##### 装饰器在路由下（&#10003;）

```python
def auth(func):
    def inner(*args,**kwargs):
        ret = func( *args, **kwargs )
        return ret
    return inner

@app.route("/login")
@auth
def login():
    ...

@app.route("/index")
@auth		
def index():
    ...
```

> 会出现一个问题，被 auth 装饰过后所有的函数名都变成了 inner ，而路由默认的endpoint 是函数名，相当于所有的视图都变成了 inner，会报错
>
> ```python
> AssertionError: View function mapping is overwriting an existing endpoint function: inner
> ```



###### 解决方法一：自定义 endpoint
```python
def auth(func):
    ...

@app.route("/login",endpoint="login" )
@auth
def login():
    ...

@app.route("/index", endpoint="index" )
@auth		
def index():
    ...
```



###### 解决方法二：functools（&#10003;）
```python
import functools
def auth(func):
    @functools.wraps(func)					# 会将原函数信息带过来
    def inner(*args,**kwargs):
        ret = func( *args, **kwargs )
        return ret
    return inner
```

> 各个视图函数看上去是 inner，本质上还是自身
> 比手动一个一个加 endpoint 方便多了



### @app.route() 和 app.add_url_rule 参数:

#### rule

> URL规则



#### view_func

> 视图函数名称



#### methods=None

flask 默认只允许 `get` 请求，要在路由里加上 `methods` 参数指定方法，具体方法如下：

```python
@app.route("/login",methods=["GET","POST"])
```

![1582600732373](assets/1582600732373.png)

flask 中请求不是通过参数传递的，而是通过导入 request 模块(上下文管理相关内容再详细解答为什么要这样)



#### endpoint=None

名称，用于反向生成URL，即： url_for('名称')

> 相当于 django 中 url 的 name，给 url 起了一个别名;
> 这里建议：**endpoint 一定要写！**

```python
from flask import  Flask,render_template,url_for
app = Flask(__name__)
@app.route("/index",endpoint="index_asName" ) # 相当于给 /index 起了一个别名
# 如果不给 endpoint 参数，则默认值为函数名
def index():
    print( url_for("index_asName") )                # /index
    # url_for()   反向生成 url
    return render_template('index.html', **{ "msg":"登录成功！"})

if __name__ == "__main__":
    app.run()
```

- 如果不给 `endpoint` 参数，则默认值为函数名;
- 通过 `url_for("endpoint名")`  我们可以反向生成回 `url`;
- 如果 endpoint 同名，flask 会报错



#### defaults=None

> 默认值,当URL中无参数，函数需要参数时，使用 `defaults={'k':'v'}` 为函数提供参数

```python
@app.route( "/index",defaults={"v":123} )
def index( v ):
    return
```



#### strict_slashes=None

 对URL最后的 `/` 符号是否严格要求，默认为 `True`

```python
@app.route('/index',strict_slashes=False)
# 访问 http://www.xx.com/index/ 或 http://www.xx.com/index均可

@app.route('/index',strict_slashes=True)
# 仅支持访问 http://www.xx.com/index 
```



#### redirect_to=None

> 重定向到指定地址

```python
@app.route('/old/<int:nid>', redirect_to='/new/<nid>')
def old(adapter, nid):
    return "/home/888"			# 不会去执行，直接跳转到 new
# 或
def old(adapter, nid):
    return "/new/888"
@app.route('/old/<int:nid>', redirect_to=old )
```



#### subdomain=None

子域名访问

```python
from flask import Flask, views, url_for
app = Flask(import_name=__name__)
app.config['SERVER_NAME'] = 'xx.com:5000'
"""
测试环境下要去本机改 host
127.0.0.1	xx.com
127.0.0.1	admin.xx.com
127.0.0.1	username.xx.com
"""

# 访问 http://admin.xx.com:5000/ 时才生效
@app.route("/", subdomain="admin")
def static_index():
    """Flask supports static subdomains
    This is available at static.your-domain.tld"""
    return "static.your-domain.tld"

# 访问 http://username.xx.com:5000/dynamic 时才生效
@app.route("/dynamic", subdomain="<username>")
def username_index(username):
    """Dynamic subdomains are also supported
    Try going to user1.your-domain.tld/dynamic"""
    return username + ".your-domain.tld"


if __name__ == '__main__':
    app.run()
```





### 动态路由
- `@app.route('/user/<username>')`	什么都没写默认代表字符串
- `@app.route('/post/<int:post_id>')`
- `@app.route('/post/<float:post_id>')`
- `@app.route('/post/<path:path>')`
- `@app.route('/login', methods=['GET', 'POST'])`

常用路由系统有以上五种，所有的路由系统都是基于一下对应关系来处理：

```python
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
# 只支持以上几种，默认不支持自定义正则
```

#### 示例：

```python
from flask import  Flask,request,render_template,url_for
app = Flask(__name__)

@app.route("/index/<int:nid>-<int:nid2>")
def index(nid,nid2):
    print( url_for("index",nid=nid,nid2=nid2) )      # /index/2018-11
    return "index"

if __name__ == "__main__":
    app.run()
```





#### url_for() 反向路由

> 通过 `url_for("endpoint名")`  我们可以反向生成回 `url`;

```python
# 这样会显示完整的url地址
login_url = url_for("login"，_external = True)   
# http://127.0.0.1:5000/login

# 传递参数，对路径进行拼接
login_url = url_for("login", a=1, _external = True)
# http://127.0.0.1:5000/login?a=1

# 文件后缀拼接
login_url = url_for("static",filename="pic.jpg", _external=True)
# http://127.0.0.1:5000/static/pic.jpg
```







### 自定义正则

```python
from flask import Flask, views, url_for
app = Flask(import_name=__name__)

# 步骤一：定制类
from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    """
    自定义URL匹配正则表达式
    """
    def __init__(self, map, regex):
        super(RegexConverter, self).__init__(map)
        self.regex = regex

    def to_python(self, value):
        """
        路由匹配时，匹配成功后传递给视图函数中参数的值
        :param value:
        :return:
        """
        return int(value)

    def to_url(self, value):
        """
        使用url_for反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
        :param value:
        :return:
        """
        val = super(RegexConverter, self).to_url(value)
        return val

"""
1. 用户发送请求
2. flask内部进行正则匹配
3. 调用to_python(正则匹配的结果)方法,to_python 返回啥 视图函数的 nid 就是啥
4. to_python方法的返回值会交给视图函数的参数

"""


# 步骤二：添加到 flask 的默认转换器中
app.url_map.converters['regex'] = RegexConverter
# 在默认 DEFAULT_CONVERTERS 中添加上 regex
# app.url_map.converters --> self.default_converters.copy()
# --> ImmutableDict(DEFAULT_CONVERTERS)

# 步骤三：使用自定义正则
@app.route('/index/<regex("\d+"):nid>')
def index(nid):
    print( nid, type(nid) )             # to_python 的值
    print(url_for('index', nid='888'))  # to_url 的值
    return 'Index'


if __name__ == '__main__':
    app.run()
```





### 路由的原理

> app.add_url_rule(rule, endpoint, f, **options)

**示例**：

```python
from flask import  Flask,request,render_template,url_for
app = Flask(__name__)

@app.route("/index")
def index(nid,nid2):
    print( url_for("index",nid=nid,nid2=nid2) )      # /index/2018-11
    return "index"

if __name__ == "__main__":
    app.run()
```

> 程序会先执行 `decorator = app.route("/index")` 	：闭包
> 再执行 @decorator
> 将 函数index 当成参数传给 decorator





#### Flask 源码实现

```python
@app.route("/index")			# 相当于 @decorator
def index():					# 相当于 @decorator( index )
    pass
```

```python
def route(self, rule, **options):		# rule相当于 /index
    def decorator(f):					# f 为 index 视图函数
        endpoint = options.pop("endpoint", None)
        # 在 option 中找endpoint ，找不到默认值就为 None
        
        # 本质上生成对应关系的就是以下该函数
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator			# 返回 decorator 函数
```

所以路由我们也可以写成：

```python
def index():
    pass
app.add_url_rule("/index",None,index)
# app.add_url_rule("/index",None,index,method=[] ...)	# 都在 option 中
```

模拟 django 的路由:

```python
# django 也是这么实现的
urlpatterns = [
    ("/index",index),
    ("/xxx",xxx),
]
for item in urlpatterns:
    app.add_url_rule( item[0],None,item[1] )
```



app.route –> add_url_rule() –>heper._endpoint_from_view_func(view_func)

return `__name__`

add_url_rule() –> url_rule_class()





## 3 视图

### FBV

> 普通函数，略






###  CBV

> 本质上也是用类的反射，getattr()

```python
from flask import Flask,views
import functools
app = Flask(__name__)


def wrapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


class UserView(views.MethodView):
    methods = ['GET']				# 只允许GET 请求，post请求发不过来
	decorators = [wrapper,]			# 全部请求加装饰器

    def get(self,*args, **kwargs):
        return "GET"

    def post(self,*args, **kwargs):
        return "POST"
app.add_url_rule( "/user", None, UserView.as_view("user") )
# app.add_url_rule( "/user",endpoint=None,view_func=UserView.as_view("/user") )
# "user" 就相当于 endpoint 传递过去了

if __name__ == '__main__':
    app.run()
  
```



#### CBV 原理

##### as_view()

```python
@classmethod
def as_view(cls, name, *class_args, **class_kwargs):
    """将类转换为可以使用的实际视图函数与路由系统。
    内部会动态生成一个函数，该函数将在每个请求上实例化View类并调用 dispatch_request方法。
     传递给：meth：`as_view`的参数将转发给类的构造函数。
        """

    def view(*args, **kwargs):
        self = view.view_class(*class_args, **class_kwargs)
        return self.dispatch_request(*args, **kwargs)

    if cls.decorators:
        view.__name__ = name
        view.__module__ = cls.__module__
        for decorator in cls.decorators:
            view = decorator(view)

            # 我们将视图类附加到视图函数有两个原因：
            # 首先，它使我们能够轻松地弄清该事物来自于基于类的视图
            # 其次，它还用于实例化视图类，因此您实际上可以将其替换为其他东西以进行测试和调试。
            view.view_class = cls
            view.__name__ = name
            view.__doc__ = cls.__doc__
            view.__module__ = cls.__module__
            view.methods = cls.methods
            view.provide_automatic_options = cls.provide_automatic_options
            return view

```





##### dispatch_request(self, *args, **kwargs)

> django 里面也有，叫 self.dispath()

```python
def dispatch_request(self, *args, **kwargs):
    meth = getattr(self, request.method.lower(), None)
    # 找到方法

    # If the request method is HEAD and we don't have a handler for it
    # retry with GET.
    if meth is None and request.method == "HEAD":
        meth = getattr(self, "get", None)

    assert meth is not None, "Unimplemented method %r" % request.method
    return meth(*args, **kwargs)	# 执行方法
```



### 视图的执行流程







## 4 请求相关数据

```python
# 访问URL：http://127.0.0.1:5000/post
# 请求相关信息
request.method
request.args
request.form
request.values
request.cookies
request.headers
request.path				# /post
request.full_path			# /post?
request.script_root			# ‘’
request.url					# http://127.0.0.1:5000/post
request.base_url			# http://127.0.0.1:5000/post
request.url_root			# http://127.0.0.1:5000/	(结尾反斜杠)
request.host_url			# http://127.0.0.1:5000/	(结尾反斜杠)
request.host				# 127.0.0.1:5000
request.url_rule			# /post	(not a `str`, type is `Rule`)
request.url_charset			# utf-8

request.files
obj = request.files['the_file_name']
obj.save('/var/www/uploads/' + secure_filename(f.filename))
```





## 5 响应：
### 响应体：

```python
return redirect()						# 跳转页面
return “asdf”							# 字符串
return render_template('xxx.html')		# 模版渲染
return jsonify({'k1':'v1'})				# json 格式
return json.dumps( {'k1':'v1'} )		# json 格式
```



### 定制响应头：

```python
# obj 是 flask.wrappers.Response 类型
obj = make_response("asdf")			# 封装 response 对象
obj.headers['xxxxxxx'] = '123'
obj.set_cookie('key', 'value')		# response.delete_cookie('key')
return obj
```





## 示例：用户信息

### 视图 app.py

```python
from flask import Flask,request,render_template,redirect, url_for，session
app = Flask(__name__)
app.config.from_object("settings.Pro")
# app.secret_key = "asdfasdf"  
# 上面这句话写到配置文件中去了

USER_DICT = {					# 模拟用户信息
    1:{"name":"test1", "age": 18, "gender":"man"},
    2:{"name":"test2", "age": 28, "gender":"man"},
    3:{"name":"test3", "age": 15, "gender":"woman"},
}

def auth(func):
    def inner(*args,**kwargs):
        if not session.get("user1"):
            return redirect(url_for("login"))
        ret = func( *args, **kwargs )
        return ret
    return inner

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    user = request.form.get("user")
    pwd = request.form.get("passwd")
    if user == "admin" and pwd == "123":
        session["user1"] = user
        return redirect("/index")          
    return render_template('login.html', error="用户名或密码错误！")


@app.route("/index")
@auth
def index():
    return render_template("index.html", user_dic=USER_DICT )

@app.route("/delete/<int:nid>")
@auth
def delete(nid):
    # 对 nid 进行处理，并提供交互信息,此处暂且省去
    del USER_DICT[nid]
    return redirect( url_for("index") )

@app.route("/detail/<int:nid>")
@auth
def detail(nid):
    # 对 nid 进行处理，并提供交互信息,此处暂且省去
    info = USER_DICT[nid]
    return render_template("detail.html", info=info )

if __name__ == '__main__':
    app.run()
```



### 配置文件

```python
class Base( object ):
    XXX = 123				# f共同的配置
    SECRET_KEY = "asdfasdf"

class Pro( Base):			# 稳定版
    DEBUG = False

class Pro( Base):			# 开发版
    DEBUG = True
```



### 模版 templates

> login.html 同上

#### index.html

```html
<body>
    <h1 align="center">欢迎使用</h1>
    <table border="1" align="center">
        <thead>
        <th>ID</th>
        <th>姓名</th>
        <th>年龄</th>
        <th>性别</th>
        <th>默认值</th>
        <th>选项</th>
        </thead>
        <tbody align="center">
            {% for key,value in user_dic.items() %}
                <tr>
                    <td>{{ key }}</td>
                    <td>{{ value.get("name") }}</td>
                    <td>{{ value["age"]}}</td>
                    <td>{{ value.gender }}</td>
                    <td>{{ value.get("sadf","默认值") }}</td>
                    <td>
                        <a href="/detail/{{ key }}">查看详情</a>
                        |
                        <a href="/delete/{{ key }}">删除</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
```

#### detail.html

```html
<body>
    <h1 align="center">欢迎使用</h1>
    {% for item in info.values() %}
        <li>{{ item }}</li>
    {% endfor %}
    <hr />
    {% for item in info.keys() %}
        <li>{{ item }}</li>
    {% endfor %}
</body>
```



## 示例：用户登录补充

### 方式一：直接加（X）

```python
@app.route('/index')
def index():
    if not session.get('user'):
        return redirect( url_for('login') )
    return render_template('index.html',stu_dic=STUDENT_DICT )
```



### 方式二：装饰器

> **应用场景**：比较少的函数中需要额外添加功能。

```python
import functools
def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        
        if not session.get('user'):
            return redirect(url_for('login'))
        
        ret = func(*args,**kwargs)
        return ret
    return inner

@app.route('/index')
@auth
def index():
    return render_template('index.html',stu_dic=STUDENT_DICT)
```



### 方式三：before_request（&#10003;）

> 中间件，一切访问都要先经过这里

```python
@app.before_request
def xxxxxx():
    if request.path == '/login':
        return None				
    # 返回 None 表示可以通过执行，返回其他如字符串等说明不再往下执行了

    if session.get('user'):
        return None

    return redirect('/login')
```





## 6 templates 模版

> **模版本质上是字符串，并不是 html文件。**
> 因为应用会将其读到内存，变成字符串再返回给浏览器。只要你的字符串长得像 html格式，浏览器就能识别，所以不管后缀名是 .html，还是 .tpl（java）等其他文件后缀名都行



### 模板语法格式

> Flask使用的是 Jinja2 模板，所以其语法和 Django 无差别

#### 取值语法

```python
{{ var }}										# var 变量名

# 获取列表里的值：
{{ list.0 }}									# 获取列表第一个元素
{{ list[0] }}									# django 不能这样获取

# 获取字典里的值：
{{ dict.key }}									# 获取字典里key的值
{{ dict["key"] }}								# D not
{{ dict.get("key") }}							# D not
{{ dict.get("NoKey","默认值") }}				  # D not

# 关系表取值：
表1( id, name, sex )
表2( id, foreignkeyId )

{{ 表2.foreignkeyId.name }}
```



#### 条件判断语句

```python
{% if the_list %}	# 如果 the_list 列表存在，则执行以下内容

{% else %}			# 如果 the_list 列表不存在，则执行以下内容

{% endif %}			# 结束判断
```



#### 循环语句

```python
{% for question in the_list  %}		# 循环从 the_list 列表取值赋值给 question
	{{ forloop.counter }}			# 循环的次数，默认从1开始
	{{ forloop.last }}				# 循环的最后一次，boolean值
    {% cycle 'value' 'value1' 'value2'%}	
    # 每循环一次，随机抓取一个 value 出来，注意：即没有逗号，也不能换行
    
    # 嵌套循环
    {% for key,value in adict.items %}				# 字典的循环
    	{{ key, value }}
    {% endfor %}				
    	...
    {% empty %}										# 为空执行
    ...
{% endfor %}										# 结束循环
```

```python
# 只取字典的 key
{% for item in info.values() %}
	{{ item }}
{% endfor %}
```

```python
# 只取字典的 value
{% for item in info.values() %}
	{{ item }}
{% endfor %}
```



#### 页面渲染安全

##### 法一：前端管道符

```python
{{ txt|safe }}
```

##### 法二：后端 Makeup

```python
from flask import Makeuo
txt = Makeup("<h1>渲染安全<h1/>")		# 相当于 Django 中的 make_safe
```



#### 定制模版函数

##### 基础使用

**后端**

```python
def func(arg):
    return arg + 1

@app.route("/index")
def index(): 
    return render_template("index.html", func = func)
```

**前端**

```python
{{ func }}			# <function func at 0x00000261F8C62E18>
{{ func(6) }}		# 7
```



##### 全局定义函数

**后端**

> 两种调用方式不一样

```python
@app.template_global
def sb(a1, a2):
    return a1 + a2

@app.template_filter
def db(a1, a2, a3):
    return a1 + a2 + a3
```

**前端**

```python
{{ sb(1,9)}}			# 10
{{ 1|db(2,6) }}			# 9
# 可以用来做条件判断
# ｛% if 1|db(2,6) %｝
```



#### 模版继承导入

##### layout.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>index</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

##### index.html

```python
{% extends "layout.html" %}
{% block content %}
    {{ bdict[0] }}
	{% include "form.html" %}
{% endblock %}
```



#### 宏
> 当我们的代码块在页面的很多地方重复出现时，我们可以使用宏
> 减少代码量

##### 宏声明

```python
# 默认是不会显示的
{% macro input(name, type='text', value='') %}
	<input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}
```

##### 宏调用

```python
{{ input('n1') }}
{{ input('n2','passwd') }}
```





### static 静态文件

static_folder 静态文件存放文件夹名，默认为 static
static_url_path 静态文件路径（用户访问图片时的前缀）, 默认为 static

![1582604127790](assets/1582604127790.png)

![1582604164333](assets/1582604164333.png)

![1582604185254](assets/1582604185254.png)

![1582604410705](assets/1582604410705.png)







## 7 session 会话
> session 允许你在不同请求间存储特定用户的信息。
- **flask 的 session 默认存储在签名的 cookie 和加密的 cookie 里面的**

  > session 是在 Cookies 的基础上实现的，并且对 Cookies 进行密钥签名。
  > django 是存储在数据库中的 

- **要使用会话，你需要设置一个密钥。**

    ```python
    app.secret_key = "asdfasdf"             # 相当于 md5 加 salt
    # session 没有上面这句话会报错：
    #   The session is unavailable because no secret key was set.
    #   Set the secret_key on the application to something unique and secret.
    ```




### 基本使用

- **设置**：``session['username'] ＝ 'xxx'``

- **删除**：

    ```python
    del session['username'] 
    session.pop('username', None)
    ```

- **示例：**

    ```python
    from flask import Flask, session, redirect, url_for, escape, request
    app = Flask(__name__)
     
    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'
     
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''
     
    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))
     
    # set the secret key.  keep this really secret:
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    ```

    



### session 的本质

&emsp;&emsp;session 拿到的是一个 `SecureCookieSession`，该类又继承了 dict，所以**session 的本质是一个封装后的字典**

```mermaid
graph LR
A(sessions 模块) -->B(SecureCookieSession 类)
B --> C(CallbackDict类)
C --> D(dict)
```

```python
from flask import Flask, session

print( type(session) )      # <class 'werkzeug.local.LocalProxy'>
# werkzeug.local.LocalProxy 就相当于一个代理，会帮你找到那个字典

from flask.sessions import SecureCookieSession
```



### session 的原理

&emsp;&emsp;当请求刚到来：flask 读取 cookie 中 session 对应的值：`eyJrMiI6NDU2LCJ1c2VyIjoib2xkYm95`，再将该值解密并反序列化成字典，放入内存以便视图函数使用。

​	当请求结束时，flask会读取内存中字典的值，进行序列化+加密，写入到用户浏览器的 cookie 中。

```python
app.__call__
app.wsgi_app
app.request_class
app.session_interface
```

![1582953401917](assets/1582953401917.png)







### session相关的配置文件
```python
{
    # 声明
    'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
    ...
    'SESSION_COOKIE_NAME':                  'session',	# 写到cookie里的名称
    'SESSION_COOKIE_DOMAIN':                None,		# 域名
    'SESSION_COOKIE_PATH':                  None,		# 路径
    'SESSION_COOKIE_HTTPONLY':              True,		#是否只设置为http读取
    'SESSION_COOKIE_SECURE':                False,		# 是否
    'SESSION_REFRESH_EACH_REQUEST':         True,
    # 每次访问刷新 session
    ...
}
```

**修改配置文件**：

```python
import timedelta
class Config( object ):
    DEBUG = False
    TESTING = False
    
    SESSION_COOKIE_NAME = "session"
    SESSION_COOKIE_DOMAIN = None		# 域名
    SESSION_COOKIE_PATH = None			# 路径
    SESSION_COOKIE_HTTPONLY = True		#是否只设置为http读取
    SESSION_COOKIE_SECURE = False		# 是否安全
    SESSION_REFRESH_EACH_REQUEST = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)	# session 超时时间
```



### 第三方 session

```shell
pip3 install redis
pip3 install flask-session
```

```python
from flask import Flask, session, redirect
from flask.ext.session import Session
app = Flask(__name__)
app.debug = True
app.secret_key = 'asdfasdfasd'

app.config['SESSION_TYPE'] = 'redis'
from redis import Redis
app.config['SESSION_REDIS'] = Redis(host='192.168.0.94',port='6379')
Session(app)

@app.route('/login')
def login():
    session['username'] = 'alex'
    return redirect('/index')

@app.route('/index')
def index():
    name = session['username']
    return name

if __name__ == '__main__':
    app.run()
```



### 自定义 Session

```python
pip3 install Flask-Session
```

#### run.py

```python
from flask import Flask
from flask import session
from pro_flask.utils.session import MySessionInterface
app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.session_interface = MySessionInterface()

@app.route('/login.html', methods=['GET', "POST"])
def login():
    print(session)
    session['user1'] = 'alex'
    session['user2'] = 'alex'
    del session['user2']

    return "内容"

if __name__ == '__main__':
    app.run()
```

#### session.py

```python
import uuid
import json
from flask.sessions import SessionInterface
from flask.sessions import SessionMixin
from itsdangerous import Signer, BadSignature, want_bytes


class MySession(dict, SessionMixin):
    def __init__(self, initial=None, sid=None):
        self.sid = sid
        self.initial = initial
        super(MySession, self).__init__(initial or ())


        def __setitem__(self, key, value):
            super(MySession, self).__setitem__(key, value)

            def __getitem__(self, item):
                return super(MySession, self).__getitem__(item)

            def __delitem__(self, key):
                super(MySession, self).__delitem__(key)



                class MySessionInterface(SessionInterface):
                    session_class = MySession
                    container = {}

                    def __init__(self):
                        import redis
                        self.redis = redis.Redis()

                        def _generate_sid(self):
                            return str(uuid.uuid4())

                        def _get_signer(self, app):
                            if not app.secret_key:
                                return None
                            return Signer(app.secret_key, salt='flask-session',
                                          key_derivation='hmac')

                        def open_session(self, app, request):
                            """
                    程序刚启动时执行，需要返回一个session对象
                    """
                            sid = request.cookies.get(app.session_cookie_name)
                            if not sid:
                                sid = self._generate_sid()
                                return self.session_class(sid=sid)

                            signer = self._get_signer(app)
                            try:
                                sid_as_bytes = signer.unsign(sid)
                                sid = sid_as_bytes.decode()
                                except BadSignature:
                                    sid = self._generate_sid()
                                    return self.session_class(sid=sid)

                                # session保存在redis中
                                # val = self.redis.get(sid)
                                # session保存在内存中
                                val = self.container.get(sid)

                                if val is not None:
                                    try:
                                        data = json.loads(val)
                                        return self.session_class(data, sid=sid)
                                    except:
                                        return self.session_class(sid=sid)
                                    return self.session_class(sid=sid)

                                def save_session(self, app, session, response):
                                    """
                    程序结束前执行，可以保存session中所有的值
                    如：
                        保存到resit
                        写入到用户cookie
                    """
                                    domain = self.get_cookie_domain(app)
                                    path = self.get_cookie_path(app)
                                    httponly = self.get_cookie_httponly(app)
                                    secure = self.get_cookie_secure(app)
                                    expires = self.get_expiration_time(app, session)

                                    val = json.dumps(dict(session))

                                    # session保存在redis中
                                    # self.redis.setex(name=session.sid, value=val, time=app.permanent_session_lifetime)
                                    # session保存在内存中
                                    self.container.setdefault(session.sid, val)

                                    session_id = self._get_signer(app).sign(want_bytes(session.sid))

                                    response.set_cookie(app.session_cookie_name, session_id,
                                                        expires=expires, httponly=httponly,
                                                        domain=domain, path=path, secure=secure)
```







## 8 闪现（flash）
> 假设现在就两个页面，访问完page1 访问 page2 ，访问page2 自动将session删去
> 相当于生命周期只有一次，取一次就没有了

### flash 本质
```python
@app.route("/page1")
def page1():
    session["key1"] = 123
    return "hello world!"

@app.route("/page1")
def page2():
    session.pop('key1',None)
    return "hello world!"
```
> 闪现，在 session 中存储一个数据，读取时通过 pop 将数据移除。



### flash 的基本使用
```python
from flask import Flask,session,flash,get_flashed_messages
app = Flask(__name__)
app.config.from_object("settings.ProductionConfig")

@app.route("/page1")
def page1():
    flash("临时数据存储")					# 临时存一次
    return "hello world!"

@app.route("/page2")
def page2():
    print( get_flashed_messages() )		# 取一次就没了
    return "hello world!"
```

![1582711851741](assets/1582711851741.png)

### flash 的分类
```python
@app.route("/page1")
def page1():
    flash("error1","error")
    flash("error2", "error")
    flash("info1", "info")
    return "hello world!"

@app.route("/page2")
def page2():
    print( get_flashed_messages( category_filter=['error']) )
    return "hello world!"
```

![1582724004702](assets/1582724004702.png)





## 9 中间件
> 和 Django 的中间件不一样，django 的中间件能够 return 返回做一些操作
> flask 只能通过自己定制一些操作，通过它可以在请求进来之前或执行之后来做一些操作
>
> 继承`__call__()`实现的



### call方法什么时候执行？

> 用户发起请求时，才执行。

```mermaid
graph LR
    b2-->a1
    c2 --> b1
    
    subgraph Flask
    a1("__call__()")-->a2(" wsgi_app()")
    end
    
    subgraph serving.py
    b1(死循环)-->b2(等待客户端响应)
    b2 --> b1
    end
    
    subgraph app.py
    c1("app.run()")-->c2("run_simple()")
    end
```





### 任务：

> 在执行call方法之前，做一个操作，call方法执行之后做一个操作。

#### 第一种方式:

> 第一种方式修改 Flask 类中的 `__call__()` 函数实现

```python
# 源码
def __call__(self, environ, start_response):
    return self.wsgi_app(environ, start_response)

# 修改
def __call__(self, environ, start_response):
    print("前")
    # print(request)	# 这时候 request 为空，太靠前了
    # 但是我们还是能拿得到请求数据，在 environ 中
    #	environ 中的请求数据更加原始，需要我们自己去拆分
    ret = self.wsgi_app(environ, start_response)
    print("后")
    return ret
```

#### 第二种方式：

> 写个类继承 Flask的 `__call__()` 函数，这样就不用去 Flask 中修改源码了

```python
class Middleware(object):
    def __init__(self,old):
        self.old = old

    def __call__(self, *args, **kwargs):
        print("前")
        ret = self.old( *args, **kwargs )
        print("后")
        return ret

if __name__ == '__main__':
    # app.__call__ = Middlware(app.__call__)
    app.wsgi_app = Middleware(app.wsgi_app )        # 和上面是一样的
    app.run()
```





## 10 特殊装饰器

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, Request, render_template

app = Flask(__name__, template_folder='templates')
app.debug = True


@app.before_first_request
def before_first_request1():
    print('before_first_request1')


@app.before_first_request
def before_first_request2():
    print('before_first_request2')

# 谁先定义谁先执行
@app.before_request						# 全局请求前都会执行
def before_request1():
    Request.nnn = 123
    print('before_request1')


@app.before_request
def before_request2():
    print('before_request2')

# 谁后定义谁先执行
@app.after_request						# 全局请求后都会执行
def after_request1(response):			# 没有参数会报错
    print('before_request1', response)
    return response						# 没有返回会报错


@app.after_request
def after_request2(response):
    print('before_request2', response)
    return response


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

# 设为全局，在模版里面也能调用
@app.template_global()
def sb(a1, a2):
    return a1 + a2

# 设为全局，在模版里面也能调用(调用方式不一样)
# {{ 1|db(2,3) }}
@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3


@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
```



### @app.before_request

> 在请求执行前进行操作，**先定义的先执行**

```python
@app.before_request                  # 全局所有请求前都会执行，并不只有 index
def before_request1():
    print('before_request1')

@app.before_request
def before_request2():              # 全局所有请求前都会执行，并不只有 index
    print('before_request2')

@app.route("/index")
def index():
    print("index")
    return "index"
```

![1582771916310](assets/1582771916310.png)

```mermaid
graph LR
A(定义before_request1) -->B(before_request2)
B --> C((index))
C --> D(执行before_request1)
D --> E(执行before_request2)
```



#### return

```python
@app.before_request                     # 全局请求前都会执行
def before_request1():
    print('before_request1')
    return "before_request1__return"	# 请求后直接返回

@app.before_request                     # 不会被执行
def before_request2():
    print('before_request2')
    return "before_request2__return"

@app.after_request						# 再执行
def after_request1(response):
    print('after_request1', response)
    return response	

@app.after_request  					# 先执行
def after_request2(response):
    print('after_request2', response)
    return response	

@app.route("/index")
def index():
    print("index")
    return "index"
```

![1582773868225](assets/1582773868225.png)





### @app.after_request

> 在请求执行前进行操作，**先定义的后执行**

```python
@app.after_request                      # 全局请求后都会执行,，并不只有 index
def after_request1(response):			
# 没有参数会报错:
# TypeError: after_request1() takes 0 positional arguments but 1 was given
    print('after_request1', response)
    return response						
	# 没有返回会报错 TypeError: 'NoneType' object is not callable

@app.after_request                     
def after_request2(response):			
    print('after_request2', response)
    return response						

@app.route("/index")
def index():
    print("index")
    return "index"
```

![1582772020149](assets/1582772020149.png)

```mermaid
graph LR
A(定义after_request1) -->B(after_request2)
B --> C((index))
C --> D(执行after_request2)
D --> E(执行after_request1)
```

#### before/after_request 执行流程

![1582773431922](assets/1582773431922.png)



### @app.before_first_request

> 只有第一次请求会被执行，也只执行一次

```python
@app.before_first_request
def before_request1():
    print('before_first_request1')

@app.route("/index")
def index():
    print("index")
    return "index"

@app.route("/order")
def order():
    print("order")
    return "order"
```

![1582775695208](assets/1582775695208.png)



### @app.template_global()

> 给模版定义全局函数

#### 后端

```python
@app.template_global()
def sb(a1, a2):
    return a1 + a2
```

#### 前端

```python
{{ sb(1,9)}}			# 10
```



### @app.template_filter()

> 给给模版定义全局函数

```python
@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3
```

**前端**

```python
{{ 1|db(2,6) }}			# 9
# 可以用来做条件判断
# ｛% if 1|db(2,6) %｝
```



### @app.errorhandler(404)

> 可以用来处理错误页面 404、500、403...

```python
@app.errorhandler(404)
def page_not_found(error):
    print( error )
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.run()
```

![1582776569033](assets/1582776569033.png)





## 11 blueprint
> 目标：给开发者提供目录结构

### 基本使用
> 注意，蓝图名不能跟函数名冲突

#### 目录结构

```shell
|project
|---|pro_flask
|-------|__init__.py
|-------|views
|-----------|account.py
|-----------|blog.py
|---|run.py
```

#### run.py

```python
from pro_flask import create_app
app = create_app()

if __name__ == '__main__':
    app.run()
```

#### `__init__.py`

```python
from flask import Flask
from .views.account import ac
from .views.blog import blog

def create_app():
    app = Flask(__name__)
    app.register_blueprint(ac)
    app.register_blueprint(blog)
    return app
```

#### account.py

```python
from flask import Blueprint
from flask import render_template, request

ac = Blueprint("ac",__name__)
@ac.route("/login.html", methods=["GET","POST"] )
def login():
    return "login.html"

@ac.route("/logout.html", methods=["GET","POST"] )
def logout():
    return "logout.html"
```

#### blog.py

```python
from flask import Blueprint

blog = Blueprint("index", __name__ )

@blog.route("/index")
def index():
    return "index"

@blog.route("/detail")
def detail():
    return "detail"
```



### 自定义模板、静态文件

#### 基本使用

```python
|project
|---|templates
|---|pro_flask
|-------|__init__.py
|-------|templates
-----------|login.html
|-------|static
|-------|views
|-----------|account.py
|---|run.py
```

> 默认会先去 `pro_flask` 目录下的 `templates` 目录下找，再去  `template_folder` 下找

```python
ac = Blueprint("ac",__name__,  template_folder='../../templates')
```



### 全局 or 单个

#### 某一类url前缀

> url_prefix

```python
def create_app():
    app = Flask(__name__)
    app.register_blueprint(ac)		# 依旧是 /login.html 和 /logout.html
    app.register_blueprint(blog, url_prefix="/api") 
    # 访问时就需要用 /api/index 和 /api/detail
    return app
```



#### templates and static

**目录结构**

```python
|project
|---|templates
|---|pro_flask
|-------|__init__.py
|-------|templates
-----------|login.html
|-------|static
|-------|views
|-----------|account.py
|-----------|blog.py
|---|run.py
```

##### 某一类改变

```python
# account.py
ac = Blueprint("ac",__name__,  template_folder='../../templates')
# blog.py 不变即可
```

##### 全局改变

```python
# __init__.py
app = Flask(__name__,template_folder='../templates')
```



#### before_request

##### 某一类要改

```python
# account.py
@ac.before_request
def x1():
    print("befor_request")
```

##### 全局改
```python
# __init__.py
@app.before_request
def x1():
    print("befor_request")
```





## 12 上下文管理

> Django 的请求和 session 都是通过参数进行传递，没有放在一个公共的地方

### threading.local

> 和 flask 无任何关系
> 作用：为每个线程创建一个独立的空间，使得线程对自己的空间中的数据进行操作（数据隔离）。

#### 例子

> 没有加锁的情况下，得到的值并不是我们期待的

```python
import threading,time
value = 0

def task(var_int):
    global value
    value = var_int
    time.sleep(1)
    print(value)

for var in range(10):
    t = threading.Thread(target=task, args=(var,) )
    t.start()
```

使用 threading.local 的情况下：

```python
import threading,time
from threading import local

obj = local()

def task(var_int):
    obj.var = var_int           # 为每一个线程都创建一个独立的空间 var
    time.sleep(1)
    print( obj.var )            # 每个线程的 obj.var 都是不一样的

for var in range(10):
    t = threading.Thread(target=task, args=(var,) )
    t.start()
```



#### 自己实现 threading.local

```python
import threading,time
DICT = {}

def task(var_int):
    ident = threading.get_ident()		# 获取一个线程的唯一标记
    if ident in DICT:
        DICT[ident]["var_int"] = var_int
    else:
        DICT[ident] = {"var_int" : var_int}
    time.sleep(2)
    print(DICT[ident]["var_int"], var_int)

for var in range(10):
    t = threading.Thread(target=task, args=(var,) )
    t.start()
```

自定义一个为每个协程开辟空间进行存取数据。

```python
import threading,time
import greenlet
DICT = {}

def task(var_int):
    ident = greenlet.getcurrent()		# 获取一个协程的唯一标记
    if ident in DICT:
        DICT[ident]["var_int"] = var_int
    else:
        DICT[ident] = {"var_int" : var_int}
    time.sleep(2)
    print(DICT[ident]["var_int"], var_int)

for var in range(10):
    t = threading.Thread(target=task, args=(var,) )
    t.start()
```



#### threading.local的加强版（协程）

```python
import time
import threading
try:
    import greenlet
    get_ident =  greenlet.getcurrent
except Exception as e:
    get_ident = threading.get_ident

class Local(object):
    DIC = {}

    def __getattr__(self, item):
        ident = get_ident()
        if ident in self.DIC:
            return self.DIC[ident].get(item)
        return None

    def __setattr__(self, key, value):
        ident = get_ident()
        if ident in self.DIC:
            self.DIC[ident][key] = value
        else:
            self.DIC[ident] = {key:value}


obj = Local()

def task(i):
    obj.xxxxx = i
    time.sleep(2)
    print(obj.xxxxx,i)

for i in range(10):
    t = threading.Thread(target=task,args=(i,))
    t.start()

```





### 请求上下文管理 ctx：

>  request，session 

```python
- 请求到来之后wsgi会触发__call__方法，由__call__方法再次调用wsgi_app方法
- 在wsgi_app方法中：
- 首先将 请求相关+空session 封装到一个RequestContext对象中，即：ctx。
- 将ctx交给LocalStack对象，再由LocalStack将ctx添加到Local中，Local结构：
__storage__ = {
    1231:{stack:[ctx,] }
}
- 根据请求中的cookie中提取名称为sessionid对应的值，对cookie进行加密+反序列化，再次赋值给ctx中的session


-> 视图函数
    - 把session中的数据再次写入到cookie中。
    - 将ctx删除
    - 结果返回给用户浏览器
    - 断开socket连接
```














# flask 进阶

## flask-sqlalchemy

### 下载安装

```python
pip3 install flask-sqlalchemy
```

### 使用

#### 第一步：导入并实例化 SQLAlchemy

> 必须在导入蓝图之前
> 必须导入 `models.py`

```python
# app.__init__.py 
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

#### 第二步：初始化

```python
# app.__init__.py 
from .model import *
db.init_app(app)
```

#### 第三步：在配置文件中写入配置

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/s9day122?charset=utf8"
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 5
```

#### 第四步：创建 models.py 中的类

```python
# test/models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,String,Text,Date,DateTime
from sqlalchemy import create_engine
from app import db

class Users(db.Model):					# 继承它
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    depart_id = Column(Integer)
```

#### 第五步：生成表

> 使用 app 上下文，否则会报错

```python
# 一般放在 project.create_table.py 中
from app import db,create_app
app = create_app()
app_ctx = app.app_context() 	# app_ctx = app/g
with app_ctx: 					# __enter__,通过LocalStack放入Local中
    db.create_all() 	# 调用LocalStack放入Local中获取app，再去app中获取配置
    # __exit__
```

#### 第六步：基于ORM对数据库进行操作。


```python
from flask import Blueprint
from chun import db
from chun import models
us = Blueprint('us',__name__)

@us.route('/index')
def index():
    # 使用SQLAlchemy在数据库中插入一条数据
    # db.session.add(models.Users(name='高件套',depart_id=1))
    # db.session.commit()
    # db.session.remove()
    result = db.session.query(models.Users).all()
    # 内部也是调用的scoped_session
    print(result)
    db.session.remove()

    return 'Index'
```




## flask-script

### 安装

```python
pip3 install flask-script 
```



### 功能

#### 增加 runserver

```python
from chun import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    # app.run()
    manager.run()

# python manage.py runserver -h 127.0.0.1 -p 8000
```

#### 位置传参

```python
from chun import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)

@manager.command
def custom(arg):
    """
    自定义命令
    python manage.py custom 123
    :param arg:
    :return:
    """
    print(arg)

    if __name__ == '__main__':
        # app.run()
        manager.run()
```

#### 关键字传参

```python
from chun import create_app
from flask_script import Manager


app = create_app()
manager = Manager(app)

@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def cmd(name, url):
    """
    自定义命令
    执行： python manage.py  cmd -n wupeiqi -u http://www.oldboyedu.com
    :param name:
    :param url:
    :return:
    """
    print(name, url)


    if __name__ == '__main__':
        # app.run()
        manager.run()
```



## flask-migrate 

### 安装

```python
#依赖：flask-script 
pip3 install flask-migrate
```

### 使用

```python
from sansa import create_app
from sansa import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
Migrate(app, db)

"""
# 数据库迁移命名
    python manage.py db init			# migrate 初始化，只需要第一次就行
    python manage.py db migrate			# 生成更改记录
    python manage.py db upgrade			# 更新到数据库
"""
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    # app.run()
```





## pipreqs

### 安装

```python
pip install pipreqs
```

### 使用

```python
pipreqs ./ --encoding=utf-8 
```







# flask 规范

- endpoint 一定要写！







# flask 源码阅读

## Flask 类

### 阅读源码入口

#### 第一个 werkzeug 应用

```python
from werkzeug.wrappers import Response		# 导入模块
from werkzeug.serving import run_simple

def hello(environ, start_response):
    response = Response('Hello World!')
    return response(environ, start_response)	# 返回 Response 对象

if __name__ == '__main__':
    run_simple('localhost', 4000, hello)
```

#### FBV --> CBV

```python
from werkzeug.wrappers import Response		# 导入模块
from werkzeug.serving import run_simple

class Foo(object):
    def __call__(environ, start_response):	# 要一进来就运行，所以为call方法
        response = Response('Hello World!')
        return response(environ, start_response)	# 返回 Response 对象

obj = Foo()
if __name__ == '__main__':
    run_simple( 'localhost', 4000, obj )
```

#### 源码入口

```python
from werkzeug.wrappers import Response		# 导入模块
from werkzeug.serving import run_simple

class Flask(object):
    def __call__(environ, start_response):	# 要一进来就运行，所以为call方法
        response = Response('Hello World!')
        return response(environ, start_response)	# 返回 Response 对象

    def run(self):
        run_simple( 'localhost', 4000, self )		# self 就是 obj 

app = Flask()
if __name__ == '__main__':
    app.run()
```



### 阅读顺序

#### app.py

```python
from flask import Flask				
# 1、实例化 Flask 对象，所有的功能都是从 Falsk 对象出发的的
app = Flask(__name__)

# 2、设置路由
@app.route('/index')		# 使用 route() 装饰器来告诉 Flask 触发函数的 URL 
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # 3、启动 socket 服务端 run_simple(host, port, self, **options)
    # 	Falsk.__call__( environ, start_response )
    # 		Falsk.wsgi_app( environ, start_response )
    app.run()
    
```



#### wsgi_app()

```python
def wsgi_app(self, environ, start_response):
    # Flask 所有的源码都是在这里面触发的
    ctx = self.request_context(environ)		
    # 1、对 environ请求数据再进行一次封装	(就是我们用的 request )
    # 2、从 environ 中获取名称为 session 的 cookie， 解密，反序列化
    # 3、把以上两个东西放到 "某个神奇的地方"
    error = None
    try:
        try:
            ctx.push()
            # 4、执行视图函数，返回响应数据
            response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:  # noqa: B001
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            # 5、去"某个神奇的地方" 获取 session ，加密，序列化 =》 写 cookie
            # 6、清空 "某个神奇的地方"
            ctx.auto_pop(error)
```





### `__init__()`

```python
def __init__(
    self,
    import_name,							# 对象名，一般为 __name__
    static_url_path=None,					# 默认静态文件存放路径
    static_folder="static",					# 默认静态文件存放文件夹
    static_host=None,
    host_matching=False,
    subdomain_matching=False,
    template_folder="templates",			# 默认模版路径
    instance_path=None,
    instance_relative_config=False,
    root_path=None,
):
	_PackageBoundObject.__init__(
        self, import_name, 
        template_folder=template_folder, 
        root_path=root_path
	)

	self.static_url_path = static_url_path
	self.static_folder = static_folder

	if instance_path is None:
        instance_path = self.auto_find_instance_path()
    elif not os.path.isabs(instance_path):
        raise ValueError(
        	"If an instance path is provided it must be absolute."
        	" A relative path was given instead."
        )

    #: Holds the path to the instance folder.
    #:
    #: .. versionadded:: 0.8
    self.instance_path = instance_path

    #: The configuration dictionary as :class:`Config`.  This behaves
    #: exactly like a regular dictionary but supports additional methods
    #: to load a config from files.
    self.config = self.make_config(instance_relative_config)

    #: A dictionary of all view functions registered.  The keys will
    #: be function names which are also used to generate URLs and
    #: the values are the function objects themselves.
    #: To register a view function, use the :meth:`route` decorator.
    self.view_functions = {}

    #: A dictionary of all registered error handlers.  The key is ``None``
    #: for error handlers active on the application, otherwise the key is
    #: the name of the blueprint.  Each key points to another dictionary
    #: where the key is the status code of the http exception.  The
    #: special key ``None`` points to a list of tuples where the first item
    #: is the class for the instance check and the second the error handler
    #: function.
    #:
    #: To register an error handler, use the :meth:`errorhandler`
    #: decorator.
    self.error_handler_spec = {}

    #: A list of functions that are called when :meth:`url_for` raises a
    #: :exc:`~werkzeug.routing.BuildError`.  Each function registered here
    #: is called with `error`, `endpoint` and `values`.  If a function
    #: returns ``None`` or raises a :exc:`BuildError` the next function is
    #: tried.
    #:
    #: .. versionadded:: 0.9
    self.url_build_error_handlers = []

    #: A dictionary with lists of functions that will be called at the
    #: beginning of each request. The key of the dictionary is the name of
    #: the blueprint this function is active for, or ``None`` for all
    #: requests. To register a function, use the :meth:`before_request`
    #: decorator.
    self.before_request_funcs = {}

    #: A list of functions that will be called at the beginning of the
    #: first request to this instance. To register a function, use the
    #: :meth:`before_first_request` decorator.
    #:
    #: .. versionadded:: 0.8
    self.before_first_request_funcs = []

    #: A dictionary with lists of functions that should be called after
    #: each request.  The key of the dictionary is the name of the blueprint
    #: this function is active for, ``None`` for all requests.  This can for
    #: example be used to close database connections. To register a function
    #: here, use the :meth:`after_request` decorator.
    self.after_request_funcs = {}

    #: A dictionary with lists of functions that are called after
    #: each request, even if an exception has occurred. The key of the
    #: dictionary is the name of the blueprint this function is active for,
    #: ``None`` for all requests. These functions are not allowed to modify
    #: the request, and their return values are ignored. If an exception
    #: occurred while processing the request, it gets passed to each
    #: teardown_request function. To register a function here, use the
    #: :meth:`teardown_request` decorator.
    #:
    #: .. versionadded:: 0.7
    self.teardown_request_funcs = {}

    #: A list of functions that are called when the application context
    #: is destroyed.  Since the application context is also torn down
    #: if the request ends this is the place to store code that disconnects
    #: from databases.
    #:
    #: .. versionadded:: 0.9
    self.teardown_appcontext_funcs = []

    #: A dictionary with lists of functions that are called before the
    #: :attr:`before_request_funcs` functions. The key of the dictionary is
    #: the name of the blueprint this function is active for, or ``None``
    #: for all requests. To register a function, use
    #: :meth:`url_value_preprocessor`.
    #:
    #: .. versionadded:: 0.7
    self.url_value_preprocessors = {}

    #: A dictionary with lists of functions that can be used as URL value
    #: preprocessors.  The key ``None`` here is used for application wide
    #: callbacks, otherwise the key is the name of the blueprint.
    #: Each of these functions has the chance to modify the dictionary
    #: of URL values before they are used as the keyword arguments of the
    #: view function.  For each function registered this one should also
    #: provide a :meth:`url_defaults` function that adds the parameters
    #: automatically again that were removed that way.
    #:
    #: .. versionadded:: 0.7
    self.url_default_functions = {}

    #: A dictionary with list of functions that are called without argument
    #: to populate the template context.  The key of the dictionary is the
    #: name of the blueprint this function is active for, ``None`` for all
    #: requests.  Each returns a dictionary that the template context is
    #: updated with.  To register a function here, use the
    #: :meth:`context_processor` decorator.
    self.template_context_processors = {None: [_default_template_ctx_processor]}

    #: A list of shell context processor functions that should be run
    #: when a shell context is created.
    #:
    #: .. versionadded:: 0.11
    self.shell_context_processors = []

    #: all the attached blueprints in a dictionary by name.  Blueprints
    #: can be attached multiple times so this dictionary does not tell
    #: you how often they got attached.
    #:
    #: .. versionadded:: 0.7
    self.blueprints = {}
    self._blueprint_order = []

    #: a place where extensions can store application specific state.  For
    #: example this is where an extension could store database engines and
    #: similar things.  For backwards compatibility extensions should register
    #: themselves like this::
    #:
    #:      if not hasattr(app, 'extensions'):
    #:          app.extensions = {}
    #:      app.extensions['extensionname'] = SomeObject()
    #:
    #: The key must match the name of the extension module. For example in
    #: case of a "Flask-Foo" extension in `flask_foo`, the key would be
    #: ``'foo'``.
    #:
    #: .. versionadded:: 0.7
    self.extensions = {}

    #: The :class:`~werkzeug.routing.Map` for this instance.  You can use
    #: this to change the routing converters after the class was created
    #: but before any routes are connected.  Example::
    #:
    #:    from werkzeug.routing import BaseConverter
    #:
    #:    class ListConverter(BaseConverter):
    #:        def to_python(self, value):
    #:            return value.split(',')
    #:        def to_url(self, values):
    #:            return ','.join(super(ListConverter, self).to_url(value)
    #:                            for value in values)
    #:
    #:    app = Flask(__name__)
    #:    app.url_map.converters['list'] = ListConverter
    self.url_map = self.url_map_class()

    self.url_map.host_matching = host_matching
    self.subdomain_matching = subdomain_matching

    # tracks internally if the application already handled at least one
    # request.
    self._got_first_request = False
    self._before_request_lock = Lock()

    # Add a static route using the provided static_url_path, static_host,
    # and static_folder if there is a configured static_folder.
    # Note we do this without checking if static_folder exists.
    # For one, it might be created while the server is running (e.g. during
    # development). Also, Google App Engine stores static files somewhere

    if self.has_static_folder:
        assert (
        	bool(static_host) == host_matching
        ), "Invalid static_host/host_matching combination"
        self.add_url_rule(
        	self.static_url_path + "/<path:filename>",
        	endpoint="static",
        	host=static_host,
        	view_func=self.send_static_file,
        )

    # Set the name of the Click group in case someone wants to add
    # the app's commands to another CLI tool.
    self.cli.name = self.name
```



#### self.config

```python
self.config = self.make_config(instance_relative_config)
```





### make_config()

```mermaid
graph LR
A((Flask)) -->B(__init__)
B --> C(self.config)
C --> D("make_config()")
```

```python
def make_config(self, instance_relative=False):
    """Used to create the config attribute by the Flask constructor.
        The `instance_relative` parameter is passed in from the constructor
        of Flask (there named `instance_relative_config`) and indicates if
        the config should be relative to the instance path or the root path
        of the application.

        .. versionadded:: 0.8
        """
    root_path = self.root_path
    if instance_relative:
        root_path = self.instance_path
        defaults = dict(self.default_config)
        defaults["ENV"] = get_env()
        defaults["DEBUG"] = get_debug_flag()
        return self.config_class(root_path, defaults)
```



add_url_rule()

```python
    @setupmethod
    def add_url_rule(
        self,
        rule,
        endpoint=None,
        view_func=None,
        provide_automatic_options=None,
        **options
    ):
        """Connects a URL rule.  Works exactly like the :meth:`route`
        decorator.  If a view_func is provided it will be registered with the
        endpoint.

        Basically this example::

            @app.route('/')
            def index():
                pass

        Is equivalent to the following::

            def index():
                pass
            app.add_url_rule('/', 'index', index)

        If the view_func is not provided you will need to connect the endpoint
        to a view function like so::

            app.view_functions['index'] = index

        Internally :meth:`route` invokes :meth:`add_url_rule` so if you want
        to customize the behavior via subclassing you only need to change
        this method.

        For more information refer to :ref:`url-route-registrations`.

        .. versionchanged:: 0.2
           `view_func` parameter added.

        .. versionchanged:: 0.6
           ``OPTIONS`` is added automatically as method.

        :param rule: the URL rule as string
        :param endpoint: the endpoint for the registered URL rule.  Flask
                         itself assumes the name of the view function as
                         endpoint
        :param view_func: the function to call when serving a request to the
                          provided endpoint
        :param provide_automatic_options: controls whether the ``OPTIONS``
            method should be added automatically. This can also be controlled
            by setting the ``view_func.provide_automatic_options = False``
            before adding the rule.
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods
                        is a list of methods this rule should be limited
                        to (``GET``, ``POST`` etc.).  By default a rule
                        just listens for ``GET`` (and implicitly ``HEAD``).
                        Starting with Flask 0.6, ``OPTIONS`` is implicitly
                        added and handled by the standard request handling.
        """
        if endpoint is None:
            endpoint = _endpoint_from_view_func(view_func)
        options["endpoint"] = endpoint
        methods = options.pop("methods", None)

        # if the methods are not given and the view_func object knows its
        # methods we can use that instead.  If neither exists, we go with
        # a tuple of only ``GET`` as default.
        if methods is None:
            methods = getattr(view_func, "methods", None) or ("GET",)
        if isinstance(methods, string_types):
            raise TypeError(
                "Allowed methods have to be iterables of strings, "
                'for example: @app.route(..., methods=["POST"])'
            )
        methods = set(item.upper() for item in methods)

        # Methods that should always be added
        required_methods = set(getattr(view_func, "required_methods", ()))

        # starting with Flask 0.8 the view_func object can disable and
        # force-enable the automatic options handling.
        if provide_automatic_options is None:
            provide_automatic_options = getattr(
                view_func, "provide_automatic_options", None
            )

        if provide_automatic_options is None:
            if "OPTIONS" not in methods:
                provide_automatic_options = True
                required_methods.add("OPTIONS")
            else:
                provide_automatic_options = False

        # 立即添加所需的方法。
        methods |= required_methods

        rule = self.url_rule_class(rule, methods=methods, **options)
        rule.provide_automatic_options = provide_automatic_options

        # view_func = 视图函数
        # self.view_functions = {
        #     endpoint : 视图函数
        # } 
        self.url_map.add(rule)
        if view_func is not None:
            old_func = self.view_functions.get(endpoint)
            if old_func is not None and old_func != view_func:
                raise AssertionError(
                    "View function mapping is overwriting an "
                    "existing endpoint function: %s" % endpoint
                )
            self.view_functions[endpoint] = view_func
```



### run( )

```python
def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    """在本地开发服务器上运行该应用程序。
		不要在生产设置中使用``run（）``。它不旨在=满足生产服务器的安全性和性能要求。
        相反，请参阅：deployment`以获取WSGI服务器建议。

 		如果设置了：attr：`debug`标志，则服务器将自动重新加载进行代码更改，并在发生异常的情况下显示调试器。
       如果要在调试模式下运行应用程序，请禁用在交互式调试器上执行代码，可以通过``use_evalex = False''作为参数。这将保留调试器的追溯屏幕处于活动状态，但禁用代码执行
 
        不建议使用此功能进行开发，因为自动重新加载功能受到严重支持。相反，你应该使用Flask命令行脚本的run支持。

		..告诫：：谨记
        .. admonition:: Keep in Mind
        
        	 Flask将使用通用错误页面抑制任何服务器错误，除非它处于调试模式。
        	 因此，仅启用无需重新加载代码的交互式调试器，您必须用``debug = True''和``use_reloader = False''来调用：meth：``run``。
        	 
        	 在不处于调试模式的情况下将 use_debugger 设置为 True不会捕获任何异常，因为不会有任何异常抓住。


        :param host: 要监听的主机名。将此设置为``0.0.0.0``。也可以从外部使用服务器。默认为``127.0.0.1''或 SERVER_NAME 配置变量中的主机，如果存在。
        :param port: Web服务器的端口。默认为``5000''或如果存在，则使用“ SERVER_NAME”配置变量中定义的端口。
        :param debug: 如果给定，启用或禁用调试模式。看到
            :attr:`debug`.
        :param load_dotenv: 加载最近的`.env` and `.flaskenv` 文件来设置环境变量。也会改变工作目录到包含找到的第一个文件的目录。
        :param options: 将被转发到基础 Werkzeug 的选项
            server. See :func:`werkzeug.serving.run_simple` for more
            information.

        .. versionchanged:: 1.0
            If installed, python-dotenv will be used to load environment
            variables from :file:`.env` and :file:`.flaskenv` files.

            If set, the :envvar:`FLASK_ENV` and :envvar:`FLASK_DEBUG`
            environment variables will override :attr:`env` and
            :attr:`debug`.
             默认情况下启用线程模式。

        .. versionchanged:: 0.10
            The default port is now picked from the ``SERVER_NAME``
            variable.
        """
    # 如果从服务器中调用服务器，则将其更改为无操作
    #  命令行。 请查看cli.py以获取更多信息
    if os.environ.get("FLASK_RUN_FROM_CLI") == "true":
        from .debughelpers import explain_ignored_app_run

        explain_ignored_app_run()
        return

    if get_load_dotenv(load_dotenv):
        cli.load_dotenv()

        # 如果设置，让env vars覆盖以前的值
        if "FLASK_ENV" in os.environ:
            self.env = get_env()
            self.debug = get_debug_flag()
            elif "FLASK_DEBUG" in os.environ:
                self.debug = get_debug_flag()

                # 传递给方法的调试将覆盖所有其他源
                if debug is not None:
                    self.debug = bool(debug)

                    _host = "127.0.0.1"
                    _port = 5000
                    server_name = self.config.get("SERVER_NAME")
                    sn_host, sn_port = None, None

                    if server_name:
                        sn_host, _, sn_port = server_name.partition(":")

                        host = host or sn_host or _host
                        # 选择第一个不为None的值（允许为0）
                        port = int(next((p for p in (port, sn_port) if p is not None), _port))

                        options.setdefault("use_reloader", self.debug)
                        options.setdefault("use_debugger", self.debug)
                        options.setdefault("threaded", True)

                        cli.show_server_banner(self.env, self.debug, self.name, False)

                        from werkzeug.serving import run_simple

                        try:
                            run_simple(host, port, self, **options)
                            # self 是我们创建的 app = Flask(..) 对象
                            finally:
                                # 如果是开发服务器，则重置第一个请求信息
                                # 正常重置。 这样可以重新启动服务器
                                # 无需重新加载程序，从交互式外壳中获取这些东西。
                                self._got_first_request = False
```



### add_url_rule(rule,endpoint,func,…)

```python
@setupmethod
def add_url_rule(
    self,
    rule,
    endpoint=None,
    view_func=None,
    provide_automatic_options=None,
    **options
):
    """连接URL规则。的工作原理与：meth：`route`装饰器完全一样.  如果提供了view_func，它将在端点注册。
        基础例子::
            @app.route('/')
            def index():
                pass
		等效于以下内容：::
            def index():
                pass
            app.add_url_rule('/', 'index', index)

        如果未提供view_func，则需要连接端点
        像这样的视图函数：
            app.view_functions['index'] = index
        内部 :meth:`route` 会调用 :meth:`add_url_rule` 所以如果您愿意
        通过子类来自定义行为，您只需要更改这种方法。

        有关更多信息，请参考 :ref:`url-route-registrations`.
        .. versionchanged:: 0.2
           `view_func` parameter added.
        .. versionchanged:: 0.6
           ``OPTIONS`` is added automatically as method.

        :param rule: URL规则为字符串
        :param endpoint: 注册URL规则的端点。Flask本身假定视图函数的名称赋给 endpoint
        :param view_func: 服务到请求时调用的函数
        :param provide_automatic_options:控制是否使用 OPTIONS 
        	方法应自动添加。这也可以  在添加规则之前通过设置控制
        :param options: 要转发到底层的选项
                        :class:`~werkzeug.routing.Rule` object. 改变
                        到Werkzeug处理方法选项 
        	methods
            	是此规则应限制的方法列表到（``GET``，``POST``等）。默认情况下只是监听``GET``（和隐式的``HEAD``）。
                        从Flask 0.6开始，``OPTIONS''是隐式的,由标准请求处理添加和处理。``HEAD``)
        """
    if endpoint is None:
        endpoint = _endpoint_from_view_func(view_func) # 返回视图函数的函数名
    options["endpoint"] = endpoint
    methods = options.pop("methods", None)

    # 如果未提供方法，并且view_func对象知道其方法，则可以使用该方法。
    # 如果两者都不存在，默认情况下，我们只使用元组“ GET”。
    if methods is None:
        methods = getattr(view_func, "methods", None) or ("GET",)
    if isinstance(methods, string_types):
        raise TypeError(
            "Allowed methods have to be iterables of strings, "
            'for example: @app.route(..., methods=["POST"])'
        )
    methods = set(item.upper() for item in methods)

    # 应始终添加的方法
    required_methods = set(getattr(view_func, "required_methods", ()))

    # 从Flask 0.8开始，view_func对象可以禁用并强制启用自动选项处理。
    if provide_automatic_options is None:
        provide_automatic_options = getattr(
            view_func, "provide_automatic_options", None
        )

    if provide_automatic_options is None:
        if "OPTIONS" not in methods:
            provide_automatic_options = True
            required_methods.add("OPTIONS")
        else:
            provide_automatic_options = False

    # 立即添加所需的方法。
    methods |= required_methods

    # 封装 rule = Rule( /xxx, get/post.., endpoint ... )
    rule = self.url_rule_class(rule, methods=methods, **options)
    rule.provide_automatic_options = provide_automatic_options
	
    # 将路由关系添加到所有的路由映射表中
    self.url_map.add(rule)
    if view_func is not None:
        # view_functions = {}
        old_func = self.view_functions.get(endpoint)
        if old_func is not None and old_func != view_func:
            # endpoint 相同，但是视图函数不同抛出错误
            raise AssertionError(
                "View function mapping is overwriting an "
                "existing endpoint function: %s" % endpoint
            )
            self.view_functions[endpoint] = view_func
```



#### _endpoint_from_view_func(view_func)

```mermaid
graph LR
A1>helper.py] --> B1("_endpoint_from_view_func(view_func)")
B1 -->|return __name__| C1((endpoint))

```





### route()

```python
def route(self, rule, **options):
    """个装饰器，用于注册一个视图功能给定的URL规则。这和add_url_rule的作用相同。但仅供装饰器使用：
        @app.route('/')
        def index():
            return 'Hello World'

        有关更多信息，请参考：url-route-registrations。

        :param rule: URL 规则为字符串
        :param endpoint: 注册URL规则的端点。 Flask 本身假定视图函数的名称为 endpoint

        :param options: 要转发到底层的选项
                        :class:`~werkzeug.routing.Rule` object. 改变
                        到Werkzeug处理方法选项 
                        methods 是此规则应限制的方法列表到（``GET``，``POST``等）。 默认情况下只是监听``GET''（和隐式的``HEAD``）。
                        从Flask 0.6开始，``OPTIONS''是隐式的,由标准请求处理添加和处理。handling.
        """

    def decorator(f):					# f 为 index 视图函数
        endpoint = options.pop("endpoint", None)
        # 在 option 中找endpoint ，找不到默认值就为 None
        
        # 本质上生成对应关系的就是以下该函数
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator			# 返回 decorator 函数
```



### endpoint()

```python
@setupmethod
def endpoint(self, endpoint):
    """装饰器，用于将函数注册为端点。
        例：：
            @app.endpoint('example.endpoint')
            def example():
                return "example"

        :param endpoint: 端点的名称
        """
    def decorator(f):
        self.view_functions[endpoint] = f
        return f
    return decorator
```



### full_dispatch_request()

```python
def full_dispatch_request(self):
    """调度请求，并在此之上执行请求的预处理和后处理以及HTTP异常捕获和错误处理。
    .. versionadded:: 0.7
    """
    self.try_trigger_before_first_request_functions()
    try:
        request_started.send(self)
        rv = self.preprocess_request()
        if rv is None:
            rv = self.dispatch_request()		# 调用视图函数
    except Exception as e:
        rv = self.handle_user_exception(e)
    
    # 执行视图函数后进行善后工作
    return self.finalize_request(rv)
```



### finalize_request(rv,,..)

```python
def finalize_request(self, rv, from_error_handler=False):
    """给定一个视图函数的返回值，它通过将请求转换为响应并调用后处理函数来最终确定请求。 正常请求分派和错误处理程序均调用此方法。

    因为这意味着可能由于失败而被调用，所以可以使用一种特殊的安全模式，该模式可以通过`from_error_handler`标志启用。 如果启用，将记录响应处理失败，否则将忽略。
    """
    response = self.make_response(rv)
    try:
        response = self.process_response(response)		# 善后工作
        request_finished.send(self, response=response)
    except Exception:
        if not from_error_handler:
            raise
        self.logger.exception(
            "Request finalizing failed with an error while handling an error"
        )
    return response
```





### request_context(environ)

```python
def request_context(self, environ):
    """创建一个 :class:`~flask.ctx.RequestContext` r代表WSGI环境. 使用``with``块来推送上下文，这将使此请求成为data请求。
    See :doc:`/reqcontext`.
    块来推送上下文，这将使此请求成为data请求。 处理请求时，：meth：`wsgi_app`自动推送请求上下文。 使用 :meth:`test_request_context` 代替此方法来创建环境和上下文。
    :param environ: WSGI环境
    """
    # self 是 app 对象
    return RequestContext(self, environ)
```



### wsgi_app()

```python
def wsgi_app(self, environ, start_response):
    # 这里才真正执行 werkzeug 的源码
    """
    实际的WSGI应用程序。 
         ：meth：`__call__` 并没有没有实现功能，以便中间件无需丢失对应用程序对象的引用。 而不是这样做：
            app = MyMiddleware(app)

        最好这样做：
            app.wsgi_app = MyMiddleware(app.wsgi_app)
		然后，仍然有原始应用程序对象和可以继续在其上调用方法。

        .. versionchanged:: 0.7
            Teardown events for the request and app contexts are called
            even if an unhandled error occurs. Other events may not be
            called depending on when an error occurs during dispatch.
            See :ref:`callbacks-and-errors`.

        :param environ: WSGI环境。
        :param start_response: 接受状态代码的可调用对象，标题列表和一个可选的异常上下文开始响应。
        """
    # ctx = RequestContext(self, environ)
    # 	ctx.request = app.request_class(environ) = Request(environ)
    #	ctx.session = None
    ctx = self.request_context(environ)		
    # 1、对 environ请求数据再进行一次封装	(就是我们用的 request )
    # 2、从 environ 中获取名称为 session 的 cookie， 解密，反序列化
    error = None
    try:
        try:
            # 将 ctx 放到"某个神奇的地方"
            # 执行 SecureCookieSessionInterface.open_session, 去 cookie 中取值并给 ctx.session 重新赋值
            ctx.push()
            # 执行视图函数，返回响应数据
            response = self.full_dispatch_request()
            except Exception as e:
                error = e
                response = self.handle_exception(e)
            except:  # noqa: B001
                error = sys.exc_info()[1]
                raise
            return response(environ, start_response)
        finally:
            if self.should_ignore_error(error):
                error = None
            ctx.auto_pop(error)
```



### `__call__()`

```python
def __call__(self, environ, start_response):
    # 整个，所有请求的入口就是这里。一旦用户请求进来，先执行这
    # environ		：请求相关的所有数据(由 wsgi 做初步封装)
    # start_response：用于设置响应相关的数据
    
    """WSGI服务器将Flask应用程序对象称为WSGI应用程序。 这会调用：meth：`wsgi_app`，它可以包装到应用中间件。"""
    return self.wsgi_app(environ, start_response)
```







## Config 类

### from_object()

```python
def from_object(self, obj):
    """更新给定对象的值。一个对象可以是以下两种类型之一：
    	-	字符串：在这种情况下，将导入具有该名称的对象
        -	实际的对象引用：直接使用该对象
        
        对象通常是模块或类。 ：meth：`from_object`
        仅加载模块/类的大写属性。 ``dict``
        object 不能与 from_object 一起使用，因为 a 的键
        dict不是dict类的属性。


		基于模块的配置示例：：
            app.config.from_object('yourapplication.default_config'）
        从您的应用程序导入 default_config
            app.config.from_object（默认设置）
       
		加载之前对对象不做任何事情。如果对象是类并具有``@property''属性，它必须是在传递给此方法之前实例化。	
		您不应该使用此功能加载实际配置，而是用来加载默认配置。实际的配置应该被加载与：meth：`from_pyfile`配合使用，最好不在同一个软件包，因为该软件包可能在系统范围内安装。
        """
    if isinstance(obj, string_types):		# 传递进来的 obj 是不是一个字符串
        obj = import_string(obj)
    for key in dir(obj):
        if key.isupper():				# 如果找到的 key 都是大写
            self[key] = getattr(obj, key)
            # self 是 app.config 对象
```



#### import_string(import_name,...)

```mermaid
graph LR
A>uitls.py] -->B("import_string()")
```





## helpers.py 模块

#### _endpoint_from_view_func(view_func)

```python
def _endpoint_from_view_func(view_func):
    """返回给内部帮助者默认的端点
    这始终是函数名称。
    """
    assert view_func is not None, "expected view func if endpoint is not provided."
    return view_func.__name__					# 返回函数名
```





### flash(message, category)

```python
def flash(message, category="message"):
    """将消息 flash 到下一个请求。为了从会话中刷新消息并将其显示给用户后删除
     模板必须调用：func：`get_flashed_messages`接受数据

    .. 版本已更改：： 0.3
        添加了“ category”参数。

    :param message: 要刷新的消息。
    :param category: 消息的类别。 以下值建议使用``'message'``进行任何形式的消息，
    				``'error'`` for errors, 
    				``'info'`` for information messages and ``'warning'`` for warnings.   但是任何字符串的种类可以用作类别。
    """
    # 原始实现：
    #     session.setdefault('_flashes', []).append((category, message))
    #
    # 假设对会话中的可变结构进行的更改是
    # 始终与会话对象同步，这不适用于会话
    # 使用外部存储来保留其键/值的实现。
    flashes = session.get("_flashes", [])		# 去 session 中取一个列表
    flashes.append((category, message))			# 把值存进去
    session["_flashes"] = flashes				# 放进 session 中
    message_flashed.send(
        current_app._get_current_object(), message=message, category=category
    )

```



### get_flashed_messages(...,category_filte )

```python
def get_flashed_messages(with_categories=False, category_filter=()):
    """从会话中拉出所有闪烁的消息并返回它们。
    在同一请求中对该函数的进一步调用将返回
    相同的消息。默认情况下，仅返回消息，但是当`with_categories`设置为``True``时，返回值将是以（类别，消息）形式的元组列表。

  通过提供以下内容，将 flashed 的消息过滤为一个或多个类别
    “ category_filter”中的类别。这允许在单独的html块。 `with_categories`和`category_filter`参数是不同的：

    * `with_categories` 控制是否通过消息返回类别
      	文本（``True``给出一个元组，其中``False``仅给出消息文本）。
    * `category_filter` 将消息过滤为仅与提供的类别。.

    See :ref:`message-flashing-pattern` for examples.

    .. versionchanged:: 0.3
       `with_categories` parameter added.

    .. versionchanged:: 0.9
        `category_filter` parameter added.

    :param with_categories: 设置为``True``也可以接收类别.
    :param category_filter: 限制返回值的类别白名单
    """
    flashes = _request_ctx_stack.top.flashes
    if flashes is None:
        _request_ctx_stack.top.flashes = flashes = (
            session.pop("_flashes") if "_flashes" in session else []
        )
        # session.pop("_flashes") 
    if category_filter:
        flashes = list(filter(lambda f: f[0] in category_filter, flashes))
    if not with_categories:
        return [x[1] for x in flashes]
    return flashes
```



## utils.py 模块

### import_string(import_name, ...)

```python
def import_string(import_name, silent=False):
    """基于字符串导入对象。如果您要使用导入路径作为端点或类似的东西。 
    	导入路径可以以虚线表示法指定（``xml.sax.saxutils.escape``）
     	或使用冒号作为对象定界符（``xml.sax.saxutils:escape``）。
    
    	如果`silent`为True，则如果导入失败，则返回值为'None'。
    	
    	：param 
    		import_name：要导入的对象的点分名称。
     		silent：如果设置为True，导入错误将被忽略并且相反，没有返回。
     	：return：导入对象
    """
    
	# 强制导入名称自动转换为字符串
    # __import__无法处理fromlist中的unicode字符串
    # 如果模块是软件包
    import_name = str(import_name).replace(":", ".")	# 处理冒号
    # 将 ： 转化为 .
    try:
        try:
            __import__(import_name)						# pass
        except ImportError:
            if "." not in import_name:
                raise
        else:
            return sys.modules[import_name]

        # 从右边第一个 . 开始切分
        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])
        try:
            # 从 model 中获取 obj_name 的值
            return getattr(module, obj_name)
        except AttributeError as e:
            raise ImportError(e)

    except ImportError as e:
        if not silent:
            reraise(
                ImportStringError, ImportStringError(import_name, e), sys.exc_info()[2]
            )
```





## builtins.py 模块

### `__import__(name,..)`

```python
def __import__(name, globals=None, locals=None, fromlist=(), level=0): # real signature unknown; restored from __doc__
    """
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> 模块
    
     功能：导入模块。 
     因为此功能是供Python使用的解释器，而不是一般用途; 编程的话最好使用importlib.import_module() 以方式导入模块。
    
    globals 参数仅用于确定上下文。
    他们没有被修改。 locals参数未使用。 
    fromlist 应该是模拟``从名称导入...''的名称列表，或者空列表以模拟``导入名称''。
		从包中导入模块时，请注意格式为 __import __（'A.B'，...）
    	当fromlist为空时返回包A，但是当fromlist不为空时返回包B 
    level参数用于确定是否执行绝对或相对导入：0为绝对，而正数是相对于当前模块搜索的父目录的数量。
    """
    pass
```





## ctx.py 模块

### RequestContext 类

#### `__init__(app, environ,...)`

```python
def __init__(self, app, environ, request=None, session=None):
    self.app = app
    if request is None:
        request = app.request_class(environ)		# 对请求数据进行封装
    self.request = request
    self.url_adapter = None
    try:
        self.url_adapter = app.create_url_adapter(self.request)
    except HTTPException as e:
        self.request.routing_exception = e
    self.flashes = None
    self.session = session

    # 请求上下文可以多次推送，并与其他请求上下文交错。 
    # 现在，仅当弹出最后一个级别时，我们才能摆脱它们。 
    # 此外，如果缺少应用程序上下文，则会隐式创建一个，因此对于每个级别，我们都添加此信息
    self._implicit_app_ctx_stack = []

    # 指示上下文是否被保留。 下次推送另一个上下文时，将弹出保留的上下文。
    self.preserved = False

    # 如果存在上下文保留启动的情况，则会记住pop的异常。
    self._preserved_exc = None

    # 在响应对象上请求之后应执行的功能。 
    # 这些将在常规的“ after_request”函数之前调用。
    self._after_request_functions = []
```



#### push()

```python
def push(self):
    """将请求上下文绑定到当前上下文。"""
    # 如果在调试模式下发生异常，或者在异常情况下激活了上下文保存，则恰好一个上下文留在堆栈上。 
    # 理由是您希望在调试情况下访问该信息。 
    # 但是，如果有人忘记再次弹出该上下文，我们要确保在下一次推送时使它无效，否则我们将冒着内存泄漏的风险。 
    # 这通常只是测试套件中的一个问题，因为此功能在生产环境中不起作用。
    top = _request_ctx_stack.top
    if top is not None and top.preserved:
        top.pop(top._preserved_exc)

    # 在推送请求上下文之前，我们必须确保有一个应用程序上下文。
    app_ctx = _app_ctx_stack.top
    if app_ctx is None or app_ctx.app != self.app:
        app_ctx = self.app.app_context()
        app_ctx.push()
        self._implicit_app_ctx_stack.append(app_ctx)
    else:
        self._implicit_app_ctx_stack.append(None)

    if hasattr(sys, "exc_clear"):
        sys.exc_clear()

    _request_ctx_stack.push(self)
    # 在请求上下文可用时打开会话。 
    # 这允许自定义的 open_session 方法使用请求上下文。
    # 如果这是第一次推送请求，则仅打开一个新会话，否则stream_with_context丢失会话。
    if self.session is None:
        # app.session_interface = flask.SecureCookieSessionInterface()
        # 	obj = SecureCookieSessionInterface对象
        # 	self.session = obj.open_session(self.app, self.request)
        session_interface = self.app.session_interface
        self.session = session_interface.open_session(self.app, self.request)

        if self.session is None:
            self.session = session_interface.make_null_session(self.app)

    if self.url_adapter is not None:
        self.match_request()
```





## sessions.py 模块

### SecureCookieSessionInterface 类

```python
class SecureCookieSessionInterface(SessionInterface):
    """The default session interface that stores sessions in signed cookies
    through the :mod:`itsdangerous` module.
    """

    #: the salt that should be applied on top of the secret key for the
    #: signing of cookie based sessions.
    salt = "cookie-session"
    #: the hash function to use for the signature.  The default is sha1
    digest_method = staticmethod(hashlib.sha1)
    #: the name of the itsdangerous supported key derivation.  The default
    #: is hmac.
    key_derivation = "hmac"
    #: A python serializer for the payload.  The default is a compact
    #: JSON derived serializer with support for some extra Python types
    #: such as datetime objects or tuples.
    serializer = session_json_serializer
    session_class = SecureCookieSession

    def get_signing_serializer(self, app):
        if not app.secret_key:
            return None
        signer_kwargs = dict(
            key_derivation=self.key_derivation, digest_method=self.digest_method
        )
        return URLSafeTimedSerializer(
            app.secret_key,
            salt=self.salt,
            serializer=self.serializer,
            signer_kwargs=signer_kwargs,
        )

    def open_session(self, app, request):
        s = self.get_signing_serializer(app)
        if s is None:
            return None
        val = request.cookies.get(app.session_cookie_name)
        if not val:
            return self.session_class()
        max_age = total_seconds(app.permanent_session_lifetime)
        try:
            data = s.loads(val, max_age=max_age)
            return self.session_class(data)
        except BadSignature:
            return self.session_class()

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)

        # If the session is modified to be empty, remove the cookie.
        # If the session is empty, return without setting the cookie.
        if not session:
            if session.modified:
                response.delete_cookie(
                    app.session_cookie_name, domain=domain, path=path
                )

            return

        # Add a "Vary: Cookie" header if the session was accessed at all.
        if session.accessed:
            response.vary.add("Cookie")

        if not self.should_set_cookie(app, session):
            return

        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        samesite = self.get_cookie_samesite(app)
        expires = self.get_expiration_time(app, session)
        val = self.get_signing_serializer(app).dumps(dict(session))
        response.set_cookie(
            app.session_cookie_name,
            val,
            expires=expires,
            httponly=httponly,
            domain=domain,
            path=path,
            secure=secure,
            samesite=samesite,
        )

```



#### open_session(app, request)

```python
def open_session(self, app, request):
    s = self.get_signing_serializer(app)
    if s is None:
        return None
    
    # app.session_cookie_name     配置文件中的默认值 “session”
    val = request.cookies.get(app.session_cookie_name)
    if not val:
        return self.session_class()			# {}
    max_age = total_seconds(app.permanent_session_lifetime)
    try:
        data = s.loads(val, max_age=max_age)	
        return self.session_class(data)		# {"k1":"fsefsdfaadfg"}
    except BadSignature:
        return self.session_class()

```



#### save_session(app, session, response)

```python
def save_session(self, app, session, response):
    domain = self.get_cookie_domain(app)
    path = self.get_cookie_path(app)

    # If the session is modified to be empty, remove the cookie.
    # If the session is empty, return without setting the cookie.
    if not session:
        if session.modified:
            response.delete_cookie(
                app.session_cookie_name, domain=domain, path=path
            )

        return

    # Add a "Vary: Cookie" header if the session was accessed at all.
    if session.accessed:
        response.vary.add("Cookie")

    if not self.should_set_cookie(app, session):
        return

    httponly = self.get_cookie_httponly(app)
    secure = self.get_cookie_secure(app)
    samesite = self.get_cookie_samesite(app)
    expires = self.get_expiration_time(app, session)
    val = self.get_signing_serializer(app).dumps(dict(session))
    # adict = self.get_signing_serializer(app) 加密
    # adict.dumps(dict(session)) 变成字符串了
    response.set_cookie(
        app.session_cookie_name,
        val,						# 再将 session 写入 response
        expires=expires,
        httponly=httponly,
        domain=domain,
        path=path,
        secure=secure,
        samesite=samesite,
    )
```



## wrappers.py 模块

```python
class Request(RequestBase, JSONMixin):
    """The request object used by default in Flask.  Remembers the
    matched endpoint and view arguments.

    It is what ends up as :class:`~flask.request`.  If you want to replace
    the request object used you can subclass this and set
    :attr:`~flask.Flask.request_class` to your subclass.

    The request object is a :class:`~werkzeug.wrappers.Request` subclass and
    provides all of the attributes Werkzeug defines plus a few Flask
    specific ones.
    """

    #: The internal URL rule that matched the request.  This can be
    #: useful to inspect which methods are allowed for the URL from
    #: a before/after handler (``request.url_rule.methods``) etc.
    #: Though if the request's method was invalid for the URL rule,
    #: the valid list is available in ``routing_exception.valid_methods``
    #: instead (an attribute of the Werkzeug exception
    #: :exc:`~werkzeug.exceptions.MethodNotAllowed`)
    #: because the request was never internally bound.
    #:
    #: .. versionadded:: 0.6
    url_rule = None

    #: A dict of view arguments that matched the request.  If an exception
    #: happened when matching, this will be ``None``.
    view_args = None

    #: If matching the URL failed, this is the exception that will be
    #: raised / was raised as part of the request handling.  This is
    #: usually a :exc:`~werkzeug.exceptions.NotFound` exception or
    #: something similar.
    routing_exception = None

    @property
    def max_content_length(self):
        """Read-only view of the ``MAX_CONTENT_LENGTH`` config key."""
        if current_app:
            return current_app.config["MAX_CONTENT_LENGTH"]

    @property
    def endpoint(self):
        """The endpoint that matched the request.  This in combination with
        :attr:`view_args` can be used to reconstruct the same or a
        modified URL.  If an exception happened when matching, this will
        be ``None``.
        """
        if self.url_rule is not None:
            return self.url_rule.endpoint

    @property
    def blueprint(self):
        """The name of the current blueprint"""
        if self.url_rule and "." in self.url_rule.endpoint:
            return self.url_rule.endpoint.rsplit(".", 1)[0]

    def _load_form_data(self):
        RequestBase._load_form_data(self)

        # In debug mode we're replacing the files multidict with an ad-hoc
        # subclass that raises a different error for key errors.
        if (
            current_app
            and current_app.debug
            and self.mimetype != "multipart/form-data"
            and not self.files
        ):
            from .debughelpers import attach_enctype_error_multidict

            attach_enctype_error_multidict(self)
```







































