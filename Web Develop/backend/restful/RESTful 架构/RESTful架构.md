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

![720333-20170504161535914-297383447](.assets/720333-20170504161535914-297383447.png)

&emsp;&emsp;Fielding 是一个非常重要的人，他是 HTTP协议（1.0版和1.1版）的主要设计者、Apache 服务器软件的作者之一、Apache 基金会的第一任主席。所以，他的这篇论文一经发表，就引起了关注，并且立即对互联网开发产生了深远的影响。



## 三、名称
&emsp;&emsp;Fielding 将他对互联网软件的架构原则，定名为 **REST**，即 **Representational State Transfer** 的缩写。我对这个词组的翻译是"**表现层状态转化**"。如果一个架构符合REST原则，就称它为RESTful架构。
&emsp;&emsp;要理解 RESTful 架构，最好的方法就是去理解 Representational State Transfer 这个词组到底是什么意思，它的每一个词代表了什么涵义。如果你把这个名称搞懂了，也就不难体会REST是一种什么样的设计。



### 资源（Resources）

&emsp;&emsp;REST 的名称"表现层状态转化"中，省略了主语。**"表现层"其实指的是"资源 "表现层"。**
&emsp;&emsp;所谓"资源"，就是网络上的一个实体，或者说是网络上的一个具体信息。它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的实在。你可以用一个URI（统一资源定位符）指向它，每种资源对应一个特定的URI。要获取这个资源，访问它的URI就可以，因此URI就成了每一个资源的地址或独一无二的识别符。
&emsp;&emsp;**所谓"上网"，就是与互联网上一系列的"资源"互动，调用它的URI。**



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

> **注**，虽说restfull规范建议版本号放在请求头而不是url里，但事实上为了使用方便，大多数开发者还是喜欢把版本号放在url上，这样容易直观区分





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





