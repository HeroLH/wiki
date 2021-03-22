----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

#  AutoHotKey 新手极速入门

## 安装
[官网](https://www.autohotkey.com/) 下载安装 AutoHotkey
官网英文教程<https://www.autohotkey.com/docs/Tutorial.htm>
ahk的每个脚本都是纯文本格式的文件，包含能被ahk识别和执行的热键和命令等组成。当然也可以不包含热键，启动即执行。



### 脚本结构

  脚本结构非常简单：热键::命令



### 2. 热键/热字符串

| 指向键盘按键 |    符号    |
| :----------- | :--------: |
| Ctrl         |     ^      |
| Shift        |     +      |
| Alt          |     !      |
| Shift        |     #      |
| 其余功能键   | 使用大括号 |
| 数字或字母   |  直接输入  |

如^{Space}表示热键为ctrl+空格，#z表示热键为shift+z。

***

### 3. 功能

######  注意：如果一个热键后的命令多余一条，则热键需要单独一行，其后每条命令单独一行，最后一行必须为return。

>运行：Run，可运行程序，打开文件或链接。

    Run Notepad
    Run C:\Users\24870\Documents\ LIST.doc
    Run www.baidu.com

>运行等待：Runwait，运行目标后等待，目标结束运行后继续执行。

    Runwait Notepad
    MsgBox Notepad has been closed

>模拟键鼠：Send命令向当前活动窗口发送键盘敲击。Click命令模拟鼠标点击

    ^!s::
    Send Sincerely,{Enter}John Smith
    return

上例即 按Control+Alt+S 输出 Sincerely, John Smith

使用鼠标命令之前需要知道要点击的的坐标，可以使用安装的时候一并装入的Windows Spy程序。其实坐标就是按照像素排列的。屏幕最左上角为0,0点，根据分辨率，右下角即为相应的坐标点。如比例为1920×1080的1080p屏幕，右下角像素点坐标为1920，1080

    click 800,0

###### 其他鼠标热键 MouseMove：滑动鼠标 ； MouseClickDrag ：拖动鼠标


连续点击：使用循环loop

    ^q::Pause
    ^w::
    loop
    {
        click right
        send {ESC}
        sleep 1000
        }
        return

ctrl+q暂停，ctrl+w循环点击。

>只在特定窗口运行的热键

>多热键

>命令和函数

>变量

>对象









