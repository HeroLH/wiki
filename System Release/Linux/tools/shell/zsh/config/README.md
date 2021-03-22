[TOC]





## 配置

&emsp;&emsp;zsh 的配置文件存在当前用户目录中的 `.zshrc` 文件，如果你发现切换了 shell 之后，以前的配置的环境变量不生效了，可以打开` .zshrc` 文件，找到：

```shell
 # User configuration
 source ~/.bash_profile
```

指定配置的环境变量文件，之后运行：

```shell
source .zshrc
```



## 主题配置

**所有主题预览：**
https://github.com/robbyrussell/oh-my-zsh/wiki/External-themes



在.zshrc文件中找到主题的配置项

```shell
 # Set name of the theme to load. Optionally, if you set this to "random"
 # it'll load a random theme each time that oh-my-zsh is loaded.
 # See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="ys"
```

这里可以设置主题的名字，那么这些主题的名字从哪里找呢？进入Oh My Zsh的配置目录中：

```shell
ls /Users/用户/.oh-my-zsh/themes
```

可以看到内置了许多主题，根据主题文件的名字替换就可以了；

```
3den.zsh-theme                essembeh.zsh-theme            junkfood.zsh-theme            rgm.zsh-theme
Soliah.zsh-theme              evan.zsh-theme                kafeitu.zsh-theme             risto.zsh-theme
adben.zsh-theme               example.zsh-theme             kardan.zsh-theme              rixius.zsh-theme
af-magic.zsh-theme            fino-time.zsh-theme           kennethreitz.zsh-theme        rkj-repos.zsh-theme
afowler.zsh-theme             fino.zsh-theme                kiwi.zsh-theme                rkj.zsh-theme
agnoster.zsh-theme            fishy.zsh-theme               kolo.zsh-theme                robbyrussell.zsh-theme
alanpeabody.zsh-theme         flazz.zsh-theme               kphoen.zsh-theme              sammy.zsh-theme
amuse.zsh-theme               fletcherm.zsh-theme           lambda.zsh-theme              simonoff.zsh-theme
apple.zsh-theme               fox.zsh-theme                 linuxonly.zsh-theme           simple.zsh-theme
arrow.zsh-theme               frisk.zsh-theme               lukerandall.zsh-theme         skaro.zsh-theme
....
```

或者我们将主题设置为随机 `('random')`，每次打开命令行窗口，都会随机在默认主题中选择一个，如果遇到你喜欢的主题，可以输入命令查看其名字：

```shell
echo $ZSH_THEME
```



## 插件开启

Oh My Zsh 默认自带了一些默认主题，存放在 `~/.oh-my-zsh/plugins` 目录中。我们可以查看这些插件:

```shell
$ ls ~/.oh-my-zsh/plugins
```

我们打开 `.zshrc` 配置文件,定位到 plugins

```
Copy plugins=(git)
```

可以看到默认只开启了git插件，我们可以将要使用的插件的名字以空格相隔接在后面就可以了，比如：

```
Copy plugins=(git adb)
```

如果我们要下载第三方的插件，只需要把插件下载存放到 `~/.oh-my-zsh/plugins` 中，然后在上面加上插件的名字即可；最后别忘了让配置生效:

```shell
source .zshrc
```





## 推荐插件

### vi-mode

> 自带，在终端下可以通过 vi 快捷键操作命令

修改配置文件 `.zshrc`

```shell
plugins=(git vi-mode)
```

快捷键：

```shell
  进入命令行模式:
    ESC          | 进入命令行模式
  进入输入模式:
    i            | 在光标前插入
    a            | 光标后插入
    I            | 在行的开头插入
    A            | 在行的结尾插入
    c<mov. comm> | Change text of a movement command <mov. comm> (见下文).
    C            | 剪切到行尾 (同 c$)
    cc 或 S      | 剪切整行 (同 0c$)
    s            | 删除光标处文本，并进入插入模式。 (同 c[SPACE])
    r            | 修改光标处文本 (没有离开命令样式)
    R            | 进入替换模式
    v            | 先执行命令，再使用编辑编辑命令。使用 $VISUAL 或 $EDITOR 变量定义编辑器, 编辑器默认 vi 。
  移动 (命令模式下):
    h            | 按字左移
    l            | 按字右移
    w            | 按词右移
    b            | 按词左移
    W            | 以空白字符按词右移(比如 ab a-b ， W 不会移动到 - 上，而 w 会)
    B            | 以空白字符按词左移
    e            | 移动光标到词尾部
    E            | 以空白符移动光标到词尾
    0            | 移动光标到行首
    ^            | 移动光标到行首不是空白符
    $            | 移动光标到行尾
    %            | 移动到左括号或右括号
  字符查找 (也是移动命令):
    fc           | 右移到字符 c .
    Fc           | 左移到字符 c .
    tc           | 右移到字符 c 的左边
    Tc           | 左移到字符 c 的右边
    ;            | 重做查找
    ,            | 反方向重做查找
    |            | 移到第 n 列 (如 3| 移到第 3 列)
  删除命令:
    x            | 删除当前光标所在字符.
    X            | 删除光标前的一个字符.
    d<mov. comm> | Delete text of a movement command <mov. comm> (see above).
    D            | 删除到行尾 (同 d$).
    dd           | 删除行 (同 0d$).
    CTRL-w       | 向左删除单词 (编辑模式下)
    CTRL-u       | 删除到进入编辑模式时光标位置
  撤销、重做、复制、粘贴:
    u            | 单步撤销
    U            | 撤销所有
    .            | 重做
    y<mov. comm> | Yank a movement into buffer (copy).
    yy           | Yank the whole line.
    p            | 在光标处粘贴
    P            | 在光标前粘贴
  历史记录:
    k            | 上一条命令
    j            | 下一条命令
    G            | 回来当前命令
    /string 或 CTRL-r  | 搜索历史命令(/string 用于命令模式下， ctrl-r 用于输入模式下)
    ?string 或 CTRL-s  | 搜索历史命令(Note that on most machines Ctrl-s STOPS the terminal | output, change it with `stty' (Ctrl-q to resume)).
    n            | 下一条历史匹配
    N            | 上一条历史匹配
  自动完成:
    TAB 或 = 或  | 列出所有可能(TAB 用于输入模式)
    CTRL-i       |
    *            | Insert all possible completions.
  其他:
    ~            | 切换当前光标处文本的大小写，并右移光标
    #            | 注释当前命令并把其放入历史
    _            | Inserts the n-th word of the previous command in the current line.
    0, 1, 2, ... | Sets the numeric argument.
    CTRL-v       | Insert a character literally (quoted insert).
    CTRL-r       | Transpose (exchange) two characters.
