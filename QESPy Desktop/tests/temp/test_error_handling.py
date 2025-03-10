import json

def error_handling(error, position):
    if isinstance(error, ValueError): # Некорректное значение
        match position:
            case 'func':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, FileNotFoundError): # Файл не найден
        match position:
            case 'func':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, KeyError): # Ключ не найден
        match position:
            case 'func':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, PermissionError): # Ошибка доступа
        match position:
            case 'func':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, IsADirectoryError): # Это каталог
        match position:
            case 'func':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, SyntaxError): # Ошибка синтаксиса
        match position:
            case 'func':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, OSError): # Ошибка ОС. Возникает при других проблемах с файловой системой, таких как недоступность файла из-за проблем с диском
        match position:
            case 'func1':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    elif isinstance(error, json.JSONDecodeError): # Ошибка декодирования JSON
        match position:
            case 'func1':
                print(f'ОШИБКА: {type(error).__name__}!\n{error}')
    else:
        print(f'Неизвестная ошибка. Тип ошибки: {type(error).__name__}.')

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
