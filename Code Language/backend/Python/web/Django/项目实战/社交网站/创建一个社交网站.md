----------------------------------------------
> *Made By Herolh*
----------------------------------------------

# 目录 {#index}
[TOC]











--------------------------------------------

# 创建一个社交网站
&emsp;&emsp;开发一个社交应用。你会为用户创建一些功能，例如：登录，登出，编辑，以及重置他们的密码。你会学习如何为你的用户创建一个定制的 profile，你还会为你的站点添加社交认证。本教程将会覆盖一下几点：
- 使用认证（authentication）框架
- 创建用户注册视图（views）
- 通过一个定制的 profile 模型扩展 User 模型
- 使用 `python-social-auth` 添加社交认证



## 创建一个社交网站项目
&emsp;&emsp;我们要创建一个社交应用允许用户分享他们在网上找到的图片。我们需要为这个项目构建以下元素：
- 一个用来给用户注册，登录，编辑他们的 profile，以及改变或重置密码的认证系统
- 一个允许用户来关注其他人的关注系统
- 为用户从其他任何网站分享过来的图片进行展示和打上书签
- 每个用户都有一个活动流允许他们看到所关注的人上传的内容



### 开始你的社交网站项目

&emsp;&emsp;打开终端使用如下命令行为你的项目创建一个虚拟环境并且激活它：


```

```

&emsp;&emsp;通过以下命令在你的虚拟环境中安装 Django：

```shell
pip install Django==2.0
```

&emsp;&emsp;运行下一条命令为 `INSTALLED_APPS `中默认包含的应用模型（models）同步到数据库中：

```shell
python manage.py migrate
```







## 使用 Django 认证(authentication)框架

&emsp;&emsp;Django 拥有一个内置的认证 (authentication) 框架用来操作用户认证 (authentication)，会话(sessions)，
权限(permissions)以及用户组。这个认证系统包含了一些普通用户的操作视图(views)，例如：登录，登出，修改密码以及重置密码。
这个认证框架位于 `django.contrib.auth`，被其他 Django 的 contrib 包调用。当你使用 `startproject` 命令创建一个新的 Django 项目，认证框架已经在你的项目设置中默认包含。它是由 `django.contrib.auth` 应用和你的项目设置中的 `MIDDLEWARE_CLASSES` 中的两个中间件类组成，如下：

- **AuthenticationMiddleware**: 使用会话（sessions）将用户和请求（requests）进行关联
- **SessionMiddleware**: 通过请求（requests）操作当前会话（sessions）

这个认证系统还包含了以下模型：

- **User**：一个包含了基础字段的用户模型；这个模型的主要字段有：username，password, email, first_name, last_name, is_active。
- **Group**：一个组模型用来分类用户
- **Permission**：执行特定操作的标识



### 创建一个 log-in 视图（view）

&emsp;&emsp;我们将要开始使用 Django 认证框架来允许用户登录我们的网站。我们的视图需要执行以下操作来登录用户：

1. 通过提交的表单获取 username 和 password
2. 通过存储在数据库中的数据对用户进行认证
3. 检查用户是否可用
4. 登录用户到网站中并且开始一个认证（authentication）会话（session）

&emsp;&emsp;首先，我们要创建一个登录表单。在你的 account 应用目录下创建一个新的 forms.py 文件，添加如下代码：

```python
from django import forms
class LoginForm(forms.Form):
     username = forms.CharField()
     password = forms.CharField(widget=forms.PasswordInput)
```

&emsp;&emsp;这个表单被用来通过数据库认证用户。请注意，我们使用 `PasswordInput` 控件来渲染 `HTMLinput`
元素，包含 `type="password"`属性。编辑你的 account 应用中的 views.py 文件，添加如下代码：

```python
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
def user_login(request):
     if request.method == 'POST':
         form = LoginForm(request.POST)
     if form.is_valid():
         cd = form.cleaned_data
         user = authenticate(username=cd['username'],password=cd['password'])
         
         if user is not None:
             if user.is_active:
                 login(request, user)
                 return HttpResponse('Authenticated successfully')
             else:
                 return HttpResponse('Disabled account')
         else:
             return HttpResponse('Invalid login')
     else:
     	form = LoginForm()
	 return render(request, 'account/login.html', {'form': form})
```





















































