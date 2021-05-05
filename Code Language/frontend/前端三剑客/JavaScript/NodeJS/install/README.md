----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# node.js 的安装 {#index}

[TOC]











--------------------------------------------

## 基本安装

### linux 平台

#### arch

```shell
yay -S npm nodejs
```

```shell
" 安装cnpm
sudo npm install -g cnpm --registry=https://registry.npm.taobao.org 
" 在当前用户目录下创建 ~/.npm-global 目录用于存放下载的包，避免使用默认的包路径时提示没有权限
mkdir ~/.npm-global
" 更改链接
npm config set prefix '~/.npm-global'
" 在用户的profile下增加path，为的是系统能够找到可执行文件的目录
export PATH=~/.npm-global/bin:$PATH
" update profile。使其生效
source ~/.profile
```





## NVM 安装

>  nvm (Node Version Manager) 是 Nodejs 版本管理器，可对不同的 node 版本快速进行切换。

&emsp;&emsp;基于 node 的工具和项目越来越多，但是每个项目使用的 node 版本可能不一致，就会出现一些奇怪的问题。比如：自己电脑安装的是最新版的 node, 接手的项目使用的是低版本的 node。那么我只有切换到低版本的 node 再进行操作才不会报错。而 NVM 就是用来帮助我们快速切换 node 版本的。



### linux 平台

#### arch

```shell
sudo pacman -S nvm
```

```shell
# 环境变量
echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.bashrc
echo 'source /usr/share/nvm/init-nvm.sh' >> ~/.zshrc
```

##### 基本使用

`nvm list` 或者 `nvm ls` 查看 node 的安装版本

`nvm install 6.9.0` 安装一个 6.9.0 版本的 node

`nvm use 6.9.0` 使用这个 6.9.0 版本的 node

`nvm uninstall 6.9.0` 删除 6.9.0 版本的 node

`nvm ls-remote` 罗列远程的 node 版本

`nvm current` 查看当前正在使用的 node 版本

`nvm alias default v4.3.0` 切换 v.4.3.0 为默认版本，每次新建的命令行中就是默认的版本了

`npm list --depth=0 -g` 查看全局都安装了那些 npm 的包

