syntax on
set number
set shell=/bin/zsh
set nocompatible
set backspace=indent,eol,start
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set smartindent
set selectmode=mouse
set cmdheight=2
set nobackup
set nowritebackup
set noswapfile
set ruler
set ignorecase
set laststatus=2
set cursorline
set lazyredraw
set showmatch
set colorcolumn=80
highlight ColorColumn ctermbg=233
autocmd Filetype javascript setlocal ts=2 sts=2 sw=2
autocmd Filetype html setlocal ts=2 sts=2 sw=2
autocmd Filetype xml setlocal ts=2 sts=2 sw=2
autocmd Filetype json setlocal ts=2 sts=2 sw=2
:nnoremap dd "_dd
:nnoremap x "_x
:nnoremap ciw "_ciw
:xnoremap p "_dP
set belloff=all
