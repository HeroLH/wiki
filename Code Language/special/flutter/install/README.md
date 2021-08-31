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

[flutter 国内官网](https://flutter-io.cn/)



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
sudo pacman -S flutter
# Flutter 安装在 /opt/flutter
# 如果您打算将其用作普通用户，请将您的用户添加到 flutterusers 组中：
gpasswd -a <用户> flutterusers

# 您需要获取 /etc/profile 或重新登录才能将 flutter 添加到您的路径中。
# 将您的终端重新登录到 flutterusers 组： 
newgrp flutterusers

# 验证
flutter -v

# 检测环境是否配置成功
flutter doctor
```



设置国内镜像

```shell
export FLUTTER_STORAGE_BASE_URL="https://storage.flutter-io.cn"
export PUB_HOSTED_URL="https://pub.flutter-io.cn"

# 清华源
# export FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter"
# export PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub"
```



