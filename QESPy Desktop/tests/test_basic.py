def decorator(func):
    def wrapper(a):
        print('Текст до функции...')
        func(a)
        print('Это текст после фунуции.')
    return wrapper

@ decorator
def functia(a: int):
    print(f'Это непосредственно функция... А сейчас {a} год...')

functia(2024)
