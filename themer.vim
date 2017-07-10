highlight clear
if exists("syntax_on")
  syntax reset
endif

set background=dark
let g:colors_name="themer"

" Highlighting scheme. current count = 9?
" if, else, return, continue, break, fn, let, switch = colour accent
" numeric constants (inc bools) = colour 2
" string/chars = color 3 
" Column = background colour (opaque)
" normal text (var names) = main text colour
" Comment text
" function, struct, enum names (in definition) = another colour?
" special text colour 1 (i.e. rust macros or annotations)
" standard library highlighting?

hi ErrorMsg         ctermfg=NONE    ctermbg=NONE    cterm=bold      term=standout 
hi Search           ctermfg=NONE    ctermbg=NONE    term=reverse
hi StatusLineNC     ctermfg=NONE    ctermbg=NONE    term=reverse

hi Boolean          ctermfg=1
hi Character        ctermfg=2
hi Number           ctermfg=1
hi String           ctermfg=2
hi Conditional      ctermfg=4       ctermbg=NONE    cterm=bold
hi Constant         ctermfg=5       ctermbg=NONE    cterm=bold
hi Cursor           ctermfg=6       ctermbg=0     
hi Debug            ctermfg=7       ctermbg=NONE    cterm=bold
hi Define           ctermfg=8    
hi Delimiter        ctermfg=5

hi DiffAdd          ctermfg=NONE    ctermbg=0 
hi DiffChange       ctermfg=0       ctermbg=0  
hi DiffDelete       ctermfg=0       ctermbg=0 
hi DiffText         ctermfg=NONE    ctermbg=0       cterm=bold

hi Directory        ctermfg=0       ctermbg=NONE    cterm=bold
hi Error            ctermfg=0       ctermbg=0 
hi ErrorMsg         ctermfg=0       ctermbg=0       cterm=bold
hi Exception        ctermfg=0       ctermbg=NONE    cterm=bold
hi Float            ctermfg=1  
hi FoldColumn       ctermfg=0       ctermbg=0 
hi Folded           ctermfg=0       ctermbg=0 
hi Function         ctermfg=3  
hi Identifier       ctermfg=0       ctermbg=NONE    cterm=none
hi Ignore           ctermfg=0       ctermbg=0  
hi IncSearch        ctermfg=0       ctermbg=0 

hi keyword          ctermfg=0       ctermbg=NONE    cterm=bold
hi Label            ctermfg=0       ctermbg=NONE    cterm=none
hi Macro            ctermfg=0
hi SpecialKey       ctermfg=0

hi MatchParen       ctermfg=0       ctermbg=0       cterm=bold
hi ModeMsg          ctermfg=0
hi MoreMsg          ctermfg=0
hi Operator         ctermfg=0

" complete menu
hi Pmenu            ctermfg=0       ctermbg=0 
hi PmenuSel         ctermfg=0       ctermbg=0  
hi PmenuSbar        ctermfg=0       ctermbg=0  
hi PmenuThumb       ctermfg=0 

hi PreCondit        ctermfg=0       ctermbg=0       cterm=bold
hi PreProc          ctermfg=0  
hi Question         ctermfg=0 
hi Repeat           ctermfg=0       ctermbg=0       cterm=bold
hi Search           ctermfg=0       ctermbg=0       cterm=NONE

" marks column
hi SignColumn       ctermfg=0       ctermbg=0  
hi SpecialChar      ctermfg=0       ctermbg=NONE    cterm=bold
hi SpecialComment   ctermfg=0       ctermbg=NONE    cterm=bold
hi Special          ctermfg=0 
if has("spell")
   hi SpellBad      ctermfg=NONE    ctermbg=0 
   hi SpellCap      ctermfg=NONE    ctermbg=0 
   hi SpellLocal    ctermfg=NONE    ctermbg=0  
   hi SpellRare     ctermfg=NONE    ctermbg=NONE    cterm=reverse
endif
hi Statement        ctermfg=0       ctermbg=NONE    cterm=bold
hi StatusLine       ctermfg=0       ctermbg=0  
hi StatusLineNC     ctermfg=0       ctermbg=0  
hi StorageClass     ctermfg=0  
hi Structure        ctermfg=0  
hi Tag              ctermfg=0  
hi Title            ctermfg=0  
hi Todo             ctermfg=0       ctermbg=0       cterm=bold


hi Typedef          ctermfg=0
hi Type             ctermfg=0       ctermbg=NONE    cterm=none
hi Underlined       ctermfg=0       ctermbg=NONE    cterm=underline

hi VertSplit        ctermfg=0       ctermbg=0       cterm=bold
hi VisualNOS        ctermfg=NONE    ctermbg=0
hi Visual           ctermfg=NONE    ctermbg=0
hi WarningMsg       ctermfg=0       ctermbg=0       cterm=bold
hi WildMenu         ctermfg=0       ctermbg=0

hi TabLineFill      ctermfg=0       ctermbg=0
hi TabLine          ctermbg=0       ctermfg=0       cterm=none
