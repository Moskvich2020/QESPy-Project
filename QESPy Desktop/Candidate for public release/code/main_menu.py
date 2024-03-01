import os
import sys
from msvcrt import getch
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()
clear = lambda: os.system('cls')

def main_menu():
    clear()
    main_menu_title_panel = Panel(
        Text(
            text='\nДобро пожаловать в QESPy CFPR!\n',
            justify='center'
        ),
        title='ГЛАВНОЕ МЕНЮ',
        subtitle='(c) Cristi Constantin (Moskvich2020) QESPy Project',
        subtitle_align='left',
    )
    main_menu_options_panel = Panel(
        Text(
            text='''
[1]    Решение квадратного уравнения (ax²+bx+c=0)
[2]    Решение кубическаго уравнения (ax³+bx²+cx+d=0)
[3]    Решение биквадратного уравнения (ax⁴+bx²+c=0)
[4]    Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))
[5]    Терминал
[6]    Справка
[E]    Выйти из программы
            '''
        ),
        title='ОПЦИИ',
        subtitle='Пожалуйста, введите идентификатор опции из меню...',
        subtitle_align='left'
    )

    console.print(main_menu_title_panel)
    console.print(main_menu_options_panel)
    
    while True:
        pressed_key = getch().lower()
        if ord(pressed_key) == ord('1'):
            pass
        elif ord(pressed_key) == ord('2'):
            pass
        elif ord(pressed_key) == ord('3'):
            pass
        elif ord(pressed_key) == ord('4'):
            pass
        elif ord(pressed_key) == ord('5'):
            pass
        elif ord(pressed_key) == ord('6'):
            pass
        elif ord(pressed_key) == ord('e'):    
            sys.exit()
            # quit()
        else:
            console.print('\n[red]Команда некорректна или не существует![/]\n')
