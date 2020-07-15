----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# python模块之 paramiko

> paramiko 模块提供了 ssh 及 sft 进行远程登录服务器执行命令和上传下载文件的功能。这是一个第三方的软件包，使用之前需要安装。 



## 1 基于用户名和密码的登录

### sshclient 方式

```python
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 没有上面一句会有以下报错：
# paramiko.ssh_exception.SSHException: Server '192.168.221.130' not found in known_hosts
# known_hosts：建立安全的签名认证

# 连接服务器
ssh.connect(hostname='192.168.193.145', port=22, username='root', password='root123')

# 执行命令，返回三个结果
# stdin：标准输入
# 以下两个只有一个会有结果：
	# stdout：标准输出
	# stderr：标准错误
stdin, stdout, stderr = ssh.exec_command('df')

# 获取命令结果
result = stdout.read().decode()
if result:
    print( result )
else:
    print( stderr.read().decode() )

# 关闭连接
ssh.close()
```



###  **transport 方式**

> 方法1是传统的连接服务器、执行命令、关闭的一个操作，有时候需要登录上服务器执行多个操作，比如执行命令、上传/下载文件，方法1则无法实现，可以通过如下方式来操作

```python
import paramiko

# 实例化一个transport对象
trans = paramiko.Transport(('192.168.193.145', 22))
# 建立连接
trans.connect(username='root', password='root123')

# 将sshclient的对象的transport指定为以上的trans
ssh = paramiko.SSHClient()
ssh._transport = trans
# 执行命令，和传统方法一样
stdin, stdout, stderr = ssh.exec_command('df -hl')
print(stdout.read().decode())

# 关闭连接
trans.close()
```





## **3 输入命令立马返回结果** 

>  以上操作都是基本的连接，如果我们想实现一个类似xshell工具的功能，登录以后可以输入命令回车后就返回结果：

```python

```























































































































