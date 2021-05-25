----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Axios 的基本使用 {#index}

[TOC]











--------------------------------------------

## 简介

Axios是一个开源的基于 promise 的可以用在浏览器端和 `Node JS` 的异步通信框架， 她的主要作用就是实现 AJAX 异步通信，其功能特点如下：

- 从浏览器中创建`XMLHttpRequests`
- 从node.js创建http请求
- 支持Promise API[JS中链式编程]
- 拦截请求和响应
- 转换请求数据和响应数据
- 取消请求
- 自动转换JSON数据
- 客户端支持防御XSRF(跨站请求伪造)

GitHub：https://github.com/axios/axios  

中文文档：http://www.axios-js.com/



### 安装

- 使用 npm:

    ```shell
    npm install axios
    ```

- 使用 cdn:

    ```shell
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    ```

    



### 框架整合

#### vue-axios

##### 引入

> 基于 vuejs 的轻度封装

```shell
npm install --save axios vue-axios
```

将下面代码加入入口文件:

```js
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
```

按照这个顺序分别引入这三个文件： `vue`, `axios` and `vue-axios`



##### 使用

该包装器将 axios 绑定到 Vue，如果您使用的是单个文件组件，则可以将其绑定到 Vue。

```js
Vue.axios.get(api).then((response) => {
  console.log(response.data)
})

this.axios.get(api).then((response) => {
  console.log(response.data)
})

this.$http.get(api).then((response) => {
  console.log(response.data)
})
```



#### react-axios

适用于 react 框架的 Axios 组件， 具有 child function callback。在 render 阶段进行异步请求。



##### 引入

```shell
npm install react-axios
```



### 创建一个 axios 实例

```js
const instance = axios.create({
  baseURL: 'https://some-domain.com/api/',
  timeout: 1000,
  headers: {'X-Custom-Header': 'foobar'}
});
```

