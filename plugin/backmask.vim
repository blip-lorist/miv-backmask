" Quit if vim hasn't been compiled with python support
if !has('python')
  finish
endif

function! Backmask()
  pyfile ../python/backmask.py
endfunc

call Backmask()
