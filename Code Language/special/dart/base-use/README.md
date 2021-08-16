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

创建和设置一个 Final 变量：