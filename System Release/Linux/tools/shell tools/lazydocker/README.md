----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# lazydocker 基本使用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| xxxx-xx-xx | Herolh | 文档创建 |
|            |        |          |



## 简介



## 安装

### ubuntu 下

```shell
curl https://raw.githubusercontent.com/jesseduffield/lazydocker/master/scripts/install_update_linux.sh | bash
```

> 网络环境不好的可以直接去 [release](https://github.com/jesseduffield/lazydocker/releases) 下载对应版本解压安装
>
> ```shell
> tar xzvf lazydocker.tar.gz lazydocker
> sudo mv -f lazydocker /usr/local/bin
> rm lazydocker.tar.gz
> ```





## 快捷键

[github README](https://github.com/jesseduffield/lazydocker/blob/master/docs/keybindings/Keybindings_en.md)



### 项目面板

| 快捷键 | 说明                           |
| :----: | ------------------------------ |
|   e    | 编辑 lazydocker 配置           |
|   o    | 打开 lazydocker 配置           |
|   [    | previous tab                   |
|   ]    | next tab                       |
|   m    | 查看日志                       |
| enter  | 焦点集中在主面板(esc 可以退出) |



### 容器面板

| 快捷键 | 说明                                   |
| :----: | -------------------------------------- |
|   [    | previous tab                           |
|   ]    | next tab                               |
|   d    | 删除容器                               |
|   e    | 隐藏或展示 已停止的容器 (docker ps -a) |
|   s    | 关闭容器                               |
|   r    | 重启容器                               |
|   a    | 进入容器                               |
|   E    | 打开容器终端                           |
|   m    | 查看日志                               |
|   c    | run predefined custom command          |
|   b    | view bulk commands                     |
|   w    | open in browser (first port is http)   |
| enter  | 焦点集中在主面板(esc 可以退出)         |



### 镜像面板

| 快捷键 | 说明                                 |
| :----: | ------------------------------------ |
|   [    | previous tab                         |
|   ]    | next tab                             |
|   c    | run predefined custom command        |
|   b    | view bulk commands                   |
|   w    | open in browser (first port is http) |
| enter  | 焦点集中在主面板(esc 可以退出)       |



卷面板

| 快捷键 | 说明                                 |
| :----: | ------------------------------------ |
|   [    | previous tab                         |
|   ]    | next tab                             |
|   c    | run predefined custom command        |
|   b    | view bulk commands                   |
|   w    | open in browser (first port is http) |
| enter  | 焦点集中在主面板(esc 可以退出)       |





## 配置

[官网 README](https://github.com/jesseduffield/lazydocker/blob/master/docs/Config.md)