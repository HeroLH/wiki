> *Made By Herolh*

----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# 初识 JQuery

##  JQuery 的基本介绍

### 什么是  JQuery

> 

jQuery相当于Python的第三方模块
第三方模块其实就是别人写好(封装)的一些代码,我们拿过来用(按照别人定好的规则)



#### 为什么要学jQuery?

> 做同样的事情 jQuery写起来极其简练 (write less, do more.)



#### jQuery 版本

- **1.x**：最终版本：1.12.4 (2016年5月20日)

    > **兼容IE678**，使用最为广泛的，官方只做BUG维护，功能不再新增。因此一般项目来说，使用1.x版本就可以了，

- **2.x**：最终版本：2.2.4 (2016年5月20日)

    >  不兼容IE678，很少有人使用，官方只做BUG维护，功能不再新增。如果不考虑兼容低版本的浏览器可以使用2.x，

- **3.x：**

    > 不兼容IE678，只支持最新的浏览器。需要注意的是很多老的 jQuery 插件不支持3.x版。目前该版本是官方主要更新维护的版本。

&emsp;&emsp;维护IE678是一件让人头疼的事情，一般我们都会额外加载一个CSS和JS单独处理。值得庆幸的是使用这些浏览器的人也逐步减少，PC端用户已经逐步被移动端用户所取代，如果没有特殊要求的话，一般都会选择放弃对678的支持。





### JQuery 的导入

```javascript
<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
```





## JQuery 的常用命令

| 命令行 | 说明 |
| :----: | :--: |
|        |      |

```shell
# 补充
```



## JQuery 的初步使用

> 对语法进行由浅入深的归纳分类

1. 改变标签
2. 改变标签的属性
3. 改变标签的样式
4. 事件相关



### 选择器

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title></title>
		<!-- 
			1.JQuery 导入:( 先导入再使用 )
				<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
			2.基础语法：
				$()     =等同于=>		JQuery()	
				通过索引取值：
					$()[0]
				取出找到标签内的文本
					$().html()				生效对象为JQuery对象
					$().[0].innerHTML		生效对象为HTML标签
				将HTML便签转化为JQuery对象：
					var aEle = document.getElementsByClassName("c2");
					var $aEle = $(aEle);
					注意：
						最好在变量前加一个$表示这是一个JQuery对象，便于区分
			3.选择器( 值都需要加类型)	
				id选择器：			$("#id")
				标签选择器：		$("tagName")
				class选择器：		$(".className")
				配合使用：			$("div.c1")  					// 找到有c1 class类的div标签
				所有元素选择器：		$("*")							// 按文档顺序排序	
				组合选择器：		$("#id, .className, tagName")
					// 逗号分隔规则，每个规则互不干扰，各自找出一批来
					// 第一个规则在列表里排最后
				
				层级选择器：		x和y可以为任意选择器					
					$("x y");			x的所有后代y（子子孙孙）
					$("x > y");			x的所有儿子y（儿子）
					$("x + y");			找到所有紧挨在x后面的兄弟y
					$("x ~ y");			x之后所有的兄弟y
				属性选择器：					
					[attribute]
					[attribute=value]							// 属性等于
					[attribute!=value]							// 属性不等于			
		-->
		<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	</head>
	<body>
		<div id="d1">d1</div>
		<div class="c1">c1</div>
		<p class="c2">p标签</p>
		<a href="" class="c2">a标签</a>
		
		<div id="d2">
			<div id="d3">d2 里的d4</div>
			<div id="d4">d2 里的d5</div>
			<div id="d5">
				<div id="d6">d5里的d6</div>
			</div>
		</div>
		
		<!--属性选择器-->
		<form action="" id="f1">
		    <label>用户名:
		        <input name="username" type="text" disabled >
		    </label>
		
		    <label>密码:
		        <input name="pwd" type="password">
		    </label>
		
		
		    <label>篮球:
		        <input name="hobby" value="basketball" type="checkbox">
		    </label>
		
		    <label>足球:
		        <input name="hobby" value="football" type="checkbox">
		    </label>
		
		
		    <label>男
		        <input name="gender" value="1" type="radio">
		    </label>
		
		    <label>女:
		        <input name="gender" value="0" type="radio">
		    </label>		
		</form>
	</body>
	<script>
		console.log( "================ 取标签内文本值  ==================" );
		console.log( $(".c2") );
		console.log( $(".c2").html() );					// 只能拿出第一个
		console.log( $(".c2")[1].innerHTML );
		console.log( "================ HTML元素和JQuery对象的转化  ==================" );
		var aEle = document.getElementsByClassName("c2");
		console.log( aEle );							// HTMLCollection(2)
		console.log( $(aEle) );							// jQuery.fn.init(2)
		console.log( aEle );							// HTMLCollection(2)
		var aEle = $(aEle);
		console.log( aEle );							// // jQuery.fn.init(2)
	</script>
	<script>
		console.log("================ id选择器 ==================");
		console.log( $("#d1") );				// 返回一个对象列表
		console.log( $("#d1")[0] );				// 取出对象列表中的第一个值
		console.log("================ 类选择器 ==================");
		console.log( $(".c2") );
		console.log( $(".c2")[0] );	
		console.log( $(".c2")[1] );	
		console.log("================ 标签选择器 ==================");
		console.log( $("div") );
		console.log( $("div")[0] );
		console.log( $("div")[1] );
		console.log("================ 配合使用 ==================");
		console.log( $("div.c1") );
		console.log( $("div.c1")[0] );
		console.log("================ 所有元素选择器 ==================");
		console.log( $("*") );	
		console.log( $("*")[0] );						// HTML标签
		console.log( $("*")[1] );						// head标签
		console.log( $("*")[3] );						// title标签
		console.log( $("*")[4] );						// script标签
		console.log("================ 组合选择器 ==================");
		console.log( $("a,.c1") );						// 第一个规则在列表里排最后
		console.log( $("a,.c1")[0] );
		console.log( $("a,.c1")[1] );
		console.log("================ 层级选择器 ==================");
		console.log( $("#d2 div") );					// x的所有后代y（子子孙孙）
		console.log( $("#d2>div") );					// x的所有儿子y（儿子）
		console.log( $("#d3+div") );					// 找到紧挨在x后面的兄弟y
		console.log( $("#d3 ~ div") );					// x之后所有的兄弟y
		console.log("================ 属性选择器 ==================");
		console.log( $("input"));
		console.log( $("input[name='gender']"));
	</script>
