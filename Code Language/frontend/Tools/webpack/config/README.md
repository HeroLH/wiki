----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Webpack 的配置 {#index}

[TOC]











--------------------------------------------

## 配置

创建 `webpack.config.js` 配置文件

- entry：入口文件， 指定Web Pack用哪个文件作为项目的入口
- output：输出， 指定WebPack把处理完成的文件放置到指定路径
- module：模块， 用于处理各种类型的文件
- plugins：插件， 如：热更新、代码重用等
- resolve：设置路径指向
- watch：监听， 用于设置文件改动后直接打包

```js
const path = require(`path`)

module.exports = {
    entry: "./src/main.js",
    output: {
        // path: "./dict",                              // 相对路径会并，要用绝对路径
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js"
    },
    // 以上相当于 `webpack ./src/main.js ./dist/bundle.js`
	module:{
		loaders:[
			{test:/\.js$/,;\loade:""}
		]
	},
	plugins:{},
	resolve: {
        alias: {
            "vue$": "vue/dist/vue.esm.js"
        },
        // 导入时可以省略后缀
        extensions: ['.js', '.css', '.vue']
    },
	watch:true
}
```

  直接运行`webpack`命令打包