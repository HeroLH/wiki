----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Webpack 基本使用 {#index}

[TOC]











--------------------------------------------

## 简介

[中文官网](https://webpack.docschina.org/)



### 什么是 webpack

> At its core, webpack is a static module bundler for modern JavaScript applications.
> 本质上， webpack 是一个现代 JavaScript 应用程序的静态模块打包器(module bundler)。

-  当 webpack 处理应用程序时， 它会递归地构建一个依赖关系图( dependency graph ) ， 其中包含应用程序需要的每个模块， 然后将所有这些模块打包成一个或多个 bundle.
- Webpack 是当下最热门的前端资源模块化管理和打包工具， 它可以将许多松散耦合的模块按照依赖和规则打包成符合生产环境部署的前端资源。还可以将按需加载的模块进行代码分离，等到实际需要时再异步加载。通过 loader  转换， 任何形式的资源都可以当做模块， 比如 `Commons JS、AMD、ES 6、CSS、JSON、Coffee Script、LESS` 等；
- 伴随着移动互联网的大潮， 当今越来越多的网站已经从网页模式进化到了 WebApp 模式。它们运行在现代浏览器里， 使用 HTML 5、CSS 3、ES6 等新的技术来开发丰富的功能， 网页已经不仅仅是完成浏览器的基本需求； WebApp 通常是一个 SPA (单页面应用) ， 每一个视图通过异步的方式加载，这导致页面初始化和使用过程中会加载越来越多的 JS 代码，这给前端的开发流程和资源组织带来了巨大挑战。
- 前端开发和其他开发工作的主要区别，首先是==前端基于多语言、多层次的编码和组织工作==，其次前端产品的交付是基于浏览器的，这些资源是通过增量加载的方式运行到浏览器端，如何在开发环境组织好这些碎片化的代码和资源，并且保证他们在浏览器端快速、优雅的加载和更新，就需要一个模块化系统，这个理想中的模块化系统是前端工程师多年来一直探索的难题。



### 模块化的演进

#### Script标签

```html
<script src = "module1.js"></script>
<script src = "module2.js"></script>
<script src = "module3.js"></script>
```

&emsp;&emsp;这是最原始的 JavaScript 文件加载方式，如果把每一个文件看做是一个模块，那么他们的接口通常是暴露在全局作用域下，也就是定义在 window 对象中，不同模块的调用都是一个作用域。这种原始的加载方式暴露了一些显而易见的弊端：
- 全局作用域下容易造成变量冲突
- 文件只能按照`<script>`的书写顺序进行加载
- 开发人员必须主观解决模块和代码库的依赖关系
- 在大型项目中各种资源难以管理，长期积累的问题导致代码库混乱不堪



#### CommonsJS

&emsp;&emsp;服务器端的 NodeJS 遵循 CommonsJS 规范，该规范核心思想是允许模块通过 require 方法来同步加载所需依赖的其它模块，然后通过 `exports` 或 `module.exports` 来导出需要暴露的接口。

```html
require("module");
require("../module.js");
export.doStuff = function(){};
module.exports = someValue;
```

##### 优点：
- 服务器端模块便于重用
- NPM中已经有超过45万个可以使用的模块包
- 简单易用



##### 缺点：

- 同步的模块加载方式不适合在浏览器环境中，同步意味着阻塞加载，浏览器资源是异步加载的
- 不能非阻塞的并行加载多个模块



##### 实现：

- 服务端的 NodeJS
- Browserify，浏览器端的 CommonsJS 实现，可以使用 NPM 的模块，但是编译打包后的文件体积较大
- modules-webmake，类似Browserify，但不如Browserify灵活
- wreq，Browserify的前身



#### AMD

&emsp;&emsp;Asynchronous Module Definition 规范其实主要一个主要接口 `define(id?,dependencies?,factory);` 它要在声明模块的时候指定所有的依赖 dependencies ，并且还要当做形参传到 factory 中，对于依赖的模块提前执行。

```html
define("module",["dep1","dep2"],functian(d1,d2){
	return someExportedValue;
});
require（["module","../file.js"],function(module，file){});
```



##### 优点

- 适合在浏览器环境中异步加载模块
- 可以并行加载多个模块



##### 缺点

- 提高了开发成本，代码的阅读和书写比较困难，模块定义方式的语义不畅
- 不符合通用的模块化思维方式，是一种妥协的实现



##### 实现

- RequireJS
- curl



#### CMD

&emsp;&emsp;Commons Module Definition 规范和 AMD 很相似，尽保持简单，并与 CommonsJS 和 NodeJS 的 Modules 规范保持了很大的兼容性。

```html
define(function(require,exports,module){
	var $=require("jquery");
	var Spinning = require("./spinning");
	exports.doSomething = ...;
	module.exports=...;
});
```

##### 优点：

- 依赖就近，延迟执行
- 可以很容易在NodeJS中运行缺点
- 依赖SPM打包，模块的加载逻辑偏重



##### 实现

- Sea.js
- coolie



#### ES6模块

&emsp;&emsp;EcmaScript 6 标准增加了 JavaScript 语言层面的模块体系定义。ES 6 模块的设计思想， 是尽量静态化， 使编译时就能确定模块的依赖关系， 以及输入和输出的变量。Commons JS 和 AMD 模块，都只能在运行时确定这些东西。

```html
import "jquery"
export function doStuff(){}
module "localModule"{}
```



##### 优点

- 容易进行静态分析
- 面向未来的EcmaScript标准

##### 缺点

- 原生浏览器端还没有实现该标准
- 全新的命令，新版的Node JS才支持

##### 实现

- Babel



#### 大家期望的模块

系统可以兼容多种模块风格， 尽量可以利用已有的代码， 不仅仅只是JavaScript模块化， 还有CSS、图片、字体等资源也需要模块化。



## 基本使用

### hello World

#### 准备工作

我们创建如下文件与文件夹：

```html
.
├── dist
└── src
    ├── commonJS.js
    ├── es6.js
    └── main.js
├── index.html
```

- `dist` 文件夹

    > 用来存放打包后的文件

- `src` 文件夹

    > 用来存在我们写的源文件

    - `main.js` 项目的入口文件
    - `es6.js` 和 `common.js` 使用不同打包规范的具体业务实现。

- `index.html` 浏览器打开展示的首页 html。

- `package.json` 通过 `npm init` 生成，npm 包管理的文件



#### 打包

```shell
webpack ./src/main.js ./dist/bundle.js
```



#### 使用打包后的文件

```html
<script src="./dist/bundle.js"></script>
```



### loader

&emsp;&emsp;loader 是 webpack 中一个十分核心的概念。在开发过程中，我们不仅有基础的 js 代码处理，还需要加载 css，图片，也包括一些高级的将 ES6 转化为 ES5 代码，将 scss、less 转化为css，将 .jsx、.vue 文件转化为 js 文件等。对于 webpack 本身的能力来说，对于这些转化是不支持的，但是给 webpack 扩展对应的 loader 即可。[中文文档](https://webpack.docschina.org/loaders/)



#### 使用过程

- 通过 npm 安装 需要使用的 loader
- 在 `webpack.config.js` 中的 modules 关键字下进行设置

大部分的 loader 我们都能从 webpack 的官网中找到，并学习对应的语法



#### 样式相关

##### style-loader

> 将模块导出的内容作为样式并添加到 DOM 中

首先，你需要安装 `style-loader`：

```console
npm install --save-dev style-loader
```

推荐将 `style-loader` 与 [`css-loader`](https://webpack.docschina.org/loaders/css-loader/) 一起使用

然后把 loader 添加到你的 `webpack` 配置中。比如：

**style.css**

```css
body {
  background: green;
}
```

**component.js**

```js
import './style.css';
```

**webpack.config.js**

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
};
```



##### css-loader

> 加载 CSS 文件并解析 import 的 CSS 文件，最终返回 CSS 代码

首先，你需要先安装 `css-loader`：

```console
npm install --save-dev css-loader
```

然后把 loader 引用到你 `webpack` 的配置中。如下所示：

**file.js**

```js
import css from "file.css";
```

**webpack.config.js**

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
};
```



##### less-loader

首先，你需要先安装 `less` 和 `less-loader`：

```console
$ npm install less less-loader --save-dev
```

然后将该 loader 添加到 `webpack` 的配置中去，例如：

**webpack.config.js**

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.less$/i,
        loader: [
          // compiles Less to CSS
          "style-loader",
          "css-loader",
          "less-loader",
        ],
      },
    ],
  },
};
```

接着使用你习惯的方式运行 `webpack`。





#### 文件

##### url-loader

> 与 `file-loader` 类似，但是如果文件大小小于一个设置的值，则会返回 [data URL](https://tools.ietf.org/html/rfc2397)

首先，你需要安装 `url-loader`：

```console
npm install url-loader --save-dev
```

`url-loader` 功能类似于 [`file-loader`](https://webpack.docschina.org/loaders/file-loader/), 但是在文件大小（单位为字节）低于指定的限制时，可以返回一个 DataURL。

**index.js**

```js
import img from './image.png';
```

**webpack.config.js**

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpg|gif)$/i,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192,
            },
          },
        ],
      },
    ],
  },
};
```

