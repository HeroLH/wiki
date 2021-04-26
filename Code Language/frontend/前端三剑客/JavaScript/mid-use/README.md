> *Made By Herolh*

----------------------------------------------

# JavaScript 的基本使用 {#index}

[TOC]











--------------------------------------------

## 简介
&emsp;&emsp;JavaScript 一门弱类型脚本语言，其源代码在发往客户端运行之前不需要经过编译，而是将文本格式的字符代码发送给浏览器，由浏览器解释运行。 Native 原生 JS 开发，也就是让我们按照【ECMAScript】标准的开发方式，简称 ES，特点是所有浏览器都支持。截至到当前，ES 标准以发布如下版本：

- ES3
- ES4（内部，未正式发布）
- ES5（全浏览器支持）
- ES6（常用，当前主流版本：webpack 打包成为 ES5 支持）
- ES7
- ES8
- ES9（草案阶段）

区别就是逐步增加新特性。



### 历史

- 1997年 ECMAScript 1.0 诞生
- 1999年12月 ECMAScript 3.0诞生，它 是一个巨大的成功，在业界得到了广泛的支持，它奠定了JS的基本语法，被其后版本完全继承。直到今天，我们一开始学习JS，其实就是在学3.0版的语法
- 2000年的ECMAScript4.0是当下ES6的前身，但由于这个版本太过激烈，对ES3做了彻底升级，所以暂时被“和谐”了
- 2009年12月，ECMAScript5.0版正式发布。ECMA专家组预计ECMAScript的第五个版本会在2013年中期到2018年作为主流的开发标准。2011年6月，ES5.1版发布，并且成为ISO国际标准
- 2013年，ES6草案冻结，不再添加新的功能，新的功能将被放到ES7中；2015年6月，ES6正式通过，成为国际标准

