----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# {Title} {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2022-01-04 | Herolh | 文档创建 |
|            |        |          |



## 简介

&emsp;&emsp;树莓派由注册于英国的慈善组织“Raspberry Pi 基金会”开发，Eben·Upton/埃·厄普顿为项目带头人。2012年3月，英国剑桥大学埃本·阿普顿（Eben Epton）正式发售世界上最小的台式机，又称卡片式电脑，外形只有信用卡大小，却具有电脑的所有基本功能，这就是 Raspberry Pi 电脑板，中文译名"树莓派"。这一基金会以提升学校计算机科学及相关学科的教育，让计算机变得有趣为宗旨。基金会期望这 一款电脑无论是在发展中国家还是在发达国家，会有更多的其它应用不断被开发出来，并应用到更多领域。在2006年树莓派早期概念是基于Atmel的 ATmega644单片机，首批上市的10000“台”树莓派的“板子”，由中国台湾和大陆厂家制造。
&emsp;&emsp;它是一款**基于 ARM 的微型电脑主板**，以SD/MicroSD卡为内存硬盘，卡片主板周围有1/2/4个USB接口和一个10/100 以太网接口（A型没有网口），可连接键盘、鼠标和网线，同时拥有视频模拟信号的电视输出接口和HDMI高清视频输出接口，以上部件全部整合在一张仅比信用卡稍大的主板上，**具备所有PC的基本功能**只需接通电视机和键盘，就能执行如电子表格、文字处理、玩游戏、播放高清视频等诸多功能。 Raspberry Pi B款只提供电脑板，无内存、电源、键盘、机箱或连线。
**树莓派**的生产是通过有生产许可的三家公司Element 14/Premier Farnell、RS Components及Egoman。这三家公司都在网上出售树莓派。你可以在诸如京东、淘宝等国内网站购买到你所想要的树莓派。
&emsp;&emsp;树莓派基金会提供了基于ARM的Debian和Arch Linux的发行版供大众下载。还计划提供支持[Python](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/Python)作为主要编程语言，支持Java、BBC BASIC (通过 RISC OS 映像或者Linux的"Brandy Basic"克隆)、C 和[Perl](https://link.zhihu.com/?target=https%3A//baike.baidu.com/item/Perl)等编程语言。



## 树莓派的特点/规格

我的板子是 树莓派3B+，下面介绍以及后面的文章无特殊说明都是 树莓派3B+ 的基础上完成的。Raspberry PI 3模式B+ 是Raspberry PI 3 范围的最终修订。

- Broadcom BCM 2837B0，Cortex-A53(ARMv 8)64位SoC@1.4GHz
- 1GB LPDDR 2 SDRAM
- 2.4GHz和5 GHz IEEE802.11.b/g/n/ac无线局域网，蓝牙4.2，BLE
- 基于USB2.0的千兆以太网(最大吞吐量300 Mbps)
- 扩展40引脚GPIO报头
- 全尺寸hdmi
- 4个USB2.0端口
- 用于连接Raspberry PI摄像机的CSI摄像机端口
- 连接Raspberry PI触摸屏显示器的DSI显示端口
- 四极立体声输出与复合视频端口
- 用于加载操作系统和存储数据的微SD端口
- 5V/2.5A直流电源输入
- 以太网电源(POE)支持(需要单独的POE帽子)





## 安装系统需要准备什么

- TF卡
    a.推荐至少8GB 4级或10级微SD卡（micro SD卡，就是我们常见的TF卡）;
    b.详细的SD卡说明可以看官方文档：[DOCUMENTATION > INSTALLATION > SD-CARDS](https://link.zhihu.com/?target=https%3A//www.raspberrypi.org/documentation/installation/sd-cards.md)
- 拥有HDMI接口的显示器
    实际我使用了我家的TCL55T6M的4K电视和ThinkVision X24q的2K显示器都是OK的。使用效果上比VNC远程连接爽太多了。
- 键盘和鼠标
    上面的特点也说明了树莓派只有4个USB接口，那么我只需要准备的USB接口的键盘和鼠标就可以了，无线和有线的都可以。
- 电源
    树莓派需要的电源是5V的，最小电流是750mA，实际中发现只要板子不是满载，使用台式机或者笔记本的USB供电就可以，手机充电器供电也可以，如果条件允许可以买个官方推荐的电源（实际真不需要买，现在哪家没有几个不用的手机充电头子呀，顶多买一根数据线）
- 网线





## 开始系统安装

现在发现使用官方工具安装方便多了。下面的内容实际也就是官方内容的搬砖，最好的做法是看着官方文档根据自己的板子实际情况操作。
下载安装工具, 安装工具的下载地址：[https://www.raspberrypi.org/downloads/](https://link.zhihu.com/?target=https%3A//www.raspberrypi.org/downloads/)
b.选择对应的版本：

a.打开软件，软件打开效果图：