# QESPy Beta 2 [build 20112023]

import os
import time

clear = lambda: os.system('cls')

def main(): # Главное меню 
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Добро пожаловать в QESPy Beta 2!                                                  ')
    print('         Программа готова к решению всех видов квадратных уравнений!                       ')
    print('         !ВНИМАНИЕ! ЭТО BETA ВЕРСИЯ!                                                       ')
    print('         !Некоторые функции прогаммы могут быть недоступны или не работать!                ')
    print('         ──────────────────────────────────────────────────────────────────────────        ')
    print('               Выберете опцию:                                                             ')
    print('         [1] Решение квадратного уравнения (ax²+bx+c=0)                                    ')
    print('         [2] Решение биквадратного уравнения (ax⁴+bx²+c=0)                                 ')
    print('         [3] Справка                                                                       ')
    print('         [4] О программе                                                                   ')
    print('         [E] Выход                                                                         ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('      Пожалуйста, введите номер опции из меню [1, 2, 3, 4, 5, E]...                        ')
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
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Решение квадратного уравнения (ax²+bx+c=0)                                 ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        coefficient_a = int(input('Введите a: '))
        coefficient_b = int(input('Введите b: '))
        coefficient_c = int(input('Введите c: '))
        print()
        if not coefficient_a and coefficient_b != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a = 0
            solution_x = -(coefficient_c/coefficient_b)
            print('──────────')
            print('Принято уравнение вида bx+c=0.')
            print('Ответ: ', 'x=', solution_x, '.', sep='')
            print('──────────')
            print()
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()
        elif not coefficient_b and coefficient_a != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > b = 0
            if coefficient_c/coefficient_a < 0:
                solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
                solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)
                print('──────────')
                print('Принято уравнение вида ax²+c=0.')
                print('Ответ: ', 'x1=', solution_x1, ';', sep='')
                print('       ', 'x2=', solution_x2, '.', sep='')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
            elif coefficient_c/coefficient_a == 0:
                solution_x = 0
                print('──────────')
                print('Принято уравнение вида ax²+c=0.')
                print('Ответ: ', 'x=', solution_x,'.', sep='')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
            else:
                print('──────────')
                print('Принято уравнение вида ax²+c=0.')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
        elif not coefficient_c and coefficient_a != 0 and coefficient_b != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c = 0
            solution_x1 = 0
            solution_x2 = -(coefficient_b/coefficient_a)
            print('──────────')
            print('Принято уравнение вида ax²+bx=0.')
            print('Ответ: ', 'x1=', solution_x1, ';', sep='')
            print('       ', 'x2=', solution_x2, '.', sep='')
            print('──────────')
            print()
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()
        elif not coefficient_a and not coefficient_b and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a и b = 0
            solution_x = None
            print('──────────')
            print('Принято уравнение вида c=0.')
            print('x может быть любым числом.')
            print('──────────')
            print()
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()
        elif not coefficient_a and not coefficient_c and coefficient_b != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a и c = 0
            solution_x = 0
            print('──────────')
            print('Принято уравнение вида bx=0.')
            print('x=', solution_x)
            print('──────────')
            print()
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()
        elif not coefficient_b and not coefficient_c and coefficient_a != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > b и c = 0
            solution_x = 0
            print('──────────')
            print('Принято уравнение вида ax²=0.')
            print('x=', solution_x)
            print('──────────')
            print()                
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()
        elif not coefficient_a and not coefficient_b and not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a и b и c = 0
            solution_x = 0
            print('──────────')
            print('Принято уравнение вида 0=0.')
            print('x=', solution_x)
            print('──────────')
            print()
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()
        elif coefficient_a == 1 and coefficient_b != 0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (x²+px+q=0) > a = 1
            if ((coefficient_b**2)/4) - coefficient_c > 0:
                solution_x1 = -(coefficient_b/2) - (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                solution_x2 = -(coefficient_b/2) + (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                print('──────────')
                print('Принято уравнение вида x²+px+q=0.')
                print('Ответ: ', 'x1=', solution_x1, ';', sep='')
                print('       ', 'x2=', solution_x2, '.', sep='')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
            elif not ((coefficient_b**2)/4) - coefficient_c:
                solution_x = -(coefficient_b/2)
                print('──────────')
                print('Принято уравнение вида x²+px+q=0.')
                print('x=', solution_x)
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
            else:
                print('──────────')
                print('Принято уравнение вида x²+px+q=0.')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
        elif coefficient_a != 0 and coefficient_b !=0 and coefficient_c != 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > Discriminant
            discriminant = (coefficient_b**2) - (4*coefficient_a*coefficient_c)
            if discriminant > 0:
                solution_x1 = (-coefficient_b - (discriminant**(1/2))) / (2*coefficient_a)
                solution_x2 = (-coefficient_b + (discriminant**(1/2))) / (2*coefficient_a)
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant, '.', sep='')
                print('Ответ: ', 'x1=', solution_x1, ';', sep='')
                print('       ', 'x2=', solution_x2, '.', sep='')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
            elif not discriminant:
                solution_x = (-coefficient_b) / (2*coefficient_a)
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant, '.', sep='')
                print('Ответ: ', 'x=', solution_x, '.', sep='')
                print('──────────')
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
                print()
            else:
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant, '.', sep='')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(1)
                while True:
                    cmd = input('[N] Продолжить, [E] Выход > ').lower()
                    if cmd == 'n':
                        print()
                        break
                    elif cmd == 'e':
                        clear()
                        main()
                    else:
                        print()
                        print('Команда не корректна или не существует!')
                        print()
        else:
            print('Error!')
            time.sleep(1)
            while True:
                cmd = input('[N] Продолжить, [E] Выход > ').lower()
                if cmd == 'n':
                    print()
                    break
                elif cmd == 'e':
                    clear()
                    main()
                else:
                    print()
                    print('Команда не корректна или не существует!')
                    print()

