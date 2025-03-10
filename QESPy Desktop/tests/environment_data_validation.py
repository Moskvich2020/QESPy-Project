import os

program_work_directory = os.path.dirname(os.path.abspath(__file__))

def integrity_validation():
    try:
        if not all(directory_name in os.listdir(program_work_directory) for directory_name in [
            'modules',
            'logs'
        ]):
            raise ValueError("В рабочей папке отсутствуют необходимые директории.")
        elif not all(file_name in os.listdir(program_work_directory) for file_name in [
            'config.json'
        ]):
            raise ValueError("В рабочей папке отсутствуют необходимые файлы.")
        else:
            print("Программа готова к работе.")
    except Exception as error:
        error_handling(error, 'integrity_validation')

integrity_validation()

def error_handling(error, position):
    print(f'Произошла ошибка в процессе {position}: {error}')
