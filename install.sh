# Installation notes

# ~/.bash_profile
# https://superuser.com/questions/544989/does-tmux-sort-the-path-variable
# if [ -f /etc/profile ]; then
#     PATH=""
#         source /etc/profile
#         fi
#
#         export BASH_SILENCE_DEPRECATION_WARNING=1
#         source ~/.bashrc
#

i Dotdrop
cd ~/etc/dotfiles
# use -p to use other profile (does not work? nothing to install)
.dotdrop/dotdrop.sh install --cfg $(pwd)/config.yaml

# iterm
Import preferences: General -> Settings

## Installing tmux-mem-cpu-load
cd ~/.tmux/plugins/tmux-mem-cpu-load
cmake .
make install

## VIM
sudo port install vim +huge +python39 +perl +ruby +gtk2