</html>
```



### 筛选器

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<!-- 筛选器：( 值都需要加类型  )
			基本筛选器：
				常用属性：
					:first 				// 第一个
					:last 				// 最后一个
					:eq(index)			// 索引等于index的那个元素,从 0 算起,可以为负数
					:even 				// 匹配所有索引值为偶数的元素，从 0 开始计数
					:odd 				// 匹配所有索引值为奇数的元素，从 0 开始计数
					:gt(index)			// 匹配所有大于给定索引值的元素,不包含本身
					:lt(index)			// 匹配所有小于给定索引值的元素,不包含本身
					:not(元素选择器)		// 移除所有满足not条件的标签
					:has(元素选择器)		// 选取所有包含一个或多个标签在其内的标签(指的是从后代元素找)
				下一个元素：
					$("#id").next()				// 下一个元素
					$("#id").nextAll()			// 以下全部元素
					$("#id").nextUntil("#i2")	// 从某个元素到某个元素之间的所有元素
				上一个元素：			
					$("#id").prev()				// 上一个元素
					$("#id").prevAll()			// 以上全部元素
					$("#id").prevUntil("#i2")	// 从某个元素到某个元素以外的所有元素
				父亲元素：				
					$("#id").parent()
					$("#id").parents()  		// 查找当前元素的所有的父辈元素
					$("#id").parentsUntil(value)// 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止。
				儿子和兄弟元素：				
					$("#id").children();		// 儿子们,不找孙子
					$("#id").siblings();		// 兄弟们
				
				查找
					搜索所有与指定表达式匹配的元素。这个函数是找出正在处理的元素的后代元素的好方法。			
					$("div").find("p")  	=等价于=>		$("div p")
				筛选				
					筛选出与指定表达式匹配的元素集合。这个方法用于缩小匹配的范围。用逗号分隔多个表达式。					
					$("div").filter(".c1")  // 从结果集中过滤出有c1样式类的
						=等价于=> 		$("div.c1")
				筛选补充：
					.first() 				// 获取匹配的第一个元素
					.last() 				// 获取匹配的最后一个元素
					.not() 					// 从匹配元素的集合中删除与指定表达式匹配的元素
					.has() 					// 保留包含特定后代的元素，去掉那些不含有指定后代的元素。
					.eq() 					// 索引值等于指定值的元素
			表单常用筛选：
				:text 		
				:password
				:file
				:radio
				:checkbox
				
				:submit
				:reset
				:button
				表单对象属性:
					:enabled		
					:disabled		禁用
					:checked		选中
					:selected
				
				=用法=> 			$(":text")  
					=相当于=>	 	$("input:text")	   
					=相当于=> 	$("input[type='text']")							
		-->
		<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	</head>
	<body>
		<form action="" id="f1">
		    <label>用户名:
		        <input name="username" type="text" disabled >
		    </label>
		
		    <label>密码:
		        <input name="pwd" type="password">
		    </label>
		
		
		    <label>篮球:
		        <input name="hobby" value="basketball" type="checkbox">
		    </label>
		
		    <label>足球:
		        <input name="hobby" value="football" type="checkbox">
		    </label>
		
		
		    <label>男
		        <input name="gender" value="1" type="radio">
		    </label>
		
		    <label>女:
		        <input name="gender" value="0" type="radio">
		    </label>		
		</form>
		
		<ul>
			<li class="cl1">1</li>
			<li class="cl2">2</li>
			<li class="cl3">3</li>
			<li class="cl4">4</li>
			<li class="cl5">5</li>
		</ul>
		
		<div id="d1">
			<div id="d2">
				<div id="d3">					
				</div>
			</div>
		</div>
	</body>
	<script>
		console.log("================ 基本筛选器 ==================");
		console.log( $( "ul li:first") );				// 第一个
		console.log( $( "ul li:last") );				// 最后一个
		console.log( $( "ul li:eq(2)") );				// 索引等于index的那个元素,从 0 算起索引等于index的那个元素,从 0 算起
		console.log( $( "ul li:eq(-2)") );				// 可以为负数
		console.log( $( "ul li:even") );				// 匹配所有索引值为偶数的元素，从 0 开始计数
		console.log( $( "ul li:odd") );					// 匹配所有索引值为奇数的元素，从 0 开始计数			
		console.log( $( "ul li:gt(3)" ) );				// 匹配所有大于给定索引值的元素,不包含本身
		console.log( $( "ul li:lt(3)" ) );				// 匹配所有小于给定索引值的元素,不包含本身
		console.log( $( "#d2 div:not(#d6)") );			// 在结果列表内将符合not条件的元素都去掉
		console.log( $( "#d2 div:has(#d6)"));			// 选取所有包含一个或多个标签在其内的标签(指的是从后代元素找)
		console.log( $(".cl3").next() );				// 下一个元素
		console.log( $(".cl3").nextAll() );				// 以下全部元素
		console.log( $(".cl2").nextUntil(".cl4"));		// 从某个元素到某个元素之间的所有元素
		console.log( $(".cl3").prev() );				// //上一个元素
		console.log( $(".cl3").prevAll() );				// 以上全部元素
		console.log( $(".cl3").prevUntil(".cl4") );		// 从某个元素到某个元素以外的所有元素
		console.log( $("#d3").parent() );				// 找出父亲元素
		console.log( $("#d3").parent().parent() );		// 支持链式操作	
		console.log( $("#d3").parents("body") );		// 查找当前元素的所有的父辈元素
		console.log( $("#d3").parentsUntil("body") );	// 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止。
		console.log( $("body").children() );			// 儿子们,不找孙子
		console.log( $("script").siblings() );			// 兄弟们
		console.log("================ 表单常用筛选 ==================");
		console.log( $(":checkbox") );  				// 找到所有的checkbox)
	</script>
</html>
```



