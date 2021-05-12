----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# KVM + Qemu + Libvirt {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-05-10 | Herolh | 文档创建 |
|            |        |          |



## 简介

> [在 Arch Linux/Manjaro 上安装 KVM、QEMU 和 Virt Manager 的方法](https://www.cnblogs.com/jpinsz/p/12345982.html)



### 什么是 KVM

&emsp;&emsp;KVM (Kernel-based Virtual Machine 的缩写)，是内核内建的虚拟机，追求简便的运作。例如运行虚拟机仅需要加载相应的 kvm 模块，但是 KVM 需要芯片支持虚拟化技术（Intel 的 VT 扩展，或是 AMD 的 AMD-V 扩展）。在 KVM 中，可以运行各种 GNU/Linux，Windows 或其他系统镜像（例如 FreeBSD，MacOS）。每个虚拟机都可以提供独享的虚拟硬件：网卡，硬盘，显卡等（虚拟机甚至可以直通主机设备，例如 GPU PCI pass through）。



### 准备工作

KVM 需要 host 的处理器支持虚拟化，通过以下命令查看 host 是否支持

```shell
LC_ALL=C lscpu | grep Virtualization
```

如我的处理器显示:

```shell
Virtualization:                  VT-x
```

**注意**: 虚拟化支持可以在 BIOS 中开启。



## 安装

### 安装 KVM

```shell
sudo pacman -S qemu libvirt ovmf virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat
```

- kvm 负责 CPU 和内存的虚拟化
- qemu 向 Guest OS 模拟硬件（例如，CPU，网卡，磁盘，等）
- ovmf 为虚拟机启用 UEFI 支持
- libvirt 提供管理虚拟机和其它虚拟化功能的工具和 API
- virt-manager 是管理虚拟机的 GUI

**注** : 实际上，这步只需要安装 qemu 就可以使用虚拟机，但是 qemu-kvm 接口有些复杂，libvirt 和 virt-manager 让配置和管理虚拟机更便捷。

还要安装 ebtables 和 iptables 软件包：

```shell
sudo pacman -S ebtables iptables
```



### 安装 libguestfs

libguestfs 是一组用于访问和修改虚拟机（VM）磁盘映像的工具

```shell
sudo pacman -S libguestfs
```

```shell
# 查看硬盘使用情况
virt-df centos.img

# 列出目录文件
virt-ls centos.img /

# 在虚拟映像中执行文件复制
virt-copy-out -d domain /etc/passwd /tmp

# 查看文件系统信息
virt-list-filesystems /file/xx.img

# 查看分区信息
virt-list-partitions /file/xx.img

# 直接将分区挂载到宿主机
guestmount -a /file/xx.qcow2(raw/qcow2都支持) -m /dev/VolGroup/lv_root --rw /mnt

# 交互式 shell，可运行上述所有命令
guestfish
```



### 启动 KVM libvirt 服务

装完成后，启动并启用 libvirtd 服务以在启动时启动：

```shell
sudo systemctl enable libvirtd.service
sudo systemctl start libvirtd.service

sudo systemctl enable virtlogd.socket
sudo systemctl start virtlogd.socket
```



### 启用普通用户帐户以使用 KVM

由于我们希望使用我们的标准 Linux 用户帐户来管理 KVM，因此我们将 KVM 配置为允许此操作。打开文件 `/etc/libvirt/libvirtd.conf` 进行编辑：

```shell
# 将 UNIX 域套接字组所有权设置为 libvirt（第 85 行）
unix_sock_group = "libvirt"

# 设置 R/W 套接字的 UNIX 套接字权限（第 102 行）：
unix_sock_rw_perms = "0770"
```

将你的用户帐户添加到 libvirt 组：

```shell
sudo usermod -a -G libvirt $(whoami)
newgrp libvirt
```

重启 libvirt 守护进程：

```shell
sudo systemctl restart libvirtd.service
```



### 启用嵌套虚拟化（可选）

嵌套虚拟化功能使你可以在 VM 中运行虚拟机，通过启用内核模块为 kvm_intel 启用嵌套虚拟化： 

```shell
sudo modprobe -r kvm_intel
sudo modprobe kvm_intel nested=1
```

要使此配置持久，请运行：

```shell
echo "options kvm-intel nested=1" | sudo tee /etc/modprobe.d/kvm-intel.conf
```

验证嵌套虚拟化已经启用：

```shell
cat /sys/module/kvm_intel/parameters/nested 
# Y
```



## 使用

### 创建 / 导入 / 导出 / 克隆虚拟机

```shell
virt-manager
```



