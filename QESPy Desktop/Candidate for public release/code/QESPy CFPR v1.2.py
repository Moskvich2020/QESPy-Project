
#* ╭─────────────────────────────────╮
#* │ Name: QESPy CFPR                │ 
#* │ Version: 1.2                    │ 
#* │ Build: 16032024                 │ 
#* │ Build Date: 16-03-2024 8:30 PM  │ 
#* │ Author: Moskvich2020            │ 
#* │ License: BSD 3-Clause License   │ 
#* ╰─────────────────────────────────╯

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


def main(): #* main
    '''
    Функция main является точкой входа в данной программе.

    Описание:
        1.Очищает консоль.
        2. Выводит интерфейс командной строки программы QESPy Desktop и после
        полусекундной задержки вызывает функцию main_menu - главное меню
        программы.

    '''
    clear()
    print('Quadratic Equation Solver in Python CFPR [Version 1.2]')
    print('(c) Cristi Constantin (Moskvich2020) QESPy Project. Все права защищены.')
    sleep(0.5)
    main_menu()


def main_menu(): #* Главное меню
    '''
    Функция main_menu отвечает за пользовательский интерфейс главного меню и
    выбор опций.

    Описание:
        1. Очищает консоль.
        2. Выводит главное меню программы.
        3. Содержит цикл while с функцией getch для отслеживания нажатой
        клавиши для выбора опции.
        4. Имеет 7 опций:
            a. Решение квадратного уравнения (ax²+bx+c=0);
            b. Решение биквадратного уравнения (ax⁴+bx²+c=0);
            c. Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂));
            d. Терминал;
            e. Настройки;
            f. Справка;
            g. Выйти из программы.

    '''
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
[2]    Решение биквадратного уравнения (ax⁴+bx²+c=0)
[3]    Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))
[4]    Терминал
[5]    Настройки
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
            solving_a_quadratic_equation()
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


