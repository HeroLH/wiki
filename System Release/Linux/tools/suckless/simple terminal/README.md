----------------------------------------------
> *Made By {Author}*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

安装

```shell
git clone https://git.suckless.org/st
cd st
# 修改内容
X11INC = /usr/include/X11
X11LIB = /usr/lib/X11

sudo make clean install 
```





插件

```shell
patch < xxx.diff
```



alpha

> 背景半透明

插件地址：http://st.suckless.org/patches/alpha/



anysize

> 占满整个屏幕

插件地址：http://st.suckless.org/patches/anysize/





dracula

> 字体颜色

插件地址：http://st.suckless.org/patches/dracula/



scrollback

> 允许往前滚动历史记录

http://st.suckless.org/patches/scrollback/



fontfix

> 修复表情图标



desktopentry

http://st.suckless.org/patches/desktopentry/

> 创建一个桌面条目。这样可以在图形菜单中找到st并用漂亮的图标显示它。



hidecursor

http://st.suckless.org/patches/hidecursor/

> 每当按下键时，隐藏X光标，并在终端窗口中移动鼠标时将其再次显示。