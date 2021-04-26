### nodejs

- 去官网https://nodejs.org/en/download/ 下载 安装(傻瓜式安装)

- 打开终端 cmd : 执行`node -v` 如果出现版本号，证明安装node成功 ，跟安装python雷同

- 下载完node之后，会自带包管理器 npm，好比 是python中 pip3包管理器。pip3 install xxx

- 使用npm

    - `npm init --yes` 自动生成一个package.json文件( 管理包 )

        ```javascript
        {
            "name": "vue_lesson",
            "version": "1.0.0",
            "description": "这是我的vue的第一个项目",
            "main": "index.js",
            "scripts": {
              "test": "echo "Error: no test specified" && exit 1"
            },
            "author": "mjj",
            "license": "ISC",
            "dependencies": {				
              "vue": "^2.5.16"
            }
        }
        ```

    - 2.下载依赖包

        ```shell
        npm install vue --save
        npm install jquery@2.1 --save			# @后面跟的是你想下载的版本号
        ```

    - 卸载包

        ```shell
        npm uninstall vue --save
        ```

    - 4.下载项目所有的依赖包

        ```shell
        npm install
        ```