```





### zsh-autosuggestions

>  它是 `Oh-myszh` 的一个插件，作用基本上是根据历史输入指令的记录即时的提示，能够很大的提高效率。[详细介绍](https://github.com/zsh-users/zsh-autosuggestions)

- 克隆到插件目录

    ```shell
    git clone git://github.com/zsh-users/zsh-autosuggestions
    ```

- 修改配置文件 `.zshrc`

    ```shell
    plugins=(git zsh-autosuggestions)
    ```



#### 使用

&emsp;&emsp;当您键入命令时，您会在光标后看到灰色的静音状态。可以通过设置`ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE`变量来更改此颜色。请参阅[配置](https://github.com/zsh-users/zsh-autosuggestions#configuration)。如果在缓冲区末尾用光标按→（`forward-char`小部件）或End（`end-of-line`小部件）键，它将接受建议，并用建议替换命令行缓冲区的内容。

- 使用（Ctrl+F）可以进行全补全



### zsh-syntax-highlighting

> 这是一个命令高亮插件，输入为绿色时表示可用命令，路径带有下划线时表示可用路径, [详细介绍](https://github.com/zsh-users/zsh-syntax-highlighting)

```shell
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
```



### autojump

> 实现目录间快速跳转，想去哪个目录直接 j + 目录名，不用在频繁的 cd 了！

此插件需要依赖一个包需要提前安装:

```shell
yay -S autojump
```

```shell
git clone git://github.com/joelthelion/autojump.git
```



#### 使用方法：

##### 法1：

```shell
autojump [目录名字的一部分]
```

autojump 加一部分名字即可自动跳转到数据库中对应目录去。使用了 `oh my zsh` 还可以敲 tab 自动补全用于直观的选择，很方便。

##### 法2：

autojump有一个自带的alias：j。只有你进入过的目录它才会记录，比如你进入过 `/home/luwnto/work/blog` 这个目录，那么下次我们要想进入这个目录的时候，不必再输入完整的路劲了，只需要一个简单的命令就可以转到对应的目录去：

```shell
j blog
```

甚至你还可以:

```shell
j bl
```

更加变态的是，你还可以:

```shell
j b
```

如果同时存在多个包含 `b` 的目录，那么 autojump 会根据你的权重进入你访问最频繁的那个目录，比如你的项目目录 `blog`



#### 对于权重数据库的访问。

autojump可以修改目录数据库来达到自定义想要的目录的效果。

```shell
$ autojump -a [dir]
 # 在数据库中添加一个目录

$ autojump -i [value]
 # 提升当前目录value数目的权重

$ autojump -d [value]
 # 降低当前目录的权重

$ autojump -s
 # 显示数据库中的统计数据

$ autojump --purge
 # 清除不再需要的目录
```





## zsh 常用快捷键

### 常用编辑操作

- ctrl + a，移动到行首
- ctrl + e，移动到行尾
- ctrl + f，前移一个字符
- ctrl + b，后移一个字符
- ctrl + w，删除光标前面的单词
- ctrl + d，删除光标所指的字符
- ctrl + k，删除光标至行尾的所有内容
- ctrl + u，清空当前行
- cmd + r，清空当前屏幕
- cmd + ; ，根据历史命令，对当前输入自动补全
- cmd + shift + h，自动补全剪贴板历史
- cmd + f，查找
    - enter，上一个匹配结果
    - shift + enter，下一个匹配结果



### 常用窗口操作

- cmd + n，新建一个终端窗口
    - cmd + option + 1、2、3，跳转到编号为 1、2、3 的终端窗口
- cmd + t，在终端窗口中新建一个 tab
    - cmd + 1、2、3，跳转到编号为 1、2、3 的 tab
    - cmd + left、right，跳转到左侧、右侧的 tab
- cmd + d，左右分屏
- cmd + shift + d，上下分屏
- cmd + w，关闭当前页
- cmd + enter，开启、关闭最大化终端窗口
- cmd + option + e，通过查找定位到 tab



## 其他

- cmd + click，打开链接
- cmd + /，突出显示光标所在位置
- cmd + option + b，通过时间线查看操作历史





## 小技巧

### 给history命令增加时间

```shell
vim ~/.zshrc
HIST_STAMPS="yyyy-mm-dd" 
source ~/.zshrc
```





### 更新oh_my_zsh

```shell
 # 设置自动更新oh-my-zsh : ~/.zshrc
DISABLE_UPDATE_PROMPT=true
 # 加入需要手动更新
$ upgrade_oh_my_zsh
```