### 样式操作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<!--样式操作( 值不需要加类型 )
			样式类			
				addClass();				// 添加指定的CSS类名。
				removeClass();			// 移除指定的CSS类名。
				hasClass();				// 判断样式存不存在
				toggleClass();			// 切换CSS类名，如果有就移除，如果没有就添加。
				示例：开关灯、分组菜单 和 模态框
			
			CSS			
				css("color","red")		//DOM操作：tag.style.color="red"
				示例：					
					$("p").css("color", "red"); //将所有p标签的字体设置为红色
			位置：			
				offset({top:100,...})	// 获取匹配元素在当前窗口的相对偏移 或 设置元素位置
				position()				// 获取匹配元素相对父元素的偏移
				scrollTop()				// 获取匹配元素相对滚动条顶部的偏移
				scrollLeft()			// 获取匹配元素相对滚动条左侧的偏移
				
				.offset()方法允许我们检索一个元素相对于文档（document）的当前位置。
					和 .position()的差别在于： .position()是相对于相对于父级元素的位移。
				
				示例：
					 返回顶部示例
			尺寸：			
				height()
				width()
				innerHeight()				// 内容 + 内边距
				innerWidth()
				outerHeight()				// 内容 + 内边距 + border
				outerWidth()
		-->
		<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
		<style>
			.c11{
				background-color: red;
				width: 100px;
				height: 100px;
				border-radius: 50%;
			}
			.c12{
				background-color: yellow;
				width: 100px;
				height: 100px;
				border-radius: 50%;
			}
			.c13{
				background-color: green;
				width: 100px;
				height: 100px;
			}
			#d10{
				background-color: yellowgreen;
				width: 80px;
				height: 50px;
				text-align: center;
				font-weight: bolder;
				font-size: 25px;
				
				position: absolute;
				bottom: 20px;
				right: 20px;
			}
		</style>
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			ul li{
				list-style-type: none;
			}
			.hide {
	            display: none;
	        }
		</style>
		
		<style>
			.cover{
				background-color: rgba(0,0,0,0.4);
				position: absolute;
				top: 0;
				left: 0;
				bottom: 0;
				right: 0;
				z-index: 998;
			}
			
			.modal{
				height: 400px;
				width: 600px;
				background-color: white;
				position: absolute;
				top: 50%;
				left: 50%;
				margin-left: -300px;
				margin-top: -200px;
				z-index: 1000;
			}
		</style>
	</head>
	<body>
		<div id="d1">
			<p>p1</p>
			<p id="p2">p2</p>
			<p>p3</p>
		</div>
		
		<div class="c11"></div>	
		<hr />
		
		<div class="left-menu">
			<div class="menu-title">菜单1</div>
			<div class="menu-items hide">
				<ul>
					<li><a href="">001</a></li>
					<li><a href="">002</a></li>
					<li><a href="">003</a></li>
				</ul>
			</div>
			<div class="menu-title">菜单2</div>
			<div class="menu-items hide">
				<ul>
					<li><a href="">001</a></li>
					<li><a href="">002</a></li>
					<li><a href="">003</a></li>
				</ul>
			</div>
			<div class="menu-title">菜单3</div>
				<div class="menu-items hide">
					<ul>
						<li><a href="">001</a></li>
						<li><a href="">002</a></li>
						<li><a href="">003</a></li>
					</ul>
				</div>
		</div>
		
		
		<button id="b1">屠龙宝刀,点击就送!</button>
		<div class="cover hide"></div>
		<div class="modal hide">
		    <form>
		        <p>
		            <label>用户名:
		                <input type="text">
		            </label>
		        </p>
		        <p>
		            <label>密码:
		                <input type="password">
		            </label>
		        </p>
		        <p>
		            <input type="submit" value="登录">	
		            <!-- submit 提交后页面自动刷新 -->
		            <input id="cancel" type="button" value="取消">
		        </p>
		    </form>
		</div>
		
		<hr />
		
		<div id="d7" class="c11"></div>
		<div id="d8" class="c13">d8
			<div id="d9" class="c12">d9</div>
		</div>
		
		<div id="d10" class="hide">top</div>
	</body>
	<script>
		console.log( $("#p2").addClass("c1 c2") );
		console.log( $("#p2").removeClass("c1") );
		console.log( $("#p2").hasClass("c1") );
		console.log( $("#p2").toggleClass("c1") );
	</script>
	
	<script>
		// 找标签
		$("div.c11").click( function(){			// 绑定对象
			console.log( this );				// 该处的this为 document 对象
			$(this).toggleClass("c12");
		})
	</script>
	
	<script>
	// 需求分析:
    // 找到所有的.menu-title标签,绑定点击事件

    // 点击事件具体要做的事儿
    // 1. 找到当前点击菜单下面的.menu-items(紧挨着的),把它显示出来(移除hide类)
    // 2. 把其他的.menu-items隐藏,添加hide类

	// 第二种方法：
    // 1. 找到所有的.menu-items, 隐藏
    // 2. 找到当前点击菜单下面的.menu-items,把它显示出来(移除hide类)
    	$(".menu-title").click(function(){
			$(this).next().toggleClass("hide");
			console.log( $(this).next().siblings( ".menu-items" ).addClass("hide") );
			
		})
	</script>
	
	<script>
		// 模态框
		$("#b1").click( function(){			// 找到点击弹出模态框的按钮
			// 把.cover和.modal显示出来(去除掉.hide)
			$(".cover").removeClass("hide");
			$(".modal").removeClass("hide");
		})
		
		$("#cancel").click( function(){		// 找到取消按钮,绑定事件
			// 给背景和模态框都加上hide类
	        $(".cover").addClass("hide");
	        $(".modal").addClass("hide");
		})
	</script>
	
	<script>
		$("p").css( "color","blue" );
		console.log( $("#d7").offset() );					// {top: 251.60000610351562, left: 0}
		console.log( $("#d7").offset({top:260,left:20}) );	// 获取匹配元素在当前窗口的相对偏移 或 设置元素位置
		
		$("#d9").offset({left:100})
		console.log( $("#d9").position() );					// 获取匹配元素相对父元素的偏移
	
		// 返回顶部示例
		$(window).scroll( function(){
			// window:		窗口	
			// .scroll()	窗口滑动事件
			if( $(window).scrollTop() < 10 ){
				$("#d10").addClass("hide");
				console.log( $("window").scrollTop()+"<10");
			}else{
				$("#d10").removeClass("hide");
				console.log( $("window").scrollTop()+">10");
			}
		})
		$("#d10").click(function(){
			$(window).scrollTop(0);
		})
	</script>
