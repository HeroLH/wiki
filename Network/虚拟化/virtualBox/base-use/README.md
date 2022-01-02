----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# VirtualBox 基本使用 {#index}

[TOC]



 





--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-12-31 | Herolh | 文档创建 |
|            |        |          |



## 简介





## 增强插件

### 安装

#### linux server 下

[Oracle VM VirtualBox在Linux系统下怎么安装增强功能](https://zhidao.baidu.com/question/494237311389069852.html)

- 选择"设备"--"安装增强功能",然后可以看到在虚拟机的光驱中自动加载了增强iso的文件(VBoxGuestAdditions.iso)

- 在linux 中挂载光驱

    ```shell
    mount /dev/cdrom /mnt
    ```

- 在将 `/mnt` 文件中的所有文件拷在 `/tmp` 目录下

    ```shell
    cp -r /mnt/* /tmp
    ```

- 在安装增强文件之前安装相应的包,安装后重启

    ```shell
    yum install kernel
    yum install kernel-headers kernel-devel gcc gcc-c++
    reboot
    ```

- 在/tmp目录下执行安装命令

    ```shell
    ./VBoxLinuxAdditions.run
    ```

    

- 共享主机文档
    在VM中选择"共享文件夹",添加需共享的文件,这里选择"固定分配",记住共享文件夹名称,如linux
    2在linux中将共享文件夹挂载/mnt目录下

    ```shell
    mount -t vboxsf 共享文件夹名称 /mnt
    ```

- 此时就可以互相访问,如在/mnt中创建一个txt文件,在主机文件夹中就可以看到。