def solution_of_biquadratic_equation(): # Главное меню > Решение биквадратного уравнения (ax⁴+bx²+c=0)
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Решение биквадратного уравнения (ax⁴+bx²+c=0)                              ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        coefficient_biq_a = int(input('Введите a: '))
        coefficient_biq_b = int(input('Введите b: '))
        coefficient_biq_c = int(input('Введите c: '))
        print()
        if coefficient_biq_a !=0 and coefficient_biq_b !=0 and coefficient_biq_c != 0:
            discriminant_biq = (coefficient_biq_b**2) - (4*coefficient_biq_a*coefficient_biq_c)
            if discriminant_biq > 0:
                solution_biq_x1 = ((-coefficient_biq_b - (discriminant_biq**(1/2))) / (2*coefficient_biq_a))**(1/2)
                solution_biq_x2 = ((-coefficient_biq_b + (discriminant_biq**(1/2))) / (2*coefficient_biq_a))**(1/2)
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant_biq, '.', sep='')
                print('Ответ: ', 'x1=', solution_biq_x1, ';', sep='')
                print('       ', 'x2=', solution_biq_x2, '.', sep='')
                print('──────────')
                print()
                time.sleep(5)
            elif not discriminant_biq:
                solution_biq_x = ((-coefficient_biq_b) / (2*coefficient_biq_a))**(1/2)
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant_biq, '.', sep='')
                print('Ответ: ', 'x=', solution_biq_x, '.', sep='')
                print('──────────')
                time.sleep(5)
                print()
            else:
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant_biq, '.', sep='')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(5)
        else:
            print()
            print('Error!')
            print('Какой-то из коэффицентов равен нулю. Программа покамест не умеет работать с такими коэффицентами.')
            print()

def reference(): # Главное меню > Справка
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка                                                                    ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Программа QESPy предназначена для решения всех видов квадратных уравнений.              ')
    print('                                                                                           ')
    print('               Более подробные сведенья:                                                   ')
    print('         [1] Инструкция по применению                                                      ')
    print('         [2] Структура программы                                                           ')
    print('         [3] Консольнве команды                                                            ')
    print('         [4] Лицензия                                                                      ')
    print('         [5] О программе                                                                   ')
    print('         [E] Выход                                                                         ')
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
            main()
        else:
            print('Команда не корректна или не существует!')

def instructions_for_use(): # Главное меню > Справка > Инструкция по применению
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Инструкция по применению                                         ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print('Команда не корректна или не существует!')

