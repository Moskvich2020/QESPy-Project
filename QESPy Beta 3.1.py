# ╭─────────────────────────────────╮
# │ QESPy Beta 3.1 [build 25122023] │ 
# ╰─────────────────────────────────╯

import os
import time


clear = lambda: os.system('cls')


def main(): # main
    clear()
    print('Quadratic Equation Solver in Python [Version 3.1.7b]')
    print('(c) Moskvich2020 (QESPy Project). Все права защищены.')
    print()
    time.sleep(0.5)
    main_menu()


def main_menu(): # Главное меню
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Добро пожаловать в QESPy Beta 3.1!                                                                            ')
    print('         Программа готова к решению всех видов квадратных уравнений!                                                   ')
    print('         ──────────────────────────────────────────────────────────────────────────────────────────────────────        ')
    print('               Выберете опцию:                                                                                         ')
    print('         [1] Решение квадратного уравнения (ax²+bx+c=0)                                                                ')
    print('         [2] Решение биквадратного уравнения (ax⁴+bx²+c=0)                                                             ')
    print('         [3] Разложение квадратного уравнения (ax²+bx+c=0)                                                             ')
    print('         [4] Терминал                                                                                                  ')
    print('         [5] Справка                                                                                                   ')
    print('         [E] Выход                                                                                                     ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('      Пожалуйста, введите номер опции из меню [1, 2, 3, 4, 5, E]...                                                    ')
    print()
    while True:
        cmd = input('> ').lower()
        if cmd == '1':
            solving_a_quadratic_equation()
        elif cmd == '2':
            solving_a_biquadratic_equation()
        elif cmd == '3':
            expansion_of_a_quadratic_equation()
        elif cmd == '4':
            terminal()
        elif cmd == '5':
            reference()
        elif cmd == 'e':
            quit()
        else:
            print()
            print('Команда некорректна или не существует!')
            print()


def solving_a_quadratic_equation(): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0)
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Решение квадратного уравнения (ax²+bx+c=0)                                                             ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        try:
            coefficient_a = int(input('   Введите a: '))
            coefficient_b = int(input('   Введите b: '))
            coefficient_c = int(input('   Введите c: '))
        except ValueError:
            print()
            print('Ошибка! Какой-то коэффициент является десятичной дробью или не является числом! Введите, пожалуйста, ещё раз числа!')
            print('Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со')
            print('значением не более 1000.')
            print()
        else:
            if not coefficient_a and coefficient_b != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx+c=0 | a = 0
                solution_x = -(coefficient_c/coefficient_b)
                if coefficient_b > 0 and coefficient_c > 0:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида bx+c=0      ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_b}x + {coefficient_c} = 0')
                    print(f'   Решение:   {coefficient_b}x + {coefficient_c} = 0')
                    print(f'              {coefficient_b}x = -{coefficient_c}')
                    print(f'              x = -{coefficient_c}/{coefficient_b}')
                    print(f'              x = -({coefficient_c}/{coefficient_b})')
                    print(f'   Ответ:     x = {solution_x:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif coefficient_b < 0 and coefficient_c > 0:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида bx+c=0      ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_b}x + {coefficient_c} = 0')
                    print(f'   Решение:   {coefficient_b}x + {coefficient_c} = 0')
                    print(f'              {coefficient_b}x = -{coefficient_c}')
                    print(f'              {-coefficient_b}x = {coefficient_c}')
                    print(f'              x = {coefficient_c}/{-coefficient_b}')
                    print(f'   Ответ:     x = {solution_x:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif coefficient_b > 0 and coefficient_c < 0:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида bx+c=0      ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_b}x - {-coefficient_c} = 0')
                    print(f'   Решение:   {coefficient_b}x - {-coefficient_c} = 0')
                    print(f'              {coefficient_b}x = {-coefficient_c}')
                    print(f'              x = {-coefficient_c}/{coefficient_b}')
                    print(f'   Ответ:     x = {solution_x:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                else:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида bx+c=0      ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_b}x - {-coefficient_c} = 0')
                    print(f'   Решение:   {coefficient_b}x - {-coefficient_c} = 0')
                    print(f'              {coefficient_b}x = {-coefficient_c}')
                    print(f'              x = {-coefficient_c}/{coefficient_b}')
                    print(f'              x = -({-coefficient_c}/{-coefficient_b})')
                    print(f'   Ответ:     x = {solution_x:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
            elif coefficient_a != 0 and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+c=0 | b = 0
                if (coefficient_c/coefficient_a) < 0:
                    solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
                    solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)
                    if coefficient_a > 0 and coefficient_c < 0:
                        print()
                        print('   ───────────────────────────────────')
                        print('   Принято уравнение вида ax²+c=0     ')
                        print('   ───────────────────────────────────')
                        print(f'   Дано:      {coefficient_a}x² - {-coefficient_c} = 0')
                        print(f'   Решение:   {coefficient_a}x² - {-coefficient_c} = 0')
                        print(f'              {coefficient_a}x² = {-coefficient_c}')
                        print(f'              x² = ±({-coefficient_c}/{coefficient_a})')
                        print(f'              x = ±√({-coefficient_c}/{coefficient_a})')
                        print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                        print(f'              x₂ = {solution_x2:.2f}')
                        print('   ───────────────────────────────────')
                        print()
                        time.sleep(1)
                        while True:
                            cmd = input('[N] Продолжить, [E] Выход > ').lower()
                            if cmd == 'n':
                                print()
                                break
                            elif cmd == 'e':
                                main_menu()
                            else:
                                print()
                                print('Команда некорректна или не существует!')
                                print()
                    if coefficient_a < 0 and coefficient_c > 0:
                        print()
                        print('   ───────────────────────────────────')
                        print('   Принято уравнение вида ax²+c=0     ')
                        print('   ───────────────────────────────────')
                        print(f'   Дано:      {coefficient_a}x² + {coefficient_c} = 0')
                        print(f'   Решение:   {coefficient_a}x² + {coefficient_c} = 0')
                        print(f'              {coefficient_a}x² = -{coefficient_c}')
                        print(f'              {-coefficient_a}x² = {coefficient_c}')
                        print(f'              x² = ±({coefficient_c}/{-coefficient_a})')
                        print(f'              x = ±√({coefficient_c}/{-coefficient_a})')
                        print(f'   Ответ:     x₁ = {solution_x1:.2f};')
                        print(f'              x₂ = {solution_x2:.2f}.')
                        print('   ───────────────────────────────────')
                        print()
                        time.sleep(1)
                        while True:
                            cmd = input('[N] Продолжить, [E] Выход > ').lower()
                            if cmd == 'n':
                                print()
                                break
                            elif cmd == 'e':
                                main_menu()
                            else:
                                print()
                                print('Команда некорректна или не существует!')
                                print()
                else:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+c=0     ')
                    print('   ───────────────────────────────────')
                    print('   Уравнение не имеет решений!        ')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
            elif coefficient_a != 0 and coefficient_b != 0 and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx=0 | c = 0
                solution_x1 = 0
                solution_x2 = -(coefficient_b/coefficient_a)
                if coefficient_a > 0 and coefficient_b > 0:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+bx=0    ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_a}x² + {coefficient_b}x = 0')
                    print(f'   Решение:   {coefficient_a}x² + {coefficient_b}x = 0')
                    print(f'              x({coefficient_a}x + {coefficient_b}) = 0')
                    print(f'              x₁ = 0')
                    print(f'              x₂ = {coefficient_a}x + {coefficient_b} = 0')
                    print(f'              x₂ = {coefficient_a}x = -{coefficient_b}')
                    print(f'              x₂ = -{coefficient_b}/{coefficient_a}')
                    print(f'              x₂ = -({coefficient_b}/{coefficient_a})')
                    print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                    print(f'              x₂ = {solution_x2:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif coefficient_a < 0 and coefficient_b > 0:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+bx=0    ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:    {coefficient_a}x² + {coefficient_b}x = 0')
                    print(f'   Решение: {coefficient_a}x² + {coefficient_b}x = 0')
                    print(f'            x({coefficient_a}x + {coefficient_b}) = 0')
                    print(f'            x₁ = 0')
                    print(f'            x₂ = {coefficient_a}x + {coefficient_b} = 0')
                    print(f'            x₂ = {coefficient_a}x = -{coefficient_b}')
                    print(f'            x₂ = -{coefficient_b}/{coefficient_a}.')
                    print(f'   Ответ:   x₁ = {solution_x1:.2f};')
                    print(f'            x₂ = {solution_x2:.2f}.')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif coefficient_a > 0 and coefficient_b < 0:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+bx=0    ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_a}x² - {-coefficient_b}x = 0')
                    print(f'   Решение:   {coefficient_a}x² - {-coefficient_b}x = 0')
                    print(f'              x({coefficient_a}x - {coefficient_b}) = 0')
                    print(f'              x₁ = 0')
                    print(f'              x₂ = {coefficient_a}x - {-coefficient_b} = 0')
                    print(f'              x₂ = {coefficient_a}x = {-coefficient_b}')
                    print(f'              x₂ = {-coefficient_b}/{coefficient_a}')
                    print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                    print(f'              x₂ = {solution_x2:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                else:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+bx=0    ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coefficient_a}x² - {-coefficient_b}x = 0')
                    print(f'   Решение:   {coefficient_a}x² - {coefficient_b}x = 0')
                    print(f'              x({coefficient_a}x - {-coefficient_b}) = 0')
                    print(f'              x₁ = 0')
                    print(f'              x₂ = {coefficient_a}x - {-coefficient_b} = 0')
                    print(f'              x₂ = {coefficient_a}x = {-coefficient_b}')
                    print(f'              x₂ = {-coefficient_b}/{coefficient_a}')
                    print(f'              x₂ = -({-coefficient_b}/{-coefficient_a})')
                    print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                    print(f'              x₂ = {solution_x2:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
            elif not coefficient_a and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c=0 | a и b = 0
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида c=0         ')
                print('   ───────────────────────────────────')
                print(f'   Ошибка! "{coefficient_c:.0f} = 0". Данное выражение не имеет смысла!')
                print('   Ответ: Пустое множество')
                print('   ───────────────────────────────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()
            elif not coefficient_a and coefficient_b != 0 and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx=0 | a и c = 0
                solution_x = 0
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида bx=0        ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coefficient_b}x = 0')
                print(f'   Решение:   x = {solution_x}')
                print(f'   Ответ:     x = {solution_x:.0f}')
                print('   ───────────────────────────────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()
            elif coefficient_a != 0 and not coefficient_b and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²=0 | b и c = 0
                solution_x1 = 0
                solution_x2 = 0
                print()
                print('   ───────────────────────────────────')
                print('   Принято уравнение вида ax²=0       ')
                print('   ───────────────────────────────────')
                print(f'   Дано:      {coefficient_a}x² = 0')
                print(f'   Решение:   x = {solution_x}')
                print(f'   Ответ:     x = {solution_x}')
                print('   ───────────────────────────────────')
                print()                
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()
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
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()
            elif coefficient_a != 0 and coefficient_b !=0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > Discriminant
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
                    print(f'   Решение:   D = {coef_b_dis}² - 4×{coef_a_dis}×{coef_c_dis}')
                    print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                    print(f'              D = {discriminant:.2f}')
                    print(f'              x = {coef_b_sol_1} ± {dis_sol}/(2×{coef_a_sol})')
                    print(f'              x = {coef_b_sol_2} ± {discriminant**(1/2):.2f})/({2*coefficient_a:.2f})')
                    print(f'   Ответ:     x₁ = {solution_x1:.2f}')
                    print(f'              x₂ = {solution_x2:.2f}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif not discriminant:
                    solution_x = -((coefficient_b) / (2*coefficient_a))
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+bx+c=0  ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                    print(f'   Решение:   D = {coef_b_dis}² - 4×{coef_a_dis}×{coef_c_dis}')
                    print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                    print(f'              D = {discriminant:.2f}')
                    print(f'              x = {coef_b_sol_1})/(2×{coef_a_sol})')
                    print(f'              x = {coef_b_sol_2})/({2*coef_a_sol})')
                    print(f'   Ответ:     x = {solution_x:.2f}')
                    print('   ───────────────────────────────────')
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                else:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax²+bx+c=0  ')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                    print(f'   Решение:   D = {coef_b_dis}² - 4×{coef_a_dis}×{coef_c_dis}')
                    print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                    print(f'              D = {discriminant:.2f}')
                    print('   Ответ:     Уравнение не имеет решений!')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
            else:
                print()
                print('Внимание! Произошла неизвестная синтаксическая/логическая ошибка.')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()


def solving_a_biquadratic_equation(): # Главное меню > Решение биквадратного уравнения (ax⁴+bx²+c=0)
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Решение биквадратного уравнения (ax⁴+bx²+c=0)                                                          ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        try:
            coefficient_biq_a = int(input('   Введите a: '))
            coefficient_biq_b = int(input('   Введите b: '))
            coefficient_biq_c = int(input('   Введите c: '))
        except ValueError:
                print()
                print('Ошибка! Какой-то коэффициент является десятичной дробью или не является числом! Введите, пожалуйста, ещё раз числа!')
                print('Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со')
                print('значением не более 1000.')
                print()
        else:
            if coefficient_biq_a !=0 and coefficient_biq_b !=0 and coefficient_biq_c != 0:
                discriminant_biq = (coefficient_biq_b**2) - (4*coefficient_biq_a*coefficient_biq_c)
                if discriminant_biq > 0:
                    solution_biq_x1 = ((-coefficient_biq_b + discriminant_biq**(1/2)) / (2*coefficient_biq_a))**(1/2)
                    solution_biq_x2 = ((-coefficient_biq_b - discriminant_biq**(1/2)) / (2*coefficient_biq_a))**(1/2)
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax⁴+bx²+c=0.')
                    print('   ───────────────────────────────────')
                    print(f'   Дискриминант = {discriminant_biq:.2f}.')
                    print(f'   Ответ: x₁ = {solution_biq_x1:.2f};')
                    print(f'          x₂ = {solution_biq_x2:.2f}.')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif not discriminant_biq:
                    solution_biq_x = ((-coefficient_biq_b) / (2*coefficient_biq_a))**(1/2)
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax⁴+bx²+c=0.')
                    print('   ───────────────────────────────────')
                    print(f'   Дискриминант = {discriminant_biq:.2f}.')
                    print(f'   Ответ: x = {solution_biq_x:.2f}.')
                    print('   ───────────────────────────────────')
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                else:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Принято уравнение вида ax⁴+bx²+c=0.')
                    print('   ───────────────────────────────────')
                    print(f'   Дискриминант = {discriminant_biq:.2f}.')
                    print('   Уравнение не имеет решений!')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
            else:
                print()
                print('Ошибка! Какой-то из коэффициентов равен нулю. Программа покамест не умеет работать с такими коэффициентами.')
                print('Пожалуйста, в следующий раз вводите коэффициенты не равные нулю.')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()


def expansion_of_a_quadratic_equation(): # Главное меню > Разложение квадратного уравнения (ax²+bx+c=0)
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))                                              ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        try:
            coefficient_a = int(input('   Введите a: '))
            coefficient_b = int(input('   Введите b: '))
            coefficient_c = int(input('   Введите c: '))
        except ValueError:
            print()
            print('Ошибка! Какой-то коэффициент является десятичной дробью или не является числом! Введите, пожалуйста, ещё раз числа!')
            print('Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со')
            print('значением не более 1000. Коэффициенты не должны быть равны нулю.')
            print()
        else:
            if coefficient_a != 0 and coefficient_b != 0 and coefficient_c != 0:
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
                coef_a_ans = f'{coefficient_a}(' if coefficient_a > 0 and abs(coefficient_a) != 1 else (f'{coefficient_a}(' if coefficient_a < 0 and abs(coefficient_a) != 1 else(f'(' if coefficient_a > 0 and coefficient_a == 1 else f'-('))

                if discriminant > 0:
                    solution_x1 = (-coefficient_b + discriminant**(1/2)) / (2*coefficient_a)
                    solution_x2 = (-coefficient_b - discriminant**(1/2)) / (2*coefficient_a)

                    x1_ans = f'x - {solution_x1:.2f})' if solution_x1 > 0 else f'x + {-solution_x1:.2f})'
                    x2_ans = f'(x - {solution_x2:.2f})' if solution_x2 > 0 else f'(x + {-solution_x2:.2f})'

                    print()
                    print('   ───────────────────────────────────')
                    print('   Разложение квадратного уравнения вида ax²+bx+c как a(x-x₁)(x-x₂)')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                    print(f'   Решение:   D = {coef_b_dis}² - 4×{coef_a_dis}×{coef_c_dis}')
                    print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                    print(f'              D = {discriminant:.2f}')
                    print(f'              x = {coef_b_sol_1} ± {dis_sol}/(2×{coef_a_sol})')
                    print(f'              x = {coef_b_sol_2} ± {discriminant**(1/2):.2f})/({2*coefficient_a:.2f})')
                    print(f'              x₁ = {solution_x1:.2f}')
                    print(f'              x₂ = {solution_x2:.2f}')
                    print(f'   Ответ:     {coef_a_str}{coef_b_str}{coef_c_str} = {coef_a_ans}{x1_ans}{x2_ans}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                elif not discriminant:
                    solution_x = -((coefficient_b) / (2*coefficient_a))

                    x_ans_1 = f'x - {solution_x:.2f})' if solution_x > 0 else f'x + {solution_x:.2f})'
                    x_ans_2 = f'(x - {solution_x:.2f})' if solution_x > 0 else f'(x + {solution_x:.2f})'

                    print()
                    print('   ───────────────────────────────────')
                    print('   Разложение квадратного уравнения вида ax²+bx+c как a(x-x₁)(x-x₂)')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                    print(f'   Решение:   D = {coef_b_dis}² - 4×{coef_a_dis}×{coef_c_dis}')
                    print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                    print(f'              D = {discriminant:.2f}')
                    print(f'              x = {coef_b_sol_1})/(2×{coef_a_sol})')
                    print(f'              x = {coef_b_sol_2})/({2*coef_a_sol})')
                    print(f'              x = {solution_x:.2f}')
                    print(f'   Ответ:     {coef_a_str}{coef_b_str}{coef_c_str} = {coef_a_ans}{x_ans_1}{x_ans_2}')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
                else:
                    print()
                    print('   ───────────────────────────────────')
                    print('   Разложение квадратного уравнения вида ax²+bx+c как a(x-x₁)(x-x₂)')
                    print('   ───────────────────────────────────')
                    print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
                    print(f'   Решение:   D = {coef_b_dis}² - 4×{coef_a_dis}×{coef_c_dis}')
                    print(f'              D = {coefficient_b**2:.2f}{a_c_dis}')
                    print(f'              D = {discriminant:.2f}')
                    print('   Ответ:     Уравнение не имеет решений, следовательно, разложение уравнения невозможно!')
                    print('   ───────────────────────────────────')
                    print()
                    time.sleep(1)
                    while True:
                        cmd = input('[N] Продолжить, [E] Выход > ').lower()
                        if cmd == 'n':
                            print()
                            break
                        elif cmd == 'e':
                            main_menu()
                        else:
                            print()
                            print('Команда некорректна или не существует!')
                            print()
            else:
                print()
                print('Ошибка! Какой-то из коэффициентов равен нулю. Разложение неполного квадратного уравнения невозможно.')
                print('Пожалуйста, в следующий раз вводите коэффициенты не равные нулю.')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        main_menu()
                    else:
                        print()
                        print('Команда некорректна или не существует!')
                        print()


def reference(): # Главное меню > Справка
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка                                                                                                ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Программа QESPy 3.1 предназначена для решения всех видов квадратных уравнений, разложения квадратного уравнения и   ')
    print('   решения биквадратного уравнения.                                                                                    ')
    print('                                                                                                                       ')
    print('               Более подробные сведенья:                                                                               ')
    print('         [1] Руководство пользователя                                                                                  ')
    print('         [2] Структура программы                                                                                       ')
    print('         [3] Терминальные команды                                                                                      ')
    print('         [4] Лицензия                                                                                                  ')
    print('         [5] О программе                                                                                               ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            main_menu()
        if cmd == '1':
            user_guide()
        if cmd == '2':
            program_structure()
        if cmd == '3':
            terminal_commands()
        if cmd == '4':
            license()
        if cmd == '5':
            about_the_program()
        if cmd == 'e':
            main_menu()
        else:
            print()
            print('Команда некорректна или не существует!')
            print()


def user_guide(): # Главное меню > Справка > Руководство пользователя
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Руководство пользователя                                                                     ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Настоящий документ представляет собой руководство пользователя (далее Руководство) для программного обеспеченья     ')
    print('   проекта QESPy Project QESPy Beta 3.1 (далее QESPy Beta 3.1).                                                        ')
    print('   Руководство определяет порядок использования пользователем программного обеспеченья.                                ')
    print('   Перед работой пользователя с QESPy Beta 3.1 рекомендуется внимательно ознакомиться с настоящим Руководством.        ')
    print('                                                                                                                       ')
    print('                                                                                                                       ')
    print('   1. ВВЕДЕНИЕ                                                                                                         ')
    print('                                                                                                                       ')
    print('   1.1. Область применения                                                                                             ')
    print('   QESPy Beta 3.1 - это бета-версия программы, предназначенной для решения всех видов квадратных уравнений и вывода    ')
    print('   подробного решения, решения биквадратных уравнений и разложения квадратных уравнений с выводом подробного           ')
    print('   разложения.                                                                                                         ')
    print('                                                                                                                       ')
    print('   1.2. Краткое описание возможностей                                                                                  ')
    print('   QESPy Beta 3.1 обеспечивает выполнение следующих основных функций:                                                  ')
    print('   - Подробное решение всех видов квадратных уравнений: Программа предоставляет подробное решение для любого           ')
    print('     введенного квадратного уравнения.                                                                                 ')
    print('   - Решение биквадратных уравнений: Программа также способна решать биквадратные уравнения.                           ')
    print('   - Разложение квадратных уравнений: Программа может разложить квадратное уравнение на множители, если это будет      ')
    print('     возможно.                                                                                                         ')
    print('                                                                                                                       ')
    print('                                                                                                                       ')
    print('   2. СИСТЕМНЫЕ ТРЕБОВАНИЯ                                                                                             ')
    print('   Далее представлены минимальные системные требования для программы QESPy Beta 3.1:                                   ')
    print('   - Операционная система: Windows NT.                                                                                 ')
    print('   - Версия операционной системы: Windows 7 и выше (рекомендуется Windows 10).                                         ')
    print('   - Оперативная память: 2 GB (рекомендуется 4 GB).                                                                    ')
    print('   - Место на HDD/SSD: 30 MB.                                                                                          ')
    print('                                                                                                                       ')
    print('                                                                                                                       ')
    print('   3. УСТАНОВКА                                                                                                        ')
    print('      1. Скачайте программу с официального сайта или из надежного источника.                                           ')
    print('      2. Запустите самораспаковывающийся архив и распакуйте файлы программы на компьютер.                              ')
    print('      3. После завершения распаковки программа будет готова к использованию.                                           ')
    print('                                                                                                                       ')
    print('                                                                                                                       ')
    print('   4. ОПИСАНИЕ ФУНКЦИЙ                                                                                                 ')
    print('   В данном разделе производится описание всех разделов и функций, предоставляемых программой QESPy Beta 3.1.          ')
    print('                                                                                                                       ')
    print('   4.1. Главное меню                                                                                                   ')
    print('   Главное меню предназначено для навигации пользователя в программе QESPy Beta 3.1.                                   ')
    print('   Основная задача Главного меню обеспечить доступ пользователя ко всем функциям программы QESPy Beta 3.1.             ')
    print('                                                                                                                       ')
    print('   4.2. Решение квадратного уравнения (ax²+bx+c=0)                                                                     ')
    print('   Данная функция предназначена для решения всех видов квадратного уравнения и вывода подробного решения на экран.     ')
    print('   Для того чтобы приступить к решению квадратного уравнения пользователю требуется ввести номер опции "Решение        ')
    print('   квадратного уравнения (ax²+bx+c=0)" из Главного меню и внутри опции "Решение квадратного уравнения (ax²+bx+c=0)"    ')
    print('   и ввести 3 коэффициента после чего наблюдать результат вычислений.                                                  ')
    print('   Для продолжения использования функций опции или выхода из неё пользователю требуется следовать инструкции,          ')
    print('   выводимой после решения.                                                                                            ')
    print('                                                                                                                       ')
    print('   4.3. Решение биквадратного уравнения (ax⁴+bx²+c=0)                                                                  ')
    print('   Данная функция предназначена для решения биквадратного уравнения, при условии, что все 3 коэффициента не равны      ')
    print('   нулю.                                                                                                               ')
    print('   Для того чтобы приступить к решению биквадратного уравнения пользователю требуется ввести номер опции "Решение      ')
    print('   биквадратного уравнения (ax²+bx+c=0)" из Главного меню и внутри опции "Решение биквадратного уравнения              ')
    print('   (ax²+bx+c=0)" и ввести 3 коэффициента после чего наблюдать результат вычислений.                                    ')
    print('   Для продолжения использования функций опции или выхода из неё пользователю требуется следовать инструкции,          ')
    print('   выводимой после решения.                                                                                            ')
    print('                                                                                                                       ')
    print('   4.4. Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))                                                      ')
    print('   Данная функция предназначена для разложения квадратного уравнения на множители с выводом подробного решения, при    ')
    print('   условии, что все 3 коэффициента не равны нулю.                                                                      ')
    print('   Для того чтобы приступить к разложению квадратного уравнения на множители пользователю требуется ввести номер       ')
    print('   опции "Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))" из Главного меню и внутри опции "Разложение       ')
    print('   квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))" и ввести 3 коэффициента после чего наблюдать результат              ')
    print('   вычислений.                                                                                                         ')
    print('   Для продолжения использования функций опции или выхода из неё пользователю требуется следовать инструкции,          ')
    print('   выводимой после решения.                                                                                            ')
    print('                                                                                                                       ')
    print('   4.5. Терминал                                                                                                       ')
    print('   Терминал используется разработчиками и опытными пользователями для настройки, тестирования и отладки программы.     ')
    print('   Неопытным пользователям настоятельно не рекомендуется пользоваться терминалом.                                      ')
    print('                                                                                                                       ')
    print('   4.6. Справка                                                                                                        ')
    print('   В справке находится вся необходимая информация для пользователей и разработчиков.                                   ')
    print('                                                                                                                       ')
    print('   4.7. Выход                                                                                                          ')
    print('   Выход из программы                                                                                                  ')
    print('                                                                                                                       ')
    print('   5. РЕШЕНИЕ ПРОБЛЕМ                                                                                                  ')
    print('   На данный момент не известно о проблемах с программой. Если вы столкнулись с проблемой, пожалуйста, свяжитесь с     ')
    print('   службой поддержки.                                                                                                  ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print()
            print('Команда некорректна или не существует!')
            print()


def program_structure():# Главное меню > Справка > Структура программы
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Структура программы                                                                          ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('      MAIN                                                                                               [BOOT]        ')
    print('      └── Главное меню                                                                                   [UInit]       ')
    print('          ├── Решение квадратного уравнения (ax²+bx+c=0)                                                 [UInit]       ')
    print('          │   ├── Решение неполного квадратного уравнения вида bx+c=0                                    [InitAl]      ')
    print('          │   ├── Решение неполного квадратного уравнения вида ax²+c=0                                   [InitAl]      ')
    print('          │   ├── Решение неполного квадратного уравнения вида ax²+bx=0                                  [InitAl]      ')
    print('          │   ├── Решение неполного квадратного уравнения вида c=0                                       [InitAl]      ')
    print('          │   ├── Решение неполного квадратного уравнения вида bx=0                                      [InitAl]      ')
    print('          │   ├── Решение неполного квадратного уравнения вида ax²=0                                     [InitAl]      ')
    print('          │   ├── Решение неполного квадратного уравнения вида 0=0                                       [InitAl]      ')
    print('          │   └── Решение квадратного уравнения общего вида ax²+bx+c=0                                   [InitAl]      ')
    print('          ├── Решение биквадратного уравнения (ax⁴+bx²+c=0)                                              [UInit]       ')
    print('          ├── Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))                                  [UInit]       ')
    print('          ├── Терминал                                                                                   [UInit]       ')
    print('          ├── Справка                                                                                    [UInit]       ')
    print('          │   ├── Руководство пользователя                                                               [UInit]       ')
    print('          │   ├── Структура программы                                                                    [UInit]       ')
    print('          │   ├── Терминальные команды                                                                   [UInit]       ')
    print('          │   ├── Лицензия                                                                               [UInit]       ')
    print('          │   └── О программе                                                                            [UInit]       ')
    print('          └── Выход                                                                                      [UInit]       ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print()
            print('Команда некорректна или не существует!')
            print()


def terminal_commands(): # Главное меню > Справка > Консольные команды
    clear()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Консольные команды                                                                           ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Этот раздел будет доступен в следующих обновлениях                                                                  ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print('Команда некорректна или не существует!')


def license(): # Главное меню > Справка > Лицензия
    clear()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Лицензия                                                                                     ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   BSD 3-Clause License                                                                                                ')
    print('                                                                                                                       ')
    print('   Copyright (c) 2023, Moskvich2020                                                                                    ')
    print('                                                                                                                       ')
    print('   Распространение и использование в исходной и бинарной форме, с модификациями или без них, разрешено при соблюде-    ')
    print('   нии следующих условий:                                                                                              ')
    print('   1. При повторном распространении исходного кода должно сохраняться вышеуказанное уведомление об авторских правах,   ')
    print('      этот список условий и следующий отказ от ответственности.                                                        ')
    print('   2. При повторном распространении в двоичной форме должно воспроизводиться вышеуказанное уведомление об авторских    ')
    print('      правах, настоящий список условий и следующий отказ от ответственности в документации и/или других материалах,    ')
    print('      о поставляемых  вместе с дистрибутивом.                                                                          ')
    print('   3. Ни имя владельца авторских прав, ни имена его участников не могут использоваться для поддержки или продвижения   ')
    print('      продуктов, созданных на основе этого программного обеспечения, без специального предварительного письменного     ')
    print('      разрешения.                                                                                                      ')
    print('                                                                                                                       ')
    print('   ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ ОБЛАДАТЕЛЯМИ АВТОРСКИХ ПРАВ И УЧАСТНИКАМИ «КАК ЕСТЬ», И ЛЮБЫЕ        ')
    print('   ЯВНЫЕ ИЛИ ПОДРАЗУМЕВАЕМЫЕ ГАРАНТИИ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ, ПОДРАЗУМЕВАЕМЫМИ ГАРАНТИЯМИ ТОВАРНОЙ ГОДНОСТИ И   ')
    print('   ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ, ОТКАЗЫВАЮТСЯ. НИ В КОЕМ СЛУЧАЕ ВЛАДЕЛЕЦ АВТОРСКОГО ПРАВА НЕ НЕСЕТ ОТВЕТСТВЕН-    ')
    print('   НОСТИ ЗА ЛЮБЫЕ ПРЯМЫЕ, КОСВЕННЫЕ, СЛУЧАЙНЫЕ, ОСОБЫЕ, ПРИМЕРНЫЕ ИЛИ КОСВЕННЫЕ УБЫТКИ(ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ,   ')
    print('   ЗАКУПКУ ЗАМЕНИТЕЛЬНЫХ ТОВАРОВ ИЛИ УСЛУГ; ПОТЕРЯ ИСПОЛЬЗОВАНИЯ, ДАННЫЕ ИЛИ ПРИБЫЛЬ; ИЛИ ПРЕРЫВАНИЕ ДЕЛОВОЙ ДЕЯТЕ-    ')
    print('   ЛЬНОСТИ), КАКОЙ-ЛИБО ВЫЗВАННОЙ, И НА ЛЮБОЙ ТЕОРИИ ОТВЕТСТВЕННОСТИ, КАК ДОГОВОР, СТРОГО ОТВЕТСТВЕННОСТЬ ИЛИ ПРАВО-   ')
    print('   НАКТ (ВКЛЮЧАЯ НЕБРЕЖНОСТЬ ИЛИ ДРУГИЕ ОБРАЗЫ), ВОЗНИКАЮЩИЕ ЛЮБЫМ СПОСОБОМ ИСПОЛЬЗОВАНИЯ ЭТОГО ПРОГРАММНОГО ОБЕСПЕ-   ')
    print('   ЧЕНИЯ, ДАЖЕ ЕСЛИ УВЕДОМЛЕНЫ О ВОЗМОЖНОСТИ ТАКОГО УЩЕРБА.                                                            ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print()
            print('Команда некорректна или не существует!')
            print()


def terminal(): # Главное меню > Терминал
    clear()
    print('Quadratic Equation Solver in Python [Version 3.1.7b]')
    print('(c) Moskvich2020 (QESPy Project). Все права защищены.')
    while True:
        print()
        cmd = input(r'QESPy\3.1.7b\User>').lower()
        if cmd == 'exit': # TUI
            main_menu()
        elif cmd == 'help': # Console
            print('<none>')
        elif cmd == 'clean': # Console
            terminal()
        elif cmd == 'reboot': # BOOT
            main()
        elif cmd == 'mainmenu': # TUI
            main_menu()
        elif cmd == 'queqsolv': # TUI
            solving_a_quadratic_equation()
        elif cmd == 'biqueqslov':
            solving_a_biquadratic_equation()
        elif cmd == 'reference': # TUI
            reference()
        elif cmd == 'usehelp': # TUI
            user_guide()
        elif cmd == 'progstruct': # TUI
            program_structure()
        elif cmd == 'termcommands': # TUI
            terminal_commands()
        elif cmd == 'license': # Console
            print('<none>')
        elif cmd == 'terminal': # TUI
            terminal()
        elif cmd == 'aboprog': # TUI
            about_the_program()
        elif cmd == 'progtree': # Console
            print('MAIN                                                                                         [BOOT]  ')
            print('└── Главное меню                                                                             [UInit] ')
            print('    ├── Решение квадратного уравнения (ax²+bx+c=0)                                           [UInit] ')
            print('    │   ├── Решение неполного квадратного уравнения вида bx+c=0                              [InitAl]')
            print('    │   ├── Решение неполного квадратного уравнения вида ax²+c=0                             [InitAl]')
            print('    │   ├── Решение неполного квадратного уравнения вида ax²+bx=0                            [InitAl]')
            print('    │   ├── Решение неполного квадратного уравнения вида c=0                                 [InitAl]')
            print('    │   ├── Решение неполного квадратного уравнения вида bx=0                                [InitAl]')
            print('    │   ├── Решение неполного квадратного уравнения вида ax²=0                               [InitAl]')
            print('    │   ├── Решение неполного квадратного уравнения вида 0=0                                 [InitAl]')
            print('    │   └── Решение квадратного уравнения общего вида ax²+bx+c=0                             [InitAl]')
            print('    ├── Решение биквадратного уравнения (ax⁴+bx²+c=0)                                        [UInit] ')
            print('    ├── Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))                            [UInit] ')
            print('    ├── Терминал                                                                             [UInit] ')
            print('    ├── Справка                                                                              [UInit] ')
            print('    │   ├── Руководство пользователя                                                         [UInit] ')
            print('    │   ├── Структура программы                                                              [UInit] ')
            print('    │   ├── Терминальные команды                                                             [UInit] ')
            print('    │   ├── Лицензия                                                                         [UInit] ')
            print('    │   └── О программе                                                                      [UInit] ')
            print('    └── Выход                                                                                [UInit] ')
        else:
            print('Команда некорректна или не существует!')


def about_the_program(): # Главное меню > О программе
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > О программе                                                                                  ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Имя программы:           QESPy                                                                                      ')
    print('   Полное имя программы:    Quadratic Equation Solver in Python                                                        ')
    print('   Версия:                  Beta 3.1                                                                                   ')
    print('   Полная версия:           v3.1.7b                                                                                    ')
    print('   Номер сборки:            25122023                                                                                   ')
    print('   Оболочка:                Отсутствует                                                                                ')
    print('   Ядро:                    IPython                                                                                    ')
    print('   Исполнитель:             Python3                                                                                    ')
    print('   Разработчик:             Moskvich2020                                                                               ')
    print('   Цвета:                   Чёрно-белые                                                                                ')
    print('   Тема:                    Dark                                                                                       ')
    print('   Иконка:                  Отсутствует                                                                                ')
    print('   Система навигации:       Не определена                                                                              ')
    print('   Размер консоли:          Не установлен                                                                              ')
    print('   Интерфейс:               TUI 1.3                                                                                    ')
    print('   Язык:                    Русский                                                                                    ')
    print('   Хост:                    This PC                                                                                    ')
    print('   Терминал:                Вкл.                                                                                       ')
    print('   Лицензия:                BSD 3-Clause License                                                                       ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print()
            print('Команда некорректна или не существует!')
            print()


main()
