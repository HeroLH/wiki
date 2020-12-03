```shell
" 不同模式下光标样式不一样(兼容性不强)
let &t_SI = "\<Esc>]50;CursorShape=1\x7"
let &t_SR = "\<Esc>]50;CursorShape=2\x7"
let &t_EI = "\<Esc>]50;CursorShape=0\x7"

"调整配色
let &t_ut=''

" 不与 Vi 兼容（采用 Vim 自己的操作命令
set nocompatible

" vim 默认是 vi 兼容的。解决退格键会失效问题
set backspace=indent,eol,start

" 支持使用鼠标
"set mouse=a



" 定义 leader 键
let mapleader="\<space>"

" 设置编码格式为 utf-8
set encoding=utf-8

"按下 Tab 键时，Vim 显示的空格数。
 set tabstop=4
 
" 如果行尾有多余的空格（包括 Tab 键），该配置将让这些空格显示成可见的小方块。
set listchars=tab:▸\ ,trail:■ 
set list

" 确保页面顶部和底部永远有五行显示
set scrolloff = 5


" 搜索时，高亮显示匹配结果
set hlsearch 
exec "nohlsearch"
  
  " 输入搜索模式时，每输入一个字符，就自动跳到第一个匹配的结果。
  set incsearch                                                                           
" 搜索时忽略大小写。
set ignorecase  

" 如果同时打开了ignorecase，那么对于只有一个大写字母的搜索词，将大小写敏感；其他情况都是大小写不敏感。比如，搜索Test时，将不匹配test；搜索test时，将匹配Test。
set smartcase  

"取消搜索高亮
noremap <LEADER><CR> :nohlsearch<CR>



" 打开语法高亮。自动识别代码，使用多种颜色显示。 
syntax on

" 显示行号
set number

" 显示光标所在的当前行的行号，其他行都为相对于该行的相对行号。
 set relativenumber
 
" 光标所在的当前行高亮。
set cursorline

"是否显示状态栏。0 表示不显示，1 表示只在多窗口时显示，2 表示显示。
set laststatus=2

" 命令模式下，在底部显示，当前键入的指令。比如，键入的指令是2y3d，那么底部就会显示2y3，当键入d的时候，操作完成，显示消失。
set showcmd

"命令模式下，底部操作指令按下 Tab 键自动补全。第一次按下 Tab，会显示所有匹配的操作指令的清单；第二次按下 Tab，会依次选择各个指令。
set wildmenu

" 在底部显示，当前处于命令模式还是插入模式。
set wildmode=longest:list,full



" 按键映射
map s <nop>
map S :w<CR>
map <C-s> :w!<CR>
map <C-q> :q<CR>
map Q :wq!<CR>
map MV :source $MYVIMRC<CR>

# 打开和关闭拼写检查
map <LEADER>sc :set spell!<CR>
map <LEADER>cs :set nospell!<CR>


"快速移动光标
noremap H 0
noremap J 10j
noremap K 10k
noremap L $

" 分屏映射
map sr :set splitright<CR>:vsplit<CR>
map sl :set nosplitright<CR>:vsplit<CR>
map su :set nosplitbelow<CR>:split<CR>
map sb :set splitbelow<CR>:split<CR>

" 分屏下光标移动方向
map <LEADER>l <C-w>l
map <LEADER>k <C-w>k
map <LEADER>h <C-w>h
map <LEADER>j <C-w>j


" 每次打开文件，光标会停留在关闭之前的位置
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif


filetype on
"自适应不同语言的智能缩进
filetype indent on
"加载对应文件类型插件
filetype plugin on
filetype plugin indent on


call plug#begin('~/.vim/plugged')
" 显示模式
Plug 'vim-airline/vim-airline'
" snazzy 配色
Plug 'connorholyday/vim-snazzy'

" File navigation
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
Plug 'Xuyuanp/nerdtree-git-plugin'



" Auto Complete
"Plug 'Valloric/YouCompleteMe'

call plug#end()




" 背景半透明
let g:SnazzyTransparent = 1

"开启snazzy 配色
"color snazzy

" ===
" === NERDTree
" ===
" 打开 NERDTree
map ff :NERDTreeToggle<CR>

" ==
" == NERDTree-git
" ==
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ "Unknown"   : "?"
    \ }

```

