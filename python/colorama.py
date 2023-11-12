#!/usr/bin/env python

import colorama
import sys

# colorama.init(strip=not sys.stdout.isatty(), autoreset=True)
# autoreset=True: change to default after one command
# strip=True: deactivate coloring

print(colorama.Fore.BLUE + 'Blue foreground')
print('Normal, since autoreset')
print(colorama.Back.GREEN + 'Green background')
print(colorama.Style.BRIGHT + 'bright text')
print(colorama.Style.DIM + 'dim text')
print(colorama.Fore.RESET + colorama.Back.RESET + colorama.Style.RESET_ALL + 'Normal text')

fores = 'BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET'.split(', ')
s = ''
for fore in fores:
    s += eval('colorama.Fore.{fore} + "{fore}"'.format(fore=fore)) + ' '
print(s)

values = 'BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET'.split(', ')
s = ''
for value in values:
    s += eval('colorama.Back.{0} + "{0}"'.format(value)) + ' '
print(s)

values = 'DIM, NORMAL, BRIGHT, RESET_ALL'.split(', ')
s = ''
for value in values:
    s += eval('colorama.Style.{0} + "{0}"'.format(value)) + ' '
print(s)
