----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# HTML 5 基础使用 {#index}

[TOC]











--------------------------------------------

## 什么是HTML

> 超文本标记语言（Hypertext Markup Language, HTML）

- **HTML 是一个标准,规定了大家怎么写网页**

  本质上是浏览器可识别的规则，我们按照规则写网页，浏览器根据规则渲染我们的网页。
  对于不同的浏览器，对同一个标签可能会有不同的解释。（兼容性问题）

- **HTML是一种标记语言（markup language），它不是一种编程语言。**

    `标记语言 --> 学标签 --> <标签名>`, HTML使用标签来描述网页。

​		

### HTML文件的结构

```shell
<!DOCTYPE html>						# 文档声明
<html>								# html标签
<head>
	# head内常用标签
	# body内常用标签
</head>
<body>
	# body标签(用户在浏览器能看到的内容)
</body>
</html>
```



### 标签

#### 	标签分类1:

- 双标签

    ```html
    <br />
    ```

- 单标签

    ```html
    <h1></h1>
    ```

    

#### 标签分类2:

- **块儿级标签**            
		默认占浏览器宽度, 能设置长和宽, 例如 `h1~h6 div p hr `
	
- **内联标签(行内标签)** 
		根据内容决定长度, 不能设置长和宽,例如 `a img u s i b span`



#### 常用标签

```html
h1~h6
img
a
p
span
div
i
s
u
...
hr
br
特殊符号 &nbsp; &copy; &lt; &gt; &reg; ...
```



#### 标签的嵌套规则

- 行内标签不能嵌套块级标签
- p 标签不能嵌套块级标签( 层会自动跑出来 )





## 主体标签

```html
<html lang="zh-CN"> 
	<!-- 通常为 lang = "en",用于网络蜘蛛，浏览器识别 -->
</html>
```



### head 头部

#### title 标题标记

```html
<title>标题标记</title>
```



#### meta 元信息标记

&emsp;&emsp;提供有关页面的原信息（meta-information）,针对搜索引擎和更新频度的描述和关键词。提供的信息是用户不可见的。



##### name 属性

> 主要用于描述网页，便于搜索引擎机器人查找信息和分类信息用的。

###### 网页作者信息标记

| 属性      | 说明                  |
| --------- | --------------------- |
| author    | 网页作者              |
| generator | 编辑软件, 如 Hbuilder |
| reply-to  | 邮箱联系地址          |

```html
<!--begin-- 网页作者信息标记 ：-->
<meta name="author" content="网页作者"/>
<meta name="generator" content="编辑软件：Hbuilder"/>
<meta name="reply-to" content="邮箱联系地址"/>
<!-- end -- 网页作者信息标记 ：-->
```



###### 网页描述信息标记

| 属性        | 说明             |
| ----------- | ---------------- |
| build       | 网站建立日期     |
| keywords    | HTML基础，关键字 |
| description | 页面描述         |
| robots      | 限制搜索方式     |
| copyright   | 网页版权信息     |

```html
<!--begin-- 网页描述信息标记 ：-->
<meta name="build" content="网站建立日期"/>
<meta name = "keywords" content="HTML基础，关键字" />
<meta name="description" content="页面描述"/>
<meta name="robots" content="All"/>
<!-- robots标签中content值：		限制搜索方式
	All	          ：表示能搜索当前网页及其链接的网页
	Index    ：表示能搜索到当前网页
	Nofollow ：表示不能搜索与当前网页链接的网页
	Noindex  ：表示不能搜索当前网页
	None     ：表示不能搜索当前网页与其链接的网页
-->
<meta name="copyright" content="网页版权信息"/>
<!-- end -- 网页描述信息标记 ：-->
```



###### 设备自适应尺寸标记

| 属性     | 说明     |
| -------- | -------- |
| viewport | 视图界面 |

```html
<!-- 这段代码的意思是，让 viewport 的宽度等于物理设备上的真实分辨率，不允许用户缩放。一都主流的 web app 都是这么设置的，它的作用其实是故意舍弃 viewport，不缩放页面，这样 dpi 肯定和设备上的真实分辨率是一样的，不做任何缩放，网页会因此显得更高细腻。
-->
<meta name="viewport" content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no" />
<!-- viewport 标签中 content 值：		
	width：控制 viewport 的大小，可以指定的一个值:
		600，或者特殊的值
		device-width 为设备的宽度（单位为缩放为 100% 时的 CSS 的像素）。
	height：和 width 相对应，指定高度。
	initial-scale：初始缩放比例，也即是当页面第一次 load 的时候缩放比例。
	maximum-scale：允许用户缩放到的最大比例。
	minimum-scale：允许用户缩放到的最小比例。
	user-scalable：用户是否可以手动缩放
-->
```



##### http-equiv 属性

> 相当于 http 的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确地显示网页内容.



###### 网页动态信息标记



