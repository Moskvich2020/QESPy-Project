# ╭─────────────────────────────────╮
# │ QESPy Beta 3.2 [build 11012024] │ 
# ╰─────────────────────────────────╯

import os
import sys
from msvcrt import getch
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()
clear = lambda: os.system('cls')
# os.system('mode 125, 30')


def main(): # main
    clear()
    print('Quadratic Equation Solver in Python [Version 3.2.4b]')
    print('(c) Cristi Constantin (Moskvich2020) QESPy Project. Все права защищены.')
    sleep(0.5)
    main_menu()


def main_menu(): # Главное меню
    clear()
    main_menu_title_panel = Panel(
        Text(
            text='\nДобро пожаловать в QESPy Beta 3.2!\nПрограмма готова к решению всех видов квадратных уравнений!\n',
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
[2]    Решение биквадратного уравнения (ax⁴+bx²+c=0)
[3]    Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))
[4]    Терминал
[5]    Справка
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
            solving_a_quadratic_equation()
        elif ord(pressed_key) == ord('2'):
            pass
        elif ord(pressed_key) == ord('3'):
            pass
        elif ord(pressed_key) == ord('4'):
            pass
        elif ord(pressed_key) == ord('5'):
            pass
        elif ord(pressed_key) == ord('e'):    
            sys.exit()
            # quit()
        else:
            console.print('\n[red]Команда некорректна или не существует![/]\n')


