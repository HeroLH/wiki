----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Webpack 安装{#index}

[TOC]











--------------------------------------------

## 依赖

- 安装 webpack 首先需要安装 nodejs, nodejs 自带了软件管理包 npm



## 安装

### 全局安装 webpack

```shell
npm  install webpack@3.6.0 -g
```



### 局部安装 webpack

```shell
--save-dev
```

开发时依赖，项目打包后就不需要继续使用了。



### 为什么全局安装后还需要局部安装？

在终端执行 webpack 命令，使用的是 全局安装的 webpack

当在 `package.json` 中 定义了 script 时，其中包含了 webpack 命令， 那么使用的就是局部 webpack



## 测试安装成功

```shell
webpack -v
```