&emsp;感兴趣的同学可以查看 [ECMAScript 6 入门](http://es6.ruanyifeng.com/)





### TypeScript  是什么

- TypeScript 是一种由微软开发的自由和开源的编程语言。它是 JavaScript 的一个超集， 而且本质上向这个语言添加了可选的静态类型和基于类的面向对象编程。由安德斯・海尔斯伯格 (C#、Delphi、TypeScript 之父； .NET 创立者) 主导。
- 该语言的特点就是除了具备 ES 的特性之外还纳入了许多不在标准范围内的新特性，所以会导致很多浏览器不能直接支持 TypeScript 语法， 需要编译后 (编译成 JS) 才能被浏览器正确执行。



### JavaScript 框架

#### JQuery
&emsp;&emsp;大家熟知的 JavaScript 库，优点就是简化了 DOM 操作，缺点就是 DOM 操作太频繁，影响前端性能；在前端眼里使用它仅仅是为了兼容 IE6，7，8；



#### Angular
&emsp;&emsp;Google 收购的前端框架，由一群 Java 程序员开发，其特点是将后台的 MVC 模式搬到了前端并增加了==模块化开发==的理念，与微软合作，采用了 TypeScript 语法开发；对后台程序员友好，对前端程序员不太友好；最大的缺点是版本迭代不合理（如 1 代–>2 代，除了名字，基本就是两个东西；截止发表博客时已推出了 Angular6）



#### React

&emsp;&emsp;Facebook 出品，一款高性能的 JS 前端框架；特点是提出了新概念 ==虚拟 DOM==用于减少真实 DOM 操作，在内存中模拟 DOM 操作，有效的提升了前端渲染效率；缺点是使用复杂，因为需要额外学习一门【JSX】语言；



#### Vue
&emsp;&emsp;一款渐进式 JavaScript 框架，所谓渐进式就是逐步实现新特性的意思，如实现模块化开发、路由、状态管理等新特性。其特点是==综合了 Angular( 模块化 )和 React( 虚拟 DOM )==的优点；



#### Axios：
&emsp;&emsp;前端通信框架；因为 Vue 的边界很明确，就是为了处理 DOM，所以并不具备通信能力，此时就需要额外使用一个通信框架与服务器交互；当然也可以直接选择使用 jQuery 提供的 AJAX 通信功能；





### JavaScript 构建工具

- Babel：JS 编译工具，主要用于浏览器不支持的 ES 新特性，比如用于编译 TypeScript
- WebPack：模块打包器，主要作用就是打包、压缩、合并及按序加载





### 主流前端框架

#### Vue.js

### iView

iview 是一个强大的基于 Vue 的 UI 库， 有很多实用的基础组件比 element ui 的组件更丰富， 主要服务于 PC 界面的中后台产品。使用单文件的 Vue 组件化开发模式基于 npm+webpack+babel 开发， 支持 ES 2015 高质量、功能丰富友好的 API， 自由灵活地使用空间。

- [官网地址](https://iviewui.com/)
- [Github](https://github.com/iview/iview)
- [iview-admin](https://www.worldlink.com.cn/en/osdir/iview-admin.html)

**备注：属于前端主流框架，选型时可考虑使用，主要特点是移动端支持较多**

### Element UI

Element 是饿了么前端开源维护的 Vue UI 组件库， 组件齐全， 基本涵盖后台所需的所有组件，文档讲解详细， 例子也很丰富。主要用于开发 PC 端的页面， 是一个质量比较高的 Vue UI 组件库。

- [官网地址](https://element.eleme.io/)
- [Github](https://github.com/ElemeFE/element)
- [vue-element-admin](https://panjiachen.github.io/vue-element-admin-site/zh/)

**备注：属于前端主流框架，选型时可考虑使用，主要特点是桌面端支持较多**

### ICE

飞冰是阿里巴巴团队基于 React/Angular/Vue 的中后台应用解决方案， 在阿里巴巴内部， 已经有 270 多个来自几乎所有 BU 的项目在使用。飞冰包含了一条从设计端到开发端的完整链路，帮助用户快速搭建属于自己的中后台应用。

- [官网地址](https://ice.work/)
- [Github](https://github.com/alibaba/ice)

**备注：主要组件还是以 React 为主， 截止 2019 年 02 月 17 日更新博客前对 Vue 的支持还不太完善，目前尚处于观望阶段**

### VantUI

Vant UI 是有赞前端团队基于有赞统一的规范实现的 Vue 组件库， 提供了 - 整套 UI 基础组件和业务组件。通过 Vant， 可以快速搭建出风格统一的页面，提升开发效率。

- [官网地址](https://youzan.github.io/vant-weapp/#/intro)
- [Github](https://github.com/youzan/vant)

### AtUI

at-ui 是一款基于 Vue 2.x 的前端 UI 组件库， 主要用于快速开发 PC 网站产品。它提供了一套 n pm+web pack+babel 前端开发工作流程， CSS 样式独立， 即使采用不同的框架实现都能保持统一的 UI 风格。

- 官网地址
- [Github](https://github.com/aliqin/atui)

### Cube Ul

cube-ui 是滴滴团队开发的基于 Vue js 实现的精致移动端组件库。支持按需引入和后编译， 轻量灵活；扩展性强，可以方便地基于现有组件实现二次开发。

- [官网地址](http://www.cubeent.co.kr/)
- [Github](https://github.com/square/cube)

### 混合开发

#### Flutter

Flutter 是谷歌的移动端 UI 框架， 可在极短的时间内构建 Android 和 iOS 上高质量的原生级应用。Flutter 可与现有代码一起工作， 它被世界各地的开发者和组织使用， 并且 Flutter 是免费和开源的。

- [官网地址](https://flutterchina.club/)
- [Github](https://github.com/flutter/flutter)

**备注：Google 出品， 主要特点是快速构建原生 APP 应用程序， 如做混合应用该框架为必选框架**

#### lonic

lonic 既是一个 CSS 框架也是一个 Javascript UI 库， lonic 是目前最有潜力的一款 HTML 5 手机应用开发框架。通过 SASS 构建应用程序， 它提供了很多 UI 组件来帮助开发者开发强大的应用。它使用 JavaScript MV VM 框架和 Angular JS/Vue 来增强应用。提供数据的双向绑定， 使用它成为 Web 和移动开发者的共同选择。

- [官网地址](https://ionicframework.com/)
- [官网文档](http://www.ionic.wang/js_doc-index.html)
- [Github](https://github.com/tonib/kaichronicles)

### 微信小程序

#### mpvue

mpvue 是美团开发的一个使用 `Vue.js` 开发小程序的前端框架， 目前支持微信小程序、百度智能小程序，头条小程序和支付宝小程序。框架基于 `Vue.js`， 修改了的运行时框架 `runtime` 和代码编译器 `compiler` 实现， 使其可运行在小程序环境中， 从而为小程序开发引入了 `Vue.js` 开发体验。

- [官网地址](http://mpvue.com/)
- [Git hub](https://github.com/Meituan-Dianping/mpvue)

**备注：完备的 Vue 开发体验， 井且支持多平台的小程序开发， 推荐使用**

#### WeUI

WeUI 是一套同微信原生视觉体验一致的基础样式库， 由微信官方设计团队为微信内网页和微信小程序量身设计， 令用户的使用感知更加统一。包含 button、cell、dialog、toast、article、icon 等各式元素。

- [官网地址](https://weui.io/)
- [Github](https://github.com/Tencent/weui)

#