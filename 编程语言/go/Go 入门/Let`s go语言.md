----------------------------------------------
> *Made By Herolh， 忠告：语言只是工具*
----------------------------------------------

# go 语言  {#index}

[TOC]













# 初识Go语言

## 什么是Go语言？

&emsp;&emsp;Go 是一个开源的编程语言，它能让构造简单、可靠且高效的软件变得容易。
&emsp;&emsp;Go 是从 2007 年末由 Robert Griesemer, Rob Pike, Ken Thompson 主持开发，后来还加入了 Ian Lance Taylor, Russ Cox 等人，并最终于 2009 年 11 月开源，在 2012 年早些时候发布了 Go 1 稳定版本。现在 Go 的开发已经是完全开放的，并且拥有一个活跃的社区。



### 版本更新：

- Go 1.14 (February 2020)
- Go 1.13 (September 2019)
- Go 1.12 (February 2019)
- Go 1.11 (August 2018)
- Go 1.10 (February 2018)
- Go 1.9 (August 2017)
- Go 1.8 (February 2017)
- Go 1.7 (August 2016)
- Go 1.6 (February 2016)
- Go 1.5 (August 2015)
- Go 1.4 (December 2014)
- Go 1.3 (June 2014)
- Go 1.2 (December 2013)
- Go 1.1 (May 2013)
- Go 1 (March 2012)







## Go 语言环境安装

>  Go 语言支持以下系统：Linux、FreeBSD、Mac OS X、Windows

Go官网安装包下载地址为：https://golang.org/dl/。

Go官方镜像站( 推荐 )：https://golang.google.cn/dl/。

各个系统对应的包名：

| 操作系统 |              包名              |
| :------: | :----------------------------: |
| Windows  |    go1.4.windows-amd64.msi     |
|  Linux   |    go1.4.linux-amd64.tar.gz    |
|   Mac    | go1.4.darwin-amd64-osx10.8.pkg |
| FreeBSD  |   go1.4.freebsd-amd64.tar.gz   |

![golist](.assets/golist.jpg)



### Windows 系统下安装

&emsp;&emsp;Windows 下可以使用 `.msi` 后缀的安装包来安装。默认情况下 `.msi` 文件会安装在 `c:\Go` 目录下。你可以将 `c:\Go\bin` 目录添加到 `Path` 环境变量中。添加后你需要重启命令窗口才能生效。

### 安装测试

- **方法一：**

    ```shell
    go version
    ```

    ![1588508331153](.assets/1588508331153.png)

- **方法二：**

    创建工作目录 `C:\>Go_WorkSpace`

    ```shell
    package main
    
    import "fmt"
    
    func main() {
       fmt.Println("Hello, World!")
    }
    ```

    使用 go 命令执行以上代码输出结果如下：

    ```shell
    C:\Go_WorkSpace>go run test.go
    
    Hello, World!
    ```

    



### 编译程序

&emsp;&emsp;使用 `go run` 这个命令，会将编译、链接和运行3个步骤合并为一步，运行完后在当前目录下也看不到任何中间文件和最终的可执行文件。如果要只生成编译结果而不自动运行，我们也可以使用 Go 命令行工具的 `build` 命令：

```shell
go build hello.go
./hello 
# Hello, World!
```

&emsp;&emsp;从根本上说，Go 命令行工具只是一个源代码管理工具，或者说是一个前端。真正的 Go 编译器和链接器被 Go 命令行工具隐藏在后面，我们可以直接使用它们：

```shell
6g helloworld.go 
6l helloworld.6 
./6.out 
# Hello, World!
```

&emsp;&emsp;6g 和 6l 是 64 位版本的 Go 编译器和链接器，对应的 32 位版本工具为 8g 和 8l。Go 还有另外一个 GCC 版本的编译器，名为 gccgo。



### 环境配置

#### 创建一个任意目录

<img src=".assets/w6.png" alt="img" style="zoom: 67%;" />

以后的 go 项目都要按照要求放在这个目录里：

```shell
E:\Project\go
----|bin	# 用于存放编译后的可执行文件
----|pkg	# 用于存放编译后的包文件
----|src	# 我们以后写的go项目代码都写到这里去，在内部为每个项目创建一个文件夹。
----|----|project_1
----|----|----|app.go
----|----|project_2
----|----|----|app.go
```

> Go 1.11 版本引入了 Module 包管理机制， 可以实现让项目放在任意目录，同时也解决了包依赖管理等问题，后续专门在 Module 专题中再进行讲解，目前先按照上图的方式进行创建项目。



#### 配置环境变量

```shell
# GOROOT，Go解释器安装路径，用于之后去调用go相关源码。
# GOPATH，Go项目代码相关目录，将你以后写的go代码及其编译生成的文件存放的目录。
# GOBIN，Go编译代码后自动生成可执行文件的路径，Go是个编译型语言，当使用go install命令对代码进行编译时，可执行文件会生成到这个目录。
```

![img](.assets/w7.png)



#### GOPATH

&emsp;&emsp;`GOROOT` 和 `GOPATH` 都是环境变量，其中`GOROOT`是我们安装 go 开发包的路径，而从 Go 1.8 版本开始，Go 开发包在安装完成后会为`GOPATH`设置一个默认目录，参见下表。

##### GOPATH在不同操作系统平台上的默认值

|  平台   |   GOPATH默认值   |        举例        |
| :-----: | :--------------: | :----------------: |
| Windows | %USERPROFILE%/go | C:\Users\用户名\go |
|  Unix   |     $HOME/go     |  /home/用户名/go   |

![1588508601767](.assets/1588508601767.png)

![img](.assets/image-20200430001257764.png)





## 第一个Go程序 Hello World!

### 目录结构

&emsp;&emsp;在 `GOPATH` 下的 `src` 目录中创建一个 `文件夹（项目）`，进入文件夹并创建一个以 `.go` 为后缀名的文件（如 `first.go`），并在 `first.go` 文件中写入 go 代码。

```shell
E:\Project\go
----|bin
----|pkg
----|src
----|----|learn
----|----|----|day1
----|----|----|----|helloWorld.go
```



### 代码示例

```go
package main

