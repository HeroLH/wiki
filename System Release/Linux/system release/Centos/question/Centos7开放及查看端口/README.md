----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

##  Centos7开放及查看端口

1、开放端口

```shell
# 开放5672端口
firewall-cmd --zone=public --add-port=5672/tcp --permanent   

#关闭5672端口
firewall-cmd --zone=public --remove-port=5672/tcp --permanent  

# 配置立即生效
firewall-cmd --reload   
```



2、查看防火墙所有开放的端口

```shell
firewall-cmd --zone=public --list-ports
```



3.、关闭防火墙

如果要开放的端口太多，嫌麻烦，可以关闭防火墙，安全性自行评估

```shell
systemctl stop firewalld.service
```



 

4、查看防火墙状态

```shell
firewall-cmd --state
```



 

5、查看监听的端口

```
netstat -lnpt
```





6、检查端口被哪个进程占用

```shell
netstat -lnpt |grep 5672
```

![img](.assets/1336432-20190302104128381-1210567174.png)

 

7、查看进程的详细信息

```shell
ps 6832
```

![img](.assets/1336432-20190302104342651-779103690.png)

 

8、中止进程

```shell
kill -9 6832
```









