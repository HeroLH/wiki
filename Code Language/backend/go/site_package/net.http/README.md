> *Made By Herolh*

----------------------------------------------

# net/http 的基本使用 {#index}

[TOC]











--------------------------------------------

## 简介

&emsp;&emsp;Go 语言内置的 `net/http` 包十分的优秀，提供了 HTTP 客户端和服务端的实现。



## HTTP 客户端

### 基本的 HTTP/HTTPS 请求

Get、Head、Post 和 PostForm 函数发出 HTTP/HTTPS 请求。

```go
resp, err := http.Get("http://example.com/")
...
resp, err := http.Post("http://example.com/upload", "image/jpeg", &buf)
...
resp, err := http.PostForm("http://example.com/form",
	url.Values{"key": {"Value"}, "id": {"123"}})
```

==程序在使用完 response 后必须关闭回复的主体。==

```go
resp, err := http.Get("http://example.com/")
if err != nil {
	// handle error
}
defer resp.Body.Close()
body, err := ioutil.ReadAll(resp.Body)
// ...
```



## HTTP 服务端

### 默认的 Server

&emsp;&emsp;`ListenAndServe` 使用指定的监听地址和处理器启动一个 HTTP 服务端。处理器参数通常是 nil，这表示采用包变量 `DefaultServeMux` 作为处理器。`Handle` 和 `HandleFunc` 函数可以向 `DefaultServeMux` 添加处理器。

```go
http.Handle("/foo", fooHandler)
http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
})
log.Fatal(http.ListenAndServe(":8080", nil))
```



#### demo

&emsp;&emsp;使用 Go 语言中的 `net/http` 包来编写一个简单的接收 HTTP 请求的 Server 端示例，`net/http` 包是对 net 包的进一步封装，专门用来处理 HTTP 协议的数据。具体的代码如下：

```go
// http server

func sayHello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Hello World！")
}

func main() {
	http.HandleFunc("/", sayHello)
	err := http.ListenAndServe(":9090", nil)
	if err != nil {
		fmt.Printf("http server failed, err:%v\n", err)
		return
	}
}
```



### 自定义 Server

要管理服务端的行为，可以创建一个自定义的 Server：

```go
s := &http.Server{
	Addr:           ":8080",
	Handler:        myHandler,
	ReadTimeout:    10 * time.Second,
	WriteTimeout:   10 * time.Second,
	MaxHeaderBytes: 1 << 20,
}
log.Fatal(s.ListenAndServe())
```











