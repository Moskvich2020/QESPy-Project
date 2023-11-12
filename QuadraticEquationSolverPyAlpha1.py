# QuadraticEquationSolverPyAlpha1 [build 25102023]

print()
print('-------------------------------------------------------------------')
print(' Добро пожаловать в QuadraticEquationSolverPyAlpha1!')
print(' Программа готова к решению квадратного уравнения вида ax²+bx+c=0!')
print()
print(' Пожалуйста, введите коэффициенты...')
print('-------------------------------------------------------------------')
print()
coefficient_a = int(input('Введите a: '))
coefficient_b = int(input('Введите b: '))
coefficient_c = int(input('Введите c: '))
discriminant = (coefficient_b**2)-(4*coefficient_a*coefficient_c);
if discriminant > 0:
    solution_x1 = (-coefficient_b-(discriminant**(1/2)))/(2*coefficient_a)
    solution_x2 = (-coefficient_b+(discriminant**(1/2)))/(2*coefficient_a)
    print('-----')
    print('D = ', discriminant)
    print('x1 = ', solution_x1)
    print('x2 = ', solution_x2)
elif discriminant == 0:
    solution_x = (-coefficient_b)/(2*coefficient_a)
    print('-----')
    print('D = ', discriminant)
    print('x = ', solution_x)
else:
    print('-----')
    print('D =', discriminant)
    print('Уравнение не имеет решений!')
