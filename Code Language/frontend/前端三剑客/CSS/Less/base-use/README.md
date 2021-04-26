----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

## 介绍
&emsp;&emsp;CSS 预处理器是一种脚本语言，可扩展 CSS 并将其编译为常规 CSS 语法，以便可以通过Web浏览器读取。 它提供诸如变量，函数， mixins 和操作等功能，可以构建动态 CSS。
&emsp;&emsp;LESS( Leaner Style Sheets 的缩写 )是一个 CSS 预处理器，可以为网站启用可自定义，可管理和==可重用==的样式表。 LESS 是一种动态样式表语言，扩展了 CSS 的功能。 LESS 也是跨浏览器友好。

[官方中文网站](https://less.bootcss.com/#%E6%A6%82%E8%A7%88)

[](https://www.w3cschool.cn/less/)



### 历史
&emsp;&emsp;2009年 LESS 由 Alexis Sellier 设计。LESS 是一个开源项目。 LESS 的第一个版本是用 Ruby 编写的，在后来的版本中，它被 JavaScript 代替。



### hello world

- 新建一个 `hello.html` 文件

    ```html
    <!doctype html>
    <head>
    	<link rel="stylesheet" href="style.css" type="text/css" />
    </head>
    <body>
    	<h1>Hello World!</h1>
    	<h3>Hi!</h3>
    </body>
    </html>
    ```

- 接下来，让我们创建一个与 CSS 非常相似的文件 `style.less`，唯一的区别是它将以 `.less` 扩展名保存。

    ```less
    @primarycolor: #FF7F50;
    @color:#800080;
    
    h1{
    color: @primarycolor;
    }
    h3{
    color: @color;
    }
    ```

- 使用以下命令将 style.less 文件编译为 style.css :

    ```shell
    lessc style.less style.css
    ```

    当您运行上述命令时，它将自动创建 style.css 文件。 无论何时更改 LESS 文件，都需要在 cmd 中运行上面的命令，然后更新 style.css 文件。运行以上命令时， style.css 文件将具有以下代码:

    ```shell
    h1 {
      color: #FF7F50;
    }
    
    h3 {
      color: #800080;
    }
    ```

    

## less 语言特性