----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# 学习 vue 前的准备工作

## 起步
- 扎实的 **HTML/CSS/Javascript** 基本功，这是前置条件。
- 不要用任何的构建项目工具，只用最简单的 `<script>`，把教程里的例子模仿一遍，理解用法。**不推荐上来就直接用 `vue-cli`  构建项目，尤其是如果没有 `Node/Webpack` 基础。**



## 什么是ECMAScript，以及es6的诞生？
- 1997年 ECMAScript 1.0 诞生
- 1999年12月 ECMAScript 3.0诞生，它 是一个巨大的成功，在业界得到了广泛的支持，它奠定了JS的基本语法，被其后版本完全继承。直到今天，我们一开始学习JS，其实就是在学3.0版的语法
- 2000年的ECMAScript4.0是当下ES6的前身，但由于这个版本太过激烈，对ES3做了彻底升级，所以暂时被“和谐”了
- 2009年12月，ECMAScript5.0版正式发布。ECMA专家组预计ECMAScript的第五个版本会在2013年中期到2018年作为主流的开发标准。2011年6月，ES5.1版发布，并且成为ISO国际标准
- 2013年，ES6草案冻结，不再添加新的功能，新的功能将被放到ES7中；2015年6月，ES6正式通过，成为国际标准

&emsp;&emsp;好的，介绍 es6 的诞生，如果感兴趣的同学可以查看 [ECMAScript 6 入门](http://es6.ruanyifeng.com/)，我们简单来学几个 es6 的语法，仅仅的只是为了后面咱们vue的课程做课前准备：



## es6 填的语法坑

### let 和 const

&emsp;&emsp;es6 新增了 let 命令，用来声明变量。它的用法类似于 var，但是**所声明的变量，只在 let 命令所在的代码块内有效。**

```javascript
var a = [];
for (var i = 0; i < 10; i++) {
  a[i] = function () {
    console.log(i);
  };
}
a[6]();
// 输出结果:10
```

&emsp;&emsp;上面代码中，变量 `i` 是 var 命令声明的，在全局范围内都有效，所以全局只有一个变量 `i`。每一次循环，变量 `i` 的值都会发生改变，而**循环内被赋给数组 `a` 的函数内部的`console.log(i)` ，里面的 `i` 指向的就是全局的 `i`**。也就是说，所有数组`a`的成员里面的`i`，指向的都是同一个`i`，导致运行时输出的是最后一轮的`i`的值，也就是 10
&emsp;&emsp;如果使用`let`，声明的变量仅在块级作用域内有效，最后输出的是 6

```javascript
var a = [];
for (let i = 0; i < 10; i++) {
  a[i] = function () {
    console.log(i);
  };
}
a[6]();

// 输出结果:6
```

上面代码中，变量`i`是 let声明的，当前的`i`只在本轮循环有效，所以每一次循环的`i`其实都是一个新的变量，所以最后输出的是`6`。你可能会问，如果每一轮循环的变量`i`都是重新声明的，那它怎么知道上一轮循环的值，从而计算出本轮循环的值？这是因为 JavaScript 引擎内部会记住上一轮循环的值，初始化本轮的变量`i`时，就在上一轮循环的基础上进行计算







## 前端框架和库的区别
- **框架**：是一套完整的解决方案；对项目的侵入性较大，项目如果需要重新更换框架，需要重新架构整个项目
- **库**： 提供某个小功能，对项目侵入性小，如果某个库无法完成某些需求，可以很容易的切换到其他库实现需求



### 功能上的不同
- **jquery库**：包含 `DOM(操作DOM)+请求`，就是一块功能。
- **art-template库**：模板引擎渲染，高性能的渲染DOM  (我们后端的一种模板  跟python的模板类似)
- **框架**：大而全的概念，简易的 `DOM体验+请求处理+模板引擎`
> 库就是一个小套餐，框架就是全家桶。



### 代码上的不同

> 一般使用库的代码，是调用某个函数或者直接使用抛出来的对象，我们自己处理库中的代码。 
> 一般使用框架，其框架本身提供的好的成套的工具帮我们运行我们编写好的代码。



### 框架的使用

- 初始化自身的一些行为
- 执行你所编写的代码
- 释放一些资源





## nodejs
- 去官网https://nodejs.org/en/download/ 下载 安装(傻瓜式安装)

- 打开终端 cmd : 执行`node -v` 如果出现版本号，证明安装node成功 ，跟安装python雷同

- 下载完node之后，会自带包管理器 npm，好比 是python中 pip3包管理器。pip3 install xxx

- 使用npm

    - `npm init --yes` 自动生成一个package.json文件( 管理包 )

        ```javascript
        {
            "name": "vue_lesson",
            "version": "1.0.0",
            "description": "这是我的vue的第一个项目",
            "main": "index.js",
            "scripts": {
              "test": "echo "Error: no test specified" && exit 1"
            },
            "author": "mjj",
            "license": "ISC",
            "dependencies": {				
              "vue": "^2.5.16"
            }
        }
        ```

    - 2.下载依赖包

        ```shell
        npm install vue --save
        npm install jquery@2.1 --save			# @后面跟的是你想下载的版本号
        ```

    - 卸载包

        ```shell
        npm uninstall vue --save
        ```

    - 4.下载项目所有的依赖包

        ```shell
        npm install
        ```



## MVVM 

&emsp;&emsp;MVVM 是前端视图层的概念，主要关注于视图层分离，也就是说 MVVM 把前端的视图层分成了三部分：`Model`、`View`、`VM ViewModel`






# vue的起步

&emsp;&emsp;Vue (读音 `/vjuː/`，类似于 **view**) 是一套用于构建用户界面的**渐进式框架**。与其它大型框架不同的是，Vue 被设计为可以**自底向上逐层应用**。Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。
&emsp;&emsp;在 vue 中，一个核心的概念，就是让用户不再操作 DOM 元素，解放了用户的双手，让程序员可以更多的时间去关注业务逻辑



## 安装

### 兼容性

&emsp;&emsp;Vue **不支持** `IE8` 及以下版本，因为 Vue 使用了 IE8 无法模拟的 `ECMAScript 5` 特性。但它支持所有兼容 `ECMAScript 5` 的浏览器。在使用 Vue 时，我们推荐在你的浏览器上安装 [Vue Devtools](https://github.com/vuejs/vue-devtools#vue-devtools)。它允许你在一个更友好的界面中审查和调试 Vue 应用。

- [开发版本](https://cn.vuejs.org/js/vue.js) : 包含完整的警告和调试模式

- [生产版本](https://cn.vuejs.org/js/vue.min.js) : 删除了警告，33.30KB min+gzip



### 引包

- 对于制作原型或学习，你可以这样使用最新版本：

    ```javascript
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    ```

- 对于生产环境，我们推荐链接到一个明确的版本号和构建文件，以避免新版本造成的不可预期的破坏：

    ```javascript
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.0"></script>
    ```

- 如果你使用原生 ES Modules，这里也有一个兼容 ES Module 的构建文件：

    ```javascript
    <script type="module">
      import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.esm.browser.js'
    </script>
    ```

    



## 创建实例化对象

``` html
<div id="app">
    <h1>{{msg}}</h1>
    <h2>字符串: {{'hello world!'}}</h2>
    <h2>运算式: {{1+1}}</h2>
    <h2>运算式: {{1==1?'真的':'假的'}}</h2>
    <h2>函数的调用:</h2>
</div>

<script>
    var app = new Vue({
        el:'#app',							// 绑定哪块区域的元素
        data:{
            msg:"hello Vue"
        }
    });
    
    // 不建议这么去用,失去了 vue 的优势
    console.log( app );
    console.log( app.$el );					// 会自动将管理块的元素转化为 $变量
    console.log( app.msg );                // data 内的数据都暴露为全局了
</script>
```



### 插值语法

```javascript
/*
{{}}: 模板语法插值
    {{变量}}
    {{1+1}}
    {{'hello'}}
    {{函数的调用}}
    {{1==1?'真的':'假的'}}
*/
```





## 指令系统

```markdown
# 常用
v-text 
v-html 
v-if
v-show
v-for
v-bind
v-on
表单控件的value (看后面)
```



### 条件渲染

#### v-if

&emsp;&emsp;`v-if` 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回 `truthy` 值的时候被渲染。

```html
<div v-if="type === 'A'"> A</div>
<div v-else-if="type === 'B'"> B</div>				<!-- 2.1.0 新增 -->
<div v-else> Not A/B</div>
```



#### v-show

&emsp;&emsp;另一个用于根据条件展示元素的选项是 `v-show` 指令。用法大致一样：

```html
<h1 v-show="ok">Hello!</h1>
```

&emsp;&emsp;不同的是带有 `v-show` 的元素始终会被渲染并保留在 DOM 中。`v-show` 只是简单地切换元素的 CSS 属性 `display`。

```html
<div id="app">
    <div v-show="show">v-show="show"</div>
    <button v-on:click="clickHandler">切换</button>
</div>

<script>
    var app = new Vue({
        el:'#app',							
        data:{
            show:true
        },
        methods:{
            clickHandler:function(){
                this.show = !this.show;
            }
        }
    });	
</script>
```



```markdown
# 注意，v-show 不支持 <template> 元素，也不支持 v-else。
```



#### v-if 和 v-show 的区别

&emsp;&emsp;`v-if` 是"真正"的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。`v-if` 也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。
&emsp;&emsp;相比之下，`v-show` 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。
&emsp;&emsp;一般来说，**`v-if` 有更高的切换开销，而 `v-show` 有更高的初始渲染开销。**因此，如果需要非常频繁地切换，则使用 `v-show` 较好；如果在运行时条件很少改变，则使用 `v-if` 较好。

```html
<div id="app">
    <div v-if="show">v-if="show"</div>
    <button v-on:click="clickHandler">切换</button>
</div>

<script>
    var app = new Vue({
        el:'#app',							// 绑定哪块区域的元素
        data:{
            show:false
        },
        methods:{
            clickHandler:function(){
                this.show = !this.show;
            }
        }
    });	
</script>
```



### 元素绑定

#### v-on
&emsp;&emsp;vue 中使用 `v-on:click` 对当前 DOM 绑定 click 事件 注意:所有的原 js 的事件使用 `v-on` 都可以绑定:

```html
<div id="app">
    <h1> The button above has been clicked {{ counter }} times. </h1>
    <button v-on:click="clickHandler">切换</button>		 <!-- 绑定事件处理 -->
    <button v-on:click="say('what')">Say what</button>
    <button v-on:click="counter += 1">Add 1</button>
</div>

<script>
    var app = new Vue({
        el:'#app',	
        data:{
            counter: 0,
        },
        methods:{
            clickHandler:function(){
                alert( "绑定无参数方法!" );
            },
            say: function (message) {
                alert(message+" 绑定有参数方法!");
            }
        }
    });	
</script>
```



##### 事件修饰符

> 修饰符是以半角句号 `.` 指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。

- `.stop`
- `.prevent`
- `.capture`
- `.self`
- `.once`
- `.passive`

```html
<!-- 阻止单击事件继续传播 -->
<a v-on:click.stop="doThis"></a>

<!-- 提交事件不再重载页面 -->
<form v-on:submit.prevent="onSubmit"></form>

<!-- 修饰符可以串联 -->
<a v-on:click.stop.prevent="doThat"></a>

<!-- 只有修饰符 -->
<form v-on:submit.prevent></form>

<!-- 添加事件监听器时使用事件捕获模式 -->
<!-- 即内部元素触发的事件先在此处理，然后才交由内部元素进行处理 -->
<div v-on:click.capture="doThis">...</div>

<!-- 只当在 event.target 是当前元素自身时触发处理函数 -->
<!-- 即事件不是从内部元素触发的 -->
<div v-on:click.self="doThat">...</div>



<!-- 2.1.4 新增 -->
<!-- 点击事件将只会触发一次 -->
<!-- .once 修饰符还能被用到自定义的组件事件上。 -->
<a v-on:click.once="doThis"></a>

<!-- 2.3.0 新增 -->
<!-- 滚动事件的默认行为 (即滚动行为) 将会立即触发 -->
<!-- 而不会等待 `onScroll` 完成  -->
<!-- 这其中包含 `event.preventDefault()` 的情况 -->
<div v-on:scroll.passive="onScroll">...</div>
```

&emsp;&emsp;使用修饰符时，顺序很重要；相应的代码会以同样的顺序产生。因此，用 `v-on:click.prevent.self`会阻止**所有的点击**，而 `v-on:click.self.prevent` 只会阻止对元素自身的点击。

&emsp;&emsp;不要把 `.passive` 和 `.prevent` 一起使用，因为 `.prevent` 将会被忽略，同时浏览器可能会向你展示一个警告。请记住，`.passive` 会告诉浏览器你*不*想阻止事件的默认行为。



##### v-on 缩写

```html
<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>

<!-- 缩写 -->
<a @click="doSomething">...</a>
```







#### v-bind

> 用于响应式地更新 HTML 特性

```html
<a v-bind:href="url">...</a>
```

在这里 `href` 是参数，告知 `v-bind` 指令将该元素的 `href` 特性与表达式 `url` 的值绑定。



##### v-bind 缩写

```html
<!-- 完整语法 -->
<a v-bind:href="url">...</a>

<!-- 缩写 -->
<a :href="url">...</a>
```











































