----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 推荐安装应用 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-09-02 | Herolh | 文档创建 |
|            |        |          |





## 包管理工具

### Homebrew

```shell
/bin/bash -c "$(curl -fsSL https://cdn.jsdelivr.net/gh/ineo6/homebrew-install/install.sh)"
```

将以上命令粘贴至终端。脚本内置 [中科大镜像](https://mirrors.ustc.edu.cn/help/brew.git.html) ，所以能让Homebrew安装的更快。

![截屏2021-09-05 00.01.03](.assets/截屏2021-09-05 00.01.03-0771323.png)



最后更新下：

```bash
brew update
```



#### 设置镜像

&emsp;&emsp;`brew`、`homebrew/core`是必备项目，`homebrew/cask`、`homebrew/bottles`按需设置。
通过 `brew config` 命令可以查看相关配置信息。更多可选源请访问 [镜像助手](https://link.zhihu.com/?target=https%3A//brew.idayer.com/guide/change-source)。



##### 中科大源

```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git

brew update
```



##### 清华大学源

```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git

brew update
```



#### 设置bottles镜像

设置环境变量需要注意终端`Shell`的类型，请看下面说明：

镜像以**中科大源**为例。

从`macOS Catalina`(10.15.x) 版开始，`Mac`使用`zsh`作为默认`Shell`，对应文件是`.zprofile`，所以命令为：

```bash
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.zprofile
source ~/.zprofile
```

如果是`macOS Mojave` 及更低版本，并且没有自己配置过`zsh`，对应文件则是`.bash_profile`：

```bash
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles/bottles' >> ~/.bash_profile
source ~/.bash_profile
```

> 注意：上述区别仅仅是`.zprofile`和`.bash_profile`不同，文章如有再次提及编辑`.zprofile`，均按此方法替换。

如果想使用清华源：

```bash
把
https://mirrors.ustc.edu.cn/homebrew-bottles/bottles

替换为
https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/bottles
```

至此，安装和设置操作都完成了。



#### 恢复默认源

```shell
git -C "$(brew --repo)" remote set-url origin https://github.com/Homebrew/brew.git


git -C "$(brew --repo homebrew/core)" remote set-url origin https://github.com/Homebrew/homebrew-core.git


git -C "$(brew --repo homebrew/cask)" remote set-url origin https://github.com/Homebrew/homebrew-cask.git


brew update
```

`homebrew-bottles`配置只能手动删除，将 `~/.zprofile` 文件中的 `HOMEBREW_BOTTLE_DOMAIN=https://mirrors.xxx.com`内容删除，并执行 `source ~/.zprofile`。



#### 卸载Homebrew

使用官方脚本同样会遇到`uninstall`地址无法访问问题，可以使用下面脚本：

```bash
/bin/bash -c "$(curl -fsSL https://cdn.jsdelivr.net/gh/ineo6/homebrew-install/uninstall.sh)"
```



## 终端工具

#### item2

```shell
brew install iterm2
```



##### 快捷键

| 快捷键               | 备注                               |
| -------------------- | ---------------------------------- |
| command + d          | 垂直分屏                           |
| command + shift + d  | 水平分屏                           |
| command + shift + h  | 打开剪切板(复制历史)               |
| command + ;          | 命令自动补全                       |
| command + shift + ;  | 查看历史命令                       |
| command + option + b | 按键回放(输入命令回放, 通过时间线) |



##### 更换主题

###### Dracula

> [参考教程原文](https://blog.csdn.net/daiyuhe/article/details/88667875)

```shell
下载 item2 的 Dracula 主题
git clone https://github.com/dracula/iterm.git
```

- 设置主题：

    ```shell
    - iTerm2 > Preferences > Profiles > Colors Tab
    - Open the Color Presets... 
    - 从列表中选择import
    - 选择刚才下载主题中 Dracula.itermcolors 文件，确定
    - 再次打开 Color Presets... ，选择Dracula 
    ```

    ![img](.assets/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2RhaXl1aGU=,size_16,color_FFFFFF,t_70.png)





## 科学上网工具

### V2rayU

下载地址：

```shell
https://github.com/yanue/V2rayU/releases
```

![image-20210904223116300](.assets/image-20210904223116300.png)



## 开发工具

### 语言

#### anaconda

```shell
brew install anaconda
```













