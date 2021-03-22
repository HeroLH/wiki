## Centos 下的安装

### 依赖项：

- git

    ```shell
    # 安装
    yum install -y git
    
    # 查看版本
    git version
    ```

    

### 安装 Vim8

```shell
# 移除旧版本
sudo yum remove vim -y
# 安装必要组件
sudo yum install ncurses-devel python-devel -y
# 下载源码编译安装
git clone https://github.com/vim/vim.git
cd vim/src
# 根据自己实际情况设置编译参数
./configure --with-features=huge --enable-pythoninterp=yes --enable-cscope --enable-fontset --with-python-config-dir=/usr/lib64/python2.7/config
make
sudo make install
```

**编译参数说明：**
–with-features=huge：支持最大特性
–enable-rubyinterp：打开对ruby编写的插件的支持
–enable-pythoninterp：打开对python编写的插件的支持
–enable-python3interp：打开对python3编写的插件的支持
–enable-luainterp：打开对lua编写的插件的支持
–enable-perlinterp：打开对perl编写的插件的支持
–enable-multibyte：打开多字节支持，可以在Vim中输入中文
–enable-cscope：打开对cscope的支持
–with-python-config-dir=/usr/lib64/python2.7/config 指定python 路径
–with-python-config-dir=/usr/lib64/python3.5/config 指定python3路径

注意：必须带上Python编写插件支持，最好带上Python路径，否则使用时会报这个错误：YouCompleteMe unavailable: requires Vim compiled with Python (2.6+ or 3.3+) support





### 添加环境变量

```
vi /etc/profile
export PATH=$PATH:/usr/local/bin/vim
source /etc/profile
```





### 安装、配置Vim-Plug

```shell
 curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

如果报错：

> Failed connect to raw.githubusercontent.com:443; Connection refused

```  shell
sudo vim /etc/hosts

# 加上一行
199.232.28.133 raw.githubusercontent.com
```





#### 配置

```shell
 vim ~/.vimrc
```

```shell
set nocompatible
filetype on
set backspace=indent,eol,start

call plug#begin('~/.vim/plugged')
Plug 'Valloric/YouCompleteMe'
call plug#end()

let g:ycm_global_ycm_extra_conf='~/.vim/plugged/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py'
let g:ycm_seed_identifiers_with_syntax=1
let g:ycm_confrm_extra_conf=0
inoremap <expr> <CR>  pumvisible() ? "\<C-y>" : "\<CR>"
set completeopt=longest,menu

```

保存并重新打开 `vim ~/.vimrc` 

执行检查状态命令：

```
:PlugStatus
```

安装插件命令：

```
:PlugInstall
```

更新插件命令：

```
:PlugUpdate
```

删除插件命令：

```
:PlugClean
```

升级Vim-Plug命令：

```
:PlugUpgrade
```



### 安装YouCompleteMe

之前在安装 Vim8 步骤已经配置插件 YouCompleteMe，再在安装 Vim-Plug 步骤执行安装插件命令，说明 YouCompleteMe 插件已经安装完成。再进行如下配置即可使用。



#### 安装Clang

```
sudo yum install cmake -y
cd ~/.vim/plugged/YouCompleteMe  
./install.py --clang-completer
123
```



#### 配置.ycm_extra_conf.py

```
import os
import ycm_core
flags = [
'-Wall',
'-Wextra',
'-Wno-long-long',
'-Wno-variadic-macros',
'-fexceptions',
'-stdlib=libc++',
'-std=c++11',
'-x',
'c++',
'-I',
'.',
'-isystem',
'/usr/include',
'-isystem',
'/usr/local/include',
'-isystem',
'/Library/Developer/CommandLineTools/usr/include',
'-isystem',
'/Library/Developer/CommandLineTools/usr/bin/../lib/c++/v1',
]

compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )

def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags

def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]

def GetCompilationInfoForFile( filename ):

  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )

def FlagsForFile( filename, **kwargs ):
  if database:


    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )

  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }
```