import "fmt"

func main() {		// 程序开始执行的函数。
   fmt.Println("Hello, World!")
}
```

- **package main**
  
    > 每个 Go 源代码文件的开头都是一个 package 声明，表示该 Go 代码所属的包。
> 必须在源文件中非注释的第一行指明这个文件属于哪个包，包是Go 语言里最基本的分发单位，也是工程管理中依赖关系的体现。

- **import "fmt"**
    >  在包声明之后，是一系列的import语句，用于导入该程序所依赖的包。由于本示例程序用到了 `Println()` 函数，所以需要导入该函数所属的 fmt 包。 
    >  有一点需要注意，**不得包含在源代码文件中没有用到的包，否则Go编译器会报编译错误。**
    >  这与下面提到的强制左花括号 `{` 的放置位置以及之后会提到的函数名的大小写规则，均体现了Go 语言在语言层面解决软件工程问题的设计哲学。


- **func **

    > 所有 Go 函数( 包括在对象编程中会提到的类型成员函数 )以关键字 func 开头。一个常规的 函数定义包含以下部分：
    >
    > ```go
    > func 函数名(参数列表)(返回值列表) {
    >     // 函数体
    > }
    > 对应的一个实例如下：
    > func Compute(value1 int, value2 float64)(result float64, err error) {
    >     // 函数体
    > } 
    > ```
    >
    > Go支持多个返回值。以上的示例函数 `Compute()` 返回了两个值，一个叫 result，另一个是 err。并不是所有返回值都必须赋值。在函数返回时没有被明确赋值的返回值都会被设置为默认值，比如result会被设为0.0，err会被设为 nil。

- **main(){}**
  
    > main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有 init() 函数则会先执行该函数）。main 函数是 Go 可执行程序的执行起点 )。
    > **Go语言的main()函数不能带参数，也不能定义返回值。**命令行传入的参数在` os.Args` 变量中保存。如果需要支持命令行开关，可使用 flag 包。



### 运行代码

本质上是将 go 代码交给 go 编译器去执行



#### 方式一：`go run`

> compile and run Go program ，其内部会【先编译】代码文件【再运行】（二合一）。

注意：`go run` 内部创建可执行文件默认保存在系统的临时目录，可以使用 `go run -work main.go`查看。

```shell
go run learn\day1
# or
go run helloWorld.go
```

<img src=".assets/image-20200726003442048.png" alt="image-20200726003442048" style="zoom:80%;" />



#### 方式二：`go build`

> compile packages and dependencies，其内部就是将 go 代码进行编译，然后手动执行。
>
> ```shell
> go build -n 
> # 进行编译时，会将底层编译不步骤展示出来。
> 
> go build -o 任意名称 
> # 进行编译，这样可自定义编译生成的可执行文件的名称。
> ```
>
> 注意：在win系统中 build 命令会生成的可执行文件默认以 .exe 为后缀。

&emsp;&emsp;执行完命令之后，就会在当前项目目录下自动生成一个可执行文件（默认文件名为项目），然后在执行此可执行文件即可。

```shell
go build
day1.exe
# or
go build -o helloWorld.exe
helloWorld.exe
```

<img src=".assets/image-20200726003941488.png" alt="image-20200726003941488" style="zoom:80%;" />



#### 方式三：`go install`

> compile and install packages and dependencies，其内部就是编译 go 代码，并将可执行文件/包文件分别放到 bin 和 pkg 目录。包文件的生成必须用 `go install`

<img src=".assets/image-20200430010105368.png" alt="img" style="zoom: 33%;" />

&emsp;&emsp;如果项目没有main包（只是一个类库），则 install 生成的包文件会放在 `$GOPATH/pkg` 目录；有 main 包则生成的可执行文件放在 `$GOPATH/src` 目录。
&emsp;&emsp;对于生成的 可执行文件 直接运行即可，而对于 包文件 可以当做是一个类库来供其他程序使用，

```shell
go install learn\day1
..\..\bin\day1.exe
```

![image-20200726004746922](.assets/image-20200726004746922.png)





## 集成开发环境

&emsp;&emsp;常用的有 vscode 和 Goland，此处用 Goland

### Goland

去[官方网站](https://www.jetbrains.com/go/)去下载 Goland 并 安装到自己的电脑中。

<img src=".assets/15.png" alt="img" style="zoom: 33%;" />

<img src=".assets/p1.png" alt="img" style="zoom:33%;" />

<img src=".assets/image-20200726012535922.png" alt="image-20200726012535922" style="zoom: 67%;" />



#### 常见配置

##### 关闭参数建议

&emsp;&emsp;你的 Goland 在编写代码时，可能会在代码发现一些 `a...:` 等标记，这其实是Goland为你提供的参数的注解，如果不想展示，则可以修改Goland的配置实现。

<img src=".assets/21.png" alt="img" style="zoom: 25%;" />



##### 字体调节

&emsp;&emsp;你的 Goland 字体大小不合适时，可以通过修改 Goland 的配置之后，通过 `Ctrl + 鼠标滚轮` 实现字体大小调节。

<img src=".assets/26.png" alt="img" style="zoom: 25%;" />





# Go 语言基础语法

## 注释与分隔符

### 注释

Go 程序的代码注释与 C++ 保持一致，即同时支持以下两种用法：

```go
/*
块注释
*/

// 行注释 
```

&emsp;&emsp;Go程序并不要求开发者在每个语句后面加上分号表示语句结束，这是与C和C++的一个明显不同之处。**需要注意的是 `{` 不能单独放在一行**，所以以下代码在运行时会产生错误，这样做的结果是 Go 编译器报告编译错误，这点需要特别注意：

```go
package main

import "fmt"

func main()  
{  // 错误，{ 不能在单独的行上
    fmt.Println("Hello, World!")
}
```

> syntax error: unexpected semicolon or newline before { 



### 分隔符

&emsp;&emsp;在 Go 程序中，一行代表一个语句结束。每个语句不需要像 C 家族中的其它语言一样以分号 `;` 结尾，因为这些工作都将由 Go 编译器自动完成。如果你打算将多个语句写在同一行，它们则必须使用 `;` 人为区分，但在实际开发中我们并不鼓励这种做法。

```go
// 以下为两个语句：
fmt.Println("Hello, World!")
fmt.Println("Hello, World!")
```







## 初识包管理

> &emsp;&emsp;`包（package）`是多个 Go 源码的集合，是一种高级的代码复用方案，Go 语言为我们提供了很多内置包，如`fmt`、`os`、`io`等。

一般来说，一个文件夹可以作为 package，同一个 package 内部变量、类型、方法等定义可以相互看到。
- 一个文件夹就可以成为一个包
- 在文件夹( 包 )中可以创建对讴歌文件
- 在同一个包下的每个文件必须指定包名且相同



### 包的分类

-  **`main` 包**

    > 如果是 main 包，则必须写一个 main 函数，此函数位项目的入口( main 主函数 )
    >
    > 编译生成的是一个可执行文件

- **非 `main` 包**

    > 用来将



### 示例

- **api 包**

    - **baidu.go**

        ```go
        package api
        
        import "fmt"
        
        func BaiDu() {
        	fmt.Println("api 包下的 baidu")
        }
        ```

    - **google.go**

        ```go
        package api
        
        import "fmt"
        
        func Google() {
        	fmt.Println("api 包下的 google")
        }
        ```

- **buff.go**

    ```go
    package main
    
    import "fmt"
    
    // 在包中编写功能时，函数首字母要大写
    // 		首字母大写说明是个公有的功能，属于外部函数
    // 		首字母小写说明时包私有功能，属于内部函数
    func Buff() {
    	fmt.Println("同一个 package 下 的Buff")
    }
    ```

- **app.go**

    ```go
    package main
    
    import (
    	"fmt"
    	"learn/api"
    )
    
    func main() {
    	fmt.Println("Hello World!")
        // 同一个包下，不需要再导入
    	Buff()
        // 不同包下，需要再导入
    	api.Google()
    	api.BaiDu()
    }
    ```

![image-20200726140530295](.assets/image-20200726140530295.png)





## 输入与输出

### 输出

在终端将数据显示出来

#### 扩展：

进程里有 `stdin/stdout/stderr` ==> `标准输入/标准输出/标准错误`



#### 法一：内置函数

> 官方不保证以后一直有这个功能
>
> 这两个函数取的值不是标准输出，而是标准错误

- **print**

    ```go
    print("hello world!")
    print("hello world!")
    ```

- **println**

    ```go
    println("hello world!")			// ==> 相当于 print("hello world!\n")
    println("hello world!")
    ```





#### 法二：fmt 包( 推荐 )

- **fmt.Print**

    ```go
    fmt.Print("hello world!")
    fmt.Print("hello world!")
    ```

- **fmt.Println**

    ```go
    fmt.Println("hello world!")
    fmt.Println("hello world!")
    
    fmt.Println("hello", "world", "!")
    ```

- **fmt.Printf**

    > 格式化输出
    > %s 			占位符，文本
    > %d			占位符，整数
    > %f		 	占位符，小数( 浮点数 )
    > 百分比		%
    
    ```go
    fmt.Printf("你好， 我是%s, 今年%d, %.2f, 百分比100%%", "lin", 18, 3.1415926)
    ```





### 输入

#### `fmt` 包获取

&emsp;&emsp;Go 语言`fmt`包下有`fmt.Scan`、`fmt.Scanf`、`fmt.Scanln`三个函数，可以在程序运行过程中从标准输入获取用户的输入。

- **fmt.Scan**

    ```go
    func Scan(a ...interface{}) (n int, err error)
    ```

```
    
    `fmt.Scan` <u>要求输入两个值， 就必须输入两个值，否则会一直等待。</u>用户输入成功后，会得到两个值：
    
    > **count**: 用户输入了几个值
    > **err**： 用户输入错误时的错误信息，没有错误返回 <nil>
    
    ```go
    var name string
    var age int
    
    count, err := fmt.Scan(&name, &age)
    fmt.Println(count, err)
    if err == nil{
        fmt.Println(name, age)
    }
    fmt.Println("用户输入错误：", err)
```


​    

- **fmt.Scanln**

    ```go
    func Scanln(a ...interface{}) (n int, err error)
    ```

    `fmt.Scanln` <u>等待回车，输入回车，输入结束</u>。用户输入成功后，会得到两个值：

    >**count**: 用户输入了几个值
    >**err**： 用户输入错误时的错误信息，没有错误返回 <nil>

    ```GO
    var name string
    var age int
    
    count, err := fmt.Scanln(&name, &age)
    fmt.Println(count, err)
    if err == nil{
        fmt.Println(name, age)
    }
    fmt.Println("用户输入错误：", err)
    ```



- **fmt.Scanf**

    ```go
    func Scanf(format string, a ...interface{}) (n int, err error)
    ```

    > 占位符后面要有空格，否则切分不准确

    ```go
    var name string
    var age int
    
    count, err := fmt.Scanf("我叫%s 今年%d 岁", &name, &age)
    fmt.Println(count, err)
    if err == nil{
        fmt.Println(name, age)
    }
    fmt.Println("用户输入错误：", err)
    ```



#### `bufio`包获取

&emsp;&emsp;有时候我们想完整获取输入的内容，而输入的内容可能包含空格，这种情况下可以使用 `bufio` 包来实现。示例代码如下：

```go
reader := bufio.NewReader(os.Stdin) // 从标准输入生成读对象
fmt.Println("请输入内容：")
// line：	 从 stdin 中读取一行的数据( 字节集合 -> 转化为字符串)
// isPrefix：默认一次能读 4096 个字节：
//		一次读完，isPrefix = false
//		一次读不完，isPrefix = true
// err:
line, isPrefix, err := reader.ReadLine()
data := string(line)
fmt.Println(data, isPrefix, err)

//text, _ := reader.ReadString('\n') 			// 读到换行
//text = strings.TrimSpace(text)
//fmt.Printf("%#v\n", text)
```





## 基本数据类型

### 数值类型

&emsp;&emsp;Go语言的数值类型包含不同大小的整数型、浮点数和负数，每种数值类型都有大小范围以及正负符号。

```go
fmt.Println(666)
fmt.Println(6 + 6)
fmt.Println(6 - 6)
fmt.Println(6 * 6)
fmt.Println(6 / 6)		// 商
fmt.Println(6 % 6)		// 余数
```





### 字符串

> 字符串默认值为 ""

```go
fmt.Println("字符串")
// fmt.Println("字符串" + 666)			// 不同数据类型不能混搭
fmt.Println("字符串" + "666")
```



#### 字符串格式化

```go
name := "lin"
age := 18
addr := "---"
result := fmt.Sprintf("我叫%s, 今年%d, 家在%s", name, age, addr)
fmt.Println(result)
```





#### 字符串的存储形式

英文字符占一位，中文字符占三位

```go
// 字符串以什么形式存在存在于 Go 编译器中
name := "abc"
fmt.Println(name[0], name[1], name[2])
// 结果： 97 98 99

fmt.Println(strconv.FormatInt(int64(name[0]), 2))		// 获取二进制
// 1100001

name2 := "一二三"
// 表示 一
fmt.Println(name2[0], name2[1], name2[2])
// 表示 二
fmt.Println(name2[3], name2[4], name2[5])
// 表示 三
fmt.Println(name2[6], name2[7], name2[8])
//fmt.Println(name2[9])								// 会报错
```





### 布尔类型

```go
fmt.Println(1 > 2)		// false	假
fmt.Println(1 < 2)		// ture		真
```





## 常量与变量

### 变量

> Go 语言变量名由字母、数字、下划线组成，其中首个字符不能为数字。声明变量的一般形式是使用 var 关键字：

#### 变量声明

> Go 语言中的变量需要声明后才能使用，同一作用域内不支持重复声明。
>  **Go语言的变量声明后必须使用**。



##### 标准声明

&emsp;&emsp;Go语言的变量声明格式为 `var 变量名 变量类型`。变量声明以关键字`var`开头，变量类型放在变量的后面，行尾无需分号：

```go
// 声明加赋值
var str string = "字符串"
fmt.Println(str)

var age int = 18
fmt.Println(age)

var  flag bool = true
fmt.Println(flag)

// 先声明后赋值
var str2 string
str2 = "字符串2"		// 赋值不算使用
fmt.Println(str2)
```



##### 批量声明

&emsp;&emsp;每声明一个变量就需要写`var`关键字会比较繁琐，go语言中还支持批量变量声明：

- **先声明再赋值**

    ```go
    var (
        a string		// 只声明不赋值，有一个默认值 ""
        b int			// 只声明不赋值，有一个默认值 0
        c bool			// 只声明不赋值，有一个默认值 false
        d float32
    )
    a = "string"
    ```

    

- **声明并赋值**

    ```go
    // 法一：
    var string1, string2, string3 string = "1", "2", "3"
    fmt.Println(string1, string2,string3)
    
    // 法二：
    var (
        a string = "1"
        b int = 2
        c bool = true
        d float32 = 3.1415926
    )
    fmt.Println(a, b, c, d)
    ```

    



#### 变量简写

- **先声明再赋值**

    ```go
    var string1 string
    var string2 string
    var string3 string
    
    // 相当于下面一行
    
    var string1, string2,string3 string
    ```

- **声明并赋值**

    ```go
    var name1 string = "字符串1"			// 最全写法
    var name2 = "字符串2"					// 自动推断出是什么类型
    name3 := "字符串3"						// 海象运算符连 var 都能省略
    
    fmt.Println(name1, name2, name3)
    ```



#### 作用域

> 如果我们定义了一个大括号，大括号内定义的变量：
> - 不能被括号外的使用。
> - 可以在同级和子级中使用。

```go
name := "global"
if true{
    fmt.Println(name)
    age := 18
    name := "local"
    fmt.Println(age, name)
}
fmt.Println(name)
//fmt.Println(age)			// 报错
```



#### 全局变量与局部变量

```go
//全局变量( 不能以省略的方式 )
var name1 string = "字符串1"				// 支持
var name2 = "字符串2"					// 支持
name3 := "字符串3"						// 不支持

// 批量声明方式
var (
	var1 = "str"
	var2 = 123
	var3 string
)

func main() {
    // 局部变量
}
```



#### 赋值与内存相关

使用值类型 int、string、bool 这三种数据类型时，如果遇到变量的赋值会拷贝一份

- **赋值给另一个变量的时候，会重新开辟一块内存用来存放数据，而不是建立指针引用**

    ```GO
    name1 := "str1"
    name2 := name1
    
    // 生成两块地址，而不是引用
    fmt.Println(name1, &name1)
    fmt.Println(name2, &name2)
    ```

    <img src=".assets/image-20200726190707781.png" alt="image-20200726190707781" style="zoom:67%;" />

- **修改变量的值不会重新开辟内存，而是直接覆盖原数据**

    ```go
    name1 := "str1"
    fmt.Println(name1, &name1)
    name1 = "str2"
    fmt.Println(name1, &name1)
    ```

    <img src=".assets/image-20200726191936074.png" alt="image-20200726191936074" style="zoom: 67%;" />







### 常量

&emsp;&emsp;相对于变量，常量是恒定不变的值，多用于定义程序运行期间不会改变的那些值，一般情况下，常量都会定义在全局。 常量的声明和变量声明非常类似，只是把`var`换成了`const`，**常量在定义的时候必须赋值, 常量可以不被使用**。

```go
// 声明了 pi 和 e 这两个常量之后，在整个程序运行期间它们的值都不能再发生变化了。
const pi = 3.1415926
const e float64 = 2.7182		// 常量可以不被使用
// age := 18					// 这是定义一个变量

// pi = 3.14					// 试图修改会报错
fmt.Println(pi)
```

多个常量也可以一起声明：

```go
const (
    pi = 3.1415
    e = 2.7182
)
```

const 同时声明多个常量时，如果省略了值则表示和上面一行的值相同:

```go
const (
    n1 = 100
    n2
    n3
)
// 常量 n1、n2、n3 的值都是 100。
```



#### iota （常量计数器）

&emsp;&emsp;`iota`是go语言的常量计数器，只能在常量的表达式中使用。
&emsp;&emsp;`iota`在const关键字出现时将被重置为0。const中每新增一行常量声明将使`iota`计数一次(iota可理解为const语句块中的行索引)。 使用iota能简化定义，在定义枚举时很有用。

```go
const (
    n1 = iota //0
    n2        //1
    n3        //2
    n4        //3
)
```



##### 几个常见的`iota`示例:

###### 使用`_`跳过某些值

```go
const (
    n1 = iota //0
    n2        //1
    _
    n4        //3
)
```

###### `iota`声明中间插队

```go
const (
    n1 = iota //0
    n2 = 100  //100
    n3 = iota //2
    n4        //3
)
const n5 = iota //0
```

###### 多个`iota`定义在一行

```go
const (
    a, b = iota + 1, iota + 2 //1,2
    c, d                      //2,3
    e, f                      //3,4
)
```

###### 定义数量级

> &emsp;&emsp;这里的 `<<` 表示左移操作，`1<<10` 表示将 1 的二进制表示向左移 10 位，也就是由 `1` 变成了`10000000000`，也就是十进制的 1024。同理 `2<<2` 表示将 2 的二进制表示向左移 2 位，也就是由 `10` 变成了 `1000`，也就是十进制的 8。

```go
const (
    _  = iota
    KB = 1 << (10 * iota)	// 1024 
    MB = 1 << (10 * iota)	// 1048576
    GB = 1 << (10 * iota)	// 1073741824
    TB = 1 << (10 * iota)	// 1099511627776
    PB = 1 << (10 * iota)	// 1125899906842624
)
```





### 标识符、关键字

#### 标识符

> 标识符用来命名变量、类型等程序实体。

&emsp;&emsp;一个标识符实际上就是一个或是多个字母( A-Z 和 a-z )数字(0-9)、下划线 `_` 组成的序列，但是第一个字符必须是字母或下划线而不能是数字。以下是有效的标识符：

```go
mahesh   kumar   abc   move_name   a_123
myname50   _temp   j   a23b9   retVal
```

以下是无效的标识符：

```go
1ab				// 以数字开头
case			// Go 语言的关键字
a+b				// 运算符是不允许的
```



当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 protected ）



#### 关键字

- 下面列举了 Go 代码中会使用到的 25 个关键字或保留字：

    > ```go
    > break  default  func  interface  select  
    > case  defer  go  map  struct  
    > chan  else  goto  package  switch  
    > const  fallthrough  if  range  type  
    > continue  for  import  return  var
    > ```

- 除了以上介绍的这些关键字，Go 语言还有 36 个预定义标识符：

    > ```go
    > int  int8  int16 int32  int64 float32 float64
    > uint uint8  uint16  uint32  uint64  uintptr
    > string  byte  complex64  complex128 bool  true  false
    > make  new  close  append  copy  len  print  println
    > cap  imag iota  complex  nil  panic  real  recover
    > ```

- 程序一般由关键字、常量、变量、运算符、类型和函数组成。

- 程序中可能会使用到这些分隔符：括号 `()`，中括号 `[]` 和大括号 `{}`。

- 程序中可能会使用到这些标点符号：`.`、`,`、`;`、`:` 和 `…`。







## 控制语句

### 条件语句

####  if else 语句

&emsp;&emsp;Go语言中`if`条件判断的格式如下：

```go
if 表达式1 {
    分支1
} else if 表达式2 {
    分支2
} else{
    分支3
}
```

> **注意：**
> &emsp;&emsp;Go 语言规定与 `if` 匹配的左括号 `{` 必须与 `if和表达式` 放在同一行，`{` 放在其他位置会触发编译错误。 同理，与 `else` 匹配的 `{` 也必须与 `else` 写在同一行，`else` 也必须与上一个 `if` 或 `else if` 右边的大括号在同一行。



##### 特殊写法

```go
func ifDemo2() {
	if score := 65; score >= 90 {
		fmt.Println("A")
	} else if score > 75 {
		fmt.Println("B")
	} else {
		fmt.Println("C")
	}
}
```



#### switch case

&emsp;&emsp;使用`switch`语句可方便地对大量的值进行条件判断。注意数据类型要一致。

```go
finger := 3
switch finger {
    case 1:
    fmt.Println("大拇指")
    case 2:
    fmt.Println("食指")
    case 3:
    fmt.Println("中指")
    case 4:
    fmt.Println("无名指")
    case 5:
    fmt.Println("小拇指")
    default:
    fmt.Println("无效的输入！")
}
```

Go语言规定每个`switch`只能有一个`default`分支。

一个分支可以有多个值，多个case值中间使用英文逗号分隔。

```go
switch n := 7; n {
    case 1, 3, 5, 7, 9:
    fmt.Println("奇数")
    case 2, 4, 6, 8:
    fmt.Println("偶数")
    default:
    fmt.Println(n)
}
```





### 循环语句

#### for 循环

Go 语言中的所有循环类型均可以使用`for`关键字来完成。for循环的基本格式如下：

```go
for 初始语句;条件表达式;结束语句{
    循环体语句
}
```

- for 循环的初始语句或结束语句可以被忽略，但是语句的分号必须要写

    ```go
    // 忽略循环的初始语句
    i := 0
    for ; i < 10; i++ {
        fmt.Println(i)
    }
    
    // 忽略循环的结束语句
    for i := 0; i < 10;{
        fmt.Println(i)
        i++
    }
    ```

- for循环的初始语句和结束语句可以一起省略

    ```go
    i := 0
    for i < 10 {
        fmt.Println(i)
        i++
    }
    ```



##### 无限循环

```go
for {
    循环体语句
}
```





#### continue and break

> 可以对 break 和 continue 进行打标签，就可以实现多层循环的跳出和终止



##### continue

> `continue`语句可以结束当前循环，开始下一次的循环迭代过程，仅限在`for`循环内使用。

- 在循环语句中，当循环遇到 `continue` 关键字的时候，会停止当前的循环，开始下一次的循环。

    ```go
    for i := 0; i < 10;i++{
        if i == 2{
            continue
        }
        fmt.Println(i)
    }
    ```

- 在 `continue`语句后添加标签时，表示开始标签对应的循环。例如：

    ```go
    forloop1:
    	for i := 0; i < 5; i++ {
    		// forloop2:
    		for j := 0; j < 5; j++ {
    			if i == 2 && j == 2 {
    				continue forloop1
    			}
    			fmt.Printf("%v-%v\n", i, j)
    		}
    	}
    ```



##### break

> `break`语句可以结束`for`、`switch`和`select`的代码块。

```go
for i := 0; i < 10;i++{
    if i == 2{
        break
    }
    fmt.Println(i)
}
```

&emsp;&emsp;`break`语句还可以在语句后面添加标签，表示退出某个标签对应的代码块，标签要求必须定义在对应的`for`、`switch`和 `select`的代码块上。 举个例子：

```go
BREAKDEMO1:
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			if j == 2 {
				break BREAKDEMO1
			}
			fmt.Printf("%v-%v\n", i, j)
		}
	}
	fmt.Println("...")
```





### goto 语句

跳跃到指定的行，然后向下执行代码：

```go
	var name string
	fmt.Println(&name)
	if name == "svip"{
		goto SVIP
	}else if name == "vip"{
		goto VIP
	}
	fmt.Println("预约...")
VIP:
	fmt.Println("等号...")
SVIP:
	fmt.Println("进入...")
```





## 运算符与进制

### 运算符

> 运算符用于在程序运行时执行数学或逻辑运算。

#### 算数运算符

| 运算符 | 描述 |
| :----: | :--: |
|   +    | 相加 |
|   -    | 相减 |
|   *    | 相乘 |
|   /    | 相除 |
|   %    | 求余 |

**注意：** `++`（自增）和`--`（自减）在Go语言中是单独的语句，并不是运算符。

#### 关系运算符

| 运算符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
|   ==   |    检查两个值是否相等，如果相等返回 True 否则返回 False。    |
|   !=   |  检查两个值是否不相等，如果不相等返回 True 否则返回 False。  |
|   >    |  检查左边值是否大于右边值，如果是返回 True 否则返回 False。  |
|   >=   | 检查左边值是否大于等于右边值，如果是返回 True 否则返回 False。 |
|   <    |  检查左边值是否小于右边值，如果是返回 True 否则返回 False。  |
|   <=   | 检查左边值是否小于等于右边值，如果是返回 True 否则返回 False。 |

#### 逻辑运算符

| 运算符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
|   &&   | 逻辑 AND 运算符。 如果两边的操作数都是 True，则为 True，否则为 False。 |
|  \|\|  | 逻辑 OR 运算符。 如果两边的操作数有一个 True，则为 True，否则为 False。 |
|   !    | 逻辑 NOT 运算符。 如果条件为 True，则为 False，否则为 True。 |

#### 位运算符

位运算符对整数在内存中的二进制位进行操作。

| 运算符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
|   &    |    参与运算的两数各对应的二进位相与。 （两位均为1才为1）     |
|   \|   |  参与运算的两数各对应的二进位相或。 （两位有一个为1就为1）   |
|   ^    | 参与运算的两数各对应的二进位相异或，当两对应的二进位相异时，结果为1。 （两位不一样则为1） |
|   <<   | 左移n位就是乘以2的n次方。 “a<<b”是把a的各二进位全部左移b位，高位丢弃，低位补0。 |
|   >>   | 右移n位就是除以2的n次方。 “a>>b”是把a的各二进位全部右移b位。 |

#### 赋值运算符

| 运算符 |                      描述                      |
| :----: | :--------------------------------------------: |
|   =    | 简单的赋值运算符，将一个表达式的值赋给一个左值 |
|   +=   |                  相加后再赋值                  |
|   -=   |                  相减后再赋值                  |
|   *=   |                  相乘后再赋值                  |
|   /=   |                  相除后再赋值                  |
|   %=   |                  求余后再赋值                  |
|  <<=   |                   左移后赋值                   |
|  >>=   |                   右移后赋值                   |
|   &=   |                  按位与后赋值                  |
|  \|=   |                  按位或后赋值                  |
|   ^=   |                 按位异或后赋值                 |





### 进制



### 单位

&emsp;&emsp;由于计算机中本质上所有的东西以为二进制存储和操作的，为了方便对于二进制值大小的表示，所以就搞了一些单位，例如：流量还有多少M、硬盘容量有1T、计算机8G内存等、宽带是200M、千兆网络等。计算机中表示对于二进制大小的常见单位有：

- **b（bit），位**

    > 表示二进制有多少位，例如：

    ```shell
    01101     		# 就是 5位 = 5b      
    011011010 		# 就是 9位 = 9b
    ```

- **B（byte），字节**

    > 8 位就是 1 个字节，例如:

    ```shell
    10100101                # 就是 8位 = 8b = 1B= 1个字节  
    1010010110100101        # 就是 16位 = 16b = 2B= 2个字节
    ```

- **KB（Kilobyte），千字节**

    > 1024个字节就是1千字节（1KB），即： 

    ```shell
    1 KB = 1024 B = 1024*8 b
    ```

- **M（Megabyte），兆**

    > 1024个千字节就是1兆（1M)，即：

    ```shell
    1M = 1024 KB = 1024 * 1024 B = 1024 * 1024 * 8 b
    ```

- **G（Gigabyte），千兆**

    > 1024个兆就是1千兆（1G)  ,即：

    ```shell
    1G = 1024 M = 1024 * 1024 KB = 1024 * 1024 * 1024 B = 1024 * 1024 * 1024 * 8 b
    ```

