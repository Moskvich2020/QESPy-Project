# QESPy Beta 3 [build 09122023]

import os
import time

clear = lambda: os.system('cls')

def main(): # main
    clear()
    print('Quadratic Equation Solver in Python [Version 3.0.5b]')
    print('(c) Moskvich2020 (QESPy Project). Все права защищены.')
    print()
    time.sleep(0.5)
    print('X:\\QESPy-Project\\3.0.5b\\User>')
    time.sleep(1)
    main_menu()

def main_menu(): # Главное меню
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Добро пожаловать в QESPy Beta 3!                                                                              ')
    print('         Программа готова к решению всех видов квадратных уравнений!                                                   ')
    print('         ──────────────────────────────────────────────────────────────────────────────────────────────────────        ')
    print('               Выберете опцию:                                                                                         ')
    print('         [1] Решение квадратного уравнения (ax²+bx+c=0)                                                                ')
    print('         [2] Решение биквадратного уравнения (ax⁴+bx²+c=0)                                                             ')
    print('         [3] Справка                                                                                                   ')
    print('         [4] О программе                                                                                               ')
    print('         [E] Выход                                                                                                     ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('      Пожалуйста, введите номер опции из меню [1, 2, 3, 4, 5, E]...                                                    ')
    print()
    while True:
        cmd = input('> ').lower()
        if cmd == '1':
            solving_a_quadratic_equation()
        elif cmd == '2':
            solution_of_biquadratic_equation()
        elif cmd == '3':
            reference()
        elif cmd == '4':
            about_the_program()
        elif cmd == 'exit':
            quit()
        elif cmd == 'e':
            quit()
        else:
            print()
            print('Команда не корректна или не существует!')
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
            print('Ошибка! Введите пожалуйста ещё раз числа!')
            print()
        else:
            if not coefficient_a and coefficient_b != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a = 0
                solution_x = -(coefficient_c/coefficient_b)
                print()
                print('   ──────────')
                print('   Принято уравнение вида bx+c=0.')
                print(f'   Ответ: x= {solution_x:.3f}.')
                print('   ──────────')
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
                        print('Команда не корректна или не существует!')
                        print()
            elif coefficient_a != 0 and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > b = 0
                if coefficient_c/coefficient_a < 0:
                    solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
                    solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax²+c=0.')
                    print(f'   Ответ: x1= {solution_x1:.3f};')
                    print(f'          x2= {solution_x2:.3f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                elif coefficient_c/coefficient_a == 0:
                    solution_x = 0
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax²+c=0.')
                    print(f'   Ответ: x= {solution_x:.0f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                else:
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax²+c=0.')
                    print('   Уравнение не имеет решений!')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
            elif coefficient_a != 0 and coefficient_b != 0 and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c = 0
                solution_x1 = 0
                solution_x2 = -(coefficient_b/coefficient_a)
                print()
                print('   ──────────')
                print('   Принято уравнение вида ax²+bx=0.')
                print(f'   Ответ: x1= {solution_x1:.3f};')
                print(f'          x2= {solution_x2:.3f}.')
                print('   ──────────')
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
                        print('Команда не корректна или не существует!')
                        print()
            elif not coefficient_a and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a и b = 0
                if not coefficient_c:
                    solution_x = 0
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида c=0.')
                    print(f'   Ответ: x= {solution_x:.0f}.')
                    print('   ──────────')
                    print()
                else:
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида c=0.')
                    print(f'   Ошибка! "{coefficient_c:.0f}=0". Данное выражение не имеет смысла.')
                    print('   Ответ: ∅.')
                    print('   ──────────')
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
                        print('Команда не корректна или не существует!')
                        print()
            elif not coefficient_a and coefficient_b != 0 and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a и c = 0
                solution_x = 0
                print()
                print('   ──────────')
                print('   Принято уравнение вида bx=0.')
                print(f'   Ответ: x= {solution_x:.0f}.')
                print('   ──────────')
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
                        print('Команда не корректна или не существует!')
                        print()
            elif coefficient_a != 0 and not coefficient_b and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > b и c = 0
                solution_x = 0
                print()
                print('   ──────────')
                print('   Принято уравнение вида ax²=0.')
                print(f'   Ответ: x= {solution_x:.0f}.')
                print('   ──────────')
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
                        print('Команда не корректна или не существует!')
                        print()
            elif not coefficient_a and not coefficient_b and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a и b и c = 0
                print()
                print('   ──────────')
                print('   Принято уравнение вида 0=0.')
                print('   Ответ: x может быть любым числом.')
                print('   ──────────')
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
                        print('Команда не корректна или не существует!')
                        print()
            elif coefficient_a == 1 and coefficient_b != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (x²+px+q=0) > a = 1
                reduced_discriminant = ((coefficient_b**2)/4) - coefficient_c
                if reduced_discriminant > 0:
                    solution_x1 = -(coefficient_b/2) - (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                    solution_x2 = -(coefficient_b/2) + (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида x²+px+q=0.')
                    print(f'   Приведённый дискриминант = {reduced_discriminant:.3f}.')
                    print(f'   Ответ: x1= {solution_x1:.3f};')
                    print(f'          x2= {solution_x2:.3f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                elif not reduced_discriminant:
                    solution_x = -(coefficient_b/2) - (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида x²+px+q=0.')
                    print('   Приведённый дискриминант = 0.')
                    print(f'   Ответ: x= {solution_x:.3f}')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                else:
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида x²+px+q=0.')
                    print(f'   Приведённый дискриминант = {reduced_discriminant:.3f}.')
                    print('   Уравнение не имеет решений!')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
            elif coefficient_a != 0 and coefficient_b !=0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > Discriminant
                discriminant = (coefficient_b**2) - (4*coefficient_a*coefficient_c)
                if discriminant > 0:
                    solution_x1 = (-coefficient_b - (discriminant**(1/2))) / (2*coefficient_a)
                    solution_x2 = (-coefficient_b + (discriminant**(1/2))) / (2*coefficient_a)
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax²+bx+c=0.')
                    print(f'   Дискриминант = {discriminant:.3f}.')
                    print(f'   Ответ: x1= {solution_x1:.3f};')
                    print(f'          x2= {solution_x2:.3f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                elif not discriminant:
                    solution_x = -((coefficient_b) / (2*coefficient_a))
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax²+bx+c=0.')
                    print(f'   Дискриминант = 0.')
                    print(f'   Ответ: x= {solution_x:.3f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                else:
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax²+bx+c=0.')
                    print(f'   Дискриминант = {discriminant:.3f}.')
                    print('   Уравнение не имеет решений!')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
            else:
                print()
                print('Внимание! Произошла неизвесная синтаксическая/логическая ошибка.')
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
                        print('Команда не корректна или не существует!')
                        print()

def solution_of_biquadratic_equation(): # Главное меню > Решение биквадратного уравнения (ax⁴+bx²+c=0)
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
                print('Ошибка! Введите пожалуйста ещё раз числа!')
                print()
        else:
            if coefficient_biq_a !=0 and coefficient_biq_b !=0 and coefficient_biq_c != 0:
                discriminant_biq = (coefficient_biq_b**2) - (4*coefficient_biq_a*coefficient_biq_c)
                if discriminant_biq > 0:
                    solution_biq_x1 = ((-coefficient_biq_b - (discriminant_biq**(1/2))) / (2*coefficient_biq_a))**(1/2)
                    solution_biq_x2 = ((-coefficient_biq_b + (discriminant_biq**(1/2))) / (2*coefficient_biq_a))**(1/2)
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax⁴+bx²+c=0.')
                    print(f'   Дискриминант = {discriminant_biq:.3f}.')
                    print(f'   Ответ: x1= {solution_biq_x1:.3f};')
                    print(f'          x2= {solution_biq_x2:.3f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                elif not discriminant_biq:
                    solution_biq_x = ((-coefficient_biq_b) / (2*coefficient_biq_a))**(1/2)
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax⁴+bx²+c=0.')
                    print(f'   Дискриминант = {discriminant_biq:.3f}.')
                    print(f'   Ответ: x= {solution_biq_x:.3f}.')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
                else:
                    print()
                    print('   ──────────')
                    print('   Принято уравнение вида ax⁴+bx²+c=0.')
                    print(f'   Дискриминант = {discriminant_biq:.3f}.')
                    print('   Уравнение не имеет решений!')
                    print('   ──────────')
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
                            print('Команда не корректна или не существует!')
                            print()
            else:
                print()
                print('Ошибка! Какой-то из коэффицентов равен нулю. Программа покамест не умеет работать с такими коэффицентами.')
                print('Пожалуйста в следующий раз вводите коэффиценты не равные нулю.')
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
                        print('Команда не корректна или не существует!')
                        print()

def reference(): # Главное меню > Справка
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка                                                                                                ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Программа QESPy предназначена для решения всех видов квадратных уравнений.                                          ')
    print('                                                                                                                       ')
    print('               Более подробные сведенья:                                                                               ')
    print('         [1] Инструкция по применению                                                                                  ')
    print('         [2] Структура программы                                                                                       ')
    print('         [3] Консольнве команды                                                                                        ')
    print('         [4] Лицензия                                                                                                  ')
    print('         [5] О программе                                                                                               ')
    print('         [E] Выход                                                                                                     ')
    print()
    while True:
        cmd = input('> ')
        if cmd == '1':
            instructions_for_use()
        if cmd == '2':
            program_structure()
        if cmd == '3':
            console_commands()
        if cmd == '4':
            license()
        if cmd == '5':
            about_the_program()
        if cmd == 'e':
            main_menu()
        else:
            print()
            print('Команда не корректна или не существует!')
            print()

def instructions_for_use(): # Главное меню > Справка > Инструкция по применению
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Инструкция по применению                                                                     ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print()
            print('Команда не корректна или не существует!')
            print()

def program_structure():# Главное меню > Справка > Структура программы
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Структура программы                                                                          ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('      Главное меню                                                                                       [UInit]       ')
    print('      ├── Решение квадратного уравнения (ax²+bx+c=0)                                                     [UInit]       ')
    print('      │   ├── Решение неполного квадратного уравнения вида bx+c=0                                        [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида ax²+c=0                                       [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида ax²+bx=0                                      [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида c=0                                           [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида bx=0                                          [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида ax²=0                                         [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида 0=0                                           [InitAl]      ')
    print('      │   ├── Решение приведённого квадратного уравнения вида x²+px+q=0                                  [InitAl]      ')
    print('      │   └── Решение квадратного уравнения общего вида ax²+bx+c=0                                       [InitAl]      ')
    print('      ├── Решение биквадратного уравнения (ax⁴+bx²+c=0)                                                  [UInit]       ')
    print('      ├── Справка                                                                                        [UInit]       ')
    print('      │   ├── Инструкция по применению                                                                   [UInit]       ')
    print('      │   ├── Структура программы                                                                        [UInit]       ')
    print('      │   ├── Консольнве команды                                                                         [UInit]       ')
    print('      │   ├── Лицензия                                                                                   [UInit]       ')
    print('      │   └── О программе                                                                                [UInit]       ')
    print('      └── О программе                                                                                    [UInit]       ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print()
            print('Команда не корректна или не существует!')
            print()

def console_commands(): # Главное меню > Справка > Консольные команды
    clear()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Консольные команды                                                                           ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print('Команда не корректна или не существует!')

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
    print('      правах, настоящий список условий и следующий отказ от тветственности в документации и/или других материалах, о   ')
    print('      поставляемых  вместе с дистрибутивом.                                                                            ')
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
            print('Команда не корректна или не существует!')
            print()

def about_the_program(): # Главное меню > О программе
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: О программе                                                                                            ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Имя программы:           QESPy                                                                                      ')
    print('   Полное имя программы:    Quadratic Equation Solver in Python                                                        ')
    print('   Версия:                  Beta 3                                                                                     ')
    print('   Полная версия:           v3.0.5b                                                                                    ')
    print('   Номер сборки:            09122023                                                                                   ')
    print('   Оболочка:                Отсутствует                                                                                ')
    print('   Ядро:                    IPython                                                                                    ')
    print('   Исполнитель:             Python3                                                                                    ')
    print('   Разработчик:             Moskvich2020                                                                               ')
    print('   Цвета:                   Чёрно-белые                                                                                ')
    print('   Тема:                    Dark                                                                                       ')
    print('   Иконка:                  Отсутствует                                                                                ')
    print('   Система навигации:       Не определена                                                                              ')
    print('   Размер консоли:          Не установлен                                                                              ')
    print('   Интерфейс:               Текстовый                                                                                  ')
    print('   Язык:                    Русский                                                                                    ')
    print('   Хост:                    This PC                                                                                    ')
    print('   Консоль админа:          Откл.                                                                                      ')
    print('   Тенрминал:               Откл.                                                                                      ')
    print('   Лицензия:                BSD 3-Clause License                                                                       ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            main_menu()
        else:
            print()
            print('Команда не корректна или не существует!')
            print()

main()