def program_structure():# Главное меню > Справка > Структура программы
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Структура программы                                              ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('      Главное меню                                                           [UInit]       ')
    print('      ├── Решение квадратного уравнения (ax²+bx+c=0)                         [UInit]       ')
    print('      │   ├── Решение неполного квадратного уравнения вида bx+c=0            [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида ax²+c=0           [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида ax²+bx=0          [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида c=0               [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида bx=0              [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида ax²=0             [InitAl]      ')
    print('      │   ├── Решение неполного квадратного уравнения вида 0=0               [InitAl]      ')
    print('      │   ├── Решение приведённого квадратного уравнения вида x²+px+q=0      [InitAl]      ')
    print('      │   └── Решение квадратного уравнения общего вида ax²+bx+c=0           [InitAl]      ')
    print('      ├── Решение биквадратного уравнения (ax⁴+bx²+c=0)                      [UInit]       ')
    print('      ├── Справка                                                            [UInit]       ')
    print('      │   ├── Инструкция по применению                                       [UInit]       ')
    print('      │   ├── Структура программы                                            [UInit]       ')
    print('      │   ├── Консольнве команды                                             [UInit]       ')
    print('      │   ├── Лицензия                                                       [UInit]       ')
    print('      │   └── О программе                                                    [UInit]       ')
    print('      └── О программе                                                        [UInit]       ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print('Команда не корректна или не существует!')

def console_commands(): # Главное меню > Справка > Консольные команды
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Консольные команды                                               ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print('Команда не корректна или не существует!')

def license(): # Главное меню > Справка > Лицензия
    clear()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: Справка > Лицензия                                                         ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   BSD 3-Clause License                                                                    ')
    print('                                                                                           ')
    print('   Copyright (c) 2023, Moskvich2020                                                        ')
    print('                                                                                           ')
    print('   Распространение и использование в исходной и бинарной форме,  с модификациями или без   ')
    print('   них, разрешено при соблюдении следующих условий:                                        ')
    print('   1. При повторном распространении исходного кода должно сохраняться вышеуказанное уве-   ')
    print('      домление об авторских правах, этот список условий и следующий отказ от ответствен-   ')
    print('      ности.                                                                               ')
    print('   2. При повторном распространении в двоичной форме должно воспроизводиться вышеуказан-   ')
    print('      ное уведомление об авторских правах, настоящий список условий и следующий отказ от   ')
    print('      ответственности в документации и/или других материалах, поставляемых вместе с дис-   ')
    print('      трибутивом.                                                                          ')
    print('   3. Ни имя владельца авторских прав, ни имена его участников не могут использоваться     ')
    print('      для поддержки или продвижения продуктов, созданных на основе этого программного      ')
    print('      обеспечения, без специального предварительного письменного разрешения.               ')
    print('                                                                                           ')
    print('   ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ ОБЛАДАТЕЛЯМИ АВТОРСКИХ ПРАВ И УЧАСТНИ-   ')
    print('   КАМИ «КАК ЕСТЬ», И ЛЮБЫЕ ЯВНЫЕ ИЛИ ПОДРАЗУМЕВАЕМЫЕ ГАРАНТИИ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИ-   ')
    print('   ВАЯСЬ, ПОДРАЗУМЕВАЕМЫМИ ГАРАНТИЯМИ ТОВАРНОЙ ГОДНОСТИ И ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННОЙ     ')
    print('   ЦЕЛИ, ОТКАЗЫВАЮТСЯ. НИ В КОЕМ СЛУЧАЕ ВЛАДЕЛЕЦ АВТОРСКОГО ПРАВА НЕ НЕСЕТ ОТВЕТСТВЕННО-   ')
    print('   СТИ ЗА ЛЮБЫЕ ПРЯМЫЕ, КОСВЕННЫЕ, СЛУЧАЙНЫЕ, ОСОБЫЕ, ПРИМЕРНЫЕ ИЛИ КОСВЕННЫЕ УБЫТКИ       ')
    print('   (ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ, ЗАКУПКУ ЗАМЕНИТЕЛЬНЫХ ТОВАРОВ ИЛИ УСЛУГ; ПОТЕРЯ ИСПО-    ')
    print('   ЛЬЗОВАНИЯ, ДАННЫЕ ИЛИ ПРИБЫЛЬ; ИЛИ ПРЕРЫВАНИЕ ДЕЛОВОЙ ДЕЯТЕЛЬНОСТИ), КАКОЙ-ЛИБО ВЫЗ-    ')
    print('   ВАННОЙ, И НА ЛЮБОЙ ТЕОРИИ ОТВЕТСТВЕННОСТИ, КАК ДОГОВОР, СТРОГО ОТВЕТСТВЕННОСТЬ ИЛИ      ')
    print('   ПРАВОНАКТ (ВКЛЮЧАЯ НЕБРЕЖНОСТЬ ИЛИ ДРУГИЕ ОБРАЗЫ), ВОЗНИКАЮЩИЕ ЛЮБЫМ СПОСОБОМ ИСПО-     ')
    print('   ЛЬЗОВАНИЯ ЭТОГО ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ, ДАЖЕ ЕСЛИ УВЕДОМЛЕНЫ О ВОЗМОЖНОСТИ ТАКОГО     ')
    print('   УЩЕРБА.                                                                                 ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            reference()
        else:
            print('Команда не корректна или не существует!')

def about_the_program(): # Главное меню > О программе
    clear()
    print()
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print('         Опция: О программе                                                                ')
    print('   ─────────────────────────────────────────────────────────────────────────────────────   ')
    print()
    print('   Имя программы:           QESPy                                                          ')
    print('   Полное имя программы:    Quadratic Equation Solver in Python                            ')
    print('   Версия:                  Beta 2                                                         ')
    print('   Полная версия:           v2.5.15b                                                       ')
    print('   Номер сборки:            20112023                                                       ')
    print('   Оболочка:                Отсутствует                                                    ')
    print('   Ядро:                    IPython                                                        ')
    print('   Исполнитель:             Python3                                                        ')
    print('   Разработчик:             Moskvich2020                                                   ')
    print('   Цвета:                   Чёрно-белые                                                    ')
    print('   Тема:                    Dark                                                           ')
    print('   Иконка:                  Отсутствует                                                    ')
    print('   Система навигации:       Не определена                                                  ')
    print('   Размер консоли:          Не установлен                                                  ')
    print('   Интерфейс:               Текстовый                                                      ')
    print('   Язык:                    Русский                                                        ')
    print('   Хост:                    This PC                                                        ')
    print('   Консоль админа:          Откл.                                                          ')
    print('   Лицензия:                BSD 3-Clause License                                           ')
    print()
    while True:
        cmd = input('[E] Выход > ').lower()
        if cmd == 'e':
            main()
        else:
            print('Команда не корректна или не существует!')

main()
