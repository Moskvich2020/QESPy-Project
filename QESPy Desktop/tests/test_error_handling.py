def error_handling(error, position):
    if isinstance(error, ValueError):
        match position:
            case 'func1':
                message = f'Ошибка в func1. Тип ошибки: {type(error).__name__}.'
            case 'func2':
                message = f'Ошибка в func2. Тип ошибки: {type(error).__name__}.'
            case 'settings_validation':
                message = 'ОШИБКА: Файл настроек повреждн!\n\nВыполните восстановление настроек!'
    elif isinstance(error, SyntaxError):
        match position:
            case 'func1':
                message = f'Ошибка в func1. Тип ошибки: {type(error).__name__}.'
            case 'func2':
                message = f'Ошибка в func2. Тип ошибки: {type(error).__name__}.'
            case 'func3':
                message = f'Ошибка в func3. Тип ошибки: {type(error).__name__}.'
                # message = f'Неизвестная ошибка. Тип ошибки: {type(exception).__name__}.'
    
    print(message)


def main():
    while True:
        try:
            while True:
                cmd = input('Введите команду: ')
                match cmd:
                    case '11':
                        position = 'func1'
                        raise ValueError('Некорректное значение')
                    case '12':
                        position = 'func1'
                        raise SyntaxError('Ошибка синтаксиса')
                    case '21':
                        position = 'func2'
                        raise ValueError('Некорректное значение')
                    case '22':
                        position = 'func2'
                        raise SyntaxError('Ошибка синтаксиса')
                    case '31':
                        position = 'func3'
                        raise SyntaxError('Ошибка синтаксиса')
                    case 'exit':
                        quit()
                    case _:
                        print('No command...')
                        break
        except Exception as error:
            error_handling(position, error)

main()