- **T（Terabyte），万亿字节**

    ```shell
    1024个G就是1T
    ```

…其他更大单位 PB/EB/ZB/YB/BB/NB/DB 不再赘述。






## 数据类型
在 Go 编程语言中，数据类型用于声明函数和变量。
数据类型的出现是为了把数据分成所需内存大小不同的数据，编程的时候需要用大数据的时候才需要申请大内存，就可以充分利用内存。
Go 语言按类别有以下几种数据类型：

- **数字类型**：

    > 整型 int 和浮点型 float32、float64，Go 语言支持整型和浮点型数字，并且支持复数，其中位的运算采用补码。

- **字符串类型**：
    > 字符串就是一串固定长度的字符连接起来的字符序列。Go 的字符串是由单个字节连接起来的。
    > Go 语言的字符串的字节使用 UTF-8 编码标识 Unicode 文本。

- **布尔类型**：
    > 布尔型的值只可以是常量 true 或者 false。一个简单的例子：`var b bool = true`
    > 在 Go 中，布尔值的类型为 bool，值是 true 或 false，默认为 false。
    > ```go
    > //示例代码
    > var isActive bool  // 全局变量声明
    > var enabled, disabled = true, false  // 忽略类型的声明
    > func test() {
    >     var available bool  // 一般声明
    >     valid := false      // 简短声明
    >     available = true    // 赋值操作
    > }
    > ```