</html>
```



### 文档操作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">		
		<title></title>	
		<!-- 
			文本操作
				HTML代码：				
					html()				// 取得第一个匹配元素的html内容，相当于[0].innerHTML
					html(val)			// 设置所有匹配元素的html内容,直接替换，不保留标签
				文本值：				
					text()				// 取得所有匹配元素的内容,相当于[0].innerText
					text(val)			// 设置所有匹配元素的内容,直接替换，不保留原有内容
				值：			
					val()				// 取得第一个匹配元素的当前值
					val(val)			// 设置所有匹配元素的值
					val([val1, val2])	// 设置checkbox、select的值,覆盖原有值
					注意：
						checkbox 获取多个值需要用循环才可以
						select直接  .val() 即可
			属性操作
				用于ID等或自定义属性：				
					attr(attrName)				// 返回第一个匹配元素的属性值
					attr(attrName, attrValue)	// 为所有匹配元素设置一个属性值
					attr({k1: v1, k2:v2})		// 为所有匹配元素设置多个属性值
					removeAttr()				// 从每一个匹配的元素中删除一个属性
				
				用于checkbox和radio				
					prop() 						// 获取属性，选中返回true，没选中返回false
					removeProp() 				// 移除属性
				注意：
					在1.x及2.x版本的jQuery中使用attr对checkbox进行赋值操作时会出bug，在3.x版本的jQuery中则没有这个问题。
					为了兼容性，我们在处理checkbox和radio的时候尽量使用特定的prop()，不要使用attr("checked", "checked")。
				示例：
					图片切换,全选 反选 取消
					
			文档处理：
				创建标签：
					JQuery没有提供创建语句，所以我们还是用JS原生的创建语句
						document。createEkement("li");
				添加到文档：
					添加到指定元素内部的后面
						$(A).append(B)				// 把B追加到A
						$(A).appendTo(B)			// 把A追加到B
					添加到指定元素内部的前面			
						$(A).prepend(B)				// 把B前置到A
						$(A).prependTo(B)			// 把A前置到B
					添加到指定元素外部的后面				
						$(A).after(B)				// 把B放到A的后面
						$(A).insertAfter(B)			// 把A放到B的后面
					添加到指定元素外部的前面				
						$(A).before(B)				// 把B放到A的前面
						$(A).insertBefore(B)		// 把A放到B的前面
				
				移除和清空元素				
					remove()						// 从DOM中删除所有匹配的元素。
					empty()							// 删除匹配的元素集合中所有的子节点。
					例子：					
						点击按钮在表格添加一行数据。					
						点击每一行的删除按钮删除当前行数据。				
				替换			
					$(A).replaceWith(B)				// 用B替换掉A
					$(A).replaceAll(B)				// 用A替换掉B
				克隆				
					clone()							// clone方法不加参数true，克隆标签但不克隆标签带的事件
													// clone方法加参数true，克隆标签并且克隆标签带的事件
		-->
		<style>
			*{
				margin: 0;
				padding: 0;
			}
		</style>
		<style>
	        .error {
	            color: red;
	        }	        
	    </style>
		<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	</head>
	<body>
		<div id="d1">
		    <p><span>span</span></p>
		    <div>div</div>
		</div>
		
		<form >
			<p>
	            <label>用户名:
	                <input class="need" name="username" type="text">
	                <span class="error"></span>
	            </label>
	        </p>
	        <p>
	            <label>密码:
	                <input class="need" name="password" type="password">
	                <span class="error"></span>
	            </label>
	        </p>
	        
	         <p>爱好:
	            <label>篮球
	                <input name="hobby" value="basketball" type="checkbox" checked="checked">
	            </label>
	            <label>足球
	                <input name="hobby" value="football" type="checkbox">
	            </label>
	            <label>双色球
	                <input name="hobby" value="doublecolorball" type="checkbox">
	            </label>
	        </p>
	        
	        <p>性别:
	            <label>男
	                <input name="gender" value="1" type="radio" checked="checked">
	            </label>
	            <label>女
	                <input name="gender" value="0" type="radio">
	            </label>
	            <label>保密
	                <input name="gender" value="2" type="radio">
	            </label>
	        </p>
		    <p>
		        <label for="s1">从哪儿来:</label>
		        <select name="from" id="s1">
		            <option value="010">北京</option>
		            <option value="021">上海</option>
		            <option value="020">广州</option>
		            <option value="0755">深圳</option>
		        </select>
		    </p>
		    
		    <p>
		        <label for="s2">从哪儿来:</label>
		        <select name="from" id="s2" multiple>
		            <option value="010" selected>北京</option>
		            <option value="021" selected>上海</option>
		            <option value="020" >广州</option>
		            <option value="0755">深圳</option>
		        </select>
		    </p>
		    
		    <p>
		        <label for="t1">个人简介:</label>
		        <textarea name="memo" id="t1" cols="30" rows="10">		
		        </textarea>
		    </p>
		    
		    <p>
	            <input id="b1" type="submit" value="登录">
	            <input id="cancel" type="button" value="取消">
	        </p>
		</form>
		
		<img src="http://image11.m1905.cn/uploadfile/s2010/0205/20100205083613178.jpg" alt="">
		<input type="button" id="bb1" value="下一个">


		<table id="t2" border="1">
		    <thead>
		    <tr>
		        <th>#</th>
		        <th>姓名</th>
		        <th>职位</th>
		    </tr>
		    </thead>
		    <tbody>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>小东北</td>
		        <td>二人转演员</td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>乔小强</td>
		        <td>xx演员</td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>韩涉</td>
		        <td>导演</td>
		    </tr>
		    </tbody>
		</table>
		
		<input type="button" id="b12" value="全选">
		<input type="button" id="b22" value="反选">
		<input type="button" id="b32" value="取消">
		
		
		<ul id="u1">
			<li id="ll1">1</li>
			<li id="l12">2</li>
			<li id="l13">3</li>
		</ul>
		<a id="a1">替换</a><br />
		<button class="cc1">false,克隆标签但不克隆标签带的事件</button><br />
		<button class="cc2">true,克隆标签并且克隆标签带的事件</button>
		
		
		<table border="1" id="t3">
		    <thead>
		    <tr>
		        <th>#</th>
		        <th>姓名</th>
		        <th>爱好</th>
		        <th>操作</th>
		    </tr>
		    </thead>
		    <tbody>
		    <tr>
		        <td>1</td>
		        <td>小强</td>
		        <td>吃冰激凌</td>
		        <td>
		            <button class="delete">删除</button>
		        </td>
		    </tr>
		    <tr>
		        <td>2</td>
		        <td>二哥</td>
		        <td>Girl</td>
		        <td>
		            <button class="delete">删除</button>
		        </td>
		    </tr>
		
		 	</tbody>
		</table>
		<button id="bb2">添加一行数据(有bug，无bug版的在jQuery5_事件)</button>
	</body>
	<script>
		// HTML代码：
		console.log( $("#d1").html() );
		console.log( $("#d1")[0].innerHTML );				// 原生 DOM
		// 文本值
		console.log( $("#d1").text() );
		console.log( $("#d1")[0].innerText );
		$("#d1").text("hehe");
		// 值
		console.log( $(":text").val() );
		// checkbox 获取多个值
		console.log( $(":checkbox") );						// 直接.val()的话只能获取或修改到第一个的值
		var $checkedEles = $(":checkbox:checked");
		for( var i = 0; i < $checkedEles.length; i++){
			console.log( $( $checkedEles[i] ).val() );		// 索引取出来之后就变成DOM对象了
		}		
		// select 获取多个值 ,直接  .val() 即可
		console.log( $("#s2").val() );
		console.log( $("#s2").val("0755") );
	</script>
	
	<script>
    // 点击登录按钮验证用户名和密码为不为空
    // 为空就在对应的input标签下面显示一个错误提示信息
    // 1. 给登录按钮绑定点击事件
    // 2. 点击事件要做的事儿
    // 2.1 找到input标签--> 取值 --> 判断为不为空 --> .length为不为0
    // 2.2 如果不为空,则什么都不做
    // 2.2 如果为空,要做几件事儿
    // 2.2.1 在当前这个input标签的下面 添加一个新的标签,内容为xx不能为空

    $("#b1").click(function () {
        var $needEles = $(".need");
        for (var i=0;i<$needEles.length;i++){
            if ($($needEles[i]).val().trim().length === 0) {
                var labelName = $($needEles[i]).parent().text().trim().slice(0,-1);
                $($needEles[i]).next().text( "*" + labelName +"不能为空!");
            }
        }
        return false;			// 必须要加这一段，否则出现的提示信息马上就被刷新没了
    })
</script>
<script>
    var oldURL;
    var newURL = "http://img01.yohoboys.com/contentimg/2017/08/12/21/012a1eab9842a752f8c4d98b8fc2777ad7.jpg"
    $("#bb1").click(function () {
        var $imgEles = $("img");
        // 修改img标签的src属性
        oldURL = $imgEles.attr("src");
        $imgEles.attr({"src":newURL,"title":"我的前女友"} );
        newURL = oldURL;
    });
</script>
<script>
	
    // 点击全选,表格中所有的checkbox都选中
    // 1. 找checkbox
    var $checkboxEle =  $("#t2 input");
    // 2. 全部选中  --> prop("checked", true);
    $("#b12").click( function(){
    	for( var i = 0; i < $checkboxEle.length; i++ ){
    		$($checkboxEle[i]).prop("checked", true );
    	}
    });

    // 点击取消
    // 1. 找checkbox
    // 2. 全部取消选中  --> prop("checked", false);
    $("#b32").click( function(){
    	for( var i = 0; i < $checkboxEle.length; i++ ){
    		$($checkboxEle[i]).prop("checked", false );
    	}
    });


    // 反选
    // 1. 找到所有的checkbox
    // 2. 判断
    // 2.1 原来没选中的,要选中
    // 2.2 原来选中的,要取消选中
    $("#b22").click( function(){
    	for( var i = 0; i < $checkboxEle.length; i++ ){
    		if( $($checkboxEle[i]).prop("checked") ){
    			$($checkboxEle[i]).prop("checked", false );
    		}else{
    			$($checkboxEle[i]).prop("checked", true );
    		}
    	}
    })
</script>
<script>
	// 文档处理
	// 创建
	var liEle = document.createElement('li');
	var liEle2 = document.createElement('li');
	var liEle3 = document.createElement('li');
	var liEle4 = document.createElement('li');
	liEle.innerText = 4;
	liEle2.innerText = 0;
	liEle3.innerText = 0.5;
	liEle4.innerText = 1.5;
	
	// 添加
	$("#u1").append(liEle);	
	$( liEle2 ).prependTo( $("#u1") );
	$("#ll1").after( liEle4);
	$("#ll1").before( liEle3 );
	$("#ll1").remove();
	
	// 替换
	$("#a1").click(function(){
		var imgEle = document.createElement("img");
		$(imgEle).attr("src","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1535020712317&di=2437a67b6966b47b1e341e217a0d1ebc&imgtype=0&src=http%3A%2F%2Fnpic30.edushi.com%2Frw%2Fzixun%2Fzh-chs%2F2017-07%2F07%2Fb2180d95424c48a4a2f04dc252e3793e.jpg")
		$(this).replaceWith(imgEle);
	})
	
	// 克隆
	// clone方法不加参数true，克隆标签但不克隆标签带的事件
	$(".cc1").on("click", function () {
	    $(this).clone().insertAfter(this);
	});
	// clone方法加参数true，克隆标签并且克隆标签带的事件
	$(".cc2").on("click", function () {
	    $(this).clone(true).insertAfter(this);
	});
</script>
<script>
	// 绑定事件 表格最后添加一条记录
	// 要使用事件委托,基于已经存在的元素(页面加载完之后存在的标签)绑定事件
	$(".delete").click(function(){						// 在页面动态生成html代码,但发现新生成的代码的click事件失效了.使用$( 父标签  ).on()方法解决
		$(this).parent().parent().remove();
	})
	
	$("#bb2").on("click", function () {
        // 生成要添加的tr标签及数据
        var trEle = document.createElement("tr");
        $(trEle).html("<td>3</td>" +
            "<td>小东北</td>" +
            "<td>社会摇</td>" +
            "<td><button class='delete'>删除</button></td>");
        // 把生成的tr插入到表格中
        $("#t3").find("tbody").append(trEle);
    });
	
</script>
</html>
```



