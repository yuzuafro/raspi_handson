set number
set showmode
set ruler
set showmatch
set title
set hlsearch

syntax on

colorscheme desert

set expandtab
set ts=4 sw=4 sts=0
set wrapscan

set list
set listchars=tab:>.,trail:_,nbsp:%

function! ZenkakuSpace()
    highlight ZenkakuSpace cterm=reverse ctermfg=DarkMagenta gui=reverse guifg=DarkMagenta
endfunction

if has('syntax')
    augroup ZenkakuSpace
        autocmd!
        autocmd ColorScheme       * call ZenkakuSpace()
        autocmd VimEnter,WinEnter * match ZenkakuSpace /　/
    augroup END
    call ZenkakuSpace()
endif
