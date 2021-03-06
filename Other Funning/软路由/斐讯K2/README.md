----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

## 斐讯 K2 刷机

### 刷入Breed 辅助工具

#### 支持版本

```
官方固件版本:
 K1： V22.4.XX.XX
 K1S：V22.3.XX.XX
 K2： V22.2.XX.XX
      V22.3.XX.XX
      V22.4.XX.XX
      V22.5.XX.XX
      V22.6.XX.XX
 K2P：V22.8.5.189 V22.10.2.24

 (V21.4.6.12版本需要升级到以上版本)
 (V21.4.6.12以下版本需要先升级到V21.4.6.12版本)
```

- 绿色小巧，不需要联网、不需要防火墙或管理员权限
- 能打开路由管理页面就可以，有线无线连接均可以
- 文件MD5多重验证，绝对安全
- 兼容众多版本
- ……



#### 刷入Breed

1. [下载辅助工具](https://tbvv.net/k2/breed.zip)，解压所有文件到任意目录。
2. 双击运行 `刷机.bat` 按照提示输入路由的IP和密码，如果是默认的直接按回车。
    (全新或恢复出厂没设置过的路由直接回车按提示配置路由)
3. 等待路由重启，1分钟左右会用浏览器打开路由页面，如果自动登录成功或者手动升级页面有变化 就说明刷breed成功了。
    (管理密码: `tbvv.net` )
4. 接着进入：高级设置 —> 系统设置 —> 手动升级 —> 下载备份EEPROM(是一个压缩包)。



#### 更新breed的方法

Breed Web 恢复控制台
作者：hackpascal
发布帖: <https://www.right.com.cn/forum/thread-161906-1-1.html>
去breed作者帖子下载新版breed—>查看服务器md5sum.txt里的MD5—>进入breed—>固件更新—>Bootloader选择下载的breed—>上传—>确认MD5一致后—>刷入

K1/K1S/K2 通用，文件名：breed-mt7620-phicomm-psg1208.bin
K2P A1/A2 文件名：breed-mt7621-phicomm-k2p.bin
K2T 文件名：breed-qca9563-phicomm-k2t.bin
机型、平台一定要选对，刷错变砖头，如无特殊需求一般不用更新。





### 刷入第三方固件

#### 方法1：

高级设置 —> 系统设置 —> 手动升级 —> 浏览 —> 选择自己下载的固件 —> 点击升级即可。
(网页刷机进度条不准确可忽略，固件写入、重启、首次启动初始化这个过程实际需要3—5分钟不等，不要着急，如果固件不兼容需要手动进breed重刷)



#### 方法2：

手动进入 breed 刷

路由WAN口的网线拔掉避免IP冲突，电脑网线连接路由LAN口，电脑网卡设置为自动获取IP
路由断电3秒—>按住复位键不要松手—>插入电源—>等待5秒后松开复位键—>浏览器输入192.168.1.1—>固件更新—>选择固件刷入。(如果网页错误说明 WAN口IP冲突 或 没有清理浏览器缓存)
(闪存布局: K2大部分固件是0x50000，官方V22.5.XX.XX以后的固件选0xA0000，固件无法做到统一，如果不启动就换另一种布局重刷)

breed详细使用说明请看[作者原帖](https://www.right.com.cn/forum/thread-161906-1-1.html)



#### 固件&其它链接

华硕padavan(hiboy)：<https://www.right.com.cn/forum/thread-161324-1-1.html>
华硕padavan(荒野无灯)：<https://www.right.com.cn/forum/thread-187654-1-1.html>
斐讯K2 官方固件定制版：<https://www.right.com.cn/forum/thread-208753-1-1.html>
Tomato Phoenix 不死鸟：<https://www.right.com.cn/forum/thread-216905-1-1.html>
PandoraBox 潘多拉：[https://pangubox.com](https://pangubox.com/)
GOCLOUD高恪：<http://www.gocloud.cn/bbs/thread-543-1-1.html> [(SSH)](https://tbvv.net/k2/ssh.config)
Tomato DualWAN(宽带宝)：[http://bbs.91kdb.com](http://bbs.91kdb.com/)

[部分文件网盘下载](https://pan.baidu.com/s/1CP8t897JalTK1X5l_9I85w)

更多固件：
<https://www.right.com.cn/forum/forum-72-1.html>
<https://www.right.com.cn/forum/forum-158-1.html>
<https://www.right.com.cn/forum/forum-161-1.html>









## 注意事项&其它

### 刷breed失败

尝试升级或降级到下列支持的版本后重试，路由管理页面或者官方Uboot界面两种升级方式

[官网下载](http://www.phicomm.com/cn/support.php/Soho/software_support/t/sm/p/1.html)
K1: [V22.4.2.15](http://www.phicomm.com/cn/Uploads/files/20161024/K1_V22.4.2.15.bin)
K1S: [V22.3.1.5](http://www.phicomm.com/cn/Uploads/files/20161009/K1S_V22.3.1.5.bin)
K2: [V22.6.526.199](http://power.qiqizz.com/img/SOP-ramips-mt7620-K2A5-199-release.bin)
K2P: [V22.8.5.189](http://www.phicomm.com/cn/Uploads/files/20180502/K2P_V22.8.5.189.bin)

官方Uboot进入方法：
电脑网线连接路由LAN口，其余网线拔掉，电脑网卡设置固定IP 192.168.2.2
关闭电源等3秒—>按住RESET键不要松手—>插入电源—>等待6秒后松开RESET键—>浏览器输入[http://192.168.2.1](http://192.168.2.1/)





### 第三方固件问题

&emsp;&emsp;第三方固件的管理地址 因固件而异，固件发布贴都有说明，比如 hiyboy 编译的华硕 padavan 是`192.168.123.1`，也可以根据获取到的IP、网关判断。
&emsp;&emsp;刷了不同版本的固件或者第三方固件时，清除一下浏览器缓存文件，推荐使用 Chromium 内核的或者 Firefox 浏览器。
&emsp;&emsp;刷了使用 nvram 存储设置的固件(华硕类)最好到管理页面恢复一下出厂设置 或者 启动固件后长按复位键恢复设置。
&emsp;&emsp;路由的指示灯是由固件控制的，有的第三方固件没有适配造成显示不正常（比如红灯长亮），不必惊慌，能正常使用固件，没有任何其他副作用，强迫症除外。