### 事件

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">		
		<title></title>	
		<style>
			*{
				margin: 0;
				padding: 0;
			}
		</style>
		<!-- 事件 
		一、 目前为止学过的绑定事件的方式
			1.在标签里面写 onclick=foo(this);
			2.原生DOM的JS绑定      DOM对象.onclick=function(){...}
			3.jQuery版的绑定事件   jQuery对象.click(function(){...})
			
		二、我们今后要用的jQuery绑定事件的方式：
			最简方式：
				.on("click", function(){...})
			语法：
				$("元素").on("click", "选择器[可不写]", function(){...})
			为什么要用：
				适用于 给未来的元素(页面生成的时候还没有的标签) 绑定事件 (事件委托)
				事件冒泡和事件捕获：
					利用事件冒泡,给已经存在的标签绑定事件,用来捕获后代标签的事件.
			注意：
				像click、keydown 等DOM中定义的事件，我们都可以使用`.on()`方法来绑定事件，
				但是`hover`这种jQuery中定义的事件就不能用`.on()`方法来绑定了。
		
		三、移除事件( 很少用  )：
			.off("click", "选择器[可不写]", function(){...})
			off()方法移除用 .on()绑定的事件处理程序。
				
		四、页面载入
			当DOM载入就绪可以查询及操纵时绑定一个要执行的函数。这是事件模块中最重要的一个函数，因为它可以极大地提高web应用程序的响应速度。			
			两种写法：			
				$(document).ready(function(){					// 确保绑定事件的时候DOM树是生成好的,而不是顺着文档从上到下执行
					// 在这里写你的JS代码...
				})
			简写：			
				$(function(){
					// 你在这里写你的代码
				})
		
		五、阻止后续事件执行
			return false; // 常见阻止表单提交等

		六、事件委托
			事件委托是通过"事件冒泡"的原理，利用父标签去捕获子标签的事件。	
			基于已经存在的元素(页面加载完之后存在的标签)绑定事件
			示例：		
				表格中每一行的编辑和删除按钮都能触发相应的事件。		
				$("table").on("click", ".delete", function () {
				  	// 删除按钮绑定的事件
				})
		
		-->
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
				<table border="1" id="t3">
		    <thead>
		    <tr>
		        <th>#</th>
		        <th>姓名</th>
		        <th>爱好</th>
		        <th>操作</th>
		    </tr>
		    </thead>
		    <tbody>
		    <tr>
		        <td>1</td>
		        <td>小强</td>
		        <td>吃冰激凌</td>
		        <td>
		            <button class="delete">删除</button>
		        </td>
		    </tr>
		    <tr>
		        <td>2</td>
		        <td>二哥</td>
		        <td>Girl</td>
		        <td>
		            <button class="delete">删除</button>
		        </td>
		    </tr>
		
		 	</tbody>
		</table>
		<button id="bb2">添加一行数据(无bug版)</button>
	</body>
	<script>
	// 绑定事件 表格最后添加一条记录
	$("tbody").on( "click",".delete",function(){	// 利用事件冒泡,给已经存在的标签绑定事件,用来捕获后代标签的事件.
		$(this).parent().parent().remove();
	})
	
	$("#bb2").on("click", function () {
        // 生成要添加的tr标签及数据
        var trEle = document.createElement("tr");
        $(trEle).html("<td>3</td>" +
            "<td>小东北</td>" +
            "<td>社会摇</td>" +
            "<td><button class='delete'>删除</button></td>");
        // 把生成的tr插入到表格中
        $("#t3").find("tbody").append(trEle);
    });
	
