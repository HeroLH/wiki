----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# 理解 RESTful 架构
&emsp;&emsp;越来越多的人开始意识到，网站即软件，而且是一种新型的软件。
&emsp;&emsp;这种"互联网软件"采用B/S模式，建立在分布式体系上，通过互联网通信，具有高延时（high latency）、高并发等特点。
&emsp;&emsp;网站开发，完全可以采用软件开发的模式。但是传统上，软件和网络是两个不同的领域，很少有交集；软件开发主要针对单机环境，网络则主要研究系统之间的通信。互联网的兴起，使得这两个领域开始融合，现在我们必须考虑，如何开发在互联网环境中使用的软件。

&emsp;&emsp;RESTful架构，就是目前最流行的一种**互联网软件架构**。它结构清晰、符合标准、易于理解、扩展方便，所以正得到越来越多网站的采用。

**补充理解: 什么是接口？**

- URL

- 约束( python 中不存在 )
    约束继承（实现）了他的类中必须含有IFoo中的方法

    

    ```java
    interface IFoo:
    	def func(self): pass 			
    
    class Foo(IFoo):
    	def func(self): 
    		print(11111)
    ```

    

 

## 一、什么是RESTful 

- REST与技术无关，代表的是一种**软件架构风格**，REST是 **Representational State Transfer** 的简称，中文翻译为“表征状态转移”
- REST从资源的角度类审视整个网络，它将分布在网络中某个节点的资源通过 URL 进行标识，客户端应用通过 URL 来获取资源的表征，获得这些表征致使这些应用转变状态
- 所有的数据，不过是通过网络获取的还是操作（增删改查）的数据，都是资源，将一切数据视为资源是 REST 区别与其他架构风格的最本质属性
- 对于 REST 这种面向资源的架构风格，有人提出一种全新的结构理念，即：**面向资源架构**（ROA：Resource Oriented Architecture）面向切面编程






## 二、起源