def solving_a_quadratic_equation(): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0)
    '''
    Функция solving_a_quadratic_equation отвечает за решение всех видов
    квадратного уравнения.

    Описание:
        1. Очищает консоль.
        2. Выводит заголовок опции.
        3. Вызывает функцию reading_coefficients для считывания коэффициентов. 

    Вложенные функции:
        reading_coefficients: считывание коэффициентов 
        solving_a_quadratic_equation_1: решение линейного уравнения вида bx+c=0
        solving_a_quadratic_equation_2: решение неполного квадратного уравнения вида ax²+c=0
        solving_a_quadratic_equation_3: решение неполного квадратного уравнения вида ax²+bx=0
        solving_a_quadratic_equation_4: решение равенства вида c=0
        solving_a_quadratic_equation_5: решение линейного уравнения вида bx=0
        solving_a_quadratic_equation_6: решение неполного квадратного уравнения вида ax²=0
        solving_a_quadratic_equation_7: решение равенства вида 0=0
        solving_a_quadratic_equation_8: решение приведённого квадратного уравнения вида x²+px+q=0
        solving_a_quadratic_equation_9: решение квадратного уравнения вида ax²+bx+c=0

    '''
    clear()
    console.print(Panel(Text(text='Решение квадратного уравнения (ax²+bx+c=0)', justify='center'), title='Опция №1'))

    def reading_coefficients():
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
                    console.print('[italic red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
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
                    console.print('[italic red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
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
                    console.print('[italic red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')

            if not coefficient_a and coefficient_b != 0 and coefficient_c != 0:
                solving_a_quadratic_equation_1(coefficient_b, coefficient_c)
            elif coefficient_a != 0 and not coefficient_b and coefficient_c != 0:
                solving_a_quadratic_equation_2(coefficient_a, coefficient_c)
            elif coefficient_a != 0 and coefficient_b != 0 and not coefficient_c:
                solving_a_quadratic_equation_3(coefficient_a, coefficient_b)
            elif not coefficient_a and not coefficient_b and (coefficient_c != 0 or not coefficient_c):
                solving_a_quadratic_equation_4(coefficient_c)
            elif not coefficient_a and coefficient_b != 0 and not coefficient_c:
                solving_a_quadratic_equation_5(coefficient_b)
            elif coefficient_a != 0 and not coefficient_b and not coefficient_c:
                solving_a_quadratic_equation_6(coefficient_a)
            elif abs(coefficient_a) == 1 and coefficient_b != 0 and coefficient_c != 0:
                solving_a_quadratic_equation_7(coefficient_a, coefficient_b, coefficient_c)
            else:
                solving_a_quadratic_equation_8(coefficient_a, coefficient_b, coefficient_c)

    def solving_a_quadratic_equation_1(coefficient_b, coefficient_c): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx+c=0 | a = 0
        '''
        Функция solving_a_quadratic_equation_1 отвечает за решениел инейного
        уравнения вида bx+c=0.

        Описание:
            1. Принимает аргументы.
            2. Находит решения.
            3. Генерирует строки для вывода решения в зависимости от коэффициентов.
            4. Выводит решение.
            5. Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_b: коэффициент b
            coefficient_c: коэффициент c

        Внутренние переменные:
            solution_x: корень уравнения
            coef_b_str: форматированный коэффициент b для вывода в строке с "Дано"
            coef_c_str: форматированный коэффициент c для вывода в строке с "Дано"
            sol_x_str: форматированный корень уравнения для вывода в строке с ответом
            coef_b_sol: форматированный коэффициент b для вывода данных в блоке решения
            coef_c_sol_1: форматированный коэффициент c для вывода данных в блоке решения
            auxiliary_line_sol_1: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_2: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_3: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol: вспомогательная строка для вывода данных в блоке решения,
                                определяющая дальнейшее действие в зависимости от модуля
                                коэффициента b
            sol_x_sol: вспомогательная строка для вывода ответа в блоке решения

        Алгоритм решения:
            bx+c=0
            │└ |b| ≠ 1
            │  bx=-c
            │  bx=-c |÷b
            │  x=-c/b
            └─ |b| = 1
                x=-c

        '''
        solution_x = -(coefficient_c/coefficient_b)

        coef_b_str = f'{coefficient_b}x' if abs(coefficient_b) != 1 else ('x' if coefficient_b == 1 else '-x')
        coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
        sol_x_str = f'{int(solution_x)}' if solution_x.is_integer() else f'{solution_x:.2f}'
        coef_b_sol = f'{coefficient_b}x' if abs(coefficient_b) != 1 else ('x' if coefficient_b == 1 else '-x')
        coef_c_sol = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
        auxiliary_line_sol_1 = f'\n              x = -({coefficient_c} / {coefficient_b})' if coefficient_b > 0 and coefficient_c > 0 else (f'\n              x = {coefficient_c} / {-coefficient_b}' if coefficient_b < 0 and coefficient_c > 0 else (f'\n              x = {-coefficient_c} / {coefficient_b}' if coefficient_b > 0 and coefficient_c < 0 else f'\n              x = -({-coefficient_c} / {-coefficient_b})'))
        auxiliary_line_sol_2 = f'\n              x = {coefficient_c}' if coefficient_b < 0 and coefficient_c > 0 else (f'\n              x = {coefficient_c}' if coefficient_b < 0 and coefficient_c < 0 else '')
        auxiliary_line_sol_3 = f'\n              {coef_b_sol} = {-coefficient_c} | ÷ {coefficient_b}{auxiliary_line_sol_1}' if coefficient_b > 0 else f'\n              {coef_b_sol} = {-coefficient_c} | ÷ ({coefficient_b}){auxiliary_line_sol_1}'
        auxiliary_line_sol = f'{coef_b_sol} = {-coefficient_c}{auxiliary_line_sol_3}' if abs(coefficient_b) != 1 else f'{coef_b_sol} = {-coefficient_c}{auxiliary_line_sol_2}'
        sol_x_sol = f'{int(solution_x)}' if solution_x.is_integer() == True else f'{solution_x:.2f}'
        
        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято линейное уравнение вида bx+c=0        ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coef_b_str}{coef_c_str} = 0')
        print(f'   Решение:   {coef_b_sol}{coef_c_sol} = 0')
        print(f'              {auxiliary_line_sol}')
        print(f'              x = {sol_x_sol}')
        print(f'   Ответ:     x = {sol_x_str}')
        print('   ──────────────────────────────────────────────')
        print()
        console.print('[italic]Примечание: данное уравнение не является квадратным, а линейным (первой степени), так как наивысшая степень этого уравнения равна 1.[/]')
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

    def solving_a_quadratic_equation_2(coefficient_a, coefficient_c): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+c=0 | b = 0
        '''
        Функция solving_a_quadratic_equation_2 отвечает за решение неполного
        квадратного уравнения вида ax²+c=0.

        Описание:
            1. Принимает аргументы.
            2. Проверяет существуют ли решения. Находит их, если они есть.
            3. Генерирует строки для вывода решения в зависимости от коэффициентов.
            4. Выводит решение.
            5. Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a
            coefficient_c: коэффициент c

        Внутренние переменные:
            |a| ≠ 1:
                solution_x1: корень уравнения №1
                solution_x2: корень уравнения №2
                coef_a_str: форматированный коэффициент a для вывода в строке "Дано"
                coef_c_str: форматированный коэффициент c для вывода в строке "Дано"
                sol_x1_str: форматированный корень №1 уравнения для вывода в строке с ответом
                sol_x2_str: форматированный корень №2 уравнения для вывода в строке с ответом
                coef_a_sol_1: форматированный коэффициент a для вывода данных в блоке решения
                coef_c_sol_1: форматированный коэффициент c для вывода данных в блоке решения
                coef_c_sol_2: форматированный коэффициент c для вывода данных в блоке решения
                auxiliary_line_sol_1: вспомогательная строка для вывода данных в блоке решения
                auxiliary_line_sol_2: вспомогательная строка для вывода данных в блоке решения
                auxiliary_line_sol_3: вспомогательная строка для вывода данных в блоке решения
                auxiliary_line_sol: вспомогательная строка для вывода данных в блоке решения,
                                    определяющая дальнейшее действие в зависимости от модуля
                                    коэффициента a
                sol_x1_sol: вспомогательная строка для вывода корня №1 в блоке решения
                sol_x2_sol: вспомогательная строка для вывода корня №2 в блоке решения

            |a| = 1:
                solution_x: корень уравнения
                coef_a_str: форматированный коэффициент a для вывода в строке "Дано"
                coef_c_str: форматированный коэффициент c для вывода в строке "Дано"
                coef_a_sol: форматированный коэффициент a для вывода данных в блоке решения
                coef_c_sol: форматированный коэффициент c для вывода данных в блоке решения

        Алгоритм решения:
            ax²+c=0
            │└ c/a < 0
            │  │└ |a| ≠ 1
            │  │  ax²=-c
            │  │  ax²=-c | ÷ a
            │  │  x²=-(c/a)
            │  │  x=±√(-(c/a))
            │  └─ |a| = 1
            │     x²=-c
            │     x=±√(-c)
            └─ Уравнение не имеет решений!

        '''
        if (coefficient_c/coefficient_a) < 0:
            solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
            solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            sol_x1_str = f'{int(solution_x1)}' if solution_x1.is_integer() else f'{solution_x1:.2f}'
            sol_x2_str = f'{int(solution_x2)}' if solution_x1.is_integer() else f'{solution_x2:.2f}'
            coef_a_sol_1 = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_c_sol_1 = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_c_sol_2 = f'{-coefficient_c}' if coefficient_c < 0 else f'({-coefficient_c})'
            auxiliary_line_sol_1 = f'\n              x = ±√({coefficient_c} / {-coefficient_a})' if coefficient_a < 0 else f'\n              x = ±√({-coefficient_c} / {coefficient_a})'
            auxiliary_line_sol_2 = f'\n              x² = {coefficient_c} / {-coefficient_a}{auxiliary_line_sol_1}' if coefficient_a < 0 else f'\n              x² = {-coefficient_c} / {coefficient_a}{auxiliary_line_sol_1}'
            auxiliary_line_sol_3 = f'\n              {coef_a_sol_1} = {-coefficient_c} | ÷ {coefficient_a}{auxiliary_line_sol_2}' if coefficient_a > 0 else f'\n              {coef_a_sol_1} = {-coefficient_c} | ÷ ({coefficient_a}){auxiliary_line_sol_2}'
            auxiliary_line_sol = f'{coef_a_sol_1} = {-coefficient_c}{auxiliary_line_sol_3}' if abs(coefficient_a) != 1 else f'x² = ±{coef_c_sol_2}\n              x = ±√{coef_c_sol_2}'
            sol_x1_sol = f'{int(solution_x1)}' if solution_x1.is_integer() else f'{solution_x1:.2f}'
            sol_x2_sol = f'{int(solution_x2)}' if solution_x1.is_integer() else f'{solution_x2:.2f}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+c=0     ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_c_str} = 0')
            print(f'   Решение:   {coef_a_sol_1}{coef_c_sol_1} = 0')
            print(f'              {auxiliary_line_sol}')
            print(f'              x₁ = {sol_x1_sol}')
            print(f'              x₂ = {sol_x2_sol}')
            print(f'   Ответ:     x₁ = {sol_x1_str}')
            print(f'              x₂ = {sol_x2_str}')
            print('   ──────────────────────────────────────────────')
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
            solution_x = 'Уравнение не имеет решений!'

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_a_sol = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_c_sol = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+c=0     ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_c_str} = 0')
            print(f'   Решение:   {coef_a_sol}{coef_c_sol} = 0')
            print(f'              {coefficient_c} / {coefficient_a} > 0')
            print(f'   Ответ:     {solution_x}')
            print('   ──────────────────────────────────────────────')
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

    def solving_a_quadratic_equation_3(coefficient_a, coefficient_b): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx=0 | c = 0
        '''
        Функция solving_a_quadratic_equation_3 отвечает за решение неполного
        квадратного уравнения вида ax²+bx=0.

        Описание:
            1. Принимает аргументы.
            2. Находит решения.
            3. Генерирует строки для вывода решения в зависимости от коэффициентов.
            4. Выводит решение.
            5. Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a
            coefficient_b: коэффициент b

        Внутренние переменные:
            solution_x1: корень уравнения №1
            solution_x2: корень уравнения №2
            coef_a_str: форматированный коэффициент a для вывода в строке "Дано"
            coef_b_str: форматированный коэффициент b для вывода в строке "Дано"
            sol_x1_str: форматированный корень №1 уравнения для вывода в строке с ответом
            sol_x2_str: форматированный корень №2 уравнения для вывода в строке с ответом
            coef_a_sol_1: форматированный коэффициент a для вывода данных в блоке решения
            coef_a_sol_2: форматированный коэффициент a для вывода данных в блоке решения
            coef_b_sol_1: форматированный коэффициент b для вывода данных в блоке решения
            coef_b_sol_2: форматированный коэффициент b для вывода данных в блоке решения
            auxiliary_line_sol_1: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_2: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_3: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol: вспомогательная строка для вывода данных в блоке решения,
                                определяющая дальнейшее действие в зависимости от модуля
                                коэффициента a
            sol_x1_sol: вспомогательная строка для вывода корня №1 в блоке решения

        Алгоритм решения:
            ax²+bx=0
            │└ |a| ≠ 1
            │  ax²+bx=0
            │  x(ax+b)=0
            │  x₁=0
            │  x₂=ax+b=0
            │  x₂=ax=-b
            │  x₂=-b/a
            └─ |a| = 1
                x²+bx=0
                x(x+b)=0
                x₁=0
                x₂=x+b=0
                x₂=x=-b
                x₂=-b

        '''
        solution_x1 = 0
        solution_x2 = -(coefficient_b/coefficient_a)

        coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
        coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else (' + x' if coefficient_b == 1 else ' - x'))
        sol_x1_str = f'{solution_x1}'
        sol_x2_str = f'{int(solution_x2)}' if solution_x2.is_integer() else f'{solution_x2:.2f}'
        coef_a_sol_1 = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
        coef_a_sol_2 = f'{coefficient_a}x' if abs(coefficient_a) != 1 else ('x' if coefficient_a == 1 else '-x')
        coef_b_sol_1 = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else (' + x' if coefficient_b == 1 else ' - x'))
        coef_b_sol_2 = f' + {coefficient_b}' if coefficient_b > 0 else f' - {-coefficient_b}'
        auxiliary_line_sol_1 = f'\n              x₂ = {int(solution_x2)}' if solution_x2.is_integer() else f'\n              x₂ = {solution_x2:.2f}'
        auxiliary_line_sol_2 = f'\n              x₂ = {-coefficient_b} / {coefficient_a}{auxiliary_line_sol_1}'
        auxiliary_line_sol_3 = f'\n              x₂ = {coef_a_sol_2} = {-coefficient_b} | ÷ {coefficient_a}{auxiliary_line_sol_2}' if coefficient_a > 0 else f'\n              x₂ = {coef_a_sol_2} = {-coefficient_b} | ÷ ({coefficient_a}){auxiliary_line_sol_2}'
        auxiliary_line_sol = f'x₂ = {coef_a_sol_2} = {-coefficient_b}{auxiliary_line_sol_3}' if abs(coefficient_a) != 1 else (f'x₂ = {-coefficient_b}' if coefficient_a > 0 else f'x₂ = {coefficient_b}')
        sol_x1_sol = f'{solution_x1}'

        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято квадратное уравнение вида ax²+bx=0    ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coef_a_str}{coef_b_str} = 0')
        print(f'   Решение:   {coef_a_sol_1}{coef_b_sol_1} = 0')
        print(f'              x({coef_a_sol_2}{coef_b_sol_2}) = 0')
        print(f'              x₁ = {sol_x1_sol}')
        print(f'              x₂ = {coef_a_sol_2}{coef_b_sol_2} = 0')
        print(f'              {auxiliary_line_sol}')
        print(f'   Ответ:     x₁ = {sol_x1_str}')
        print(f'              x₂ = {sol_x2_str}')
        print('   ──────────────────────────────────────────────')
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

    def solving_a_quadratic_equation_4(coefficient_c): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c=0 | a и b = 0
        '''
        Функция solving_a_quadratic_equation_4 отвечает за решение равенства
        (линейного уравнения) вида c=0.

        Описание:
            1. Принимает аргумент.
            2. Проверяет равен ли коэффициент c нулю и в зависимости от этого
                определяет истинность равенства.
            3. Выводит решение.
            4. Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_c: коэффициент c

        Внутренние переменные:
            solution_x: корень уравнения

        Алгоритм решения:
            c=0
            │└ c≠0
            │  x∈∅
            └─ c=0
                x∈R

        '''
        if coefficient_c != 0:
            solution_x = 'Пустое множество!'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято линейное уравнение вида c=0           ')
            print('   ──────────────────────────────────────────────')
            print(f'   Ошибка! "{coefficient_c} = 0".')
            print('   Данное выражение не имеет смысла!')
            print(f'   Ответ: {solution_x}')
            print('   ──────────────────────────────────────────────')
            print()
            console.print('[italic]Примечание: данное равенство не является уравнением, так как содержит одну неизвестнную величину и очевидно.[/]')
            console.print('[italic]В данном случае, равенство c = 0 ложно, так как c ≠ 0.[/]')
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
            solution_x = 'x может быть любым числом.'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида 0=0         ')
            print('   ──────────────────────────────────────────────')
            print('   Дано:      0 = 0')
            print('   Решение:   x принадлежит R')
            print(f'   Ответ:     {solution_x}')
            print('   ──────────────────────────────────────────────')
            print()
            console.print('[italic]Примечание: данное равенство не является уравнением и очевидно, так как не содержит неизвестных величин и тривиально.[/]')
            console.print('[italic]В данном случае, равенство 0 = 0 верно и является интуитивно понятным и формально обоснованным утверждением, но с другой стороны не имеет смысла.[/]')
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

    def solving_a_quadratic_equation_5(coefficient_b): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx=0 | a и c = 0
        '''
        Функция solving_a_quadratic_equation_5 отвечает за решение линейного
        уравнения вида bx=0.

        Описание:
            1. Принимает аргумент.
            2. Выводит решение.
            3. Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_b: коэффициент b

        Внутренние переменные:
            solution_x: корень уравнения

        Алгоритм решения:
            0=0

        '''
        solution_x = 0

        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято линейное уравнение вида bx=0          ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coefficient_b}x = 0')
        print(f'   Решение:   x = {solution_x}')
        print(f'   Ответ:     x = {solution_x}')
        print('   ──────────────────────────────────────────────')
        print()
        console.print('[italic]Примечание: данное уравнение не является квадратным, а линейным (первой степени), так как наивысшая степень этого уравнения 1.[/]')
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
    
    def solving_a_quadratic_equation_6(coefficient_a): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²=0 | b и c = 0
        '''
        Функция solving_a_quadratic_equation_6 отвечает за решение неполного
        квадратного уравнения вида ax²=0

        Описание:
            1. Принимает аргумент.
            2. Выводит решения.
            3. Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a

        Внутренние переменные:
            solution_x: корень уравнения
            auxiliary_line_sol: вспомогательная строка для вывода данных в блоке
            решения

        Алгоритм решения:
            ax²=0
            ax²=0 | ÷ a
            x²=0
            x=√0
            x=0

        '''
        solution_x = 0

        auxiliary_line_sol = f'{coefficient_a}x² = 0 | ÷ {coefficient_a}' if coefficient_a > 0 else f'{coefficient_a}x² = 0 | ÷ ({coefficient_a})'

        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято квадратное уравнение вида ax²=0       ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coefficient_a}x² = 0')
        print(f'   Решение:   {coefficient_a}x² = 0')
        print(f'              {auxiliary_line_sol}')
        print('              x² = 0')
        print('              x = √0')
        print('              x = 0')
        print(f'   Ответ:     x = {solution_x}')
        print('   ──────────────────────────────────────────────')
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
    
    def solving_a_quadratic_equation_7(coefficient_a, coefficient_b, coefficient_c):  #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > x²+px+q=0 | a = 1, b и c ≠ 0 
        reduced_discriminant = coefficient_b**2 / 4 - coefficient_c

        x_str = 'x²' if coefficient_a > 0 else '-x²'
        coef_p_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
        coef_q_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
        coef_p_red_dis = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
        coef_q_red_dis = f' - {coefficient_c}' if coefficient_c > 0 else f' + {-coefficient_c}'
        coef_p_sol = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
        coef_q_sol = f' - {coefficient_c}' if coefficient_c > 0 else f' + {-coefficient_c}'

        if reduced_discriminant > 0:
            solution_x1 = -coefficient_b / 2 + (coefficient_b**2 / 4 - coefficient_c)**(1/2)
            solution_x2 = -coefficient_b / 2 - (coefficient_b**2 / 4 - coefficient_c)**(1/2)
            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида x²+px+q=0   ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {x_str}{coef_p_str}{coef_q_str} = 0')
            print(f'   Решение:   D = {coef_p_red_dis}² / 4{coef_q_red_dis}')
            print(f'              D = {coefficient_b**2:.2f} / 4{coef_q_red_dis}')
            print(f'              D = {coefficient_b**2 / 4:.2f}{coef_q_red_dis}')
            print(f'              D = {reduced_discriminant:.2f}')
            print(f'              x = -({coefficient_b} / 2) ± √({coef_p_sol}² / 4{coef_q_sol})')
            print(f'              x = {-coefficient_b / 2:.2f} ± √({coefficient_b**2:.2f} / 4{coef_q_sol})')
            print(f'              x = {-coefficient_b / 2:.2f} ± √({coefficient_b**2 / 4:.2f}{coef_q_sol})')
            print(f'              x = {-coefficient_b / 2:.2f} ± √{reduced_discriminant}')
            print(f'   Ответ:     x₁ = {solution_x1:.2f}')
            print(f'              x₂ = {solution_x2:.2f}')
            print('   ──────────────────────────────────────────────')
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
        elif not reduced_discriminant:
            solution_x = -coefficient_b / 2
            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида x²+px+q=0   ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {x_str}{coef_p_str}{coef_q_str} = 0')
            print(f'   Решение:   D = {coef_p_red_dis}² / 4{coef_q_red_dis}')
            print(f'              D = {coefficient_b**2:.2f} / 4{coef_q_red_dis}')
            print(f'              D = {coefficient_b**2 / 4:.2f}{coef_q_red_dis}')
            print(f'              D = {reduced_discriminant:.2f}')
            print(f'              x = -({coefficient_b} / 2)')
            print(f'   Ответ:     x = {solution_x:.2f}')
            print('   ──────────────────────────────────────────────')
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
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида x²+px+q=0   ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {x_str}{coef_p_str}{coef_q_str} = 0')
            print(f'   Решение:   D = {coef_p_red_dis}² / 4{coef_q_red_dis}')
            print(f'              D = {coefficient_b**2:.2f} / 4{coef_q_red_dis}')
            print(f'              D = {coefficient_b**2 / 4:.2f}{coef_q_red_dis}')
            print(f'              D = {reduced_discriminant:.2f}')
            print('   Ответ:     Уравнение не имеет решений!')
            print('   ──────────────────────────────────────────────')
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
    
    def solving_a_quadratic_equation_8(coefficient_a, coefficient_b, coefficient_c): #* Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx+c=0 | a и b и c ≠ 0 
        discriminant = coefficient_b**2 - 4*coefficient_a*coefficient_c

        coef_a_str = f'{coefficient_a}x²'
        coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
        coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
        coef_a_dis = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
        coef_b_dis = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
        coef_c_dis = f'{coefficient_c}' if coefficient_c > 0 else f'({coefficient_c})'
        a_c_dis = f' - {4 * coefficient_a * coefficient_c:.2f}' if 4 * coefficient_a * coefficient_c > 0 else f' + {abs(4*coefficient_a*coefficient_c):.2f}'
        coef_a_sol = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
        coef_b_sol_1 = f'(-{coefficient_b}' if coefficient_b > 0 else f'(-({coefficient_b})'
        coef_b_sol_2 = f'(-{coefficient_b}' if coefficient_b > 0 else f'({-coefficient_b}'
        dis_sol = f'√{discriminant:.2f})' if discriminant > 0 else f'√({discriminant:.2f}))'

        if discriminant > 0:
            solution_x1 = (-coefficient_b + discriminant**(1/2)) / (2*coefficient_a)
            solution_x2 = (-coefficient_b - discriminant**(1/2)) / (2*coefficient_a)
            print()
            print('   ─────────────────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+bx+c=0  ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
            print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
            print(f'              D = {discriminant:.2f}')
            print(f'              x = {coef_b_sol_1} ± {dis_sol} / (2 × {coef_a_sol})')
            print(f'              x = {coef_b_sol_2} ± {discriminant**(1/2):.2f}) / ({2*coefficient_a:.2f})')
            print(f'   Ответ:     x₁ = {solution_x1:.2f}')
            print(f'              x₂ = {solution_x2:.2f}')
            print('   ──────────────────────────────────────────────')
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
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+bx+c=0  ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
            print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
            print(f'              D = {discriminant:.2f}')
            print(f'              x = {coef_b_sol_1}) / ( 2 × {coef_a_sol})')
            print(f'              x = {coef_b_sol_2}) / ({2*coef_a_sol})')
            print(f'   Ответ:     x = {solution_x:.2f}')
            print('   ──────────────────────────────────────────────')
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
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+bx+c=0  ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
            print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
            print(f'              D = {discriminant:.2f}')
            print('   Ответ:     Уравнение не имеет решений!')
            print('   ──────────────────────────────────────────────')
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
    
    reading_coefficients()


if __name__ == '__main__':
    main()
