----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# 问题：

> 安装包出现连接超时问题:
```python
Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'ConnectTimeoutError
```


## 解决办法：

### 方法一 设置超时时间

```shell
pip --default-timeout=100 install 软件包
```





### 方法二 pip 换源

```
pip install 软件包 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

#### 其他源总结：

&emsp;&emsp;通过几次 pip 的使用，对于默认的 pip 源的速度实在无法忍受，于是便搜集了一些国内的pip源，如下：

- 阿里云 <http://mirrors.aliyun.com/pypi/simple/>
- 中国科技大学 [https://pypi.mirrors.ustc.edu.cn/simple/ ](https://pypi.mirrors.ustc.edu.cn/simple/%20)
- 豆瓣(douban) <http://pypi.douban.com/simple/> 
- 清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple/>
- 中国科学技术大学 <http://pypi.mirrors.ustc.edu.cn/simple/>



如果想配置成默认的源，需要创建或修改配置文件（一般都是创建）:
- linux的文件在 `~/.pip/pip.conf`
- windows在 `%HOMEPATH%\pip\pip.ini`，
修改内容为：  
```shell
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```


这样在使用pip来安装时，会默认调用该镜像。
临时使用其他源安装软件包的python脚本如下：
```python
#!/usr/bin/python

import os
package = raw_input("Please input the package which you want to install!\n")
command = "pip install %s -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn" % package
os.system(command)
```