&emsp;&emsp;REST这个词，是 [Roy Thomas Fielding](http://en.wikipedia.org/wiki/Roy_Fielding) 在他2000年的 [博士论文](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) 中提出的

&emsp;&emsp;Fielding 是一个非常重要的人，他是 HTTP协议（1.0版和1.1版）的主要设计者、Apache 服务器软件的作者之一、Apache 基金会的第一任主席。所以，他的这篇论文一经发表，就引起了关注，并且立即对互联网开发产生了深远的影响。



## 三、名称

&emsp;&emsp;Fielding 将他对互联网软件的架构原则，定名为 **REST**，即 **Representational State Transfer** 的缩写。我对这个词组的翻译是"**表现层状态转化**"。如果一个架构符合REST原则，就称它为RESTful架构。

&emsp;&emsp;要理解 RESTful 架构，最好的方法就是去理解 Representational State Transfer 这个词组到底是什么意思，它的每一个词代表了什么涵义。如果你把这个名称搞懂了，也就不难体会REST是一种什么样的设计。



### 资源（Resources）
&emsp;&emsp;REST 的名称"表现层状态转化"中，省略了主语。**"表现层"其实指的是"资源 "表现层"。**
&emsp;&emsp;所谓"资源"，就是网络上的一个实体，或者说是网络上的一个具体信息。它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的实在。你可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。
&emsp;&emsp;**所谓"上网"，就是与互联网上一系列的"资源"互动，调用它的 URI。**



### 表现层(Representation)
&emsp;&emsp;"资源"是一种信息实体，它可以有多种外在表现形式。我们**把"资源"具体呈现出来的形式，叫做它的"表现层"**。
&emsp;&emsp;比如，文本可以用 txt 格式表现，也可以用 HTML格式、XML格式、JSON 格式表现，甚至可以采用二进制格式；图片可以用JPG格式表现，也可以用PNG格式表现。
&emsp;&emsp;URI 只代表资源的实体，不代表它的形式。严格地说，有些网址最后的".html"后缀名是不必要的，因为这个后缀名表示格式，属于"表现层"范畴，而URI应该只代表"资源"的位置。它的具体表现形式，应该在 HTTP 请求的头信息中用 `Accept` 和 `Content-Type` 字段指定，这两个字段才是对"表现层"的描述。



### 状态转化（State Transfer）
&emsp;&emsp;访问一个网站，就代表了客户端和服务器的一个互动过程。在这个过程中，势必涉及到数据和状态的变化。
&emsp;&emsp;互联网通信协议 HTTP 协议，是一个无状态协议。这意味着，所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生"状态转化"（State Transfer）。而这种转化是建立在表现层之上的，所以就是"表现层状态转化"。
&emsp;&emsp;客户端用到的手段，只能是 HTTP 协议。具体来说，就是 HTTP 协议里面，四个表示操作方式的动词：GET、POST、PUT、DELETE。它们分别对应四种基本操作：GET用来获取资源，POST用来新建资源（也可以用于更新资源），PUT用来更新资源，DELETE用来删除资源。



## 四、综述
综合上面的解释，我们总结一下什么是RESTful架构：
- 每一个URI代表一种资源；
- 客户端和服务器之间，传递这种资源的某种表现层；
- 客户端通过四个 HTTP 动词，对服务器端资源进行操作，实现"表现层状态转化"。



## 五、误区

### URI 包含动词

&emsp;&emsp;RESTful 架构有一些典型的设计误区。最常见的一种设计错误，就是 **URI 包含动词**。因为"资源"表示一种实体，所以应该是名词，URI不应该有动词，动词应该放在 HTTP 协议中。举例来说: 某个 URI 是 `/posts/show/1`，其中 show 是动词，这个URI就设计错了，正确的写法应该是`/posts/1`，然后用 GET 方法表示 show。
&emsp;&emsp;**如果某些动作是HTTP动词表示不了的，你就应该把动作做成一种资源**。比如网上汇款，从账户1向账户2汇款500元，错误的URI是：
```python
POST /accounts/1/transfer/500/to/2
```

&emsp;&emsp;正确的写法是把动词 `transfer` 改成名词 `transaction`，资源不能是动词，但是可以是一种服务：

```python
POST /transaction HTTP/1.1
Host: 127.0.0.1
 
from=1&to=2&amount=500.00
```



### URI 中加入版本号

&emsp;&emsp;另一个设计误区，就是在 **URI 中加入版本号**：

```python
http://www.example.com/app/1.0/foo
http://www.example.com/app/1.1/foo
http://www.example.com/app/2.0/foo
```

&emsp;&emsp;因为不同的版本，可以理解成同一种资源的不同表现形式，所以应该采用同一个 URI。版本号可以在 HTTP 请求头信息的 Accept 字段中进行区分（参见 [Versioning REST Services](http://www.informit.com/articles/article.aspx?p=1566460)）：

```python
Accept: vnd.example-com.foo+json; version=1.0
Accept: vnd.example-com.foo+json; version=1.1
Accept: vnd.example-com.foo+json; version=2.0
```

> **注**，虽说 restfull 规范建议版本号放在请求头而不是url里，但事实上为了使用方便，大多数开发者还是喜欢把版本号放在url上，这样容易直观区分





# Restful API设计指南

接下来我将介绍RESTful API的设计细节，探讨如何设计一套合理、好用的API

## 一、协议
API与用户的通信协议，总是使用 [HTTPs协议](http://www.ruanyifeng.com/blog/2014/02/ssl_tls.html)。



## 二、域名
应该尽量将API部署在专用域名之下。(**会出现跨域问题**,建议采用下一种方式 )
```markdown
https://api.example.com
```
如果确定API很简单，不会有进一步扩展，可以考虑放在主域名下。　　
```markdown
https://example.org/api/
```



## 三、版本（Versioning）
- 应该将API的版本号放入URL。

```markdown
https://api.example.com/v1/
https://example.org/api/v1/
```

- 另一种做法是，将版本号放在HTTP头信息中，但不如放入URL方便和直观。[Github](https://developer.github.com/v3/media/#request-specific-version) 采用这种做法。



## 四、路径（Endpoint）
&emsp;&emsp;路径又称"终点"（endpoint），表示API的具体网址。
&emsp;&emsp;在 RESTful 架构中，每个网址代表一种资源（resource），所以网址中不能有动词，只能有名词，而且所用的名词往往与数据库的表格名对应。一般来说，数据库中的表都是同种记录的"集合"（collection），所以**API中的名词也应该使用复数。**举例来说，有一个API提供动物园 (zoo) 的信息，还包括各种动物和雇员的信息，则它的路径应该设计成下面这样。
```markdown
https://api.example.com/v1/zoos
https://api.example.com/v1/animals
https://api.example.com/v1/employees`
```



## 五、HTTP动词
对于资源的具体操作类型，由HTTP动词表示。
常用的HTTP动词有下面五个（括号里是对应的SQL命令）。

```markdown
GET（SELECT）：从服务器取出资源（一项或多项）。
POST（CREATE）：在服务器新建一个资源。
PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
DELETE（DELETE）：从服务器删除资源。`
```

还有两个不常用的HTTP动词。
```markdown
HEAD：获取资源的元数据。
OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的。
CONNECT: HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。通常用于SSL加密服务器的链接（经由非加密的HTTP代理服务器）。
```

下面是一些例子:

```markdown
GET /zoos：					列出所有动物园
POST /zoos：					新建一个动物园
GET /zoos/ID：				获取某个指定动物园的信息
PUT /zoos/ID：				更新某个指定动物园的信息（提供该动物园的全部信息）
PATCH /zoos/ID：				更新某个指定动物园的信息（提供该动物园的部分信息）
DELETE /zoos/ID：			删除某个动物园
GET /zoos/ID/animals：		列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID：	删除某个指定动物园的指定动物
```



## 六、过滤信息（Filtering）
&emsp;&emsp;如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。下面是一些常见的参数。

```markdown
`?limit=10：指定返回记录的数量``?offset=10：指定返回记录的开始位置。``?page=2&per_page=100：指定第几页，以及每页的记录数。``?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。``?animal_type_id=1：指定筛选条件`
```

&emsp;&emsp;参数的设计允许存在冗余，即允许 API 路径和 URL 参数偶尔有重复。比如，`GET /zoo/ID/animals` 与 `GET /animals?zoo_id=ID` 的含义是相同的。



## 七、状态码（Status Codes）
&emsp;&emsp;服务器向用户返回的状态码和提示信息，常见的有以下一些（方括号中是该状态码对应的HTTP动词）。但是状态码表示的信息很有限,现在一般用code,或是混用

| 状态码 |                状态信息                |                             说明                             |
| :----: | :------------------------------------: | :----------------------------------------------------------: |
|  200   |               OK - [GET]               |  服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）  |
|  201   |       CREATED - [POST/PUT/PATCH]       |                    用户新建或修改数据成功                    |
|  202   |             Accepted - [*]             |           表示一个请求已经进入后台排队（异步任务）           |
|  204   |         NO CONTENT - [DELETE]          |                       用户删除数据成功                       |
|  400   |   INVALID REQUEST - [POST/PUT/PATCH]   | 用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的 |
|  401   |           Unauthorized - [*]           |          表示用户没有权限（令牌、用户名、密码错误）          |
|  403   |            Forbidden - [*]             |    表示用户得到授权（与401错误相对），但是访问是被禁止的     |
|  404   |            NOT FOUND - [*]             | 用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的 |
|  406   |         Not Acceptable - [GET]         | 用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式） |
|  410   |              Gone -[GET]               |           用户请求的资源被永久删除，且不会再得到的           |
|  422   | Unprocesable entity - [POST/PUT/PATCH] |              当创建一个对象时，发生一个验证错误              |
|  500   |      INTERNAL SERVER ERROR - [*]       |       服务器发生错误，用户将无法判断发出的请求是否成功       |

状态码的完全列表参见 [这里](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)。



## 八、错误处理（Error handling）
&emsp;&emsp;如果状态码是4xx，就应该向用户返回出错信息。一般来说，返回的信息中将 error 作为键名，出错信息作为键值即可。

```python
{
    error: "Invalid API key"
}
```





## 九、返回结果
&emsp;&emsp;针对不同操作，服务器向用户返回的结果应该符合以下规范。

|          返回结果           |            说明            |
| :-------------------------: | :------------------------: |
|       GET /collection       | 返回资源对象的列表（数组） |
|  GET /collection/resource   |      返回单个资源对象      |
|      POST /collection       |    返回新生成的资源对象    |
|  PUT /collection/resource   |     返回完整的资源对象     |
| PATCH /collection/resource  |     返回完整的资源对象     |
| DELETE /collection/resource |       返回一个空文档       |



## 十、Hypermedia API
&emsp;&emsp;RESTful API 最好做到 Hypermedia，即返回结果中提供链接，连向其他 API 方法，使得用户不查文档，也知道下一步应该做什么。比如，当用户向api.example.com的根目录发出请求，会得到这样一个文档。

```python
{
    "link": {
      	"rel":   "collection https://www.example.com/zoos",
      	"href":  "https://api.example.com/zoos",
      	"title": "List of zoos",
      	"type":  "application/vnd.yourformat+json"
    }
}
```

&emsp;&emsp;上面代码表示，文档中有一个 link 属性，用户读取这个属性就知道下一步该调用什么API 了。
- rel 表示这个 API 与当前网址的关系: collection 关系，并给出该 collection 的网址）
- href 表示 API 的路径
- title 表示 API的标题
- type 表示返回类型。

&emsp;&emsp;Hypermedia API 的设计被称为 [HATEOAS](http://en.wikipedia.org/wiki/HATEOAS)。Github 的 API 就是这种设计，访问[api.github.com](https://api.github.com/) 会得到一个所有可用API的网址列表。

 ```python
{
  "current_user_url": "https://api.github.com/user",
  "authorizations_url": "https://api.github.com/authorizations",
  // ...
}
 ```

&emsp;&emsp;从上面可以看到，如果想获取当前用户的信息，应该去访问 [api.github.com/user](https://api.github.com/user)，然后就得到了下面结果。

```python
{
  "message": "Requires authentication",
  "documentation_url": "https://developer.github.com/v3"
}
```

&emsp;&emsp;上面代码表示，服务器给出了提示信息，以及文档的网址。　　



## 十一、其他
（1）API的身份认证应该使用 [OAuth 2.0](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html) 框架。
（2）服务器返回的数据格式，应该尽量使用JSON，避免使用XML。





## 总结

- **https**

- **根据method不同，进行不同操作**

    > GET/POST/PUT/DELETE/PATCH

- **面向资源编程**

    ```python
    http://www.luffycity.com/salary
    ```

- **体现版本**

    ```python
    http://www.luffycity.com/v1/salary
    http://www.luffycity.com/v2/salary
    
    # 举例:
    https://v4.bootcss.com/
    https://v3.bootcss.com/
    ```

- **体现是API**

    ```python
    # 推荐使用以下
    http://www.luffycity.com/api/v1/salary
    http://www.luffycity.com/api/v2/salary	
    
    # 涉及到跨域
    http://api.luffycity.com/v1/salary	
    http://api.luffycity.com/v2/salary	
    ```

- **响应式设置状态码**

    ```python
    return HttpResponse('adfasdf',status=300)
    ```

- **条件** 

    ```python
    https://www.luffycity.com/api/v2/salary?page=1&size=10
    ```

- **返回值**

    ```python
    https://www.luffycity.com/api/v2/salary
    ```

    ```python
    GET: 所有列表
    {
        code: 10000,
        data: [    
            {'id':1,'title':'高亮'},
            {'id':1,'title':'龙泰'},
            {'id':1,'title':'小东北'},
        ]
    }
    
    POST: 返回新增的数据
    {'id':1,'title':'高亮'}
    
    
    # 必需要有明确对象才可以进行修改
    https://www.luffycity.com/api/v2/salary/1/
    GET: 获取单条数据
    {'id':1,'title':'高亮'}
    PUT：更新
    {'id':1,'title':'高亮'}
    PATCH: 局部更新
    {'id':1,'title':'高亮'}
    DELETE：删除
    ```

- **返回错误信息**

    ```python
    {
        code: 100001,
        error: 'xxx错误'
    }
    ```

- **Hypermedia API**

    ```python
    ret = {
        code: 1000,
        data:{
            id:1,
            name:'小强',
            depart_id:http://www.luffycity.com/api/v1/depart/8/
        }
    }
    ```







# Django rest framework(10个组件)

```shell
# 安装
pip install restframework
```

- 权限
- 认证
- 访问频率限制
- 序列化
- 路由 
- 视图

- 分页 
- 解析器
- 渲染器
- 版本 



## 1.基本流程
### 原先的开发
#### **urls.py**
```python
urlpatterns = [
    url(r'^get_user/', api_views.get_user ),
    url(r'^add_user/', api_views.add_user ),
    url(r'^del_user/', api_views.del_user ),
    url(r'^update_user/', api_views.update_user ),
]
```

#### **views.py**
```python
def get_user( request ):
    return HttpResponse("get_user")

def add_user( request ):
    return HttpResponse("add_user")

def del_user( request ):
    return HttpResponse("del_user")

def update_user( request ):
    return HttpResponse("update_user")
```






### Django实现 restful 规范
#### **路由系统：**
```python
urlpatterns = [
    url(r'^users/', api_views.users ),
]
```

#### **视图：**
```python
from django.views import View
from django.http import JsonResponse
 
#FBV 
def users(request):
    if request.method == "GET":
        return HttpResponse( "users_get" )
    elif request.method == "POST":
        return HttpResponse( "users_post" )
    elif request.method == "PUT":
        return HttpResponse( "users_put" )
    elif request.method == "DELETE":
        return HttpResponse( "users_delete" )

#CBV  
class UsersView( View ):
    
    def get(self, request, *args, **kwrgs ):
        return HttpResponse("get_users")
    
    def post(self, request, *args, **kwrgs ):
        return HttpResponse("post_users")
    
    def delete(self, request, *args, **kwrgs ):
        return HttpResponse("delete_users")
    
    def put(self, request, *args, **kwrgs ):
        return HttpResponse("update_users")
```





### 基于 Django Rest Framework 框架实现
#### url.py
```python
from django.conf.urls import url, include
from web.views.s1_api import TestView
 
urlpatterns = [
    url(r'^test/', TestView.as_view()),
]
```

#### views.py
```python
from rest_framework.views import APIView
from rest_framework.response import Response
 
 
class TestView(APIView):
    
    def dispatch(self, request, *args, **kwargs):
        """
        请求到来之后，都要执行 dispatch 方法，dispatch 方法根据请求方式不同触发 get/post/put 等方法
        注意：APIView 中的 dispatch 方法有好多好多的功能
        """
        return super().dispatch(request, *args, **kwargs)
 
    def get(self, request, *args, **kwargs):
        return Response('GET请求，响应内容')
 
    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')
 
    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```





## **2.  认证**
> 有些 api 须要用户登陆认证之后才能访问

### 使用

- **创建类：** 继承 `BaseAuthentication`, 实现 `authenticate` 和 `authenticate_header` 方法

- **返回值:**  

    - **None** :  循环到下一个认证

    - **raise**:   抛出异常

        ```python
        from rest_framework.authentication import exceptions    # 异常处理
        raise exceptions.AuthenticationFailed("Authtiction: 用户认证失败")
        ```

    - **返回值( 元素1, 元素2)**: 元素 1 赋值给 `request.user` , 元素 2 赋值给 `request.authr `

- **局部使用**

    ```python
    class Authtiction( BaseAuthentication ):
        ...
    
    class UsersView( APIView ):   
        authentication_classes = [Authtiction,]
        def get(self, request, *args, **kwargs ):
    		...
    ```

- **全局使用**

    **setting.py**

    ```python
    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES":[
            # 要写完整的地址
            "api.utils.auth.FirstAuthtication",
            "api.utils.auth.Authtication",
        ],
        # "UNAUTHENTICATED_USER":lambda:"匿名用户"
        "UNAUTHENTICATED_USER":None			# 设置匿名用户,默认为 AnonmousUser
    	"UNAUTHENTICATED_TOKEN":None		# token值默认为 None
    }
    ```


- **全局下的局部使用**

    ```python
     authentication_classes = []		# 不使用任何全局或局部的认证
    ```

    




### 原理

#### url.py

```python
from django.conf.urls import url, include
from web.viewsimport TestView

urlpatterns = [
    url(r'^test/', TestView.as_view()),
]
```


#### view.py
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions

token_list = [
    'sfsfss123kuf3j123',
    'asijnfowerkkf9812',
]

class TestAuthentication( object ):	
    # 可以使用 object, 建议最好继承 BaseAuthentication类
    def authenticate(self, request):			# 做具体的认证流程
        val = request.query_params.get('token')
        # val = request._request.GET.get('token')
        # 获取用户名密码,去数据库校验
        if val not in token_list:
            raise exceptions.AuthenticationFailed("用户认证失败")
        return ('登录用户', '用户token')

    def authenticate_header(self, request):
        # 验证失败时，返回的响应头WWW-Authenticate对应的值
        pass


class TestView(View):
    # 走自己的认证,不加默认步骤认证
    authentication_classes = [TestAuthentication, ]		
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print(request.user)			# 上面返回的登陆用户
        print(request.auth)
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')
```

#### 源码流程
```mermaid
graph TD
Z("TestView") -->|super 继承|Y("View")
Y -->A("dispatch()")
A -->|封装 原生 request | B("initialize_request()")
A--> C("initial()")
B -->|返回封装| D("Request")
D -->|调用原生 request| E(request._request)
D -->|封装身份验证器列表| F("get_authenticators()")
D -->|属性方法|I
F -->|返回实例化身份验证器列表|G("self.authentication_classes")
G -->|restframework 默认配置|X(api_settings.DEFAULT_AUTHENTICATION_CLASSES)
G -->|自身类配置|N
C -->|用户认证|H("perform_authentication()")
H -->|返回|I("request.user")
I -->|用户认证方法,循环认证类的所有对象|J("_authenticate()")
J -->|执行认证类的 authenticate方法|K("authenticator.authenticate(self)")
K -->|返回一个元组|M("赋值给self.user, self.auth")
M -->|查找自身的authentication_classes有没有|N("authentication_classes = [ TestAuthentication, ]")
K -->|抛出异常|W("_not_authenticated()")
K -->|返回None|W2("循环列表里的下一个认证处理")
W2-->|都没有认证方法处理|W3("_not_authenticated()")
W3-->|给user和auth赋默认值|W4("AnonymousUser,None")
N -->|调用|O("authenticate()")
O -->|用户认证,验证成功后返回元组|P("get/post...")
```

```markdown
# 流程图不生效时生效
![1572692357297](.assets/1572692357297.png) 
```





### 用户url传入的 token 认证

#### auth 用户登陆

##### model.py

```python
class UserInfo( models.Model ):
    user_type_choise = (
        (1,"普通用户" ),
        (2, "VIP" ),
        (3, "SVIP" )
    )
    user_type = models.IntegerField( choices=user_type_choise )
    username = models.CharField( max_length=32,unique=True )
    passwd = models.CharField( max_length=64 )

class UserToken( models.Model ):
    user = models.OneToOneField(to="UserInfo")
    token = models.CharField( max_length=64 )
```

##### urls.py

```python
url(r'^api/v1/auth$', api_views.AuthView.as_view() ),
```

##### views.py

```python
from django.http import JsonResponse
from api import models
class AuthView( APIView ):
    """用户登录认证"""
    # 一般用 post 认证就好了
    def post(self,request, *args, **kwargs ):
        ret = {"code": 1000, "msg": None,}
        try:
            user = request._request.POST.get( "username" )
            password = request._request.POST.get( "password" )
            # request.query_params.get( "password" )
            obj = models.UserInfo.objects.filter( username=user, passwd=password ).first()
            if not obj:
                ret['code'] = 1001
                ret["msg"] = "用户名或密码错误"

            # 为用户创建token
            token = md5( user )
            models.UserToken.objects.update_or_create( user=obj, defaults={'token':token} )			# 有则更新,无则创建
            ret["token"] = token
        except Exception as e:
            ret['code'] = 999
            ret["msg"] = e
        return JsonResponse( ret )


import hashlib
import time
def md5(user):
    ctime = str( time.time() )
    m = hashlib.md5( bytes(user,encoding="utf-8") )
    m.update( bytes( ctime, encoding="utf-8") )
    return m.hexdigest()
```



#### auth 认证

##### 不用框架实现

> 缺点是每个函数(get/post...)你都要去添加认证函数

###### **urls.py**

```python
url(r'^users/', api_views.UsersView.as_view() ),
```

###### **views.py**

```python
class UsersView( APIView ):
    def get(self, request, *args, **kwargs ):
        ret = { "code":1000,"msg":None, "data":{}, }
        # --begin--: 用户登录认证
        token = request._request.GET.get("token")
        # request.query_params.get( "token" )
        if not token:
            ret["code"] = 998
            ret["msg"] = "用户未登录"
            return JsonResponse( ret )
		# -- end --: 用户登录认证
        try:
            for data in models.UserInfo.objects.all().values():
                ret["data"][data["id"]] = data
            ret["msg"] = "success"
        except Exception as Error:
            ret["code"] = 999
            ret["msg"] = Error
        return JsonResponse( ret )
```



##### 使用 rest Framework 框架

> 添加一条配置文件,再写一个认证类即可对所有方法函数(get/post...)进行认证

###### **法一:局部使用(写在一个文件里)**

**urls.py**

```python
url(r'^users/', api_views.UsersView.as_view() ),
```

**views.py**

```python
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import exceptions    # 异常处理

class Authtiction( object ):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        # val = request.query_params.get('token')
        token_obj = models.UserToken.objects.filter( token=token ).first()
        if not token_obj:
            #异常是抛出给 dispatch函数的initial函数
            raise exceptions.AuthenticationFailed("Authtiction: 用户认证失败")

        # 在 restframework 内部会把这两个字段赋值给 request, 以便后续操作使用
        return( token_obj.user,token_obj )
        # request.user = token_obj.user
        # request.auth = token_obj

    def authenticate_header(self, request):
        pass

class UsersView( APIView ):   
    authentication_classes = [Authtiction,]
    def get(self, request, *args, **kwargs ):
		...
```



###### **法二: 全局配置(修改配置文件)**

**urls.py**

```python
url(r'^users/', api_views.UsersView.as_view() ),
```

**views.py**

```python
class UsersView( APIView ):  
    # 使用下面写的认证方法
    def get(self, request, *args, **kwargs ):
		pass
        
class UsersView2( APIView ):  
    # 不使用认证方法
    authentication_classes = []
    def get(self, request, *args, **kwargs ):
		...
```

**新建 utils/auth.py**

```python
from rest_framework.request import Request
from rest_framework.authentication import BaseAuthentication

class FirstAuthtication( object ):
    def authenticate(self, request):
		pass

    def authenticate_header(self, request):
        pass

class Authtication( object ):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        # request.query_params.get('token')
        token_obj = models.UserToken.objects.filter( token=token ).first()
        if not token_obj:
            #异常是抛出给 dispatch函数的initial函数
            raise exceptions.AuthenticationFailed("Authtiction: 用户认证失败")

        # 在 restframework 内部会把这两个字段赋值给 request, 以便后续操作使用
        return( token_obj.user,token_obj )
        # request.user = token_obj.user
        # request.auth = token_obj

    def authenticate_header(self, request):
        pass
```

**settings.py**

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":[
        # 要写完整的地址
        "api.utils.auth.FirstAuthtication",
        "api.utils.auth.Authtication",
    ],
    # "UNAUTHENTICATED_USER":lambda:"匿名用户"
    "UNAUTHENTICATED_USER":None			# 设置匿名用户,默认为 AnonmousUser
	"UNAUTHENTICATED_TOKEN":None		# token值默认为 None
}
```



### 请求头认证



#### views.py

``` python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions

token_list = [
    'sfsfss123kuf3j123',
    'asijnfowerkkf9812',
]


class Test1Authentication(BaseAuthentication):
        import base64
        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if auth:
            auth = auth.encode('utf-8')
        else:
            return None
        print(auth,'xxxx')
        auth = auth.split()
        if not auth or auth[0].lower() != b'basic':
            raise exceptions.AuthenticationFailed('验证失败')
        if len(auth) != 2:
            raise exceptions.AuthenticationFailed('验证失败')
        username, part, password = base64.b64decode(auth[1]).decode('utf-8').partition(':')
        if username == 'alex' and password == '123':
            return ('登录用户', '用户token')
        else:
            raise exceptions.AuthenticationFailed('用户名或密码错误')

    def authenticate_header(self, request):
        pass

class Test2Authentication(BaseAuthentication):
    def authenticate(self, request):
        val = request.query_params.get('token')
        if val not in token_list:
            raise exceptions.AuthenticationFailed("用户认证失败")
        return ('登录用户', '用户token')

    def authenticate_header(self, request):
        pass


class TestView(APIView):
    authentication_classes = [Test1Authentication, Test2Authentication]
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.auth)
        return Response('GET请求，响应内容')

    def post(self, request, *args, **kwargs):
        return Response('POST请求，响应内容')

    def put(self, request, *args, **kwargs):
        return Response('PUT请求，响应内容')

views.py
```







## 3. 权限

### 使用

- **创建类：** 继承 `BasePermission`, 实现 `has_permission` 方法

- **返回值:**  

    - **True**:  有权访问
    - **False**:   无权访问

- **局部使用**

    ```python
    class MyPermission( BasePermission ):
        # 提供一种权限
        ...
    
    class UsersView( APIView ):   
        permission_classes = [MyPermission,]
        def get(self, request, *args, **kwargs ):
    		...
    ```

- **全局使用**

    ```python
    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES":[
            # 要写完整的地址
            "api.utils.permission.MyPermission",
            "api.utils.permission.MyPermission2",
        ],
    }
    ```


```markdown
# 用户类型不同,权限不同,所以要结合认证来处理
```



### 原理

#### views.py

```python
class MyPermission( object ):
    # 提供一种权限
    def has_permission(self, request, View):
        if request.user.user_type != 3:
            return False		# 无权限访问
        return True             # 说明有权限访问

class MyPermission2( object ):
    # 提供另一种权限
    def has_permission(self, request, View):
        if request.user.user_type == 3:
            return False		# 无权限访问
        return True             # 说明有权限访问
    
    
class OrdersView( APIView ):
    permission_classes = [MyPermission,]
    def get(self, request, *args, **kwrgs):
        ret = {"code": 1000, "msg": None, "data": {}, }
        try:
            for data in models.UserInfo.objects.all().values():
                ret["data"][data["id"]] = data
            ret["msg"] = "success"
        except Exception as Error:
            ret["code"] = 999
            ret["msg"] = Error
        return JsonResponse(ret)

    def post(self, request, *args, **kwrgs):
        return HttpResponse("post_orders")

class OrdersView2( APIView ):
    permission_classes = [MyPermission2,]
    def get(self, request, *args, **kwrgs):
		....

```



#### 源码流程

```
dispatch() --> initial() --> check_permissions() --> get_permissions()
get_permissions() --自身没有去父类找--> View --列表生成式 -->|| get_permissions()


```

```mermaid
graph TD
A("dispatch()") -->|封装request|B("initialize_request()")
B -->|顺序执行| C("initial()") 
C -->|权限认证方法,循环认证类的所有对象|D("check_permissions()")
D -->|返回实例化权限验证器列表|E("get_permissions()")
E -->|重写该方法|F("has_permission")
F -->|无权访问|F1("返回 False")
F -->|有权访问|F2("返回 True")
```





## 4. 访问频率

### 使用

- **创建类：

    - 继承 `BaseThrottle`, 实现 `allow_request` 和 `wait` 方法  
    - 继承 `SimpleRateThrottle`, 实现 `get_cache_key()` 方法  和配置文件 `scope="节流规则"`

- **局部使用**

    ```python
    class VisitThrottle( BaseThrottle ):
        # 提供一种权限
        ...
    
    class UsersView( APIView ):   
        permission_classes = [VisitThrottle,]
        def get(self, request, *args, **kwargs ):
    		...
    ```

- **全局使用**

    ```python
    REST_FRAMEWORK = {
        "DEFAULT_THROTTLE_CLASSES":["api.utils.throttke.visitThrottle"],
        "DEFAULT_THROTTLE_RATES":{
            "节流规则1":"6/m"
        }
    }
    ```

```markdown
# 匿名和登陆用户可做区分,可以跟认证结合使用,也可以跟权限结合
```



### 原理  

#### views.py  

```python
import time
# 实际业务场景请存在缓存中,Django 提供缓存机制
VISIT_RECODE = {}
class VisitThrottle( object ):
    def __init__(self):
        self.history = None
        self.frequency_time = 10    # 访问时间长度
        self.frequency_num = 3      # 访问次数

    def allow_request(self, request, view):
        # 获取用户 IP
        # remote_addr = request.META.get('REMOTE_ADDR')
        remote_addr = self.get_ident( request )   # 基类提供的方法

        ctime = time.time()
        if remote_addr not in VISIT_RECODE:
            # 不在 IP 列表中
            VISIT_RECODE[remote_addr] = [ctime,]
        history = VISIT_RECODE.get( remote_addr )
        self.history = history
        while history and history[-1] < ctime - self.frequency_time :
            history.pop()           # 清除历史几率记录
        if len( history ) < self.frequency_num:
            history.insert(0,ctime)
            return True
        return False            # 返回错误信息 {"detail": "Request was throttled."}

    def wait(self):
        # 你再等待多久就可以访问
        ctime = time.time()
        return self.frequency_time - ( ctime - self.history[-1] )


class UsersView2( APIView ):
    throttle_classes = [VisitThrottle,]
    def get(self, request, *args, **kwargs ):
		...
```

#### 全局配置

```python
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES":[
        # 要写完整的地址
        "api.utils.throttle.MyPermission",
    ],
}
```









### 内置 SimpleRateThrottle 类使用

####  源码流程

```python
__init__() --开发者是否自己写了rate函数,没有则调用自身 -->  get_rate()
--开者自定义映射值--> scope --> self.THROTTLE_RATES[scope]取值
--> setting中查找映射 -->返回限制频率  --> parse_rate() --对返回的字符串进行切分> num_requests,duration --> 
--> allow_request() --自己实现> get_cache_key() --> 返回缓存存储键
--存储进默认缓存>  self.cache.get()  --记录时间> self.history
--自己实现> wait() --超出访问频率> 抛出异常
```

```mermaid
graph TD
A("BaseThrottle") -->|继承|B(SimpleRateThrottle)
B -->|初始化| C("__init__()")
C -->|检查开发者是否自己写了rate函数,没有则调用自身|C1("get_rate()")
C1 -->|开者自定义映射值|C12("self.scope")
C12 -->|取值|C13("self.THROTTLE_RATES[scope]")
C13 -->|查找映射,返回限制频率|C14("setting")
C14 -->|限制频率的字符串|C2
C -->|开发者自己写了rate函数|C2("parse_rate()")
C2 -->|对返回的字符串进行切分,返回元组|C21("num_requests,duration")
C21 -->D
C -->D("allow_request()")
D -->|自己实现,返回缓存存储键|E("get_cache_key()")
E -->|存储进默认缓存|D1("self.history = self.cache.get()")
D -->|重写该函数|F("wait()")
F -->|超出频率|G("抛出异常")
```





#### 使用

##### views.py

```python
class VisitThrottle3( SimpleRateThrottle ):
    scope = "节流规则1"

    def get_cache_key(self, request, view):
        return self.get_ident( request )		# 匿名用户的获取限制
    
class VisitThrottle31( SimpleRateThrottle ):
    scope = "节流规则2"

    def get_cache_key(self, request, view):
        return request.user.username			# 利用用户名进行获取限制
```

##### setting.py

```python
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES":["api.utils.throttke.visitThrottle"],
    "DEFAULT_THROTTLE_RATES":{
        "节流规则1":"6/m"
    }
}
```



## 5. 版本控制

### 基于url的 get 传参方式

#### 基于 BaseVersioning 类

##### urls.py

```python
# 项目 urls.py
url( r'^api_test/', include("api_2_version.urls") )

# 应用 urls.py
url(r'^users/$', api_views.UserView.as_view() ),
```

##### views.py

```python
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.
from rest_framework.versioning import QueryParameterVersioning,BaseVersioning
class ParamsVision( object ):
    def determine_version(self, request, *args, **kwargs):
        version = request.query_params.get("version")
        return version


class UserView( APIView ):
    authentication_classes = []
    versioning_class = ParamsVision
    def get(self, request, *args, **kwargs):
        print( request.version )            # 获取版本
        print( request.versioning_scheme )  # # 获取版本管理的类
        return JsonResponse({"version":request.version})

```



#### 基于 QueryParameterVersioning 类

##### settings.py

```python
REST_FRAMEWORK = {
    # 版本控制
    "DEFAULT_VERSION":"v1",
    "ALLOWED_VERSIONS":['v1','v2'],                 # 允许访问的版本号
    "VERSION_PARAM":"version",                      # 默认也是version
}
```

##### views.py

```python
class UserView( APIView ):
    authentication_classes = []
    # versioning_class = ParamsVision
    versioning_class = QueryParameterVersioning
    def get(self, request, *args, **kwargs):
        print( request.version )                # 获取版本
        print( request.versioning_scheme )      # # 获取版本管理的类
        return JsonResponse({"version":request.version})

```



### 基于 url 的正则方式(推荐)

#### 基于 URLPathVersioning 类

##### urls.py

```python
# 在 url 中对版本信息进行控制,拿到的版本信息也是存在 request.version 中
url(r'^(?P<version>[v1|v2]+)/users/', api_views.UserView.as_view() ),
```

##### views.py

```python
from rest_framework.versioning import URLPathVersioning
class UserView( APIView ):
    versioning_class = URLPathVersioning        # 基于 url 的正则方式
    def get(self, request, *args, **kwargs):
        print( request.version )                # 获取版本
        print( request.versioning_scheme )      # # 获取版本管理的类
        print( request.versioning_scheme.reverse(viewname="vision_reserve_test",request=request) )
        # http://127.0.0.1:8000/api_test/v2/users/
        # 使用该方法必须在给该 url 起个别名
        # url(r'^(?P<version>[v1|v2]+)/users/', api_views.UserView.as_view(),name="vision_reserve_test" ),
        return JsonResponse({"version":request.version})

```



### 全局配置版本

```python
# settings.py
REST_FRAMEWORK = {
    # 版本控制
    "DEFAULT_VERSIONING_CLASS":" rest_framework.versioning.URLPathVersioning",
    # 有上面一条就不需要下面的了
    # "DEFAULT_VERSION":"v1",
    # "ALLOWED_VERSIONS":['v1','v2'],                 # 允许访问的版本号
    # "VERSION_PARAM":"version",                      # 默认也是version
}
```



### url 反向生成器

#### Django 自带的

##### urls.py

```python
urlpatterns = [
   url(r'^(?P<version>[v1|v2]+)/users/', api_views.UserView.as_view(),name="vision_reserve_test" ),
]
```

##### views.py

```python
# django 自带的反向生成机制
from django.urls import reverse
print( reverse( viewname="vision_reserve_test", kwargs={ "version":"1django" } ) )
```



#### restframework 框架的

##### urls.py

```python
urlpatterns = [
   url(r'^(?P<version>[v1|v2]+)/users/', api_views.UserView.as_view(),name="vision_reserve_test" ),
]
```

##### views.py

```python
print( request.versioning_scheme.reverse(viewname="vision_reserve_test",request=request) )
# http://127.0.0.1:8000/api_test/v2/users/
```

##### 源码流程

```mermaid
graph TD
A(URLPathVersioning类) -->|执行| A1("reverse()")
A1 -->|继承 super| B("BaseVersioning类")
B --> B1("reverse()")
B1 --> B11("_reverse()")
B11 -->|调用的还是 django的方法 | B12("django_reverse()")
```





## 6. 解析器

> 对请求体的数据进行解析

### 准备知识

#### request.PODT/request.body

要想在 Django 服务端的 `request.POST` 中有值，必需满足以下要求:

- **请求头要求:**

    ```python
    Content-Type:'application/x-www-form-urlencoded'
    ```

- **数据格式要求:**

    ```python
    name=王老六&age=18&gender=男
    ```

##### 正常情况

###### 方式一: 表单

```html
<form>
    input...
</form>
默认带的头就是 Content-Type:'application/x-www-form-urlencoded'  
默认的数据库就是 name=王老六&age=18&gender=男
```

###### 方式二: ajax

```javascript
$.ajax({
    url:...,
    type:POST,
    data:{name:"王老六",age }
})
// 在内部也会将数据进行转化,并带上请求头给服务端传送过去
```



##### 特殊情况

###### 特殊情况一:

```javascript
// request.POST无值, request.body 有值
$.ajax({
    url:...,
    type:POST,
        headers:{'Content-Type':'application/json'}	 // 自定义请求头
    data:{name:"王老六",age:18 }			// 在内部也会将数据进行转化
})
```

###### 特殊情况二:

```javascript
// request.POST无值, request.body 有值
$.ajax({
    url:...,
    type:POST,
        headers:{'Content-Type':'application/json'}	 // 自定义请求头
    data:JSON.stringfy({name:"王老六",age:18 })		// 数据格式改变
})

// 服务端处理: json.loads( request.body )
```



### 使用

> 如果同时使用多个 `parser `时， `rest framework` 会根据请求头 `content-type` 自动进行比对，并使用对应 `parser`

#### 处理正常表单和ajax请求

> 仅处理请求头 `content-type` 为 `application/x-www-form-urlencoded` 的请求体

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser

class TestView(APIView):
    parser_classes = [FormParser, ]				# 只要加上它就好了
    def post(self, request, *args, **kwargs):
        print(request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)

        return Response('POST请求，响应内容')
```



#### 处理Json 数据请求头

> 仅处理请求头 `content-type` 为 `application/json` 的请求体

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import FormParser

class TestView(APIView):
    parser_classes = [JSONParser, ]					# 只要加上它就好了
    def post(self, request, *args, **kwargs):
        print(request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)

        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')
```



#### 处理二进制数据

> 仅处理请求头 `content-type` 为 `multipart/form-data` 的请求体

##### html文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="http://127.0.0.1:8000/test/" method="post" enctype="multipart/form-data">
    <input type="text" name="user" />
    <input type="file" name="img">
    <input type="submit" value="提交">
</form>
</body>
</html>
```

##### views.py

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import MultiPartParser


class TestView(APIView):
    parser_classes = [MultiPartParser, ]

    def post(self, request, *args, **kwargs):
        print(request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')
```



#### 仅上传文件

##### html文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="http://127.0.0.1:8000/test/f1.numbers" method="post" enctype="multipart/form-data">
    <input type="text" name="user" />
    <input type="file" name="img">
    <input type="submit" value="提交">
</form>
</body>
</html>
```

##### urls.py

```python
from django.conf.urls import url, include
from web.views import TestView
urlpatterns = [
    url(r'test/(?P<filename>[^/]+)', TestView.as_view(), name='test'),
]
```

##### views.py

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import FileUploadParser


class TestView(APIView):
    parser_classes = [FileUploadParser, ]
    def post(self, request, filename, *args, **kwargs):
        print(filename)
        print(request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print(request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print(request.POST)
        print(request.FILES)
        return Response('POST请求，响应内容')
```



### 全局配置

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES':[
        'rest_framework.parsers.JSONParser'
        'rest_framework.parsers.FormParser'
        'rest_framework.parsers.MultiPartParser'
    ]
}
```



### 原理讲解

#### 本质

##### 预备知识

- 请求头

- 状态码
- 请求方法

#### 源码流程

1. 获取用户请求
2. 获取用户请求体
3. 根据用户请求头 和 `parser_classes `中支持的请求头进行比较  
4. JSONParser 对象去解析请求体  
5. `request.data` 提取请求内容  








## 7.序列化(*)

- 请求数据进行校验
- 对 `QuerySet` 进行序列化







## 8.分页(*)



## 9. 路由系统(*)



## 10. 视图(*)



## 11.渲染器





# rest framework 下的 Django 生命周期

```python
as_view()  --> super().as_view()  --> view()  --> dispatch()
```





# rest framework 源码阅读

## dispatch()

```python
def dispatch(self, request, *args, **kwargs):
	self.args = args
	self.kwargs = kwargs
	# 修改原有的 request，　对原生进行加工
	request = self.initialize_request(request, *args, **kwargs)
	self.request = request
	self.headers = self.default_response_headers  # deprecate?

	try:
		self.initial(request, *args, **kwargs)
		# --begin--: Django 原有的代码 
		if request.method.lower() in self.http_method_names:
			handler = getattr(
                self, request.method.lower(),
                self.http_method_not_allowed 
            )
		else:
			handler = self.http_method_not_allowed
		# -- end --: Django 原有的代码 
		response = handler(request, *args, **kwargs) 

	except Exception as exc:
		response = self.handle_exception(exc)

	self.response = self.finalize_response(request, response, *args, **kwargs)
	return self.response
```



###　initialize_request()

```python
# 对原生 request 进行封装  
def initialize_request(self, request, *args, **kwargs):
    parser_context = self.get_parser_context(request)
    return Request(
        request,
        # self 都是先从自身找,再去父类找,即 TestView --> APIView --> View
        parsers=self.get_parsers(),
        authenticators=self.get_authenticators(),	# [Foo(),Bar()]
        negotiator=self.get_content_negotiator(),
        parser_context=parser_context
    )
#　self._request = request　获取原生　request：　request.＿request
```

#### get_authenticators()

```python
def get_authenticators(self):
    """ 实例化并返回此视图可以使用的身份验证器列表。  """
    # self.authentication_classes = [Foo,Bar]
    return [auth() for auth in self.authentication_classes]
	# restframework 的配置文件
```



### initial()

```python
def initial(self, request, *args, **kwargs):
    """
    运行在调用方法处理程序之前需要发生的任何事情。
    """
    self.format_kwarg = self.get_format_suffix(**kwargs)
    # 执行内容协商并在请求上存储接受的信息
    neg = self.perform_content_negotiation(request)
    request.accepted_renderer, request.accepted_media_type = neg

    # 确定API版本（如果正在使用版本控制）。(版本信息和版本类对象)
    version, scheme = self.determine_version(request, *args, **kwargs)
    request.version, request.versioning_scheme = version, scheme

    # 用户认证
    self.perform_authentication(request)
    # 权限认证
    self.check_permissions(request)
    # 访问频率
    self.check_throttles(request)
```

#### perform_authentication()

> 登陆认证

```python
def perform_authentication(self, request):
    request.user		# 封装后的 Request
```

##### request.user

```python
@property
def user(self):
    if not hasattr(self, '_user'):
        with wrap_attributeerrors():
            self._authenticate()
    return self._user

@user.setter
def user(self, value):
    self._user = value
    self._request.user = value
```

###### _authenticate()

```python
def _authenticate(self):
    #　self.authenticators -->　request 里加工的值
    for authenticator in self.authenticators:
        try:
            # authenticator.authenticate(self) 认证是否已经登陆
            user_auth_tuple = authenticator.authenticate(self)
        except exceptions.APIException:
            self._not_authenticated()
            raise

        if user_auth_tuple is not None:
            self._authenticator = authenticator
            self.user, self.auth = user_auth_tuple
            return

    self._not_authenticated()
```

######   _not_authenticated()

```python
def _not_authenticated(self):
    """给 request.user 和 request.auth 赋默认值"""
    self._authenticator = None

    if api_settings.UNAUTHENTICATED_USER:				# 修改它即可
        self.user = api_settings.UNAUTHENTICATED_USER() # AnonmousUser
    else:
        self.user = None

    if api_settings.UNAUTHENTICATED_TOKEN:
        self.auth = api_settings.UNAUTHENTICATED_TOKEN() # None
        else:
            self.auth = None
```



####　check_permissions()

> 权限认证

```python
def check_permissions(self, request):
    """检查是否应允许该请求。如果不允许该请求，则引发适当的异常。"""
    for permission in self.get_permissions():
        # 权限验证通过,不执行任何操作
        if not permission.has_permission(request, self):
            # 权限验证不通过, 抛出异常
            self.permission_denied(
                request, message=getattr(permission, 'message', None)
            )
```

##### get_permissions()

```python
def get_permissions(self):
    """实例化并返回此视图所需的权限列表。"""
    return [permission() for permission in self.permission_classes]
```

##### permission_denied()

```python
def permission_denied(self, request, message=None):
    """如果不允许请求，请确定要提出哪种异常。"""
    if request.authenticators and not request.successful_authenticator:
        raise exceptions.NotAuthenticated()
    raise exceptions.PermissionDenied(detail=message)
```

####　check_throttles()

```python
def check_throttles(self, request):
    throttle_durations = []
    for throttle in self.get_throttles():
        if not throttle.allow_request(request, self):
            throttle_durations.append(throttle.wait())

     if throttle_durations:
        durations = [
            duration for duration in throttle_durations
            if duration is not None
        ]

        duration = max(durations, default=None)
        self.throttled(request, duration)
```

##### get_throttles():

```python
    def get_throttles(self):
        return [throttle() for throttle in self.throttle_classes]
```



#### determine_version()

```python
    def determine_version(self, request, *args, **kwargs):
        """如果正在使用版本控制，则确定该版本的任何API版本
         传入请求。返回的两元组（版本，versioning_scheme）
        """
        if self.versioning_class is None:
            return (None, None)
        
        # 处理版本类对象, URLPathVersioning对象 
        scheme = self.versioning_class()
        # 返回 (版本信息,版本类对象)
        return (scheme.determine_version(request, *args, **kwargs), scheme)

```





## Request 的封装

```python
class Request:
    def __init__(self, request, parsers=None, authenticators=None,
                 negotiator=None, parser_context=None):
        assert isinstance(request, HttpRequest), (
            'The `request` argument must be an instance of '
            '`django.http.HttpRequest`, not `{}.{}`.'
            .format(request.__class__.__module__, request.__class__.__name__)
        )

        self._request = request
        self.parsers = parsers or ()
        self.authenticators = authenticators or ()
        self.negotiator = negotiator or self._default_negotiator()
        self.parser_context = parser_context
        self._data = Empty
        self._files = Empty
        self._full_data = Empty
        self._content_type = Empty
        self._stream = Empty

        if self.parser_context is None:
            self.parser_context = {}
        self.parser_context['request'] = self
        self.parser_context['encoding'] = request.encoding or settings.DEFAULT_CHARSET

        force_user = getattr(request, '_force_auth_user', None)
        force_token = getattr(request, '_force_auth_token', None)
        if force_user is not None or force_token is not None:
            forced_auth = ForcedAuthentication(force_user, force_token)
            self.authenticators = (forced_auth,)

    def _default_negotiator(self):
        return api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS()

    @property
    def content_type(self):
        meta = self._request.META
        return meta.get('CONTENT_TYPE', meta.get('HTTP_CONTENT_TYPE', ''))

    @property
    def stream(self):
        """返回可以用于流式传输请求内容的对象。"""
        if not _hasattr(self, '_stream'):
            self._load_stream()
        return self._stream

    @property
    def query_params(self):
        """request.GET的语义上更正确的名称。"""
        return self._request.GET

    @property
    def data(self):
        if not _hasattr(self, '_full_data'):
            self._load_data_and_files()
        return self._full_data

    @property
    def user(self):
        """返回与当前请求关联的用户，经过身份验证"""
        if not hasattr(self, '_user'):
            with wrap_attributeerrors():
                self._authenticate()
        return self._user

    @user.setter
    def user(self, value):
        self._user = value
        self._request.user = value

    @property
    def auth(self):
        if not hasattr(self, '_auth'):
            with wrap_attributeerrors():
                self._authenticate()
        return self._auth

    @auth.setter
    def auth(self, value):
        self._auth = value
        self._request.auth = value

    @property
    def successful_authenticator(self):
        if not hasattr(self, '_authenticator'):
            with wrap_attributeerrors():
                self._authenticate()
        return self._authenticator

    def _load_data_and_files(self):
        if not _hasattr(self, '_data'):
            self._data, self._files = self._parse()
            if self._files:
                self._full_data = self._data.copy()
                self._full_data.update(self._files)
            else:
                self._full_data = self._data

            # if a form media type, copy data & files refs to the underlying
            # http request so that closable objects are handled appropriately.
            if is_form_media_type(self.content_type):
                self._request._post = self.POST
                self._request._files = self.FILES

    def _load_stream(self):
        meta = self._request.META
        try:
            content_length = int(
                meta.get('CONTENT_LENGTH', meta.get('HTTP_CONTENT_LENGTH', 0))
            )
        except (ValueError, TypeError):
            content_length = 0

        if content_length == 0:
            self._stream = None
        elif not self._request._read_started:
            self._stream = self._request
        else:
            self._stream = io.BytesIO(self.body)

    def _supports_form_parsing(self):
        form_media = (
            'application/x-www-form-urlencoded',
            'multipart/form-data'
        )
        return any([parser.media_type in form_media for parser in self.parsers])

    def _parse(self):
        media_type = self.content_type
        try:
            stream = self.stream
        except RawPostDataException:
            if not hasattr(self._request, '_post'):
                raise
            # If request.POST has been accessed in middleware, and a method='POST'
            # request was made with 'multipart/form-data', then the request stream
            # will already have been exhausted.
            if self._supports_form_parsing():
                return (self._request.POST, self._request.FILES)
            stream = None

        if stream is None or media_type is None:
            if media_type and is_form_media_type(media_type):
                empty_data = QueryDict('', encoding=self._request._encoding)
            else:
                empty_data = {}
            empty_files = MultiValueDict()
            return (empty_data, empty_files)

        parser = self.negotiator.select_parser(self, self.parsers)

        if not parser:
            raise exceptions.UnsupportedMediaType(media_type)

        try:
            parsed = parser.parse(stream, media_type, self.parser_context)
        except Exception:
            # If we get an exception during parsing, fill in empty data and
            # re-raise.  Ensures we don't simply repeat the error when
            # attempting to render the browsable renderer response, or when
            # logging the request or similar.
            self._data = QueryDict('', encoding=self._request._encoding)
            self._files = MultiValueDict()
            self._full_data = self._data
            raise

        # Parser classes may return the raw data, or a
        # DataAndFiles object.  Unpack the result as required.
        try:
            return (parsed.data, parsed.files)
        except AttributeError:
            empty_files = MultiValueDict()
            return (parsed, empty_files)

    def _authenticate(self):
        """
        Attempt to authenticate the request using each authentication instance
        in turn.
        """
        for authenticator in self.authenticators:
            try:
                user_auth_tuple = authenticator.authenticate(self)
            except exceptions.APIException:
                self._not_authenticated()
                raise

            if user_auth_tuple is not None:
                self._authenticator = authenticator
                self.user, self.auth = user_auth_tuple
                return

        self._not_authenticated()

    def _not_authenticated(self):
        """
        Set authenticator, user & authtoken representing an unauthenticated request.

        Defaults are None, AnonymousUser & None.
        """
        self._authenticator = None

        if api_settings.UNAUTHENTICATED_USER:
            self.user = api_settings.UNAUTHENTICATED_USER()
        else:
            self.user = None

        if api_settings.UNAUTHENTICATED_TOKEN:
            self.auth = api_settings.UNAUTHENTICATED_TOKEN()
        else:
            self.auth = None

    def __getattr__(self, attr):
        """
        If an attribute does not exist on this instance, then we also attempt
        to proxy it to the underlying HttpRequest object.
        """
        try:
            return getattr(self._request, attr)
        except AttributeError:
            return self.__getattribute__(attr)

    @property
    def DATA(self):
        raise NotImplementedError(
            '`request.DATA` has been deprecated in favor of `request.data` '
            'since version 3.0, and has been fully removed as of version 3.2.'
        )

    @property
    def POST(self):
        # Ensure that request.POST uses our request parsing.
        if not _hasattr(self, '_data'):
            self._load_data_and_files()
        if is_form_media_type(self.content_type):
            return self._data
        return QueryDict('', encoding=self._request._encoding)

    @property
    def FILES(self):
        # Leave this one alone for backwards compat with Django's request.FILES
        # Different from the other two cases, which are not valid property
        # names on the WSGIRequest class.
        if not _hasattr(self, '_files'):
            self._load_data_and_files()
        return self._files

    @property
    def QUERY_PARAMS(self):
        raise NotImplementedError(
            '`request.QUERY_PARAMS` has been deprecated in favor of `request.query_params` '
            'since version 3.0, and has been fully removed as of version 3.2.'
        )

    def force_plaintext_errors(self, value):
        # Hack to allow our exception handler to force choice of
        # plaintext or html error responses.
        self._request.is_ajax = lambda: value

```

### data()

```python
@property
def data(self):
    if not _hasattr(self, '_full_data'):
        self._load_data_and_files()
    return self._full_data
```

#### _load_data_and_files()

```python
def _load_data_and_files(self):
    """Parses the request content into `self.data`."""
    if not _hasattr(self, '_data'):
        self._data, self._files = self._parse()
        if self._files:
            self._full_data = self._data.copy()
            self._full_data.update(self._files)
        else:
            self._full_data = self._data

        # if a form media type, copy data & files refs to the underlying
        # http request so that closable objects are handled appropriately.
        if is_form_media_type(self.content_type):
            self._request._post = self.POST
            self._request._files = self.FILES
```

#####　_parse()

```python
def _parse(self):
    """解析请求内容，返回两个（数据，文件）
    可能会引发“ UnsupportedMediaType”或“ ParseError”异常。
    """
    media_type = self.content_type # 用户提交的content_type的值
    try:
        stream = self.stream
    except RawPostDataException:
        if not hasattr(self._request, '_post'):
            raise
        if self._supports_form_parsing():
            return (self._request.POST, self._request.FILES)
        stream = None

        if stream is None or media_type is None:
            if media_type and is_form_media_type(media_type):
                empty_data = QueryDict('', encoding = self._request._encoding )
            else:
                empty_data = {}
            empty_files = MultiValueDict()
            return (empty_data, empty_files)

        # 选择解析器, self 是请求对象
        parser = self.negotiator.select_parser(self, self.parsers)

        if not parser:
            raise exceptions.UnsupportedMediaType(media_type)

        try:
            parsed = parser.parse(stream, media_type, self.parser_context )
        except Exception:
            self._data = QueryDict('', encoding= self._request._encoding )
            self._files = MultiValueDict()
            self._full_data = self._data
            raise

        try:
            return (parsed.data, parsed.files)
        except AttributeError:
            empty_files = MultiValueDict()
            return (parsed, empty_files)
```

###### select_parser()

```python
def select_parser(self, request, parsers):
    for parser in parsers:
        if media_type_matches(parser.media_type, request.content_type):
            return parser
    return None
```





## 内置认证类
> 自己在写认证的时候, 最后也继承 `BaseAuthentication`

### BaseAuthentication
```python
class BaseAuthentication:
    def authenticate(self, request):
		"""具体做认证的方法,必需重写,默认抛出异常"""
        raise NotImplementedError(".authenticate() must be overridden.")

    def authenticate_header(self, request):
        """认证失败的时候给用户浏览器返回的响应头"""
        pass
```


### BasicAuthentication
```python
class BasicAuthentication(BaseAuthentication):
    """浏览器封装的针对用户名/密码的HTTP基本身份验证,加密后放到一个请求头里给服务端发过去。一般不用"""
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """如果提供了正确的用户名和密码，则返回“用户” 否则返回“无”。"""
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'basic':
            return None

        if len(auth) == 1:
            msg = _('Invalid basic header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid basic header. Credentials string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')
        except (TypeError, UnicodeDecodeError, binascii.Error):
            msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
            raise exceptions.AuthenticationFailed(msg)

        userid, password = auth_parts[0], auth_parts[2]
        return self.authenticate_credentials(userid, password, request)

    def authenticate_credentials(self, userid, password, request=None):
        """根据用户名和密码对用户标识和密码进行身份验证。"""
        credentials = {
            get_user_model().USERNAME_FIELD: userid,
            'password': password
        }
        user = authenticate(request=request, **credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (user, None)

    def authenticate_header(self, request):
        return 'Basic realm="%s"' % self.www_authenticate_realm
```


### SessionAuthentication
```python
class SessionAuthentication(BaseAuthentication):
    """使用Django的会话框架进行身份验证。"""
    def authenticate(self, request):
        """如果请求会话当前有一个登录用户，则返回一个“用户”。否则返回“无”。"""

        # 从基础HttpRequest对象获取基于会话的用户
        user = getattr(request._request, 'user', None)

        # 未经身份验证，不需要CSRF验证
        if not user or not user.is_active:
            return None

        self.enforce_csrf(request)

        # CSRF已通过身份验证的用户
        return (user, None)

    def enforce_csrf(self, request):
        """对基于会话的身份验证强制执行CSRF验证。"""
        check = CSRFCheck()
        # populates request.META['CSRF_COOKIE'], which is used in process_view()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)
```


### TokenAuthentication
```python
class TokenAuthentication(BaseAuthentication):
    """基于简单令牌的身份验证。客户应通过在“授权”中传递令牌密钥进行身份验证HTTP标头，以字符串“ Token”开头For example:
        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """
    keyword = 'Token'
    model = None

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        return Token

    """可以使用自定义令牌模型，但必须具有以下属性。
     * key-标识令牌的字符串
     * 用户-令牌所属的用户
    """

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (token.user, token)

    def authenticate_header(self, request):
        return self.keyword
```



### RemoteUserAuthentication
```python
class RemoteUserAuthentication(BaseAuthentication):
    """
    REMOTE_USER authentication.

    To use this, set up your web server to perform authentication, which will
    set the REMOTE_USER environment variable. You will need to have
    'django.contrib.auth.backends.RemoteUserBackend in your
    AUTHENTICATION_BACKENDS setting
    """

    # Name of request header to grab username from.  This will be the key as
    # used in the request.META dictionary, i.e. the normalization of headers to
    # all uppercase and the addition of "HTTP_" prefix apply.
    header = "REMOTE_USER"

    def authenticate(self, request):
        user = authenticate(remote_user=request.META.get(self.header))
        if user and user.is_active:
            return (user, None)
```





## 内置权限类

```python
from rest_framework.permissions import BasePermission
```

### BasePermission类

```python
class BasePermission(metaclass=BasePermissionMetaclass):
    """所有权限类都应从中继承的基类。"""
    def has_permission(self, request, view):
        """如果授予许可，则返回True，否则返回False。"""
        return True

    def has_object_permission(self, request, view, obj):
        """如果授予许可，则返回True，否则返回False。"""
        return True
```

### AllowAny 类

```python
class AllowAny(BasePermission):
    """允许所有人"""
    def has_permission(self, request, view):
        return True
```

### IsAuthenticated 类

```python
class IsAuthenticated(BasePermission):
    """只允许经过身份验证的用户访问。"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
```



## 内置节流类
```python
from rest_framework.throttling import BaseThrottle
```

### BaseThrottle

```python
class BaseThrottle:
    def allow_request(self, request, view):
        """如果应允许该请求，则返回True，否则返回False。"""
        raise NotImplementedError('.allow_request() must be overridden')

    def get_ident(self, request):
        xff = request.META.get('HTTP_X_FORWARDED_FOR')	# 用户所经历代理
        remote_addr = request.META.get('REMOTE_ADDR')   # 获取访问 IP 
        num_proxies = api_settings.NUM_PROXIES

        if num_proxies is not None:
            if num_proxies == 0 or xff is None:
                return remote_addr
            addrs = xff.split(',')
            client_addr = addrs[-min(num_proxies, len(addrs))]
            return client_addr.strip()

        return ''.join(xff.split()) if xff else remote_addr

    def wait(self):
        return None
```



### SimpleRateThrottle

```python
class SimpleRateThrottle(BaseThrottle):
    cache = default_cache
    timer = time.time
    cache_format = 'throttle_%(scope)s_%(ident)s'
    scope = None
    THROTTLE_RATES = api_settings.DEFAULT_THROTTLE_RATES

    def __init__(self):
        if not getattr(self, 'rate', None):		# 开发者是否有重写方法
            self.rate = self.get_rate()			# 没有则调用框架自身的
        self.num_requests, self.duration = self.parse_rate(self.rate)

    def get_cache_key(self, request, view):
        """Must be overridden.开发者必须重写该方法"""
        raise NotImplementedError('.get_cache_key() must be overridden')

    def get_rate(self):
        """确定允许的请求速率的字符串表示形式,例如: 3/m 一分钟3次"""
        if not getattr(self, 'scope', None):# 查看用户是否有自定义代表脸
            msg = ("You must set either `.scope` or `.rate` for '%s' throttle" % self.__class__.__name__)
            raise ImproperlyConfigured(msg)		# 没有则报错

        try:
            # 配置文件中去查找映射
            return self.THROTTLE_RATES[self.scope]
        except KeyError:
            msg = "No defaul  
            raise ImproperlyConfigured(msg)

    def parse_rate(self, rate):
        """给定请求率字符串，返回两个元组：<允许的请求数>，<以秒为单位的时间段>"""
        if rate is None:
            return (None, None)
        num, period = rate.split('/')
        num_requests = int(num)
        duration = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}[period[0]]
        return (num_requests, duration)

    def allow_request(self, request, view):
        """一般需要用户自己重写"""
        if self.rate is None:		# 没设置访问频率限制
            return True

        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True

        self.history = self.cache.get(self.key, [])		
        # 调用django内置的缓存
        self.now = self.timer()	# 获取当前时间 timer = time.time

        # Drop any requests from the history which have now passed the
        # throttle duration
        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) >= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()

    def throttle_success(self):
        """插入当前请求的时间戳和键进入缓存。
        """
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True

    def throttle_failure(self):
        """当由于限制而对API的请求失败时调用。"""
        return False

    def wait(self):
        """
        Returns the recommended next request time in seconds.
        """
        if self.history:
            remaining_duration = self.duration - (self.now - self.history[-1])
        else:
            remaining_duration = self.duration

        available_requests = self.num_requests - len(self.history) + 1
        if available_requests <= 0:
            return None

        return remaining_duration / float(available_requests)
```

### AnonRateThrottle

```python
class AnonRateThrottle(SimpleRateThrottle):
    """限制匿名用户可能进行的API调用的速率。请求的IP地址将用作唯一的缓存密钥。"""
    scope = 'anon'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return None  # Only throttle unauthenticated requests.

        # 多做了一部字符串格式化
        # cache_format = 'throttle_%(scope)s_%(ident)s'
        return self.cache_format % {
            'scope': self.scope,
            'ident': self.get_ident(request)
        }

```



## 内置版本控制类

### BaseVersioning 类

```python
class BaseVersioning:
    # 配置文件参数
    default_version = api_settings.DEFAULT_VERSION
    allowed_versions = api_settings.ALLOWED_VERSIONS
    version_param = api_settings.VERSION_PARAM

    def determine_version(self, request, *args, **kwargs):
        # 重写该方法,用以获取版本信息,默认抛出异常
        msg = '{cls}.determine_version() must be implemented.'
        raise NotImplementedError(msg.format(
            cls=self.__class__.__name__
        ))

    def reverse(self, viewname, args=None, kwargs=None, request=None, format=None, **extra):
        # 反向生成 url
        return _reverse(viewname, args, kwargs, request, format, **extra)

    def is_allowed_version(self, version):
        if not self.allowed_versions:
            return True
        return ((version is not None and version == self.default_version) or
                (version in self.allowed_versions))

```



### QueryParameterVersioning 类

```python
class QueryParameterVersioning(BaseVersioning):
    """
    GET /something/?version=0.1 HTTP/1.1
    Host: example.com
    Accept: application/json
    """
    invalid_version_message = _('Invalid version in query parameter.')

    def determine_version(self, request, *args, **kwargs):
        # 获取版本信息
        version = request.query_params.get(self.version_param, self.default_version)
        if not self.is_allowed_version(version):
            raise exceptions.NotFound(self.invalid_version_message)
        return version

    def reverse(self, viewname, args=None, kwargs=None, request=None, format=None, **extra):
        # 反向生成 url
        url = super().reverse(
            viewname, args, kwargs, request, format, **extra
        )
        if request.version is not None:
            return replace_query_param(url, self.version_param, request.version)
        return url

```



### URLPathVersioning 类

```python
class URLPathVersioning(BaseVersioning):
    """
    An example URL conf for two views that accept two different versions.
    urlpatterns = [
        url(r'^(?P<version>[v1|v2]+)/users/$', users_list, name='users-list'),
        url(r'^(?P<version>[v1|v2]+)/users/(?P<pk>[0-9]+)/$', users_detail, name='users-detail')
    ]

    GET /1.0/something/ HTTP/1.1
    Host: example.com
    Accept: application/json
    """
    invalid_version_message = _('Invalid version in URL path.')

    def determine_version(self, request, *args, **kwargs):
        version = kwargs.get(self.version_param, self.default_version)
        if version is None:
            version = self.default_version

        if not self.is_allowed_version(version):
            raise exceptions.NotFound(self.invalid_version_message)
        return version

    def reverse(self, viewname, args=None, kwargs=None, request=None, format=None, **extra):
        if request.version is not None:
            kwargs = {} if (kwargs is None) else kwargs
            kwargs[self.version_param] = request.version

        return super().reverse(
            viewname, args, kwargs, request, format, **extra
        )
```



### HostNameVersioning 类

```python
class HostNameVersioning(BaseVersioning):
    """
    GET /something/ HTTP/1.1
    Host: v1.example.com
    Accept: application/json
    """
    hostname_regex = re.compile(r'^([a-zA-Z0-9]+)\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
    invalid_version_message = _('Invalid version in hostname.')

    def determine_version(self, request, *args, **kwargs):
        hostname, separator, port = request.get_host().partition(':')
        match = self.hostname_regex.match(hostname)
        if not match:
            return self.default_version
        version = match.group(1)
        if not self.is_allowed_version(version):
            raise exceptions.NotFound(self.invalid_version_message)
        return version

    # ＃我们不需要实现`reverse`，因为主机名已经是保留为REST框架“反向”实现的一部分。
```



### AcceptHeaderVersioning 类

```python
class AcceptHeaderVersioning(BaseVersioning):
    """版本信息放在请求头里
    GET /something/ HTTP/1.1
    Host: example.com
    Accept: application/json; version=1.0
    """
    invalid_version_message = _('Invalid version in "Accept" header.')

    def determine_version(self, request, *args, **kwargs):
        media_type = _MediaType(request.accepted_media_type)
        version = media_type.params.get(self.version_param, self.default_version)
        version = unicode_http_header(version)
        if not self.is_allowed_version(version):
            raise exceptions.NotAcceptable(self.invalid_version_message)
        return version

    # 我们不需要实现`reverse`，因为版本控制是基于在`Accept`标头上，而不是在请求URL上。
```



## 内置解析器

### BaseParser 类

```python
class BaseParser:
    """所有解析器都应该扩展BaseParser，并指定一个media_type。属性，并覆盖`.parse（）`方法。
    """
    media_type = None
    def parse(self, stream, media_type=None, parser_context=None):
        """给定要读取的流，返回解析的表示形式。
         应该返回已解析的数据，或者返回包含以下内容的“ DataAndFiles”对象：
         解析的数据和文件。
        """
        raise NotImplementedError(".parse() must be overridden.")
```

### JSONParser 类

```python
class JSONParser(BaseParser):
    media_type = 'application/json'
    renderer_class = renderers.JSONRenderer
    strict = api_settings.STRICT_JSON

    def parse(self, stream, media_type=None, parser_context=None):
        """将传入的字节流解析为JSON并返回结果数据。"""
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            decoded_stream = codecs.getreader(encoding)(stream)
            parse_constant = json.strict_constant if self.strict else None
            return json.load(decoded_stream, parse_constant=parse_constant)
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % str(exc))
```

### FormParser 类

```python
class FormParser(BaseParser):
    media_type = 'application/x-www-form-urlencoded'

    def parse(self, stream, media_type=None, parser_context=None):
        """将传入的字节流解析为URL编码形式，并返回结果QueryDict。"""
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        return QueryDict(stream.read(), encoding=encoding)
```

### MultiPartParser 类

```python
class MultiPartParser(BaseParser):
    media_type = 'multipart/form-data'

    def parse(self, stream, media_type=None, parser_context=None):
        """将传入的字节流解析为多部分编码形式，并返回一个DataAndFiles对象。
			.data将是包含所有表单参数的QueryDict。
         	.files将是一个包含所有表单文件的QueryDict。
        """
        parser_context = parser_context or {}
        request = parser_context['request']
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        meta = request.META.copy()
        meta['CONTENT_TYPE'] = media_type
        upload_handlers = request.upload_handlers

        try:
            parser = DjangoMultiPartParser(meta, stream, upload_handlers, encoding)
            data, files = parser.parse()
            return DataAndFiles(data, files)
        except MultiPartParserError as exc:
            raise ParseError('Multipart form parse error - %s' % str(exc))
```

### FileUploadParser 类

```python
class FileUploadParser(BaseParser):
    media_type = '*/*'
    errors = {
        'unhandled': 'FileUpload parse error - none of upload handlers can handle the stream',
        'no_filename': 'Missing filename. Request should include a Content-Disposition header with a filename parameter.',
    }

    def parse(self, stream, media_type=None, parser_context=None):
        """将传入的字节流视为原始文件上传并返回一个DataAndFiles对象。
			.data将为None（我们希望请求正文为文件内容）。
         	.files将是一个包含一个file元素的QueryDict。
         """
        parser_context = parser_context or {}
        request = parser_context['request']
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        meta = request.META
        upload_handlers = request.upload_handlers
        filename = self.get_filename(stream, media_type, parser_context)

        if not filename:
            raise ParseError(self.errors['no_filename'])
        content_type = meta.get('HTTP_CONTENT_TYPE',
                                meta.get('CONTENT_TYPE', ''))
        try:
            content_length = int(meta.get('HTTP_CONTENT_LENGTH',
                                          meta.get('CONTENT_LENGTH', 0)))
        except (ValueError, TypeError):
            content_length = None

        # See if the handler will want to take care of the parsing.
        for handler in upload_handlers:
            result = handler.handle_raw_input(stream,
                                              meta,
                                              content_length,
                                              None,
                                              encoding)
            if result is not None:
                return DataAndFiles({}, {'file': result[1]})

        # This is the standard case.
        possible_sizes = [x.chunk_size for x in upload_handlers if x.chunk_size]
        chunk_size = min([2 ** 31 - 4] + possible_sizes)
        chunks = ChunkIter(stream, chunk_size)
        counters = [0] * len(upload_handlers)

        for index, handler in enumerate(upload_handlers):
            try:
                handler.new_file(None, filename, content_type,
                                 content_length, encoding)
            except StopFutureHandlers:
                upload_handlers = upload_handlers[:index + 1]
                break

        for chunk in chunks:
            for index, handler in enumerate(upload_handlers):
                chunk_length = len(chunk)
                chunk = handler.receive_data_chunk(chunk, counters[index])
                counters[index] += chunk_length
                if chunk is None:
                    break

        for index, handler in enumerate(upload_handlers):
            file_obj = handler.file_complete(counters[index])
            if file_obj is not None:
                return DataAndFiles({}, {'file': file_obj})

        raise ParseError(self.errors['unhandled'])

    def get_filename(self, stream, media_type, parser_context):
        """检测上传的文件名。 首先搜索“文件名”网址kwarg。
         然后尝试解析Content-Disposition标头。
         """
        try:
            return parser_context['kwargs']['filename']
        except KeyError:
            pass

        try:
            meta = parser_context['request'].META
            disposition = parse_header(meta['HTTP_CONTENT_DISPOSITION'].encode())
            filename_parm = disposition[1]
            if 'filename*' in filename_parm:
                return self.get_encoded_filename(filename_parm)
            return force_str(filename_parm['filename'])
        except (AttributeError, KeyError, ValueError):
            pass

    def get_encoded_filename(self, filename_parm):
        """根据RFC6266处理编码的文件名。 也可以看看：
         https://tools.ietf.org/html/rfc2231#section-4
        """
        encoded_filename = force_str(filename_parm['filename*'])
        try:
            charset, lang, filename = encoded_filename.split('\'', 2)
            filename = parse.unquote(filename)
        except (ValueError, LookupError):
            filename = force_str(filename_parm['filename'])
        return filename
```






# 自己对 restful api 的认识
- 本质上一个规范, 可以不遵守, 挑着遵守
    - 不遵守
        > https  
        > api.xxx.com/  

    - 遵守
        > http动词/路径(CBV)  
        > /api/版本  
        > 状态码  
        > 过滤信息(分页)  
        > 返回结果(url/错误信息)  
        > Hypermedia api  
- 不用 framework 也可以实现
- django 推荐使用 CBV