- **派生类型**：
    ```go
    指针类型（Pointer）
    数组类型
    结构化类型(struct)
    Channel 类型
    函数类型
    切片类型
    接口类型(interface)
    Map 类型
    ```



### 数字类型

> Go 也有基于架构的类型，例如：int、uint 和 uintptr。

|  类型  |                             描述                             |
| :----: | :----------------------------------------------------------: |
| uint8  |                  无符号 8 位整型 (0 到 255)                  |
| uint16 |                无符号 16 位整型 (0 到 65535)                 |
| uint32 |              无符号 32 位整型 (0 到 4294967295)              |
| uint64 |         无符号 64 位整型 (0 到 18446744073709551615)         |
|  int8  |                有符号 8 位整型 (-128 到 127)                 |
| int16  |              有符号 16 位整型 (-32768 到 32767)              |
| int32  |         有符号 32 位整型 (-2147483648 到 2147483647)         |
| int64  | 有符号 64 位整型 (-9223372036854775808 到 9223372036854775807) |



### 浮点类型

|   类型    |         描述          |
| :-------: | :-------------------: |
|  float32  | IEEE-754 32位浮点型数 |
|  float64  | IEEE-754 64位浮点型数 |
| complex64 |    32 位实数和虚数    |
| complex64 |    64 位实数和虚数    |