然后通过你的首选方法运行 `webpack`。



##### file-loader

> 将文件保存至输出文件夹中并返回（相对）URL

首先，你需要安装 `file-loader`：

```console
$ npm install file-loader --save-dev
```

在一个 bundle 文件中 import（或 `require`）目标文件：

**file.js**

```js
import img from './file.png';
```

然后，在 `webpack` 配置中添加 loader。例如：

**webpack.config.js**

```js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader',
          },
        ],
      },
    ],
  },
};
```

然后，通过你喜欢的方式运行 `webpack`。将 `file.png` 作为一个文件，发送到输出目录， （如果指定了配置项，则使用指定的命名约定） 并返回文件的 public URI。

> 默认情况下，生成文件的文件名，是文件内容的哈希值，并会保留所引用资源的原始扩展名。





#### ES6 => ES5

在 webpack 配置对象中，需要将 babel-loader 添加到 module 列表中，就像下面这样：

```javascript
module: {
  rules: [
    {
      test: /\.m?js$/,
      exclude: /(node_modules|bower_components)/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env']
        }
      }
    }
  ]
}
```



### plugin

#### BannerPlugin

> webpack 自带的插件，为打包的文件添加版权声明

```json
const webpack = require('webpack')

plugins: [
        new webpack.BannerPlugin("最终解释权归 xxx 所有")
    ]
```

