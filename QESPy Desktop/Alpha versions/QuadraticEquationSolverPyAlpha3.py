# QuadraticEquationSolverPyAlpha3 [build 02112023]

import time

print()
print('───────────────────────────────────────────────────────────────────')
print(' Добро пожаловать в QuadraticEquationSolverPyAlpha3                ')
print(' Программа готова к решению квадратного уравнения вида ax²+bx+c=0! ')
print(' ───────────────────────────────────────────────────────────────── ')
print(' Пожалуйста, введите коэффициенты...                               ')
print('───────────────────────────────────────────────────────────────────')
print()
coefficient_a = int(input('Введите a: '))
coefficient_b = int(input('Введите b: '))
coefficient_c = int(input('Введите c: '))
print()
if not coefficient_a: # a = 0
    solution_x = -(coefficient_c/coefficient_b)
    print('──────────')
    print('Принято уравнение вида bx+c=0.')
    print('Ответ: ', 'x=', solution_x, '.', sep='')
    print()
    time.sleep(5)
if not coefficient_b: # b = 0
    if coefficient_c/coefficient_a < 0:
        solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
        solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)
        print('──────────')
        print('Принято уравнение вида ax²+c=0.')
        print('Ответ: ', 'x1=', solution_x1, ';', sep='')
        print('       ', 'x2=', solution_x2, '.', sep='')
        time.sleep(5)
    elif coefficient_c/coefficient_a == 0:
        solution_x = 0
        print('──────────')
        print('Принято уравнение вида ax²+c=0.')
        print('Ответ: ', 'x=', solution_x,'.', sep='')
        time.sleep(5)
    else:
        print('──────────')
        print('Принято уравнение вида ax²+c=0.')
        print('Уравнение не имеет решений!')
        time.sleep(5)
if not coefficient_c: # c = 0
    solution_x1 = 0
    solution_x2 = -(coefficient_b/coefficient_a)
    print('──────────')
    print('Принято уравнение вида ax²+bx=0.')
    print('Ответ: ', 'x1=', solution_x1, ';', sep='')
    print('       ', 'x2=', solution_x2, '.', sep='')
    time.sleep(5)
if coefficient_a == 1: # a = 1
    if ((coefficient_b**2)/4) - coefficient_c > 0:
        solution_x1 = -(coefficient_b/2) - (((coefficient_b**2)/4) - coefficient_c)**(1/2)
        solution_x2 = -(coefficient_b/2) + (((coefficient_b**2)/4) - coefficient_c)**(1/2)
        print('──────────')
        print('Принято уравнение вида x²+px+q=0.')
        print('Ответ: ', 'x1=', solution_x1, ';', sep='')
        print('       ', 'x2=', solution_x2, '.', sep='')
        time.sleep(5)
    elif not ((coefficient_b**2)/4) - coefficient_c:
        solution_x = -(coefficient_b/2)
        print('──────────')
        print('Принято уравнение вида x²+px+q=0.')
        print('x=', solution_x)
        time.sleep(5)
    else:
        print('──────────')
        print('Принято уравнение вида x²+px+q=0.')
        print('Уравнение не имеет решений!')
        time.sleep(5)
if coefficient_a and coefficient_b and coefficient_c > 0: # Discriminant
    discriminant = (coefficient_b**2) - (4*coefficient_a*coefficient_c)
    if discriminant > 0:
        solution_x1 = (-coefficient_b - (discriminant**(1/2))) / (2*coefficient_a)
        solution_x2 = (-coefficient_b + (discriminant**(1/2))) / (2*coefficient_a)
        print('──────────')
        print('Принято уравнение вида ax²+bx+c=0.')
        print('Discriminant = ', discriminant, '.', sep='')
        print('Ответ: ', 'x1=', solution_x1, ';', sep='')
        print('       ', 'x2=', solution_x2, '.', sep='')
        time.sleep(5)
    elif not discriminant:
        solution_x = (-coefficient_b) / (2*coefficient_a)
        print('──────────')
        print('Принято уравнение вида ax²+bx+c=0.')
        print('Discriminant = ', discriminant, '.', sep='')
        print('Ответ: ', 'x=', solution_x, '.', sep='')
        time.sleep(5)
    else:
        print('──────────')
        print('Принято уравнение вида ax²+bx+c=0.')
        print('Discriminant = ', discriminant, '.', sep='')
        print('Уравнение не имеет решений!')
        time.sleep(5)
