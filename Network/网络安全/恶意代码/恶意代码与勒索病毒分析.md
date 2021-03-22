----------------------------------------------
> *Made By {Author}*
----------------------------------------------

# 目录 {#index}

[TOC]











--------------------------------------------

#

查看注册表帮助

```shell
reg add /?
```

```shell
  /v       所选项之下要添加的值名称。

  /ve      为注册表项添加空白值名称(默认)。

  /t       RegKey 数据类型
           [ REG_SZ    | REG_MULTI_SZ | REG_EXPAND_SZ |
             REG_DWORD | REG_QWORD    | REG_BINARY    | REG_NONE ]
           如果忽略，则采用 REG_SZ。

  /s       指定一个在 REG_MULTI_SZ 数据字符串中用作分隔符的字符
           如果忽略，则将 "\0" 用作分隔符。

  /d       要分配给添加的注册表 ValueName 的数据。

  /f       不用提示就强行覆盖现有注册表项。

 /reg:32  指定应该使用 32 位注册表视图访问的注册表项。

 /reg:64  指定应该使用 64 位注册表视图访问的注册表项。
```



```shell
@echo off				# 关闭回响(不关闭会有个黑框框)
# 注册表修改IE主页, HKCU = HKEY_CURRENT_USER
reg add "HKCU\Software\Microsoft\Internet Explorer\Main" /v "Start Page" /d "http://www.baidu.com" /f
reg add ""
```