重新打包，查看 bundle.js 文件的头部，看到如下信息：

```js
/*! 最终解释权归 xxx 所有 */
/******/ (function(modules) { // webpackBootstrap
......
```



#### HtmlWebpackPlugin

>在真实发布项目时，发布的是 dist 文件夹中的内容，但是 dist 文件夹中如果没有index.html，那么打包的 js 文件就没有意义了。HtmlWebpackPlugin 会自动生成一个 index.html 文件，将打包的 js 文件，自动通过 script 标签 插入到 body 中。

##### 安装

```shell
npm install html-webpack-plugin -save-dev
```



##### 配置

```json
const htmlWebpackPlugin = require('html-webpack-plugin')

plugins: [
    new htmlWebpackPlugin({
        template: "index.html"
    })
]
```

template 表示根据什么模板来生成 index.html

另外，我们需要删除之前在 output 中添加的 publicPath 属性，否则插入的 script 标签中的 src 可能会有问题



#### uglifyJsPlugin

> 对打包的 js 文件进行压缩

##### 安装

```shell
npm install uglifyjs-webpack-plugin@1.1.1 -save-dev

```



##### 配置

```json
const uglifyJsPlugin = require('uglifyjs-webpack-plugin')

plugins: [
    new uglifyJsPlugin()
]
```



### 使用 Vue

```shell
npm install vue@2.5.21 --save
```

- runtime-only

    > 代码中不能有任何的 template

- runtime-compiler

    > 代码中可以有 template，因为有 compiler 可以用于编译 template

```shell
npm install vue-loader vue-template-compiler --save-dev
```



### 搭建本地服务器

webpack 提供了一个可选的本地开发服务器，这个本地服务器基于node.js 搭建，内部使用 express 框架，可以实现我们想要的让浏览器自动刷新显示我们修改后的结果，不过他是个独立的模块，在 webpack 中使用之前需要先安装它：

```shell
npm install vue-loader webpack-dev-server@2.9.1 --save-dev
```



#### 配置

##### `webpack.config.js`

```shell
devServer: {
	contentBase: "./dist",
	inline: true
}
```

- contentBase

    > 为拿个文件夹提供本地服务，默认是根文件夹

- `port`：端口号

- `inline`：页面实时刷新

- `historyApiFallBack`：在 SPA 页面中， 依赖 HTML 的 history 模式



##### package.json

```json
"scripts": {
    ...
    "dev": "webpack-dev-server"
  },
```

``"dev": "webpack-dev-server --open"`` 自动打开浏览器



### 配置分环境

#### 安装

```shell
npm install webpack-merge --save-dev
```



#### 配置

在 package.json 中修改:

```json
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack --config ./build/prod.config.js",
    "dev": "webpack-dev-server --config ./build/dev.config.js"
},
```



#### 使用

```json
const webpackMerge = require(`webpack-merge`)
const baseConfig = require('./base.config')

module.exports = webpackMerge(baseConfig, {
    plugins: [
        new uglifyJsPlugin(),
    ],
})
```

