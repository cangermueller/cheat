#!/usr/bin/env bash

./configure \
    --with-features=huge \
    --enable-perlinterp \
    --enable-python3interp \
    --enable-cscope \
    --enable-gui=auto \
    --enable-gtk2-check \
    --enable-gnome-check \
    --enable-multibyte \
    --with-x \
    --prefix=$HOME/opt/stow/vim74

