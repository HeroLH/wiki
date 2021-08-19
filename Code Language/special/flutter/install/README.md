----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Flutter 的安装 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-08-19 | Herolh | 文档创建 |
|            |        |          |



## 简介

### 依赖项

- JDK
- android-sdk
- android studio
- flutter SDK



## Linux 下

### Arch 

```shell
# 安装 android-sdk
sudo pacman -S android-sdk

# 安装 android-studio
sudo pacman -S android-studio

# 安装 flutter SDK
sudo pacman -Ss flutter
# Flutter 安装在 /opt/flutter
# 如果您打算将其用作普通用户，请将您的用户添加到 flutterusers 组中：
gpasswd -a <用户> flutterusers

# 您需要获取 /etc/profile 或重新登录才能将 flutter 添加到您的路径中。
# 将您的终端重新登录到 flutterusers 组： 
newgrp flutterusers
```

