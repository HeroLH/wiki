> *Made By Herolh*

----------------------------------------------

# http/template 的基本使用 {#index}

[TOC]











--------------------------------------------

## 简介
&emsp;&emsp;`html/template` 包实现了数据驱动的模板，用于生成可防止代码注入的安全的 HTML 内容。它提供了和 `text/template` 包相同的接口，Go 语言中输出 HTML 的场景都应使用 `html/template` 这个包。



### 教程

- [李文周的博客 - Go 语言标准库之 http/template](https://liwenzhou.com/posts/Go/go_template)
- [bilibili - qimi - 最新 Go Web 开发教程基于 gin 框架和 gorm 的 web 开发实战](https://www.bilibili.com/video/BV1gJ411p7xC?p=5)



### 模板与渲染

&emsp;&emsp;在一些前后端不分离的 Web 架构中，我们通常需要在后端将一些数据渲染到 HTML 文档中，从而实现动态的网页（网页的布局和样式大致一样，但展示的内容并不一样）效果。
&emsp;&emsp;我们这里说的模板可以理解为事先定义好的 HTML 文档文件，模板渲染的作用机制可以简单理解为文本替换操作–使用相应的数据去替换 HTML 文档中事先准备好的标记。很多编程语言的 Web 框架中都使用各种模板引擎，比如 Python 语言中 Flask 框架中使用的 jinja2 模板引擎。



### Go 语言的模板引擎

Go 语言内置了文本模板引擎 `text/template` 和用于 HTML 文档的 `html/template`。它们的作用机制可以简单归纳如下：
- 模板文件通常定义为`.tmpl` 和`.tpl` 为后缀（也可以使用其他的后缀），必须使用 `UTF8` 编码。
- 模板文件中使用 `{{`和`}}` 包裹和标识需要传入的数据。
- 传给模板这样的数据就可以通过点号（`.`）来访问，如果数据是复杂类型的数据，可以通过 `{{ .FieldName}}` 来访问它的字段。
- 除 `{{`和`}}` 包裹的内容外，其他内容均不做修改原样输出。



### 模板引擎的使用

Go 语言模板引擎的使用可以分为三部分：定义模板文件、解析模板文件和模板渲染.



#### 定义模板文件

其中，定义模板文件时需要我们按照相关语法规则去编写，后文会详细介绍。



#### 解析模板文件

上面定义好了模板文件之后，可以使用下面的常用方法去解析模板文件，得到模板对象：

```go
func (t *Template) Parse(src string) (*Template, error)
func ParseFiles(filenames ...string) (*Template, error)
func ParseGlob(pattern string) (*Template, error)
```

当然，你也可以使用 `func New(name string) *Template` 函数创建一个名为 `name` 的模板，然后对其调用上面的方法去解析模板字符串或模板文件。



#### 模板渲染

渲染模板简单来说就是使用数据去填充模板，当然实际上可能会复杂很多。

```go
func (t *Template) Execute(wr io.Writer, data interface{}) error
func (t *Template) ExecuteTemplate(wr io.Writer, name string, data interface{}) error
```





## 模板语法

### {{.}}

模板语法都包含在 `{{`和`}}` 中间，其中 `{{.}}` 中的点表示当前对象。当我们传入一个结构体对象时，我们可以根据 `.` 来访问结构体的对应字段。例如：

```go
type UserInfo struct {
    Name   string
    Age    int
    Desc   map[string]string
}

func sayHello(w http.ResponseWriter, r *http.Request) {
    // 解析指定文件生成模板对象
    tmpl, err := template.ParseFiles("./hello.tmpl")
    if err != nil {
        fmt.Println("create template failed, err:", err)
        return
    }
    // 利用给定数据渲染模板，并将结果写入w
    user := UserInfo{
        Name:   "小王子",
        Age:    18,
        Desc:   map[string]string{
            "message": "123",
        },
    }
    tmpl.Execute(w, user)
    //tmpl.Execute(w, map[string]interface{}{
	//	"userInfo1": userInfo,
	//	"userInfo2": userInfo2,
	//})
}
```

模板文件 `hello.tmpl` 内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Hello</title>
</head>
<body>
    <p>Hello {{.Name}}</p>
    <p>年龄：{{.Age}}</p>
    <p>性别：{{.Desc.message}}</p>
</body>
</html>
```

同理，当我们传入的变量是 map 时，也可以在模板文件中通过`.` 根据 key 来取值。



### 注释

注释，执行时会忽略。
可以多行。
注释不能嵌套，并且必须紧贴分界符始止。

```go
{{/* a comment */}}
```



### pipeline

`pipeline` 是指产生数据的操作。比如 `{{.}}`、`{{.Name}}` 等。Go 的模板语法中支持使用管道符号 `|` 链接多个命令，用法和 unix 下的管道类似：`|` 前面的命令会将运算结果 (或返回值) 传递给后一个命令的最后一个位置。

**注意：**并不是只有使用了 `|` 才是 pipeline。Go 的模板语法中，`pipeline` 的概念是传递数据，只要能产生数据的，都是 `pipeline`。



### 变量

我们还可以在模板中声明变量，用来保存传入模板的数据或其他语句生成的结果。具体语法如下：

```go
$obj := {{.}}
// 其中 $obj 是变量的名字，在后续的代码中就可以使用该变量了。

{{ $var1 := 100 }}
{{ $age := .m1.age }}
```



### 移除空格

有时候我们在使用模板语法的时候会不可避免的引入一下空格或者换行符，这样模板最终渲染出来的内容可能就和我们想的不一样，这个时候可以使用 `{{-` 语法去除模板内容左侧的所有空白符号， 使用 `-}}` 去除模板内容右侧的所有空白符号。

```go
{{- .Name -}}
```

**注意：**`-` 要紧挨 `{{`和`}}`，同时与模板值之间需要使用空格分隔。



### 控制语句

#### 条件判断

```go
{{if pipeline}} T1 {{end}}

{{if pipeline}} T1 {{else}} T0 {{end}}

{{if pipeline}} T1 {{else if pipeline}} T0 {{end}}
```



#### range

Go 的模板语法中使用 `range` 关键字进行遍历，有以下两种写法，其中 `pipeline` 的值必须是数组、切片、字典或者通道。

```go
{{range pipeline}} T1 {{end}}
如果pipeline的值其长度为0，不会有任何输出

{{range pipeline}} T1 {{else}} T0 {{end}}
如果pipeline的值其长度为0，则会执行T0。
```



#### with

```go
{{with pipeline}} T1 {{end}}
如果pipeline为empty不产生输出，否则将dot设为pipeline的值并执行T1。不修改外面的dot。

{{with pipeline}} T1 {{else}} T0 {{end}}
如果pipeline为empty，不改变dot并执行T0，否则dot设为pipeline的值并执行T1。
```



### 模板函数

#### 预定义函数

执行模板时，函数从两个函数字典中查找：首先是模板函数字典，然后是全局函数字典。一般不在模板内定义函数，而是使用 Funcs 方法添加函数到模板里。预定义的全局函数如下：

```go
and
    函数返回它的第一个empty参数或者最后一个参数；
    就是说"and x y"等价于"if x then y else x"；所有参数都会执行；
or
    返回第一个非empty参数或者最后一个参数；
    亦即"or x y"等价于"if x then x else y"；所有参数都会执行；
not
    返回它的单个参数的布尔值的否定
len
    返回它的参数的整数类型长度
index
    执行结果为第一个参数以剩下的参数为索引/键指向的值；
    如"index x 1 2 3"返回x[1][2][3]的值；每个被索引的主体必须是数组、切片或者字典。
print
    即fmt.Sprint
printf
    即fmt.Sprintf
println
    即fmt.Sprintln
html
    返回与其参数的文本表示形式等效的转义HTML。
    这个函数在html/template中不可用。
urlquery
    以适合嵌入到网址查询中的形式返回其参数的文本表示的转义值。
    这个函数在html/template中不可用。
js
    返回与其参数的文本表示形式等效的转义JavaScript。
call
    执行结果是调用第一个参数的返回值，该参数必须是函数类型，其余参数作为调用该函数的参数；
    如"call .X.Y 1 2"等价于go语言里的dot.X.Y(1, 2)；
    其中Y是函数类型的字段或者字典的值，或者其他类似情况；
    call的第一个参数的执行结果必须是函数类型的值（和预定义函数如print明显不同）；
    该函数类型值必须有1到2个返回值，如果有2个则后一个必须是error接口类型；
    如果有2个返回值的方法返回的error非nil，模板执行会中断并返回给调用模板执行者该错误；
```



#### 比较函数

布尔函数会将任何类型的零值视为假，其余视为真。下面是定义为函数的二元比较运算的集合：

```shell
eq      如果arg1 == arg2则返回真
ne      如果arg1 != arg2则返回真
lt      如果arg1 < arg2则返回真
le      如果arg1 <= arg2则返回真
gt      如果arg1 > arg2则返回真
ge      如果arg1 >= arg2则返回真
```

为了简化多参数相等检测，eq（只有 eq）可以接受 2 个或更多个参数，它会将第一个参数和其余参数依次比较，返回下式的结果：

```go
{{eq arg1 arg2 arg3}}
```

比较函数只适用于基本类型（或重定义的基本类型，如”type Celsius float32”）。但是，整数和浮点数不能互相比较。



#### 自定义函数

```go
func sayHello(w http.ResponseWriter, r *http.Request) {
	htmlByte, err := ioutil.ReadFile("./hello.tmpl")
	if err != nil {
		fmt.Println("read html failed, err:", err)
		return
	}
	// 自定义一个夸人的模板函数
	kua := func(arg string) (string, error) {
		return arg + "真帅", nil
	}
	// 采用链式操作在Parse之前调用Funcs添加自定义的kua函数
	tmpl, err := template.New("hello").Funcs(template.FuncMap{"kua": kua}).Parse(string(htmlByte))
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}

	user := UserInfo{
		Name:   "小王子",
		Gender: "男",
		Age:    18,
	}
	// 使用user渲染模板，并将结果写入w
	tmpl.Execute(w, user)
}
```

我们可以在模板文件 `hello.tmpl` 中按照如下方式使用我们自定义的 `kua` 函数了。

```go
{{kua .Name}}
```



### 模板嵌套

我们可以在 template 中嵌套其他的 template。这个 template 可以是单独的文件，也可以是通过 `define` 定义的 template。举个例子： `t.tmpl` 文件内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>tmpl test</title>
</head>
<body>
    
    <h1>测试嵌套template语法</h1>
    <hr>
    {{template "ul.tmpl"}}
    <hr>
    {{template "ol.tmpl"}}
</body>
</html>

{{ define "ol.tmpl"}}
<ol>
    <li>吃饭</li>
    <li>睡觉</li>
    <li>打豆豆</li>
</ol>
{{end}}
```

`ul.tmpl` 文件内容如下：

```html
<ul>
    <li>注释</li>
    <li>日志</li>
    <li>测试</li>
</ul>
```

我们注册一个 `templDemo` 路由处理函数：

```go
http.HandleFunc("/tmpl", tmplDemo)
```

`tmplDemo` 函数的具体内容如下：

```go
func tmplDemo(w http.ResponseWriter, r *http.Request) {
	tmpl, err := template.ParseFiles("./t.tmpl", "./ul.tmpl")
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}
	user := UserInfo{
		Name:   "小王子",
		Gender: "男",
		Age:    18,
	}
	tmpl.Execute(w, user)
}
```

**注意**：在解析模板时，被嵌套的模板一定要在后面解析，例如上面的示例中 `t.tmpl` 模板中嵌套了 `ul.tmpl`，所以 `ul.tmpl` 要在 `t.tmpl` 后进行解析。



### block

```shell
{{block "name" pipeline}} T1 {{end}}
```

`block` 是定义模板 `{{define "name"}} T1 {{end}}` 和执行 `{{template "name" pipeline}}` 缩写，典型的用法是定义一组根模板，然后通过在其中重新定义块模板进行自定义。定义一个根模板 `templates/base.tmpl`，内容如下：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <title>Go Templates</title>
</head>
<body>
<div class="container-fluid">
    {{block "content" . }}{{end}}
</div>
</body>
</html>
```

然后定义一个 `templates/index.tmpl`，” 继承”`base.tmpl`：

```go
{{template "base.tmpl"}}

{{define "content"}}
    <div>Hello world!</div>
{{end}}
```

然后使用 `template.ParseGlob` 按照正则匹配规则解析模板文件，然后通过 `ExecuteTemplate` 渲染指定的模板：

```go
func index(w http.ResponseWriter, r *http.Request){
	tmpl, err := template.ParseGlob("templates/*.tmpl")
	if err != nil {
		fmt.Println("create template failed, err:", err)
		return
	}
	err = tmpl.ExecuteTemplate(w, "index.tmpl", nil)
	if err != nil {
		fmt.Println("render template failed, err:", err)
		return
	}
}
```

如果我们的模板名称冲突了，例如不同业务线下都定义了一个 `index.tmpl` 模板，我们可以通过下面两种方法来解决。

- 在模板文件开头使用 `{{define 模板名}}` 语句显式的为模板命名。

- 可以把模板文件存放在 `templates` 文件夹下面的不同目录中，然后使用 `template.ParseGlob("templates/**/*.tmpl")` 解析模板。



### 修改默认的标识符

Go 标准库的模板引擎使用的花括号 `{{`和`}}` 作为标识，而许多前端框架（如 `Vue` 和 `AngularJS`）也使用 `{{`和`}}` 作为标识符，所以当我们同时使用 Go 语言模板引擎和以上前端框架时就会出现冲突，这个时候我们需要修改标识符，修改前端的或者修改 Go 语言的。这里演示如何修改 Go 语言模板引擎默认的标识符：

```go
template.New("test").Delims("{[", "]}").ParseFiles("./t.tmpl")
```







