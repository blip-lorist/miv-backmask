import vim

# Normal mode backmask
vim.command(":noremap j k")
vim.command(":noremap k j")
vim.command(":noremap h l")
vim.command(":noremap l h")

# Neat read: https://stackoverflow.com/questions/3776117/what-is-the-difference-between-the-remap-noremap-nnoremap-and-vnoremap-mapping