</script>
</html>
```



### 动画效果

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<!-- 
			// 基本
				show([s,[e],[fn]])				// 逐渐显示，show( 5000 )
				hide([s,[e],[fn]])				// 逐渐隐藏，hide( 5000 )
				toggle([s],[e],[fn])			// 原来隐藏就显示，原来显示就隐藏，hide( 5000 )
			// 滑动
				slideDown([s],[e],[fn])			// 往下展开
				slideUp([s,[e],[fn]])			// 往上收缩
				slideToggle([s],[e],[fn])		
			// 淡入淡出
				fadeIn([s],[e],[fn])
				fadeOut([s],[e],[fn])
				fadeTo([[s],o,[e],[fn]])		// fadeTo(s=时间,o=透明度)
				fadeToggle([s,[e],[fn]])
			// 自定义（了解即可）
				animate(p,[s],[e],[fn])
			
			注意：
				定义的秒数，不占脚本编译运行空间
		-->
		<style>
		    div {
		      position: relative;
		      display: inline-block;
		    }
		    div>i {
		      display: inline-block;
		      color: red;
		      position: absolute;
		      right: -16px;
		      top: -5px;
		      opacity: 1;
		    }
		</style>
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
		<img width="200px" src="img/timg.jpg" alt="" />
		
		<ul class="menu-list">
			<li>001</li>
			<li>002</li>
			<li>003</li>
		</ul>
		
		<div id="d1">点赞</div>
	</body>
	<script>
		$( "img").hide( 2000 );
		$( "img").show( 2000 );
		$( "img").toggle( 1000 );
		$( "img").toggle( 1000 );
		$( ".menu-list").slideUp(1000);
		$( ".menu-list").slideDown(1000);
		// 自定义
		$( "#d1").on("click",function(){
			var newI = document.createElement("i");
			newI.innerText = "+1";
			
			$( this ).append( newI );
			$( this ).children("i").animate({
				opacity:0
			},1000,function(){
				console.log( $( this ).children("i") );
				$( this ).children("i").remove();				// 貌似有 bug 
			})
			
		})
	</script>
</html>
```



### 插件

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<!--插件
			jQuery.extend(object)
				jQuery的命名空间下添加新的功能。多用于插件开发者向 jQuery 中添加新函数时使用。
				即：
					$.editor();
					
			jQuery.fn.extend(object)
				一个对象的内容合并到jQuery的原型，以提供新的jQuery实例方法。
				即：
					$(元素兑现).editor();
		-->
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
		<div>
			<img src="img/timg.jpg" alt="" width="200px" />
		</div>
	</body>
	<script>
		// 定义插件
		$.fn.extend({
			"editor":function(){
				console.log( "The pages made by Lws!" );
			}
		})
		
		$.extend({
			"editor":function(){
				console.log( "The pages is free！" );
			}
		})
		
		// 调用插件
		$("img").editor();
		$("div").editor();
		$.editor();
	</script>
</html>
```





## JQuery 模拟场景

### shift 全选

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
		<table border="1" id="t1">
		    <thead>
		    <tr>
		        <th>#</th>
		        <th>姓名</th>
		        <th>爱好</th>
		        <th>操作</th>
		    </tr>
		    </thead>
		    <tbody>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>小强</td>
		        <td>吃冰激凌</td>
		        <td>
		            <select>
		                <option value="0">下线</option>
		                <option value="1">上线</option>
		                <option value="2">离线</option>
		            </select>
		        </td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>二哥</td>
		        <td>Girl</td>
		        <td>
		            <select>
		                <option value="0">下线</option>
		                <option value="1">上线</option>
		                <option value="2">离线</option>
		            </select>
		        </td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>二哥</td>
		        <td>Girl</td>
		        <td>
		            <select>
		                <option value="0">下线</option>
		                <option value="1">上线</option>
		                <option value="2">离线</option>
		            </select>
		        </td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>二哥</td>
		        <td>Girl</td>
		        <td>
		            <select>
		                <option value="0">下线</option>
		                <option value="1">上线</option>
		                <option value="2">离线</option>
		            </select>
		        </td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>二哥</td>
		        <td>Girl</td>
		        <td>
		            <select>
		                <option value="0">下线</option>
		                <option value="1">上线</option>
		                <option value="2">离线</option>
		            </select>
		        </td>
		    </tr>
		
		    </tbody>
		</table>
	</body>
	<script>
		// 确保绑定事件的时候DOM树是生成好的
	    $(document).ready(function () {
	        var mode = false;							// 设立一个标志位
	        var $bodyEle = $("body");
	        // 给文档绑定 监听键盘按键被按下去的事件
	        $bodyEle.on("keydown", function (event) {	// event：形参，持续监听的事件
	            //
	            console.log(event.keyCode);
	            if (event.keyCode === 16) {
	                // 进入批量操作模式
	                mode = true;
	                console.log( "shift键被按下");
	            }
	       	});
	       	
	       	// 按键抬起来的时候,退出批量操作模式
	        $bodyEle.on("keyup", function (event) {
	            //
	            console.log(event.keyCode);
	            if (event.keyCode === 16) {
	                // 进入批量操作模式
	                mode = false;
	                console.log( "shift键被抬起");
	            }
	        });
	        
	        $("select").on("change", function () {
	            // 取到当前select的值
	            var value = $(this).val();
	            var $thisCheckbox = $(this).parent().siblings().first().find(":checkbox");
	            // 判断checkbox有没有被选中
	            if ( $thisCheckbox.prop("checked") && mode) {
	                // 真正进入批量操作模式
	                var $checkedEles = $("input[type='checkbox']:checked");
	                for (var i = 0; i < $checkedEles.length; i++) {
	                    // 找到同一行的select
	                    $($checkedEles[i]).parent().siblings().last().find("select").val(value);
	                }
	            }
	        })
	    });
	</script>
</html>
```



