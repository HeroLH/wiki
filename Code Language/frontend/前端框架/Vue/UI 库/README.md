----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Vue UI 库的使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | /修改人 | 内容     |
| :--------: | :-----: | :------- |
| 2021-05-15 | Herolh  | 文档创建 |
|            |         |          |



## Bootstrap Vue

### 简介

> 借助 BootstrapVue，您可以使用 Vue.js 和世界上最受欢迎的前端 CSS 库 Bootstrap v4 在网络上构建响应式，移动优先和 ARIA 可访问的项目 。

[官网](https://bootstrap-vue.org/)



#### 安装

```shell
# With npm
npm install vue bootstrap bootstrap-vue

# With yarn
yarn add vue bootstrap bootstrap-vue

# 如果你和我一样出现了 Undefined variable: "$custom-control-indicator-size". 这样的错误
# 请尝试降级 bootstrap, 以下是我安装的版本
vue@2.6.12
bootstrap@4.5.3
bootstrap-vue@2.21.2
```

然后，在您的应用程序入口点( 通常是 app.js 或 main.js )中注册 BootstrapVue：

```js
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
```

























