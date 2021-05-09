----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Vue Route 基本使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-05-08 | Herolh | 文档创建 |
|            |        |          |



## 简介

Vue Router 是 Vue.js 官方的路由管理器。它和 Vue.js 的核心深度集成， 让构建单页面应用变得易如反掌。包含的功能有：

- 嵌套的路由 / 视图表
- 模块化的、基于组件的路由配置
- 路由参数、查询、通配符
- 基于 Vue js 过渡系统的视图过渡效果
- 细粒度的导航控制
- 带有自动激活的 CSS class 的链接
- HTML5 历史模式或 hash 模式， 在 IE 9 中自动降级
- 自定义的滚动行为



### 安装

基于第一个 vue-cli 进行测试学习； 先查看 node modules 中是否存在 vue-router， vue-router 是一个插件包， 所以我们还是需要用 n pm/cnpm 来进行安装的。打开命令行工具，进入你的项目目录，输入下面命令：

```shell
npm install vue-router --save-dev
```

如果在一个模块化工程中使用它，必须要通过 `Vue.use ()` 明确地安装路由功能：

```js
import Vue from 'vue'
//导入路由插件
import VueRouter from 'vue-router'

//安装路由
Vue.use(VueRouter);

//配置路由
// 创建 VueRouter 对象
const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  }
]

// 将 VueRouter 对象传入 Vue 对象，并导出
export default new Router({
  routes
})
```



### 测试

1、先删除没有用的东西 2、`components` 目录下存放我们自己编写的组件 3、定义一个 `Content.vue` 的组件