### 正选反选取消

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">		
		<title></title>	
		<style>
			*{
				margin: 0;
				padding: 0;
			}
		</style>
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
		<table id="t2" border="1">
		    <thead>
		    <tr>
		        <th>#</th>
		        <th>姓名</th>
		        <th>职位</th>
		    </tr>
		    </thead>
		    <tbody>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>小东北</td>
		        <td>二人转演员</td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>乔小强</td>
		        <td>xx演员</td>
		    </tr>
		    <tr>
		        <td><input type="checkbox"></td>
		        <td>韩涉</td>
		        <td>导演</td>
		    </tr>
		    </tbody>
		</table>
		<input type="button" id="b12" value="全选">
		<input type="button" id="b22" value="反选">
		<input type="button" id="b32" value="取消">
		
	</body>
	<script>	
	    // 点击全选,表格中所有的checkbox都选中
	    // 1. 找checkbox
	    var $checkboxEle =  $("#t2 input");
	    // 2. 全部选中  --> prop("checked", true);
	    $("#b12").click( function(){
	    	for( var i = 0; i < $checkboxEle.length; i++ ){
	    		$($checkboxEle[i]).prop("checked", true );
	    	}
	    });
	
	    // 点击取消
	    // 1. 找checkbox
	    // 2. 全部取消选中  --> prop("checked", false);
	    $("#b32").click( function(){
	    	for( var i = 0; i < $checkboxEle.length; i++ ){
	    		$($checkboxEle[i]).prop("checked", false );
	    	}
	    });
	
	
	    // 反选
	    // 1. 找到所有的checkbox
	    // 2. 判断
	    // 2.1 原来没选中的,要选中
	    // 2.2 原来选中的,要取消选中
	    $("#b22").click( function(){
	    	for( var i = 0; i < $checkboxEle.length; i++ ){
	    		if( $($checkboxEle[i]).prop("checked") ){
	    			$($checkboxEle[i]).prop("checked", false );
	    		}else{
	    			$($checkboxEle[i]).prop("checked", true );
	    		}
	    	}
	    })
	</script>
</html>
```



### 登录校验

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>登录校验完整版</title>
		<style>
	        .error {
	            color: red;
	        }
    </style>
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
		<form id="f1">
	        <p>
	            <label>用户名:
	                <input class="need" name="username" type="text">
	                <span class="error"></span>
	            </label>
	        </p>
	        <p>
	            <label>密码:
	                <input class="need" name="password" type="password">
	                <span class="error"></span>
	            </label>
	        </p>
	
	        <p>爱好:
	            <label>篮球
	                <input name="hobby" value="basketball" type="checkbox">
	            </label>
	            <label>足球
	                <input name="hobby" value="football" type="checkbox">
	            </label>
	            <label>双色球
	                <input name="hobby" value="doublecolorball" type="checkbox">
	            </label>
	        </p>
	
		    <p>性别:
		            <label>男
		                <input name="gender" value="1" type="radio">
		            </label>
		            <label>女
		                <input name="gender" value="0" type="radio">
		            </label>
		            <label>保密
		                <input name="gender" value="2" type="radio">
		            </label>
		        </p>
		
		    <p>
		        <label for="s1">从哪儿来:</label>
		        <select name="from" id="s1">
		            <option value="010">北京</option>
		            <option value="021">上海</option>
		            <option value="020">广州</option>
		        </select>
		    </p>
		      <p>
		        <label for="s2">从哪儿来:</label>
		        <select name="from" id="s2" multiple>
		            <option value="010">北京</option>
		            <option value="021">上海</option>
		            <option value="020">广州</option>
		            <option value="0755">深圳</option>
		        </select>
		    </p>
		    <p>
		        <label for="t1">个人简介:</label>
		        <textarea name="memo" id="t1" cols="30" rows="10">
		
		        </textarea>
		    </p>
		        <p>
		            <input id="b1" type="submit" value="登录">
		            <input id="cancel" type="button" value="取消">
		        </p>
		</form>
		
		<button id="b1">添加一行数据</button>
	</body>
	<script>
	    // 点击登录按钮验证用户名和密码为不为空
	    // 为空就在对应的input标签下面显示一个错误提示信息
	
	    // 1. 给登录按钮绑定点击事件
	    // 2. 点击事件要做的事儿
	    // 2.1 找到input标签--> 取值 --> 判断为不为空 --> .length为不为0
	    // 2.2 如果不为空,则什么都不做
	    // 2.2 如果为空,要做几件事儿
	    // 2.2.1 在当前这个input标签的下面 添加一个新的标签,内容为xx不能为空
	
	    $("#b1").click(function () {
	        var $needEles = $(".need");
	        // 定义一个标志位
	        var flag = true;
	        for (var i=0;i<$needEles.length;i++){
	            // 如果有错误
	            if ($($needEles[i]).val().trim().length === 0) {
	                var labelName = $($needEles[i]).parent().text().trim().slice(0,-1);
	                $($needEles[i]).next().text( labelName +"不能为空!");
	                // 将标志位置为false
	                flag = false;
	                break;
	            }
	        }
	        return flag;
	    })
	
	</script>
</html>
```





# JQuery 进阶

