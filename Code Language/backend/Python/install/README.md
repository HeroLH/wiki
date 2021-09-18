----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# Python 的安装 {#index}

[TOC]



 







--------------------------------------------

## 文档版本

|    时间    | 修改人 | 内容     |
| :--------: | :----: | :------- |
| 2021-09-18 | Herolh | 文档创建 |
|            |        |          |



## 简介



## 安装

### docker 下

```shell
docker pull python:3.7

docker run -v /pyapp:/usr/src/python -w /usr/src/python python:3.7 python test.py
```





### Linux 下

> 一般linux系统的桌面会自动安装python2.0，可以在提示符下输入 python 命令进行验证：
>
> ```shell
> python                   			# 运行这个命令会启动交互式python解释器。
> # 若没有安装python解释器会报错：       
> # bash:python:command not found
> ```



#### Arch  下

```shell
sudo pacman -S python
```



#### 特殊:从源文件编译

&emsp;&emsp;如果没有包管理器，或者不愿意使用，也可以自己编译 python。选择这个方法的另一个原因可能是没有正在使用的 root 权限。这个方法非常的灵活，你可以在任何位置安装 python，甚至在用户的主目录下。

- 访问下载网页( 参照 window 下载的前两步 )，按照说明下载源码。

- 下载扩展名为 `.tgz` 或者 `.tar.xz` 的文件，将其保存在临时位置，假定读者想将 python 安装在自己的目录下，可以把它放在类似 `~/python` 的目录中。进入这个目录( 比如使用 `cd ~/python` 命令 )。

- 在终端命令模式使用 `tar –xzvf Python-3.4.2.tgz` 解压缩文件。( 3.4.2是版本号 )。

- 进入解压好的文件夹：

    ```shell
    cd python-3.4.2
    ```

- 如果提示安装错误或者缺少某个依赖库，请先行安装再执行下列命令：

    ```shell
    ./configure
    Make install
    Make
    ```

- 最后应该能在文件夹内找到一个名为python的可执行文件。将当前文件夹的路径加入到环境变量path里，安装完成。

- 若要查看其他配置命令，执行以下命令：

    ```shell
    ./configure --help
    ```

    

### Windows 下

&emsp;&emsp;访问 [python 官网](http://www.python.org/)，点击 download 链接，选择 pyhon3.x windows installer 下载，双击下载的文件一路 next 即可。 

