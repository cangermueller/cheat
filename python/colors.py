#!/usr/bin/env python

from colorama import Fore, Back, Style, init
import sys

init(strip=not sys.stdout.isatty(), autoreset=True)
# autoreset=True: change to default after one command
# strip=True: deactivate coloring

print(Fore.BLUE + 'Blue foreground')
print('Normal, since autoreset')
print(Back.GREEN + 'Green background')
print(Style.BRIGHT + 'bright text')
print(Style.DIM + 'dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL + 'Normal text')

fores = 'BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET'.split(', ')
s = ''
for fore in fores:
    s += eval('Fore.{fore} + "{fore}"'.format(fore=fore)) + ' '
print(s)

values = 'BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET'.split(', ')
s = ''
for value in values:
    s += eval('Back.{0} + "{0}"'.format(value)) + ' '
print(s)

values = 'DIM, NORMAL, BRIGHT, RESET_ALL'.split(', ')
s = ''
for value in values:
    s += eval('Style.{0} + "{0}"'.format(value)) + ' '
print(s)
