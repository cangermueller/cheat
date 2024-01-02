#!/usr/bin/env bash

# sudo port install vim +huge +python39 +perl +ruby +gtk2

## For COC
sudo port install go nodejs18
cd $VB/coc.vim && git checkout release  // https://github.com/neoclide/coc.nvim/issues/3258#issuecomment-1565392051

# 200324
./configure \
    --with-features=huge \
    --enable-python3interp \
    --enable-cscope \
    --enable-gui=auto \
    --enable-gtk2-check \
    --enable-gnome-check \
    --enable-multibyte \
    --with-python3-config-dir=/usr/local/google/home/christofa/opt/stow/anaconda3/pkgs/python-3.7.6-h0371630_2/lib/python3.7/config-3.7m-x86_64-linux-gnu \
    --enable-fontset \
    --enable-largefile \
    --enable-fail-if-missing \
    --prefix=$HOME/opt/stow/vim81

# ./configure \
#     --with-features=huge \
#     --enable-perlinterp \
#     --enable-python3interp \
#     --enable-cscope \
#     --enable-gui=auto \
#     --enable-gtk2-check \
#     --enable-gnome-check \
#     --enable-multibyte \
#     --with-x \
#     --with-python3-config-dir=/usr/local/google/home/christofa/opt/stow/anaconda3/pkgs/python-3.7.0-hc3d631a_0/lib/python3.7/config-3.7m-x86_64-linux-gnu \
#     --enable-fontset \
#     --enable-largefile \
#     --enable-fail-if-missing \
#     --prefix=$HOME/opt/stow/vim81
