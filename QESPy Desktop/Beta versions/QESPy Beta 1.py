# QESPy Beta 1 [build 04112023]

import os
import time

clear = lambda: os.system('cls')

def main(): # Главное меню
    clear()
    print()
    print('────────────────────────────────────────────────────────────────────────────')
    print('      Добро пожаловать в QESPy Beta 1!                                      ')
    print('      Программа готова к решению квадратных уравнений!                      ')
    print('      !ВНИМАНИЕ! ЭТО BETA ВЕРСИЯ!                                           ')
    print('      !Некоторые функции прогаммы могут быть недоступны или не работать!    ')
    print('      ─────────────────────────────────────────────────────────────────     ')
    print('           Выберете опцию:                                                  ')
    print('      [1] Решение квадратного уравнения (ax²+bx+c=0)                        ')
    print('      [2] Решение биквадратного уравнения (ax⁴+bx²+c=0)                     ')
    print('      [3] Справка                                                           ')
    print('      [4] О программе                                                       ')
    print('      [E] Выход                                                             ')
    print('────────────────────────────────────────────────────────────────────────────')
    print('   Пожалуйста, введите номер опции из меню [1, 2, 3, 4, 5]...               ')
    print()
    while True:
        cmd = input('> ')
        if cmd == '1':
            clear()
            solving_a_quadratic_equation()
        elif cmd == '2':
            clear()
            solution_of_biquadratic_equation()
        elif cmd == '3':
            clear()
            reference()
        elif cmd == '4':
            about_the_program()
        elif cmd == 'Exit':
            quit()
        elif cmd == 'exit':
            quit()
        elif cmd == 'E':
            quit()
        elif cmd == 'e':
            quit()
        else:
            print()
            print('Команда не корректна или не существует!')
            print()

def solving_a_quadratic_equation(): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0)
    print()
    print('────────────────────────────────────────────────────────────────────────────')
    print('      Опция: Решение квадратного уравнения (ax²+bx+c=0)                     ')
    print('────────────────────────────────────────────────────────────────────────────')
    print()
    while True:
        coefficient_a = int(input('Введите a: '))
        coefficient_b = int(input('Введите b: '))
        coefficient_c = int(input('Введите c: '))
        print()
        if not coefficient_a: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a = 0
            solution_x = -(coefficient_c/coefficient_b)
            print('──────────')
            print('Принято уравнение вида bx+c=0.')
            print('Ответ: ', 'x=', solution_x, '.', sep='')
            print('──────────')
            print()
            time.sleep(5)
        if not coefficient_b: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > b = 0
            if coefficient_c/coefficient_a < 0:
                solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
                solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)
                print('──────────')
                print('Принято уравнение вида ax²+c=0.')
                print('Ответ: ', 'x1=', solution_x1, ';', sep='')
                print('       ', 'x2=', solution_x2, '.', sep='')
                print('──────────')
                print()
                time.sleep(5)
            elif coefficient_c/coefficient_a == 0:
                solution_x = 0
                print('──────────')
                print('Принято уравнение вида ax²+c=0.')
                print('Ответ: ', 'x=', solution_x,'.', sep='')
                print('──────────')
                print()
                time.sleep(5)
            else:
                print('──────────')
                print('Принято уравнение вида ax²+c=0.')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(5)
        if not coefficient_c: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c = 0
            solution_x1 = 0
            solution_x2 = -(coefficient_b/coefficient_a)
            print('──────────')
            print('Принято уравнение вида ax²+bx=0.')
            print('Ответ: ', 'x1=', solution_x1, ';', sep='')
            print('       ', 'x2=', solution_x2, '.', sep='')
            print('──────────')
            print()
            time.sleep(5)
        if coefficient_a == 1: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > a = 1
            if ((coefficient_b**2)/4) - coefficient_c > 0:
                solution_x1 = -(coefficient_b/2) - (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                solution_x2 = -(coefficient_b/2) + (((coefficient_b**2)/4) - coefficient_c)**(1/2)
                print('──────────')
                print('Принято уравнение вида x²+px+q=0.')
                print('Ответ: ', 'x1=', solution_x1, ';', sep='')
                print('       ', 'x2=', solution_x2, '.', sep='')
                print('──────────')
                print()
                time.sleep(5)
            elif not ((coefficient_b**2)/4) - coefficient_c:
                solution_x = -(coefficient_b/2)
                print('──────────')
                print('Принято уравнение вида x²+px+q=0.')
                print('x=', solution_x)
                print('──────────')
                print()
                time.sleep(5)
            else:
                print('──────────')
                print('Принято уравнение вида x²+px+q=0.')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(5)
        if coefficient_a and coefficient_b and coefficient_c > 0: # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > Discriminant
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
                time.sleep(5)
            elif not discriminant:
                solution_x = (-coefficient_b) / (2*coefficient_a)
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant, '.', sep='')
                print('Ответ: ', 'x=', solution_x, '.', sep='')
                print('──────────')
                time.sleep(5)
                print()
            else:
                print('──────────')
                print('Принято уравнение вида ax²+bx+c=0.')
                print('Дискриминант = ', discriminant, '.', sep='')
                print('Уравнение не имеет решений!')
                print('──────────')
                print()
                time.sleep(5)

def solution_of_biquadratic_equation(): # Главное меню > Решение биквадратного уравнения (ax⁴+bx²+c=0)
    print()
    print('────────────────────────────────────────────────────────────────────────────')
    print('      Опция: Решение биквадратного уравнения (ax⁴+bx²+c=0)                  ')
    print('────────────────────────────────────────────────────────────────────────────')
    print()
    while True:
        coefficient_biq_a = int(input('Введите a: '))
        coefficient_biq_b = int(input('Введите b: '))
        coefficient_biq_c = int(input('Введите c: '))
        print()
        if coefficient_biq_a and coefficient_biq_b and coefficient_biq_c > 0:
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
            print('Error!')
            print('Какой-то из коэффицентов равен нулю. Программа покамест не умеет работать с такими коэффицентами.')

def about_the_program(): # Главное меню > О программе
    print()
    print('────────────────────────────────────────────────────────────────────────────')
    print('      Опция: О программе                                                    ')
    print('────────────────────────────────────────────────────────────────────────────')
    print()
    while True:
        cmd = input('> ')
        if cmd == 'e':
            main()
        else:
            print('Error! No comand!')

def reference(): # Главное меню > Справка
    print()
    print('────────────────────────────────────────────────────────────────────────────')
    print('      Опция: Справка                                                        ')
    print('────────────────────────────────────────────────────────────────────────────')
    print()
    while True:
        cmd = input('> ')
        if cmd == 'e':
            main()
        else:
            print('Error! No comand!')

main()
