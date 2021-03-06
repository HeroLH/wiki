# 目录 {#index}

[TOC]











--------------------------------------------
## 一、先行知识  

​	在说Web服务器之前，先说说线程、进程、以及并发连接数。

### 1.进程与线程
> ​	进程是具有一定独立功能的程序，关于某个数据集合上的一次运行活动，进程是系统进行资源分配和调度的一个独立单位。

​	从逻辑角度来看，多线程的意义在于一个应用程序（进程）中，有多个执行部分可以同时执行。但**操作系统并没有将多个线程看做多个独立的应用来实现，而是作为进程来调度和管理以及资源分配**。这就是进程和线程的重要区别，进程和线程的主要差别在于:

- 进程有独立的地址空间，一个进程崩溃后，在保护模式下不会对其它进程产生影响，而线程只是一个进程中的不同执行路径。
- 线程有自己的堆栈和局部变量，但线程之间没有单独的地址空间，一个线程死掉就等于整个进程死掉，所以多进程的程序要比多线程的程序健壮，但在进程切换时，耗费资源较大，效率要差一些。但对于一些要求同时进行并且又要共享某些变量的并发操作，只能用线程，不能用进程。

### 2.并发连接数

- **什么是最大并发连接数呢？**

	最大并发连接数是服务器同一时间能处理最大会话数量。

- **何为会话？**

	我们打开一个网站就是一个客户端浏览器与服务端的一个会话，而我们浏览网页是基于http协议。

- **HTTP协议如何工作？**

	HTTP支持两种建立连接的方式：非持久连接和持久连接(HTTP1.1默认的连接方式为持久连接)。

- **浏览器与Web服务器之间将完成下列7个步骤**
	建立TCP连接
	Web浏览器向Web服务器发送请求命令
	Web浏览器发送请求头信息
	Web服务器应答
	Web服务器发送应答头信息
	Web服务器向浏览器发送数据
	Web服务器关闭TCP连接

​       一般情况下，一旦Web服务器向浏览器发送了请求数据，它就要关闭TCP连接，但是浏览器一般其头信息加入了这行代码 ***Connection:keep-alive***，TCP连接在发送后将仍然保持打开状态，于是，浏览器可以继续通过相同的连接发送请求。保持连接目的，节省了为每 个请求建立新连接所需的时间，还节约了网络带宽。

### 3.并发连接数的计算方法

​        用户下载服务器上的文件，则为一个连接，用户文件下载完毕后这个连接就消失了。有时候用户用迅雷的多线程方式下载的话，这一个用户开启了5个线程的话，就算是5个连接。

​        用户打开你的页面，就算停留在页面没有对服务器发出任何请求，那么在用户打开页面以后的15分钟内也都要算一个在线。上面的情况用户继续打开同一个网站的其他页面，那么在线人数按照用户最后一次点击（发出请求）以后的15分钟计算，在这个15分钟内不管用户怎么点击（包括新窗口打开）都还是一人在线。

​         当用户打开页面然后正常关闭浏览器，用户的在线人数也会马上清除。











--------------------------------------------
## 二、Web服务器提供服务的方式

 	Web服务器由于要同时为多个客户提供服务，就必须使用某种方式来支持这种多任务的服务方式。一般情况下可以有以下三种方式来选择，多进程方式、多线程方式及异步方式。其中，多进程方式中服务器对一个客户要使用一个进程来提供服务，由于在操作系统中，生成一个进程需要进程内存复制等额外的开销，这样在客户较多时的性能就会降低。为了克服这种生成进程的额外开销，可以使用多线程方式或异步方式。在多线程方式中，使用进程中的多个线程提供服务， 由于线程的开销较小，性能就会提高。事实上，不需要任何额外开销的方式还是异步方式，它使用非阻塞的方式与每个客户通信，服务器使用一个进程进行轮询就行了。

​       虽然异步方式最为高效，但它也有自己的缺点。因为**异步方式下，多个任务之间的调度是由服务器程序自身来完成的，而且一旦一个地方出现问题则整个服务器就会出现问题**。因此，向这种服务器增加功能，一方面要遵从该服务器自身特定的任务调度方式，另一方面要确保代码中没有错误存在，这就限制了服务器的功能，使得异步方式的Web服务器的效率最高，但功能简单，如Nginx服务器。

​       由于多线程方式使用线程进行任务调度，这样服务器的开发由于遵从标准，从而变得简单并有利于多人协作。然而多个线程位于同一个进程内，可以访问同样的内存空间，因此存在线程之间的影响，并且申请的内存必须确保申请和释放。对于服务器系统来讲，由于它要数天、数月甚至数年连续不停的运转，一点点错误就会逐渐积累而最终导致影响服务器的正常运转，因此很难编写一个高稳定性的多线程服务器程序。但是，不是不能做到, Apache的worker模块就能很好的支持多线程的方式。

​       多进程方式的优势就在于稳定性，因为一个进程退出的时候，操作系统会回收其占用的资源，从而使它不会留下任何垃圾。即便程序中出现错误，由于进程是相互隔离的，那么这个错误不会积累起来，而是随着这个进程的退出而得到清除。Apache的prefork模块就是支持多进程的模块。











--------------------------------------------
## 三、多进程、多线程、异步模式的对比

​     Web服务器总的来说提供服务的方式有三种,多进程方式，多线程的方式，异步方式。其中效率最高的是异步的方式，最稳定的是多进程方式，占用资源较少的是多线程的方式。

1.多进程

​       此种架构方式中，web服务器生成多个进程并行处理多个用户请求，进程可以按需或事先生成。有的web服务器应用程序为每个用户请求生成一个单独的进程来进行响应，不过，一旦并发请求数量达到成千上万时，多个同时运行的进程将会消耗大量的系统资源。（即每个进程只能响应一个请求或多个进程对应多个请求）

优点：

- 最大的优势就在于稳定性，一个进程出错不会影响其它进程。如，服务器同时连接100个请求对就的是100个进程，其中一个进程出错，只会杀死一个进程，还有99个进程继续响应用户请求。每个进程响应一个请求

缺点：

- 进程量大，进程切换次数过多，导致CPU资源使用效率低，每个进程的地址空间是独立的，很多空间中重复的数据，所以内存使用效率低，进程切换由于内核完成，占用CPU资源。

2.多线程

​       在多线程方式中，每个线程来响应一下请求，由于线程之间共享进程的数据，所以线程的开销较小，性能就会提高。

优点：

- 线程间共享进程数据，每个线程响应一个请求，线程切换不可避免（切换量级比较轻量），同一进程的线程可以共享进程的诸多资源，对内存的需求较之进程有很大下降，读可以共享，写不可以共享

缺点：

- 线程快速切换时会带来线程抖动，多线程会导致服务器不稳定

3.异步方式

​       一个进程或线程响应多个请求，不需要任何额外开销的，性能最高，占用资源最少。但也有问题一但进程或线程出错就会导致整个服务器的宕机。