def solving_a_quadratic_equation(): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0)
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

        if not coefficient_a and coefficient_b != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx+c=0 | a = 0
            solution_x = -(coefficient_c/coefficient_b)

            coef_b_str = f'{coefficient_b}x' if abs(coefficient_b) != 1 else ('x' if coefficient_b == 1 else '-x')
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            sol_x_str = f'{solution_x}' if isinstance(solution_x, int) == True else f'{solution_x:.2f}'
            coef_b_sol_1 = f'{coefficient_b}x' if abs(coefficient_b) != 1 else ('x' if coefficient_b == 1 else '-x')
            coef_b_sol_2 = f'{-coefficient_b}'
            coef_b_sol_3 = f'{coefficient_b}'
            coef_c_sol_1 = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_c_sol_2 = f'{-coefficient_c}'
            auxiliary_line_sol_1 = f'\n              x = -({coefficient_c} / {coefficient_b})' if coefficient_b > 0 and coefficient_c > 0 else (f'\n              x = {coefficient_c} / {-coefficient_b}' if coefficient_b < 0 and coefficient_c > 0 else ('' if coefficient_b > 0 and coefficient_c < 0 else f'\n              x = -({-coefficient_c} / {-coefficient_b})'))
            auxiliary_line_sol_2 = f'\n              x = {coefficient_c}' if coefficient_b < 0 and coefficient_c > 0 else (f'\n              x = {coefficient_c}' if coefficient_b < 0 and coefficient_c < 0 else '')
            auxiliary_line_sol = f'x = {coef_c_sol_2} / {coef_b_sol_3}{auxiliary_line_sol_1}\n' if abs(coefficient_b) != 1 else f'{coef_b_sol_1} = {coef_c_sol_2}{auxiliary_line_sol_2}\n'
            sol_x_sol = f'{solution_x}' if isinstance(solution_x, int) == True else f'{solution_x:.2f}'

            print()
            print('   ───────────────────────────────────')
            print('   Принято уравнение вида bx+c=0      ')
            print('   ───────────────────────────────────')
            print(f'   Дано:      {coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   {coef_b_sol_1}{coef_c_sol_1} = 0')
            print(f'              {auxiliary_line_sol}', end='')
            print(f'              x = {sol_x_sol}')
            print(f'   Ответ:     x = {sol_x_str}')
            print('   ───────────────────────────────────')
            print()
            sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')
        elif coefficient_a != 0 and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+c=0 | b = 0
            if (coefficient_c/coefficient_a) < 0:
                solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
                solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)

                coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
                coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
                coef_a_sol_1 = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
                coef_c_sol_1 = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
                coef_c_sol_2 = f'{-coefficient_c}'
                coef_c_sol_3 = f'{-coefficient_c}' if coefficient_c < 0 else f'({-coefficient_c})'
                auxiliary_line_sol = f'\n              {coef_a_sol_1} = {coef_c_sol_2}\n              x = ±√({coef_c_sol_2} / {coefficient_a})' if abs(coefficient_a) != 1 else f'\n              x² = ±{coef_c_sol_3}\n              x = ±√{coef_c_sol_3}'

                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида ax²+c=0     ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coef_a_str}{coef_c_str} = 0')
                print(f'   Решение:   {coef_a_sol_1}{coef_c_sol_1} = 0', end='')
                print(f'              {auxiliary_line_sol}')
                print(f'              x₁ = {solution_x1:.2f}')
                print(f'              x₂ = {solution_x2:.2f}')
                print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                print(f'              x₂ = {solution_x2:.2f}')
                print('   ───────────────────────────────────')
                print()
                sleep(1)
                while True:
                    print('[N] Продолжить, [E] Выход')
                    pressed_key = getch().lower()
                    if ord(pressed_key) == ord('n'):
                        print()
                        break
                    elif ord(pressed_key) == ord('e'):
                        main_menu()
                    else:
                        console.print('\n[red]Команда некорректна или не существует![/]\n')
            else:
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида ax²+c=0     ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coef_a_str}{coef_c_str} = 0')
                print(f'   Решение:   {coef_a_sol_1}{coef_c_sol_1} = 0')
                print(f'              {coefficient_c} / {coefficient_a} < 0')
                print('   Ответ: Уравнение не имеет решений!        ')
                print('   ───────────────────────────────────')
                print()
                sleep(1)
                while True:
                    print('[N] Продолжить, [E] Выход')
                    pressed_key = getch().lower()
                    if ord(pressed_key) == ord('n'):
                        print()
                        break
                    elif ord(pressed_key) == ord('e'):
                        main_menu()
                    else:
                        console.print('\n[red]Команда некорректна или не существует![/]\n')
        elif coefficient_a != 0 and coefficient_b != 0 and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx=0 | c = 0
            solution_x1 = 0
            solution_x2 = -(coefficient_b/coefficient_a)

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else (' + x' if coefficient_b == 1 else ' - x'))
            coef_a_sol_1 = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_a_sol_2 = f'{coefficient_a}x' if abs(coefficient_a) != 1 else ('x' if coefficient_a == 1 else '-x')
            coef_b_sol_1 = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else (' + x' if coefficient_b == 1 else ' - x'))
            coef_b_sol_2 = f' + {coefficient_b}' if coefficient_b > 0 else f' - {-coefficient_b}'
            auxiliary_line_sol_1 = f'\n              x₂ = {coef_a_sol_2} = {-coefficient_b}' if abs(coefficient_a) != 1 else (f'\n              x₂ = {-coefficient_b}' if coefficient_a > 0 else f'\n              x₂ = {coefficient_b}')
            auxiliary_line_sol_2 = f'\n              x₂ = {-coefficient_b} / {coefficient_a}' if abs(coefficient_a) != 1 else ''

            print()
            print('   ───────────────────────────────────')
            print('   Принято уравнение вида ax²+bx=0    ')
            print('   ───────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str} = 0')
            print(f'   Решение:   {coef_a_sol_1}{coef_b_sol_1} = 0')
            print(f'              x({coef_a_sol_2}{coef_b_sol_2}) = 0')
            print(f'              x₁ = 0')
            print(f'              x₂ = {coef_a_sol_2}{coef_b_sol_2} = 0', end='')
            print(f'              {auxiliary_line_sol_1}', end='')
            print(f'              {auxiliary_line_sol_2}')
            print(f'              x₂ = {solution_x2:.2f}')
            print(f'   Ответ:     x₁ = {solution_x1:.2f}')
            print(f'              x₂ = {solution_x2:.2f}')
            print('   ───────────────────────────────────')
            print()
            sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')
        elif not coefficient_a and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c=0 | a и b = 0
            print()
            print('   ───────────────────────────────────')
            print('   Принято уравнение вида c=0         ')
            print('   ───────────────────────────────────')
            print(f'   Ошибка! "{coefficient_c} = 0". Данное выражение не имеет смысла!')
            print('   Ответ: Пустое множество')
            print('   ───────────────────────────────────')
            print()
            sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')
        elif not coefficient_a and coefficient_b != 0 and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx=0 | a и c = 0
            solution_x = 0
            print()
            print('   ───────────────────────────────────')
            print('   Принято уравнение вида bx=0        ')
            print('   ───────────────────────────────────')
            print(f'   Дано:      {coefficient_b}x = 0')
            print(f'   Решение:   x = {solution_x}')
            print(f'   Ответ:     x = {solution_x}')
            print('   ───────────────────────────────────')
            print()
            sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')
        elif coefficient_a != 0 and not coefficient_b and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²=0 | b и c = 0
            solution_x1 = 0
            solution_x2 = 0
            print()
            print('   ───────────────────────────────────')
            print('   Принято уравнение вида ax²=0       ')
            print('   ───────────────────────────────────')
            print(f'   Дано:      {coefficient_a}x² = 0')
            print('   Решение:   x² = 0')
            print('              x = √0')
            print(f'   Ответ:     x₁ = {solution_x1}')
            print(f'              x₂ = {solution_x2}')
            print('   ───────────────────────────────────')
            print()                
            sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')
        elif not coefficient_a and not coefficient_b and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > 0=0 | a и b и c = 0
            print()
            print('   ───────────────────────────────────')
            print('   Принято уравнение вида 0=0         ')
            print('   ───────────────────────────────────')
            print('   Дано:      0 = 0')
            print('   Решение:   x принадлежит R')
            print('   Ответ:     x может быть любым числом')
            print('   ───────────────────────────────────')
            print()
            sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')
        else: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx+c=0 | a и b и c != 0 
            discriminant = coefficient_b**2 - 4*coefficient_a*coefficient_c

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_a_dis = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            coef_b_dis = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_c_dis = f'{coefficient_c}' if coefficient_c > 0 else f'({coefficient_c})'
            a_c_dis = f' - {4*coefficient_a*coefficient_c:.2f}' if 4*coefficient_a*coefficient_c > 0 else f' + {abs(4*coefficient_a*coefficient_c):.2f}'
            coef_a_sol = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            coef_b_sol_1 = f'(-{coefficient_b}' if coefficient_b > 0 else f'(-({coefficient_b})'
            coef_b_sol_2 = f'(-{coefficient_b}' if coefficient_b > 0 else f'({-coefficient_b}'
            dis_sol = f'√{discriminant:.2f})' if discriminant > 0 else f'√({discriminant:.2f}))'

            if discriminant > 0:
                solution_x1 = (-coefficient_b + discriminant**(1/2)) / (2*coefficient_a)
                solution_x2 = (-coefficient_b - discriminant**(1/2)) / (2*coefficient_a)
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида ax²+bx+c=0  ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
                print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                print(f'              D = {discriminant:.2f}')
                print(f'              x = {coef_b_sol_1} ± {dis_sol} / (2 × {coef_a_sol})')
                print(f'              x = {coef_b_sol_2} ± {discriminant**(1/2):.2f}) / ({2*coefficient_a:.2f})')
                print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                print(f'              x₂ = {solution_x2:.2f}')
                print('   ───────────────────────────────────')
                print()
                sleep(1)
                while True:
                    print('[N] Продолжить, [E] Выход')
                    pressed_key = getch().lower()
                    if ord(pressed_key) == ord('n'):
                        print()
                        break
                    elif ord(pressed_key) == ord('e'):
                        main_menu()
                    else:
                        console.print('\n[red]Команда некорректна или не существует![/]\n')
            elif not discriminant:
                solution_x = -((coefficient_b) / (2*coefficient_a))
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида ax²+bx+c=0  ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
                print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                print(f'              D = {discriminant:.2f}')
                print(f'              x = {coef_b_sol_1}) / ( 2 × {coef_a_sol})')
                print(f'              x = {coef_b_sol_2}) / ({2*coef_a_sol})')
                print(f'   Ответ:     x = {solution_x:.2f}')
                print('   ───────────────────────────────────')
                sleep(1)
                while True:
                    print('[N] Продолжить, [E] Выход')
                    pressed_key = getch().lower()
                    if ord(pressed_key) == ord('n'):
                        print()
                        break
                    elif ord(pressed_key) == ord('e'):
                        main_menu()
                    else:
                        console.print('\n[red]Команда некорректна или не существует![/]\n')
            else:
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида ax²+bx+c=0  ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
                print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                print(f'              D = {discriminant:.2f}')
                print('   Ответ:     Уравнение не имеет решений!')
                print('   ───────────────────────────────────')
                print()
                sleep(1)
                while True:
                    print('[N] Продолжить, [E] Выход')
                    pressed_key = getch().lower()
                    if ord(pressed_key) == ord('n'):
                        print()
                        break
                    elif ord(pressed_key) == ord('e'):
                        main_menu()
                    else:
                        console.print('\n[red]Команда некорректна или не существует![/]\n')

main()
