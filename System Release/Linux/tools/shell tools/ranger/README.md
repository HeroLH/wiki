----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

# Range 的安装及使用

## 安装

```shell
git clone https://github.com/ranger/ranger
pip3 install ranger-fm
cd ~/ranger
sudo make install
sudo ln -s /usr/bin/ranger /usr/bin/ra
sudo ln -s /usr/local/bin/ranger /usr/local/bin/ra
```

安装好了 ranger 之后，将其图标的插件安装上。

```bash
rererranger --copy-config=all
git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons

echo "default_linemode devicons" >> $HOME/.config/ranger/rc.conf
```

如果出现乱码:

```shell
git clone https://github.com/ryanoasis/nerd-fonts.git
cd nerd-fonts
./install.sh Noto
```





## 配置

ranger默认情况下不会生成配置文件，需要手动生成（拷贝）：

```shell
ranger --copy-config=all
```

这个时候ranger就会生成配置文件目录~/.config/ranger，下面主要有这样几个文件：

```shell
rc.conf     - 选项设置和快捷键
commands.py - 能通过 : 执行的命令
rifle.conf  - 指定不同类型的文件的默认打开程序。
scope.sh    - 用于指定预览程序的文件
```



### 配置文件添加

```shell
 # cw 重命名文件，多选单选都可以
map cw eval fm.execute_console("bulkrename") if fm.thisdir.marked_items else fm.open_console("rename ")
```





### 终端预览图片

```shell
sudo pacman -S python-ueberzug
vi ~/.config/ranger/rc.conf
 # 修改
set preview_images_method ueberzug
```



### 预览代码高亮

```shell
sudo pacman -S highlight
```



### 解压缩与压缩

```shell
sudo pacman -S atool
git clone https://github.com/maximtrp/ranger-archives.git
cd ranger-archives
 # 复制compress.py并将extract.py文件复制到~/.config/ranger/plugins文件夹，然后重新启动Ranger。
```

#### 用法

可以使用以下命令：

- `:extract [DIRECTORY]`：将文件提取到当前目录或指定目录（可选）。
- `:extract_to_dirs`：将每个存档提取到单独的目录。例如：`1.zip`到dir `1`，`2.zip`到dir`2`等。
- `:compress [FILENAME.EXT]`：将选定/标记的文件/目录压缩到存档中。如果未指定档案文件名，它将以父目录命名。

#### 捷径

您还可以添加以下行以`~/.config/ranger/rc.conf`使用以下键盘快捷键（`ec`，`ex`）：

```shell
map ex extract
map ec compress
```



## 快捷键

### 浏览

|    按键    | 说明                             |
| :--------: | -------------------------------- |
|    j，J    | 向下选择文件，快速向下选择文件   |
|    k，K    | 向上选择文件，快速向上选择文件   |
| left 或 h  | 返回父目录                       |
| right 或 l | 前进，进入下一目录               |
|     H      | 退回上一个位置                   |
|     L      | 撤销退回                         |
|     gg     | 跳到顶端                         |
|     G      | 跳到底端                         |
|     gh     | go home                          |
|     gn     | 新建标签                         |
|     [      | 移动至上一个父文件夹             |
|     ]      | 移动至下一个父文件夹             |
|     f      | 查找文件，并直接指向该文件       |
|     /      | 搜素文件，`n` 下一个，`N` 上一个 |
|     g*     | 快速进入目录                     |
|   Ctrl-f   | 向下翻页                         |
|   Ctrl-b   | 向上翻页                         |




### 编辑

|  按键  | 说明                             |
| :----: | -------------------------------- |
| space  | 选择                             |
|   uv   | 取消选择                         |
|   v    | 反转选择                         |
|   V    | 进入可视模式，结合移动键进行选择 |
|   yy   | 复制                             |
|   dd   | 剪切                             |
|   pp   | 粘贴                             |
| delete | 删除                             |
|   cw   | 重命名                           |
|   A    | 在当前文件的基础上重命名         |
|   I    | 类似A，但是光标会跳到起始位置    |



### 复制粘贴