| 属性                          | 说明               |
| ----------------------------- | ------------------ |
| expires                       | 设置网页到期时间   |
| Content-type/Content-language | 设置网页文字及语言 |
| refresh                       | 设置定时跳转       |
| Cache-Control                 | 禁止缓存调用       |
| set-cookie                    | 删除过期 cookie    |
| windows-target                | 网页打开方式       |
| Page-Enter/page-exit          | 设置网页过渡效果   |

```html
<!--begin--： 网页动态信息标记 : -->

<!-- 设置网页到期时间： content = "星期 日 月 年 时 分 秒 GMT"-->
<meta http-equiv = "expires" content="28 february 2019 00:00:00 GMT"/>

<!--begin-- 设置网页文字及语言： -->
    <!--第一种表示方法：-->
    <!-- 字符集类型如"utf-8"等等 ，以下语句相当于开头的<meta charset="UTF-8">  -->
    <meta http-equiv =  "Content-type" content="text/html;charset =字符集类型"/>
    <!--第二种表示方法：-->
    <meta http-equiv = "Content-language" content="zh_CN"/>
<!-- end -- 设置网页文字及语言： -->

                                                                                                                           <!-- 设置定时跳转： -->
<meta http-equiv="refresh" content="3;url = http://www.baidu.com"/>          	

<!-- 禁止缓存调用：  设置缓存属性："Cache-Control " "Pragma"-->
<meta http-equiv="Cache-Control" content="no-cache"/>
<!-- <meta http-equiv="Pragma" content="no-cache"/> -->

<!-- 删除过期cookie： -->
<meta http-equiv="set-cookie" content="28 february 2019 00:00:00 GMT"/>

<!-- 强制打开新窗口：windos-target : 网页打开方式 -->
<meta http-equiv="windows-target" content="_top"/>

<!-- 设置网页过渡效果： 
	<meta http-equiv="过渡事件" content="revealtrans(duration = 持续时间,transition = 过渡方式0~23)" >
-->
<!--begin: 大部分浏览器并不支持  -->
	<meta http-equiv="Page-Enter" content="revealtrans(duration = 5,transition = 21)" >
	<meta http-equiv="page-exit" content="revealtrans(duration = 5,transition = 8)">
<!-- end : 大部分浏览器并不支持  -->

<!-- end --： 网页动态信息标记 : -->
```



##### charset 属性

```html
<meta charset="UTF-8">
```



#### base 基底网址标记

> 基底网址标记：将相对路径补成绝对路径



##### target 属性

> 新窗口打开方式

| 属性    | 说明                                     |
| ------- | ---------------------------------------- |
| _parent | 在上一级窗口打开，一般用于分帧的框架页中 |
| _blank  | 在新窗口打开                             |
| _self   | 在同一窗口打开，可以省略                 |
| _top    | 在浏览器整个窗口打开，忽略任何框架       |

```html
<base href="http://www.baidu.com" target="_blank"/>

<body>
    <a href="../123">我的博客</a>
    <!-- 相当于 http://www.baidu.com/123 -->
</body>
```



### body 主体

页面的主体标记



```html
<!DOCTYPE html>
<html>
<!--
1.<body></body>：页面的主体标记
    (1)字体：
        text			设置页面文字默认颜色 
    (2)背景：			
        bgcolor			背景颜色
        background		背景图片
        bgproperties		背景图片固定属性
    (3)链接：
        link			链接默认颜色
        alink			按下链接颜色
		vlink			按下链接后颜色
    (4)边距：
        margin			HTML页面内容与浏览器边框的距离
-->
	<head>
		<meta charset="UTF-8">
		<title></title>
		
		<!--begin--: CSS：背景图片不重复显示： -->
		<style type="text/css">
			body{background-repeat:no-repeat}
		</style>
		<!-- end --: CSS：背景图片不重复显示： -->
	</head>
	<body text="#FFFFFF" bgcolor ="aquamarine" background = "img/640.webp" 
		bgproperties = "fixed"
		link="#FF0000" alink="#99FF00" vlink="CCCCCC"
		topmargin="100" leftmargin = "100">
	<!--begin--： 页面的主体标记  <body></body> -->
	<!--
		字体：
		text        ：设置页面文字的颜色 ：改变整个页面的默认字体颜色
			                     在没有对文字进行单独定义颜色是时，这个属性对页面所有文字产生作用
		背景：
		bgcolor     ：背景颜色
       	background  ：背景图片
       	bgproperties：背景图片固定属性，默认情况下图片会按照水平和垂直方向不断出现，直至铺满整个画面
       				   当设置为fixed时，当滚动页面，背景图片也会跟着移动，对于浏览者来说，总是停留在相同位置
       				  若希望图片不重复显示，则需要借助CSS样式
       	链接：
  		link        ：链接默认颜色
  		alink       ：按下链接颜色
  		vlink       ：按下链接后颜色
  		边距：
  		margin      ：HTML页面内容与浏览器边框的距离
  			leftmargin,topmargin
  	--!>
	<!-- end --： 页面的主体标记  <body></body> -->
	<h1>这是一个跳转链接：</h1>
	<a href="http://www.baidu.com"><h1>跳转百度</h1></a>
	</body>
</html>

```



