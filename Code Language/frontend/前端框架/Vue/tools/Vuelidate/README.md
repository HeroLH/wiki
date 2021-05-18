----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# vuelidate 基本使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | /修改人 | 内容     |
| :--------: | :-----: | :------- |
| 2021-05-16 | Herolh  | 文档创建 |
|            |         |          |



## 简介

> Vue.js 的简单，轻量级基于模型的验证

[中文官网](https://www.vuelidate.cn/)



### 安装

软件包可通过 npm 安装

```bash
npm install vuelidate --save
```



## 基本用法

### 引入

您可以导入库并将其 use 作为 Vue 插件导入，以在包含验证配置的所有组件上全局启用该功能。

```js
import Vue from 'vue'
// 必须在 App.vue 前进行引入
import Vuelidate from 'vuelidate'
Vue.use(Vuelidate)
```

另外，也可以将混合直接导入到将使用混合的组件中。

```js
import { validationMixin } from 'vuelidate'
var Component = Vue.extend({
  mixins: [validationMixin],
  validations: { ... }
})
```



如果您更喜欢使用 require，则可以使用它代替 import 语句。这特别适用于解构语法。

```js
const { validationMixin, default: Vuelidate } = require('vuelidate')
const { required, minLength } = require('vuelidate/lib/validators')
```

软件包中还提供了支持浏览器的捆绑软件。

```js
<script src="vuelidate/dist/vuelidate.min.js"></script>
```





### 基本形式

对于每个要验证的值，您必须在 `validations` 选项内部创建一个键。您可以通过在输入框上使用适当的事件来指定输入何时变脏。

```js
import { required, minLength, between } from 'vuelidate/lib/validators'
export default {
  data() {
    return {
      name: '',
      age: 0
    }
  },
  validations: {
    name: {
      required,
      minLength: minLength(4)
    },
    age: {
      between: between(20, 30)
    }
  }
}

```

















