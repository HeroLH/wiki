----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 非常好用的第三方库 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2022-02-21 | Herolh | 文档创建 |
|            |        |          |



## 简介





## 时间处理

### Carbon

carbon 是一个轻量级、语义化、对开发者友好的 Golang 时间处理库，支持链式调用和 gorm、xorm、zorm 等主流 orm。

[github 仓库地址](https://github.com/golang-module/carbon)



#### 使用

[官方使用手册](https://github.com/golang-module/carbon/wiki/%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)

```shell
# Golang 版本小于1.16
go get -u github.com/golang-module/carbon

# Golang 版本大于等于1.16
go get -u github.com/golang-module/carbon/v2
```



#### Carbon 和 time.Time 互转

```go
// 将 time.Time 转换成 Carbon
carbon.Time2Carbon(time.Now())

// 将 Carbon 转换成 time.Time
carbon.Now().Carbon2Time()
```