### 其他数字类型
|  类型   |             描述             |
| :-----: | :--------------------------: |
|  byte   |          类似 uint8          |
|  rune   |          类似 int32          |
|  uint   |         32 或 64 位          |
|   int   |       与 uint 一样大小       |
| uintptr | 无符号整型，用于存放一个指针 |



### 注意：

- go 1.9版本对于数字类型，无需定义 int 及 float32、float64，系统会自动识别。
    ```go
    package main
    import "fmt"
    
    func main() {
       var a = 1.5
       var b =2
       fmt.Println(a,b)
    }
    // 1.5 2
    ```



## 变量与常量

### 变量



```go
var identifier type
// 可以一次声明多个变量：
var identifier1, identifier2 type
```



#### 变量声明

第一种，指定变量类型，如果没有初始化，则变量默认为零值。





## 字符串连接

Go 语言的字符串可以通过 **+** 实现：

```go
package main
import "fmt"
func main() {
    fmt.Println("Google" + "Runoob")
}
// GoogleRunoob
```





字符串去除空格和换行符

```go
package main  
  
import (  
    "fmt"  
    "strings"  
)  
  
func main() {  
    str := "这里是 www\n.runoob\n.com"  
    fmt.Println("-------- 原字符串 ----------")  
    fmt.Println(str)  
    // 去除空格  
    str = strings.Replace(str, " ", "", -1)  
    // 去除换行符  
    str = strings.Replace(str, "\n", "", -1)  
    fmt.Println("-------- 去除空格与换行后 ----------")  
    fmt.Println(str)  
}

// -------- 原字符串 ----------
// 这里是 www
// .runoob
// .com
// -------- 去除空格与换行后 ----------
// 这里是www.runoob.com
```





## 异常捕捉

Go语言处理异常不同于其他语言处理异常的方式：

```go
// 传统语言处理异常：
try 
catch
finally

// go 语言处理异常：
引入了defer、panic、recover
1.Go程序抛出一个panic异常，在defer中通过recover捕获异常，然后处理
```



### defer与recover捕获异常

```go
package main
import "fmt"
func test() {
    //在函数退出前，执行defer
    //捕捉异常后，程序不会异常退出
    defer func() {
        err := recover() //内置函数，可以捕捉到函数异常
        if err != nil {
            //这里是打印错误，还可以进行报警处理，例如微信，邮箱通知
            fmt.Println("err错误信息：", err)
        }
    }()
    //如果没有异常捕获，直接报错panic，运行时出错
    num1 := 10
    num2 := 0
    res := num1 / num2
    fmt.Println("res结果：", res)
}
func main() {
    test()
    fmt.Println("如果程序没退出，就走我这里")
}
```