> 中高级的应用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<!-- 
			jQuery.each( )
			.data()
		-->
		<!-- 
		一、each
			jQuery.each( 值或对象, callback(索引, value) )：			
			描述：
				一个通用的迭代函数，它可以用来无缝迭代对象和数组。
				数组和类似数组的对象通过一个长度属性（如一个函数的参数对象）来迭代数字索引，从0到length - 1。其他对象通过其属性名进行迭代。
			退出循环：
				return false;		// 退出全部循环
				return;				// 退出一次循环
		
		二、.data()：全局数据，可在不同函数内调用数据
			在匹配的元素集合中的所有元素上存储任意相关数据或返回匹配的元素集合中的第一个元素的给定名称的数据存储的值。			
			
			.data(key, value):			
				描述：
					在匹配的元素上存储任意相关数据。				
				$("div").data("k",100);				//给所有div标签都保存一个名为k，值为100
			
			.data(key):
				描述: 
					返回匹配的元素集合中的第一个元素的给定名称的数据存储的值—通过 .data(name, value)或 HTML5 data-*属性设置。
				$("div").data("k");					//返回第一个div标签中保存的"k"的值
			
			.removeData(key):
				描述：
					移除存放在元素上的数据，不加key参数表示移除所有保存的数据。
				$("div").removeData("k");  			//移除元素上存放k对应的数据
			示例：
				模态框编辑的数据回填表格
		
		-->
		<style>
			*{
				margin: 0;
				padding: 0;
			}
			.cover{
				position: fixed;
				top: 0;
				right: 0;
				bottom: 0;
				left: 0;
				background-color: #616161;
				opacity: 0.3;		
				z-index: 998;		
			}
			.modal{
				height: 200px;
				width: 300px;
				background-color: white;
				position: absolute;
				top: 50%;
				left: 50%;
				margin-top: -100px;
				margin-left: -150px;
				z-index: 999;
				
			}
			.hide{
				display: none;
			}
		</style>
	</head>
	<script type="text/javascript" src="js/jquery-3.3.1.js" ></script>
	<body>
		<ul>
			<li>001</li>
			<li>002</li>
			<li>003</li>
			<li>004</li>
			<li>005</li>
		</ul>
		
		<button id="add">新增</button>
		<table border="1">
		  	<thead>
		  		<tr>
				    <th>#</th>
				    <th>姓名</th>
				    <th>爱好</th>
				    <th>操作</th>
		  		</tr>
		  	</thead>
		  	<tbody>
			  	<tr>
				    <td>1</td>
				    <td>Egon</td>
				    <td>街舞</td>
				    <td>
				      	<button class="edit-btn">编辑</button>
				      	<button class="delete-btn">删除</button>
				    </td>
			  	</tr>
			  	<tr>
				    <td>2</td>
				    <td>Alex</td>
				    <td>烫头</td>
				    <td>
				      	<button class="edit-btn">编辑</button>
				      	<button class="delete-btn">删除</button>
				    </td>
			  	</tr>
			  	<tr>
				    <td>3</td>
				    <td>苑局</td>
				    <td>日天</td>
				    <td>
				      	<button class="edit-btn">编辑</button>
				      	<button class="delete-btn">删除</button>
				    </td>
			  	</tr>
		  	</tbody>
		</table>
		
		<div id="myCover" class="cover hide"></div>
		<div id="myModal" class="modal hide">
		  	<div>
			    <p>
			      	<label for="modal-name">姓名</label>
			      	<input type="text" id="modal-name">
			    </p>
			    <p>
			      	<label for="modal-habit">爱好</label>
			      	<input type="text" id="modal-hobby">
			    </p>
			    <p>
			      	<button id="modal-submit">提交</button>
			      	<button id="modal-cancel">取消</button>
			    </p>
		  	</div>
		</div>
	</body>
		<script>
			li =[10,20,30,40]
			$.each(li,function(i, v){			  	
			  	if( v === 20){
			  		return;
			  	}
			  	console.log(i, v);						//index是索引，ele是每次循环的具体元素。
			})
			
			$("li").each(function(){
			  	$(this).addClass("c1");					
			  	console.log( $(this) );								// this指的是每次循环的具体元素。
			  	if( $(this).text() === "002" ){
			  		return false;
			  	}
			});
		</script>
		<script>
			function showModal(){
				// 弹出模态框!
				 $("#myCover,#myModal").removeClass("hide");
			}
			
			function closeModal(){
				//1. 清空模态框中的input
//		        $("#myModal nput").val("");							// 效率略低
		        $("#myModal").find("input").val("");
		        // 2. 隐藏模态框
				$("#myCover,#myModal").addClass("hide");
			}
			
		    // 给新增按钮绑定事件
		    $("#add").on("click", function () {
		        // 把模态框弹出!
		       showModal()
		    });
		
		    // 模态框中的取消按钮绑定事件
		    $("#modal-cancel").on("click", function () {	        
		        closeModal();
		    })
		
		    // 模态框中的提交按钮绑定事件
		    $("#modal-submit").on( "click",function(){
		    	// 1. 取到 用户 填写的 input框的值
		    	var aname = $("#modal-name").val();
		    	var ahobby = $( "#modal-hobby").val();
		    	
		    	var $myModalEle = $("#myModal");
		    	 // 判断,按需操作
        		var $currentTrEle = $myModalEle.data("currentTr");
        		if ($currentTrEle !== undefined) { 					// 说明是编辑状态		           
		            $currentTrEle.children().eq(1).text( aname );
		            $currentTrEle.children().eq(2).text( ahobby );			            
		            $myModalEle.removeData();						// 清空之前保存的当前行,恢复提交 undifined
		        } else {
			    	// 创建tr标签把数据填进去
			    	var trEle = document.createElement("tr");
			    	var num = $("tr").length;
			    	$(trEle).html("<td>"+ num +"</td>" + 
			    		"<td>"+ aname +"</td>" +
			    		"<td>"+ ahobby +"</td>" +
			    		'<td><button class="edit-btn">编辑</button><button class="delete-btn">删除</button></td>'
			    	);
			    	$("tbody").append(trEle);
		    	}
		    	closeModal();
		    
		    })
		    
		    // 2. 根据是编辑 还是新增 做不同的操作
		    // 2.1 如果是新增操作,就生成一条新的tr,加到table的最后
		    // 2.2 如果是编辑操作, 根据先前 编辑 按钮那一行
		    // 难点在于 如何确定 编辑的是哪一行?  --> 利用data()可以存具体的jQuery对象
		
		    // 给每一行的编辑按钮绑定事件
			$( "tbody" ).on( "click",".edit-btn",function(){		// 要使用事件委托,基于已经存在的元素(页面加载完之后存在的标签)绑定事件
				showModal();
				var $currentTrEle = $(this).parent().parent();
				
				// 把当前行的jQuery对象保存起来
        		$("#myModal").data("currentTr", $currentTrEle);
				
				var name = $currentTrEle.children().eq(1).text();
				var hobby = $currentTrEle.children().eq(2).text();
				
				// 把原来的数据填写到模态框中的input
				$( "#modal-name").val( name );
				$( "#modal-hobby").val( hobby );
			})

		 	// 给每一行的删除按钮绑定事件
			$("tbody").on( "click",".delete-btn",function(){		// 要使用事件委托,基于已经存在的元素(页面加载完之后存在的标签)绑定事件
				var $currentTrEle = $(this).parent().parent();				
				// 更新序号
				$currentTrEle.nextAll().each( function(){
					var oldNumber = $(this).children().first().text();
					$(this).children().first().text( oldNumber - 1 );
				})
				
				//删除对象
				$currentTrEle.remove();
			})
		
		</script>
</html>
```



## ajax

https://blog.csdn.net/zhangank/article/details/90731461

> Ajax（Asynchronous Javascript + XML）

### `$.ajax`

&emsp;&emsp;这个是 JQuery 对 ajax 封装的最基础步，通过使用这个函数可以完成异步通讯的所有功能。也就是说什么情况下我们都可以通过此方法进行异步刷新的操作。但是它的参数较多，有的时候可能会麻烦一些。看一下常用的参数：  

```javascript
$.ajax({
    type: "POST",  				//提交方式
    url: "数据的提交路径",
    data: {},					//需要提交的数据
    dataType: "JSON",			//服务器返回数据的类型，例如xml,String,Json等
    success: function(result) {
        //请求成功后的回调函数, 根据结果进行相应的处理  
    },
    error: function(result) { 
        // 请求失败后的回调函数
    }
})
```



### `$.post`

&emsp;&emsp;这个函数其实就是对 `$.ajax` 进行了更进一步的封装，减少了参数，简化了操作，但是运用的范围更小了。`$.post` 简化了数据提交方式，只能采用 POST 方式提交。只能是异步访问服务器，不能同步访问，不能进行错误处理。在满足这些情况下，我们可以使用这个函数来方便我们的编程，它的主要几个参数，像 method，async 等进行了默认设置，我们不可以改变的。例子不再介绍。



### `$.get`

&emsp;&emsp;和 `$.post` 一样，这个函数是对 get 方法的提交数据进行封装，只能使用在 get 提交数据解决异步刷新的方式上，使用方式和上边的也差不多。这里不再演示。



### `$.getJSON`

`$.getJSON`，这个是进一步的封装，也就是对返回数据类型为 Json 进行操作。里边就三个参数，需要我们设置，非常简单：url,[data],[callback]。



# JQuery 源码分析





# JQuery 注意事项





# JQuery 思考

