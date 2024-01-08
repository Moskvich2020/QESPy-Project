# QuadraticEquationSolverPyAlpha2 [build 28102023]

print()
print('───────────────────────────────────────────────────────────────────')
print(' Добро пожаловать в QuadraticEquationSolverPyAlpha2                ')
print(' Программа готова к решению квадратного уравнения вида ax²+bx+c=0! ')
print(' ───────────────────────────────────────────────────────────────── ')
print(' Пожалуйста, введите коэффициенты...                               ')
print('───────────────────────────────────────────────────────────────────')
print()
coefficient_a = int(input('Введите a: '))
coefficient_b = int(input('Введите b: '))
coefficient_c = int(input('Введите c: '))
if not coefficient_a: # a = 0
    solution_x = -(coefficient_c/coefficient_b)
    print('-----')
    print('x=', solution_x)
if not coefficient_b: # b = 0
    if coefficient_c/coefficient_a < 0:
        solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
        solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)
        print('-----')
        print('x1 = ', solution_x1)
        print('x2 = ', solution_x2)
    elif coefficient_c/coefficient_a < 0:
        solution_x = 0
        print('-----')
        print('x= ', solution_x)
    else:
        print('-----')
        print('Уравнение не имеет решений!')
if not coefficient_c: # c = 0
    solution_x1 = 0
    solution_x2 = -(coefficient_b/coefficient_a)
    print('-----')
    print('x1= ', solution_x1)
    print('x2= ', solution_x2)
if coefficient_a == 1: # a = 1
    if ((coefficient_b**2)/4) - coefficient_c > 0:
        solution_x1 = -(coefficient_b/2) - (((coefficient_b**2)/4) - coefficient_c)**(1/2)
        solution_x2 = -(coefficient_b/2) + (((coefficient_b**2)/4) - coefficient_c)**(1/2)
        print('-----')
        print('x1=', solution_x1)
        print('x2=', solution_x2)
    elif not ((coefficient_b**2)/4) - coefficient_c:
        solution_x = -(coefficient_b/2)
        print('-----')
        print('x=', solution_x)
    else:
        print('-----')
        print('Уравнение не имеет решений!')
if coefficient_a and coefficient_b and coefficient_c > 0: # Discriminant
    discriminant = (coefficient_b**2)-(4*coefficient_a*coefficient_c)
    if discriminant > 0:
        solution_x1 = (-coefficient_b-(discriminant**(1/2)))/(2*coefficient_a)
        solution_x2 = (-coefficient_b+(discriminant**(1/2)))/(2*coefficient_a)
        print('-----')
        print('D = ', discriminant)
        print('x1 = ', solution_x1)
        print('x2 = ', solution_x2)
    elif not discriminant:
        solution_x = (-coefficient_b)/(2*coefficient_a)
        print('-----')
        print('D = ', discriminant)
        print('x = ', solution_x)
    else:
        print('-----')
        print('D =', discriminant)
        print('Уравнение не имеет решений!')
