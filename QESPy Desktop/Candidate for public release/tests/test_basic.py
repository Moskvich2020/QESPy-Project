import os
import sys
from msvcrt import getch
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()
clear = lambda: os.system('cls')

def title(func):
    def wrapper():
        print('1')
        func()
        print('2')
    return wrapper

@title
def coefficient_reading(): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0)
    clear()
    console.print(Panel(Text(text='Решение квадратного уравнения (ax²+bx+c=0)', justify='center'), title='Опция №1'))
    while True:
        while True:
            coefficient_a = input('   Введите коэффициент a: ')
            try:
                coefficient_a = float(coefficient_a)
                if coefficient_a.is_integer():
                    coefficient_a = int(coefficient_a)
                else:
                    pass
                break
            except ValueError:
                console.print('\n[red]Ошибка! Коэффициент a не является числом! Введите, пожалуйста, ещё раз число![/]')
                console.print('[red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
        while True:
            coefficient_b = input('   Введите коэффициент b: ')
            try:
                coefficient_b = float(coefficient_b)
                if coefficient_b.is_integer():
                    coefficient_b = int(coefficient_b)
                else:
                    pass
                break
            except ValueError:
                console.print('\n[red]Ошибка! Коэффициент b не является числом! Введите, пожалуйста, ещё раз число![/]')
                console.print('[red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
        while True:
            coefficient_c = input('   Введите коэффициент c: ')
            try:
                coefficient_c = float(coefficient_c)
                if coefficient_c.is_integer():
                    coefficient_c = int(coefficient_c)
                else:
                    pass
                break
            except ValueError:
                console.print('\n[red]Ошибка! Коэффициент c не является числом! Введите, пожалуйста, ещё раз число![/]')
                console.print('[red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')

coefficient_reading()
