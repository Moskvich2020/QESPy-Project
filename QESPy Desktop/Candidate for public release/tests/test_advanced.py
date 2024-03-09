var1 = 2.00
var2 = 3.14

sol1 = f'{int(var1)}' if var1.is_integer() else f'{var1}'
sol2 = f'{int(var2)}' if var2.is_integer() else f'{var2}'

print(sol1, sol2)