| 按键         | 说明                                       |
| :----------- | ------------------------------------------ |
| y            | 按照提示选择复制的内容，如文件，文件路径等 |
| yy           | 复制                                       |
| p            | 按照提示招贴                               |
| pp           | 粘贴                                       |
| po           | 复制并覆盖重名文件                         |
| dd           | 剪切                                       |
| delete 或 dD | 删除                                       |



### 查看信息

| 按键 | 说明               |
| :--- | ------------------ |
| du   | 查看文件大小       |
| dU   | 查看文件大小并排序 |



### 排序

```shell
o(*)    改变排序方式
```

|  按键  | 说明                                                         |
| :----: | ------------------------------------------------------------ |
| on、ob | 根据文件名进行排序(natural/basename)                         |
|   oc   | 根据改变时间进行排序 (Change Time 文件的权限组别和文件自身数据被修改的时间) |
|   os   | 根据文件大小进行排序(Size)                                   |
|   oa   | 根据访问时间进行排序 (Access Time 访问文件自身数据的时间)    |
|   om   | 根据修改进行排序 (Modify time 文件自身内容被修改的时间)      |



### 标签

|        按键         | 说明     |
| :-----------------: | -------- |
|     gn、Ctrl-n      | 新建标签 |
|   Tab、Shift-tab    | 切换标签 |
| Alt-Right、Alt-Left | 切换标签 |
|     gc、Ctrl-w      | 关闭标签 |



### 书签

| 按键 | 说明     |
| :--: | -------- |
|  m   | 新建书签 |
|  `   | 打开书签 |
|  um  | 删除书签 |



### 链接(Link)

| 按键 | 说明               |
| ---- | ------------------ |
| pl   | 粘贴绝对路径的链接 |
| pL   | 粘贴相对路径的链接 |
| phl  | 硬链接             |





### 其他

| 按键                  | 说明                                                       |
| --------------------- | ---------------------------------------------------------- |
| zh                    | 显示隐藏文件                                               |
| zp                    | 打开/关闭文件预览功能                                      |
| zP                    | 打开目录预览功能                                           |
| zf                    | 过滤器(如过滤pdf文件, zf+pdf,回车)                         |
| z(*)                  | 改变设置, *表示在弹出选项中的选择                          |
| ! / s                 | 使用shell命令(！shell -w ls -hl %s,%s代表当前被选中的文件) |
| :                     | 使用ranger命令(3? 查看可用命令)                            |
| :set colorscheme snow | 设置颜色模式                                               |



### 任务管理

在执行某些操作(比如复制一个大文件)时不能立即完成, 这在 ranger 中就是一个任务. 你可以停止, 启动某个任务, 也可以对某个任务设置优先级.

| 按键 | 说明                                    |
| :--: | --------------------------------------- |
|  w   | 打开/关闭任务视图. 在w打开的任务视图中: |
|  dd  | 终止一个任务                            |
|  J   | 降低当前任务的优先级                    |
|  K   | 提升当前任务的优先级                    |





## 命令

```shell
:cd <dirname> 跳转到目录 <dirname>  
:chmod <octal_number> 设置被选条目的权限  
:delete 删除被选条目  
:edit <filename> 编辑文件  
:filter <string> 只显示文件名中含有给定字符串 <string> 的文件  
:find <regexp> 查找匹配给定正则表达式的文件，并且执行第一个匹配的文件  
:grep <string> 在选定的条目中查找给定的字符串 <string>  
:mark <regexp> 选定匹配正则表达式的所有文件  
:unmark <regexp> 取消选定匹配正则表达式的所有文件  
:mkdir <dirname> 创建目录  
:open_with <program< <mode> <flags> 用给定的 <program>、<mode> 和 <flags> 打开文件。 所有参数都是可选的，未给出任何参数的时候，等价于 <Enter> 。  
:quit 退出 quit  
:rename <newname> 重命名当前文件  
:search <regexp> 搜索所有匹配正则表达式 <regexp> 的文件，相当与 vim 中的 “/”。快捷键： "/"  
:shell [-<flags>] <command> 运行命令 <command>  
:touch <filename> 创建文件 
```





## 使用场景

### 批量改名

批量选择文件后, 键入命令:bulkname, 会打开编辑器, 其中的文件名编辑后保存退出, 再次打开操作确认编辑, 然后就批量改名了, 如果想取消批量改名, 在确认时把文件内容删除即可.