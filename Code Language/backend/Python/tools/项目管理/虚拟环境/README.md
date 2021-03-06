----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 虚拟环境的使用 {#index}
[TOC]











--------------------------------------------

# python 版本环境管理

## Anaconda 管理

### conda常用的命令

|              命令               |              说明               |
| :-----------------------------: | :-----------------------------: |
|            conda -V             | 检验是否安装以及当前conda的版本 |
|           conda list            |        查看安装了哪些包         |
| conda env list 或 conda info -e |    查看当前存在哪些虚拟环境     |
|       conda update conda        |        检查更新当前conda        |





### 虚拟环境

#### 创建python虚拟环境

```shell
# 创建 python 版本为 X.X、名字为 your_env_name 的虚拟环境。
conda create -n your_env_name python=X.X	#(2.7、3.6等)
```

> your_env_name 文件可以在 Anaconda 安装目录 envs 文件下找到。
>
> ```shell
> ~/anaconda3/envs/python36/bin/python3.6
> ```



#### 激活虚拟环境

```shell
# Linux:  
source activate your_env_name	#(虚拟环境名称)

# Windows: 
activate your_env_name			#(虚拟环境名称)
```

>   打开命令行输入 python --version 可以检查当前 python 的版本。



#### 关闭虚拟环境

```shell
# Linux: 
source deactivate

#Windows: 
deactivate
```



#### 删除虚拟环境

```shell
conda remove -n your_env_name(虚拟环境名称) --all
```





#### 虚拟环境中管理包

> 不建议直接使用

##### 安装额外的包

```shell
conda install -n your_env_name [package]
```

>  使用命令即可安装 package 到 your_env_name 中



##### 删除环境中的某个包

```python
conda remove --name your_env_name  package_name
```



## conda 常见问题：





# python 包管理

## pipenv

[在线体验](https://rootnroll.com/d/pipenv/)

### 常用命令

|      命令      |          说明          |
| :------------: | :--------------------: |
| pipenv --venv  | 当前绑定的虚拟环境目录 |
| pipenv --where |     当前项目根目录     |
|  pipenv --rm   |      删除虚拟环境      |



### 安装

```shell
pip install pipenv			# 依赖与 virtualenv-clone
pipenv --version
```



### 第一个项目工程

```shell
mkdir myweb
cd myweb
```



####  项目初始化

```python
# 如果要指定版本创建环境，可以使用如下命令，当然前提是本地启动目录能找到该版本的python
pipenv --python 3	

# 在指定目录下创建虚拟环境, 会使用本地默认版本的python
pipenv install

# 基于 conda 的 Python3.6版本构建 demo_project 虚拟开发环境
pipenv install --python ~/anaconda3/envs/python36/bin/python3.6
# 此时pipenv会构建一个关于 demo_project 项目的开发环境 

# 激活虚拟环境
pipenv shell
```



### 管理第三方模块

#### 安装第三方模块

> 运行后会生成 Pipfile 和 Pipfile.lock 文件

```shell
pipenv install flask==0.12.1
# 当然也可以不指定版本
```

如果想只安装在开发环境才使用的包，这么做：

```shell
pipenv install pytest --dev
```

> 无论是生产环境还是开发环境的包都会写入一个 Pipfile 里面，而如果是用传统方法，需要2个文件：dev-requirements.txt 和 test-requirements.txt。



接下来如果在开发环境已经完成开发，如何构建生产环境的东东呢？这时候就要使用 Pipfile.lock 了，运行以下命令，把当前环境的模块 lock 住, 它会更新 Pipfile.lock 文件，该文件是用于生产环境的，你永远不应该编辑它。

```shell
pipenv lock
```

然后只需要把代码和 Pipfile.lock 放到生产环境，运行下面的代码，就可以创建和开发环境一样的环境咯，Pipfile.lock 里记录了所有包和子依赖包的确切版本，因此是**确定构建**：

```shell
pipenv install --ignore-pipfile
```

如果要在另一个开发环境做开发，则将代码和Pipfile复制过去，运行以下命令：

```shell
pipenv install --dev
```



#### 卸载包

```python
pipenv uninstall numpy
```





### 代码运行

#### 运行脚本

```shell
pipenv run python xxx.py
```

#### 自定义脚本

```python
[scripts]
start = "python xxx.py"
list = pip list
```







### pipenv依赖分析详解

pipenv 每次安装核心包时，都会检测所有核心包的子依赖包，对不满足的子依赖包会做更新。如果核心包 package_a 和 package_b 依赖有矛盾，比如(package_a依赖package_c>2.0, package_b依赖package_c<1.9），则会有警告提示。

```shell
pipenv graph
```





### Pipfile

> 举个栗子，它是 [TOML](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Ftoml-lang%2Ftoml) 格式的：

```python
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[dev-packages]
pytest = "*"

[packages]
flask = "==0.12.1"
numpy = "*"
requests = {git = "https://github.com/requests/requests.git", editable = true}

[requires]
python_version = "3.6"
```

> 我不用管子依赖包，只会把我项目中实际用到的包放进去，子依赖包在`pipenv install package`的时候自动安装或更新。



### Pipfile.lock

> 举个栗子，它是JSON格式的，它包含了所有子依赖包的确定版本：

```shell
{
    "_meta": {
        ...
    },
    "default": {
        "flask": {
            "hashes": [
                "sha256:6c3130c8927109a08225993e4e503de4ac4f2678678ae211b33b519c622a7242",
                "sha256:9dce4b6bfbb5b062181d3f7da8f727ff70c1156cbb4024351eafd426deb5fb88"
            ],
            "version": "==0.12.1"
        },
        "requests": {
            "editable": true,
            "git": "https://github.com/requests/requests.git",
            "ref": "4ea09e49f7d518d365e7c6f7ff6ed9ca70d6ec2e"
        },
        "werkzeug": {
            "hashes": [
                "sha256:d5da73735293558eb1651ee2fddc4d0dedcfa06538b8813a2e20011583c9e49b",
                "sha256:c3fd7a7d41976d9f44db327260e263132466836cef6f91512889ed60ad26557c"
            ],
            "version": "==0.14.1"
        }
        ...
    },
    "develop": {
        "pytest": {
            "hashes": [
                "sha256:8970e25181e15ab14ae895599a0a0e0ade7d1f1c4c8ca1072ce16f25526a184d",
                "sha256:9ddcb879c8cc859d2540204b5399011f842e5e8823674bf429f70ada281b3cc6"
            ],
            "version": "==3.4.1"
        },
        ...
    }
}
```

**永远也不应该编辑 Pipfile.lock, 它只应该由`pipenv lock`生成。**



### 旧项目的 requirments.txt 转化为 Pipfile

使用`pipenv install`会自动检测当前目录下的requirments.txt, 并生成Pipfile, 我也可以再对生成的Pipfile做修改。

```shell
pipenv install -r requirements.txt
```

如果我有一个开发环境的requirent-dev.txt, 可以用以下命令加入到Pipfile:

```python
pipenv install -r dev-requirements.txt --dev
```



### 是否要将Pipfile加入到版本管理

按照上文分析，代码和 Pipfile 都应该加入版本管理，Pipfile.lock 就见仁见智了，我倾向于不加入到版本管理，因为Pipfile.lock在不同的操作系统，不同的开发阶段都可能发生变化。





## poetry

[poetry 官方文档](https://python-poetry.org/docs)



### 安装poetry

```shell
pip install poetry

poetry --version			# 确认是否安装成功以及查看版本号
```



### 在 python 项目中使用 Poetry

#### 初始化poetry

```shell
poetry init 
# 在现有项目中使用来创建一个pyproject.toml文件

pyproject.toml: 
使用此文件管理依赖列表和项目的各种meta信息，用来替代 Pipfile、requirements.txt、setup.py、setup.cfg、MANIFEST.in 等等各种配置文件。
```



#### 虚拟环境

```shell
# 创建虚拟环境（确保当前目录存在pyproject.toml文件）
poetry install  

# 激活虚拟环境
poetry shell    
```





### 安装依赖包

```shell
poetry install  
# 安装依赖 首次安装会自动创建虚拟环境, 如果想手动选择本地python的版本，请使用poetry env 命令，具体可以参考官方文档
# 如果不想使用虚拟环境，可以执行 poetry config virtualenvs.create false 关闭，依赖将会安装到系统的

poetry env info # 可以查看虚拟环境信息 如果使用pycharm，请添加这个虚拟环境到项目配置
```



### 添加依赖包

```shell
poetry add
```



### 包管理

```shell
# 查看python版本
poetry run python -V

# 更新所有锁定版本的依赖
poetry update

# 更新某个指定的依赖
poetry update <依赖name>

# 卸载包
poetry remove <依赖name>

# 让 poetry 使用 python3
poetry env use python3.7 
```



### 在docker中使用

```shell
# 确保命令执行所在目录有 pyproject.toml文件
# 如果想安装固定版本,可以保存通过 lock 文件
# 在Dockerfile中添加以下执行脚本
RUN poetry config virtualenvs.create false
RUN poetry install
```

