----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Dart 的基本使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-08-16 | Herolh | 文档创建 |
|            |        |          |



## 简介
[官网](https://flutter.dev/)

Dart 是由谷歌开发的计算机编程语言,它可以被用于 web、服务器、移动应用 和物联网等领域的开发。
Dart 诞生于 2011 年，号称要取代 JavaScript。但是过去的几年中一直不温不火。直到 Flutter 的出现现在被人们重新重视。
要学 Flutter 的话我们必须首先得会 Dart。



## 使用

### Hello world

```shell
main() {
  print("hello world!");
}
```



### 入口方法

```dart
main() {
  print("hello world!");
}

// 表示main方法没有返回值   == ts ==>  function main:void(){}
void main() {
  print("hello world!");
}
```





### 注释

```dart
//
///
/* 注释 */
```



### 变量

变量是一个引用，根据Dart中“万物皆对象”原则，即变量存储的都是对象的引用，或者说它们都是指向对象.



#### 申明变量

声明可以有两种方式，一种是不指定类型，即使用 var关键字；另一种是明确指定类型（Optional types）：

- 不指定类型

    ```dart
    var name = 'Bob';
    ```

- 明确指定类型

    ```dart
    String name = 'Bob';
    ```

因为有类型推导，所以两种实现效果一样，官方推荐在函数内的本地变量尽量使用 var 声明。



##### 注意：

- 在变量类型并不明确的情况下，可以使用 dynamic 关键字：

    ```dart
    dynamic name = 'Bob';
    ```

- dart 是强类型语言，有类型校验：

    ```dart
    var str = "";
    String str0 = 123; 	// 强行赋值会报错！
    str = 123; 			// 强行赋值会报错！
    ```

    



#### 默认值

==未初始化的变量默认值是 null。即使变量是数字类型默认值也是 null==，因为在 Dart 中一切都是对象，数字类型也不例外。

```dart
int lineCount;
assert(lineCount == null);
```

提示： 在生产环境代码中 `assert()` 函数会被忽略，不会被调用。 在开发过程中, `assert(condition)` 会在非 true 的条件下抛出异常。



#### Final 和 Const
&emsp;&emsp;使用过程中从来不会被修改的变量， 可以使用 final 或 const，而不是 var 或者其他类型，Final 变量的值只能被设置一次； Const 变量在编译时就已经固定 (Const 变量 是隐式 Final 的类型) 。最高级 final 变量或类变量在第一次使用时被初始化。
提示： 
&emsp;&emsp;实例变量可以是 final 类型但不能是 const 类型。 必须在构造函数体执行之前初始化 final 实例变量 —— 在变量声明中，参数构造函数中或构造函数的初始化列表中进行初始化。

```dart
final a=new DateTime.now();
print(a);   					// 2019-05-10 15:59:02.966122
//const a=new DateTime.now();   // 报错了

//区别：
// final 可以开始不赋值 只能赋一次 ; 而final不仅有const的编译时常量的特性，最重要的它是运行时常量，并且final是惰性初始化，即在运行时第一次使用前才初始化
```





#### Dart 的命名规则
- 变量名称必须由数字、字母、下划线和美元符($)组成。

- 标识符开头不能是数字

- 标识符不能是保留字和关键字。

- 变量的名字是区分大小写的。

    > 如: age 和 Age是不同的变量。在实际的运用中,也建议,不要用一个单词大小写区分两个变量。

- 标识符(变量名称)一定要见名思意 ：变量名称建议用名词，方法名称建议用动词*  





### 常用数据类型

#### Numbers

##### int

##### double

```dart
void main() {
  //1、int   必须是整型
  int a = 123;
  a = 45;
  print(a);

  //2、double  既可以是整型 也可是浮点型
  double b = 23.5;
  b = 24;
  print(b);

  //3、运算符
  // + - * / %
  var c = a + b;
  print(c);
}
```





####  Strings

```shell
void main() {
  String str1_1 = '''this is str1
  this is str1
  this is str1
  ''';

  print(str1_1);

  String str1_2 = """
    this is str1
    this is str1
    this is str1
    """;

  print(str1_2);

  //2、字符串的拼接

  String str1 = '你好';
  String str2 = 'Dart';

  print("$str1 $str2");
  print(str1 + str2);
  print(str1 + " " + str2);
}
```



#### Booleans

```dart
void main() {
  //1、bool
  bool flag1 = true;
  print(flag1);
  bool flag2 = false;
  print(flag2);

  //2、条件判断语句
  var flag = true;
  if (flag) {
    print('真');
  } else {
    print('假');
  }

  // var a = 123;
  // var b = '123';
  // if (a == b) {         // 类型不一致报错
  //   print('a=b');
  // } else {
  //   print('a!=b');
  // }

  var a = 123;
  var b = 123;
  if (a == b) {
    print('a=b');
  } else {
    print('a!=b');
  }
}
```



#### List

> 在 Dart 中，数组是列表对象，所以大多数人只是称它们为列表

```dart
/*
Dart数据类型： List（数组/集合）
*/
void main() {
  //1、第一种定义List的方式
  var l1 = ["张三", 20, true];
  print(l1); //[张三, 20, true]
  print(l1.length); //3
  print(l1[0]); //张三

  //2、第二种定义List的方式 指定类型
  var l2 = <String>["张三", "李四"];
  print(l2);

  //3、第三种定义List的方式  增加数据 ,通过[]创建的集合它的容量可以变化
  var l3 = [];
  print(l3);
  print(l3.length);
  l3.add("张三");
  l3.add("李四");
  l3.add(20);
  print(l3);
  print(l3.length);

  //4、第四种定义List的方式
  // var l6 = new List(); //在新版本的dart里面没法使用这个方法了
  var l6 = List.filled(2, ""); //创建一个固定长度的集合
  print(l6);
  print(l6[0]);
  l6[0] = "张三"; //修改集合的内容
  l6[1] = "李四";
  print(l6); //[张三, 李四]
  l6.add("王五"); //错误写法
  //通过List.filled创建的集合长度是固定
  // var l6=List.filled(2, "");
  // print(l6.length);
  // l6.length=0;  //修改集合的长度   报错

  var l7 = <String>["张三", "李四"];
  print(l7.length); //2
  l7.length = 0; //可以改变的
  print(l7); //[]

  var l8 = List<String>.filled(2, "");

  l8[0] = "string";
  // l8[0] = 222; // 报错
  print(l8);
}
```







#### Maps

> 通常来说，Map 是一个键值对相关的对象。 键和值可以是任何类型的对象。每个键只出现一次， 而一个值则可以出现多次

```DART
void main() {
  //第一种定义 Maps的方式
  var person = {
    "name": "张三",
    "age": 20,
    "work": ["程序员", "送外卖"]
  };

  print(person);
  print(person["name"]);
  print(person["work"]);

  //第二种定义 Maps的方式

  var p = new Map();

  p["name"] = "李四";
  p["age"] = 22;
  p["work"] = ["程序员", "送外卖"];
  print(p);

  print(p["age"]);
}

```





#### Runes

> *Rune是UTF-32编码的字符串。它可以通过文字转换成符号表情或者代表特定的文字。*

```dart
main() {
    var clapping = '\u{1f44f}';
    print(clapping);
    print(clapping.codeUnits);
    print(clapping.runes.toList());

    Runes input = new Runes(
        '\u2665  \u{1f605}  \u{1f60e}  \u{1f47b}  \u{1f596}  \u{1f44d}');
    print(new String.fromCharCodes(input));
}
```



#### Symbols

> Symbol 对象表示在 Dart 程序中声明的运算符或标识符。您可能永远不需要使用符号，但它们对于按名称引用标识符的 API 非常有用，因为缩小会更改标识符名称而不会更改标识符符号。要获取标识符的符号，请使用符号文字，它只是＃后跟标识符：

在 Dart 中符号用 # 开头来表示，入门阶段不需要了解这东西，可能永远也用不上。 *http://dart.goodev.org/guides/libraries/library-tour#dartmirrors---reflection*



#### 类型判断 is

```dart
void main() {
  var str = 123;
  if (str is String) {
    print('是string类型');
  } else if (str is int) {
    print('int');
  } else {
    print('其他类型');
  }
}
```



#### 类型转换

```dart
void main() {
  //1、Number与String类型之间的转换
  // Number类型转换成String类型 toString()
  // String类型转成Number类型  int.parse()
  // String str='123';
  // var myNum=int.parse(str);
  // print(myNum is int);
  // String str='123.1';
  // var myNum=double.parse(str);
  // print(myNum is double);
  //  String price='12';
  // var myNum=double.parse(price);
  // print(myNum);
  // print(myNum is double);

  //报错
  // String price='';
  // var myNum=double.parse(price);
  // print(myNum);
  // print(myNum is double);
  // try  ... catch
  //  String price='';
  //   try{
  //     var myNum=double.parse(price);
  //     print(myNum);
  //   }catch(err){
  //        print(0);
  //   }

  // var myNum=12;
  // var str=myNum.toString();
  // print(str is String);

  // 2、其他类型转换成Booleans类型
  // isEmpty:判断字符串是否为空
  // var str='';
  // if(str.isEmpty){
  //   print('str空');
  // }else{
  //   print('str不为空');
  // }

  // var myNum=123;

  // if(myNum==0){
  //    print('0');
  // }else{
  //   print('非0');
  // }

  // var myNum;

  // if(myNum==0){
  //    print('0');
  // }else{
  //   print('非0');
  // }

  // var myNum;
  // if(myNum==null){
  //    print('空');
  // }else{
  //   print('非空');
  // }

  var myNum = 0 / 0;

  // print(myNum);

  if (myNum.isNaN) {
    print('NaN');
  }
}

```



### 控制语句

#### 循环语句

#### for 循环

```dart
for(int i=1;i<=10;i++){
   print(i);
}
```



#### while 循环

```dart
void main() {
  /*
    int i=1;
    while(i<=10){

        print(i);
    }
    //死循环
 
 */

  // int i=1;
  // while(i<=10){
  //     print(i);
  //     i++;
  // }

//1、求1+2+3+4 ...+100的和

  // int i=1;
  // var sum=0;
  // while(i<=100){
  //    sum+=i;
  //    i++;
  // }
  // print(sum);

  // int i=1;
  // var sum=0;
  // do{
  //    sum+=i;
  //    i++;
  // }while(i<=100);
  // print(sum);

  //while 和 do while的区别   第一次循环条件不成立的情况下
  int i = 10;
  while (i < 2) {
    print('执行代码');
  }

  var j = 10;
  do {
    print('执行代码');
  } while (j < 2);
}
```

