
# ╭──────────────────────────────────────────╮
# │ Name: QESPy Desktop                      │
# │ Version: 0.8.0                           │ 
# │ Build: 23072024                          │ 
# │ Build Date: 23-07-2024 7:00 PM           │ 
# │ Author: Cristi Constantin (Moskvich2020) │ 
# │ License: MAF Original License            │ 
# ╰──────────────────────────────────────────╯

import json
import logging
import msvcrt
import os
import sys
import time
import winreg

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

# os.system('mode 125, 30')

# TODO: Навести порядок в новом коде.
# TODO: Задокументировать новые функции.
# TODO: Добавить логгеры в ключевые места функций.
# TODO: Добавить красивую отладочную информацию.
# TODO: Добавить валидацию и восстановление настроек.

# ! MAIN доработать!!!

def main(): # main
    '''
    Функция main является точкой входа в данной программе.

    Описание:
        1.  Очищает консоль.
        2.  Выводит интерфейс командной строки программы QESPy Desktop и после
            полусекундной задержки вызывает функцию main_menu - главное меню
            программы.

    '''
    global script_dir, json_path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'settings.json')

    os.system('cls')
    print('Quadratic Equation Solver in Python [Version 0.8.0]')
    print('(c) Cristi Constantin (Moskvich2020), QESPy Project. Все права защищены.\n')

    time.sleep(1)
    print(f'{os.getcwd()}>load\n')
    print('Определение абсолютного пути к директории программы...')
    time.sleep(1)
    print(f'Абсолютный путь определён: {script_dir}')
    time.sleep(1)

    print('Настройка логгирования...')
    setup_loggers()
    time.sleep(0.5)
    print('   Логгирование событий: НАСТРОЕНО\n   Логгирование ошибок: НАСТРОЕНО')
    time.sleep(1)

    print('Загрузка настроек...')
    load_settings()
    time.sleep(2)

    print('Загрузка пользовательского интерфейса...')
    time.sleep(3)
    main_menu()


def setup_loggers():
    global event_logger, error_logger

    event_logger = logging.getLogger('event_logger')
    event_logger.setLevel(logging.DEBUG)
    event_handler = logging.FileHandler(os.path.join(script_dir, 'events.log'), encoding='utf-8')
    event_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    event_handler.setFormatter(event_formatter)
    event_logger.addHandler(event_handler)

    error_logger = logging.getLogger('error_logger')
    error_logger.setLevel(logging.ERROR)
    error_handler = logging.FileHandler(os.path.join(script_dir, 'errors.log'), encoding='utf-8')
    error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s', datefmt='%d.%m.%Y %H:%M:%S')
    error_handler.setFormatter(error_formatter)
    error_logger.addHandler(error_handler)


def load_settings():
    def get_windows_theme():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
            value, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')
            winreg.CloseKey(key)

            if value == 0:
                return True # Тёмная тема
            else:
                return False # Светлая тема
        except Exception as error:
            error_handling(error, position='get_windows_theme')

    global settings_data

    print(f'   Текущий файл настроек: {json_path}')
    time.sleep(0.5)
    print('   Чтение и загрузка настроек...')
    time.sleep(2)
    
    try:
        with open(json_path, 'r') as json_file:
            settings_data = json.load(json_file)

        print('   Настройки успешно загруженны!')
        time.sleep(1)

    except Exception as error:
        error_handling(error, 'load_settings_process')

    try:
        if settings_data['set_theme'] == 'system':
            if get_windows_theme():
                theme = Theme(settings_data['theme']['dark'])

                print('   Загрузка системной темы...\n   Тёмная тема включена!')
            else:
                theme = Theme(settings_data['theme']['light'])

                print('   Загрузка системной темы...\n   Светлая тема включена!')
        elif settings_data['set_theme'] == 'dark':
            theme = Theme(settings_data['theme']['dark'])

            print('   Загрузка темы...\n   Тёмная тема включена!')
        elif settings_data['set_theme'] == 'light':
            theme = Theme(settings_data['theme']['light'])

            print('   Загрузка темы...\n   Светлая тема включена!')
        else:
            error_handling(error=NameError, position='set_theme')

        global console
        console = Console(theme=theme)

        print(f'   Консоль инициализирована: {console}')

    except Exception as error:
        error_handling(error, 'load_settings')



def error_handling(error, position):
    if isinstance(error, FileNotFoundError):
        match position:
            case 'load_settings_process':
                print('ОШИБКА: Файл настроек не найден!\n')
                print('В рабочей папки программы не найдены настройки.\n')
                print('Для исправления этой проблеммы выполните следующие шаги и перезапустите программу:')
                print('1. Если вы НЕ выполняли никаких действий с файлом настроек, восстановите его полной')
                print('   переустановкой программы, либо, если вы уверенны в том, что делайте, восстановите')
                print('   его отдельно из установочных файлов.\n')
                print('   ПРЕДУПРЕЖДЕНИЕ: После восстановления файла настроек, старые настройки, естественно,')
                print('                   не сохранятся!\n')
                print('2. Если вы выполняли какие-то действия над файлом настроек (перемещение/удаление/редактирование),')
                print('   то верните, по возможности, верните статус-кво и перезапустите программу. Если восстановить')
                print('   статус-кво не удастся, следуйте шагам из пункта 1.\n')
                print('Для прерывания загрузки нажмите любую клавишу...')
                msvcrt.getch()
                quit()
            case 'get_windows_theme':
                print('ОШИБКА: Не удалось определить системную тему!\n')
                print(r'Ключ реестра "AppsUseLightTheme" по адресу "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"')
                print('не обнаружен. Возможно, он повреждён или находится по другому адресу...\n')
                print('Для прерывания загрузки нажмите любую клавишу...')
                msvcrt.getch()
                quit()
    elif isinstance(error, NameError):
        match position:
            case 'set_theme':
                print('ОШИБКА: Неизвестное имя темы!\n')
                print('В файле настроек указана неизвестная тема.\n')
                print('Для исправления этой проблеммы выполните следующие шаги, после рограмма будет автоматически перезапущенна:')
                print('1. Если вы изменяли файл настроек, то верните, по возможности, верните статус-кво и перезапустите')
                print('программу. Если восстановить статус-кво не удастся, следуйте шагам из пункта 2.\n')
                print('ПРЕДУПРЕЖДЕНИЕ: Если вы не уверенны в том, что делайте, не изменяйте файл настроек вручную,')
                print('                а воспользуйтесь методом автоматической перезаписи из пункта 2!\n')
                print('2. Если вы НЕ изменяли файл настроек, либо НЕ можете после изменения восстановить статус-кво, введите')
                print('   "rewrite", чтобы выбрать настройку темы вручную и автоматически перезаписать её, либо "exit", чтобы')
                print('   выйти из программы. После загрузки запустите утилиту восстановления настроек.')
                while True:
                    cmd = input('>').lower()
                    if cmd == 'system':
                        settings_data['set_theme'] = 'system'
                        main()
                    elif cmd == 'light':
                        settings_data['set_theme'] = 'light'
                        main()
                    elif cmd == 'dark':
                        settings_data['set_theme'] = 'dark'
                        main()
                    elif cmd == 'exit':
                        quit()
                    else:
                        print('Команда некорректна или не существует!')
    elif isinstance(error, ValueError):
        match position:
            case 'load_settings_process':
                print('ОШИБКА: Данные настроек поврежденны!\n')
                print('В файле настроек указана неверные значения.\n')
                print('Восстановить настройки поумолчанию? [Y/N]')
                while True:
                    pressed_key = msvcrt.getch().lower()
                    if ord(pressed_key) == ord('y'):
                        pass
                    elif ord(pressed_key) == ord('n'):
                        pass
                    else:
                        print('Команда некорректна или не существует!')
    
    else:
        match position:
            case 'load_settings':
                print(f'Произошла неизвестная ошибка!!! {error}')


def main_menu(): # Главное меню
    '''
    Функция main_menu отвечает за пользовательский интерфейс главного меню и
    выбор опций.

    Описание:
        1.  Очищает консоль.
        2.  Выводит главное меню программы.
        3.  Содержит цикл while с функцией getch для отслеживания нажатой
            клавиши для выбора опции.
        4.  Имеет 7 опций:
            a. Решение квадратного уравнения (ax²+bx+c=0);
            b. Решение биквадратного уравнения (ax⁴+bx²+c=0);
            c. Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂));
            d. Терминал;
            e. Настройки;
            f. Справка;
            g. Выйти из программы.

    '''
    os.system('cls')
    main_menu_title_panel = Panel(
        Text(
            text='\nДобро пожаловать в QESPy Desktop!\n',
            justify='center'
        ),
        title='ГЛАВНОЕ МЕНЮ',
        subtitle='(c) Cristi Constantin (Moskvich2020) QESPy Project',
        subtitle_align='left',
    )
    main_menu_panel = Panel(
        Text(
            text='''
[1]    Решение квадратного уравнения (ax²+bx+c=0)
[2]    Решение биквадратного уравнения (ax⁴+bx²+c=0)
[3]    Разложение квадратного уравнения (ax²+bx+c=a(x-x₁)(x-x₂))
[4]    Терминал
[5]    Настройки
[6]    Справка
[E]    Выйти из программы
            '''
        ),
        title='ГЛАВНОЕ МЕНЮ',
        subtitle='Пожалуйста, введите идентификатор опции из меню...',
        subtitle_align='left',
    )

    console.print(main_menu_title_panel)
    console.print(main_menu_panel)
    
    while True:
        pressed_key = msvcrt.getch().lower()
        if ord(pressed_key) == ord('1'):
            solving_a_quadratic_equation()
        elif ord(pressed_key) == ord('2'):
            pass
        elif ord(pressed_key) == ord('3'):
            pass
        elif ord(pressed_key) == ord('4'):
            pass
        elif ord(pressed_key) == ord('5'):
            pass
        elif ord(pressed_key) == ord('6'):
            pass
        elif ord(pressed_key) == ord('e'):
            sys.exit()
            # quit()
        else:
            console.print('\n[error]Команда некорректна или не существует![/]\n')


def solving_a_quadratic_equation(): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0)
    '''
    Функция solving_a_quadratic_equation отвечает за решение всех видов
    квадратного уравнения.

    Содержит в себе вложенные функции для более структурированного и логично
    построенного алгоритма решения квадратного уравнения. Сама по себе
    функция является лишь оболочкой для других функций, выполняющих
    непосредственно решение уравнения.

    Функция так же способна решать и линейные уравнения (когда коэффициент a
    равен нулю). При этом, после решения, выводится сообщение о том, что
    полученное уравнение линейное, так как наибольшая степень в нём первая.

    Каждая вложенная функция принимает необходимые для решения уравнения
    коэффициенты (не принимаются нули, так как они не участвуют в процессе
    решения). После принятия аргументов функция подставляет коэффициенты в
    формулы и вычисляет корни уравнения, либо, если существование решений
    зависит от какого-то условия, проверяет это условие, после аналогично
    подставляет в формулу. Далее выполняется генерация строк для вывода
    решения в зависимости от коэффициентов. После функция предлагает
    продолжить решение или выйти из опции.

    Описание:
        1.  Очищает консоль.
        2.  Выводит заголовок опции.
        3.  Вызывает функцию reading_coefficients для считывания коэффициентов. 

    Вложенные функции:
        reading_coefficients: считывание коэффициентов 
        solving_a_quadratic_equation_1: решение линейного уравнения вида bx+c=0
        solving_a_quadratic_equation_2: решение неполного квадратного уравнения вида ax²+c=0
        solving_a_quadratic_equation_3: решение неполного квадратного уравнения вида ax²+bx=0
        solving_a_quadratic_equation_4: решение равенства вида c=0
        solving_a_quadratic_equation_5: решение линейного уравнения вида bx=0
        solving_a_quadratic_equation_6: решение неполного квадратного уравнения вида ax²=0
        solving_a_quadratic_equation_7: решение равенства вида 0=0
        solving_a_quadratic_equation_8: решение приведённого квадратного уравнения вида x²+px+q=0
        solving_a_quadratic_equation_9: решение квадратного уравнения вида ax²+bx+c=0

    '''
    os.system('cls')
    console.print(Panel(Text(text='Решение квадратного уравнения (ax²+bx+c=0)', justify='center'), title='Опция №1'))

    def action_menu_decorator(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            time.sleep(1)
            while True:
                print('[N] Продолжить, [E] Выход')
                pressed_key = msvcrt.getch().lower()
                if ord(pressed_key) == ord('n'):
                    print()
                    break
                elif ord(pressed_key) == ord('e'):
                    main_menu()
                else:
                    console.print('\n[red]Команда некорректна или не существует![/]\n')

        return wrapper

    def reading_coefficients():
        '''
        Функция reading_coefficients() отвечает за считывание коэффициентов.

        Описание:
            1.  Считывает по очереди коэффициенты.
            2.  После считывания каждого коэффициента, запускается цикл while с
                обработчиком ошибок, внутри которого происходит преобразование типа
                данного считаного коэффициента с типа string на тип float. После идёт
                проверка, является ли коэффициент целочисленный и при истинности условия
                преобразовывает коэффициент в тип integer. Это сделано для более
                презентабельного отображения коэффициентов в блоке с решением уравнения.
                Коэффициенты выводятся с двумя знаками после запятой. Во время выполнения
                этих преобразований обработчик ошибок отслеживает исключение ValueError.
                Это сделано на тот случай если пользователь введёт вместо числа строку.
                При возникновении данной ошибки пользователю выводится сообщение об ошибке
                и предлагается ввести коэффициент ещё раз. Если ошибок не возникает,
                происходит выход из цикла и продолжение выполнение кода.
            3.  Определяет тип квадратного уравнения и вызывает функцию для решения
                этого типа квадратного уравнения, предавая коэффициенты как аргументы.

        Внутренние переменные:
            coefficient_a: коэффициент a
            coefficient_b: коэффициент b
            coefficient_c: коэффициент c
        
        '''
        while True:
            while True:
                try:
                    coefficient_a = float(input('   Введите коэффициент a: '))
                    if coefficient_a.is_integer():
                        coefficient_a = int(coefficient_a)
                    break
                except ValueError:
                    console.print('\n[red]Ошибка! Коэффициент a не является числом! Введите, пожалуйста, ещё раз число![/]')
                    console.print('[italic red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
            while True:
                try:
                    coefficient_b = float(input('   Введите коэффициент b: '))
                    if coefficient_b.is_integer():
                        coefficient_b = int(coefficient_b)
                    break
                except ValueError:
                    console.print('\n[red]Ошибка! Коэффициент b не является числом! Введите, пожалуйста, ещё раз число![/]')
                    console.print('[italic red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
            while True:
                try:
                    coefficient_c = float(input('   Введите коэффициент c: '))
                    if coefficient_c.is_integer():
                        coefficient_c = int(coefficient_c)
                    break
                except ValueError:
                    console.print('\n[red]Ошибка! Коэффициент c не является числом! Введите, пожалуйста, ещё раз число![/]')
                    console.print('[italic red]Примечание: старайтесь использовать целочисленные коэффициенты с не более чем двумя цифрами после запятой и со значением не более 1000. Обязательно разделяйте целую часть числа от дробной точкой (".").[/]\n')
            
            if not coefficient_a and coefficient_b != 0 and coefficient_c != 0:
                solving_a_quadratic_equation_1(coefficient_b, coefficient_c)
            elif coefficient_a != 0 and not coefficient_b and coefficient_c != 0:
                solving_a_quadratic_equation_2(coefficient_a, coefficient_c)
            elif coefficient_a != 0 and coefficient_b != 0 and not coefficient_c:
                solving_a_quadratic_equation_3(coefficient_a, coefficient_b)
            elif not coefficient_a and not coefficient_b and (coefficient_c != 0 or not coefficient_c):
                solving_a_quadratic_equation_4(coefficient_c)
            elif not coefficient_a and coefficient_b != 0 and not coefficient_c:
                solving_a_quadratic_equation_5(coefficient_b)
            elif coefficient_a != 0 and not coefficient_b and not coefficient_c:
                solving_a_quadratic_equation_6(coefficient_a)
            elif abs(coefficient_a) == 1 and coefficient_b != 0 and coefficient_c != 0:
                solving_a_quadratic_equation_7(coefficient_a, coefficient_b, coefficient_c)
            else:
                solving_a_quadratic_equation_8(coefficient_a, coefficient_b, coefficient_c)

    @action_menu_decorator
    def solving_a_quadratic_equation_1(coefficient_b, coefficient_c): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx+c=0 | a = 0
        '''
        Функция solving_a_quadratic_equation_1 отвечает за решениел инейного
        уравнения вида bx+c=0.

        Описание:
            1.  Принимает аргументы.
            2.  Находит решения.
            3.  Генерирует строки для вывода решения в зависимости от коэффициентов.
            4.  Выводит решение.
            5.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_b: коэффициент b
            coefficient_c: коэффициент c

        Внутренние переменные:
            solution_x: корень уравнения
            coef_b_str: форматированный коэффициент b для вывода в блоке решения
            coef_c_str: форматированный коэффициент c для вывода в блоке решения
            sol_x_str: форматированный корень уравнения для вывода в строке с ответом
            auxiliary_line_1: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_2: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_3: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line: вспомогательная строка для вывода данных в блоке решения,
                                определяющая дальнейшее действие в зависимости от модуля
                                коэффициента b

        Алгоритм решения:
            bx+c=0
            │└ |b| ≠ 1
            │  bx=-c
            │  bx=-c |÷b
            │  x=-c/b
            └─ |b| = 1
                x=-c

        '''
        solution_x = -(coefficient_c/coefficient_b)

        coef_b_str = f'{coefficient_b}x' if abs(coefficient_b) != 1 else ('x' if coefficient_b == 1 else '-x')
        coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
        sol_x_str = f'{int(solution_x)}' if solution_x.is_integer() else f'{solution_x:.2f}'
        auxiliary_line_sol = f'\n              x = {sol_x_str}'
        auxiliary_line_1 = f'\n              x = -({coefficient_c} / {coefficient_b}){auxiliary_line_sol}' if coefficient_b > 0 and coefficient_c > 0 else (f'\n              x = {coefficient_c} / {-coefficient_b}{auxiliary_line_sol}' if coefficient_b < 0 and coefficient_c > 0 else (f'\n              x = {-coefficient_c} / {coefficient_b}{auxiliary_line_sol}' if coefficient_b > 0 and coefficient_c < 0 else f'\n              x = -({-coefficient_c} / {-coefficient_b}){auxiliary_line_sol}'))
        auxiliary_line_2 = f'{coef_b_str} = {-coefficient_c}\n              {coef_b_str} = {-coefficient_c} | × (-1){auxiliary_line_sol}' if coefficient_b < 0 else f'x = {sol_x_str}'
        auxiliary_line_3 = f'\n              {coef_b_str} = {-coefficient_c} | ÷ {coefficient_b}{auxiliary_line_1}' if coefficient_b > 0 else f'\n              {coef_b_str} = {-coefficient_c} | ÷ ({coefficient_b}){auxiliary_line_1}'
        auxiliary_line = f'{coef_b_str} = {-coefficient_c}{auxiliary_line_3}' if abs(coefficient_b) != 1 else f'{auxiliary_line_2}'
        
        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято линейное уравнение вида bx+c=0        ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coef_b_str}{coef_c_str} = 0')
        print(f'   Решение:   {coef_b_str}{coef_c_str} = 0')
        print(f'              {auxiliary_line}')
        print(f'   Ответ:     x = {sol_x_str}')
        print('   ──────────────────────────────────────────────')
        print()
        console.print('[italic]Примечание: данное уравнение не является квадратным, а линейным (первой степени), так как наивысшая степень этого уравнения равна 1.[/]')
        print()

    @action_menu_decorator
    def solving_a_quadratic_equation_2(coefficient_a, coefficient_c): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+c=0 | b = 0
        '''
        Функция solving_a_quadratic_equation_2 отвечает за решение неполного
        квадратного уравнения вида ax²+c=0.

        Описание:
            1.  Принимает аргументы.
            2.  Проверяет существуют ли решения. Находит их, если они есть.
            3.  Генерирует строки для вывода решения в зависимости от коэффициентов.
            4.  Выводит решение.
            5.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a
            coefficient_c: коэффициент c

        Внутренние переменные:
            |a| ≠ 1:
                solution_x1: корень уравнения №1
                solution_x2: корень уравнения №2
                coef_a_str: форматированный коэффициент a для вывода в строке 'Дано'
                coef_c_str: форматированный коэффициент c для вывода в строке 'Дано'
                sol_x1_str: форматированный корень №1 уравнения для вывода в строке с ответом
                sol_x2_str: форматированный корень №2 уравнения для вывода в строке с ответом
                coef_a_sol_1: форматированный коэффициент a для вывода данных в блоке решения
                coef_c_sol_1: форматированный коэффициент c для вывода данных в блоке решения
                coef_c_sol_2: форматированный коэффициент c для вывода данных в блоке решения
                auxiliary_line_sol_1: вспомогательная строка для вывода данных в блоке решения
                auxiliary_line_sol_2: вспомогательная строка для вывода данных в блоке решения
                auxiliary_line_sol_3: вспомогательная строка для вывода данных в блоке решения
                auxiliary_line_sol: вспомогательная строка для вывода данных в блоке решения,
                                    определяющая дальнейшее действие в зависимости от модуля
                                    коэффициента a
                sol_x1_sol: вспомогательная строка для вывода корня №1 в блоке решения
                sol_x2_sol: вспомогательная строка для вывода корня №2 в блоке решения

            |a| = 1:
                solution_x: корень уравнения
                coef_a_str: форматированный коэффициент a для вывода в строке 'Дано'
                coef_c_str: форматированный коэффициент c для вывода в строке 'Дано'
                coef_a_sol: форматированный коэффициент a для вывода данных в блоке решения
                coef_c_sol: форматированный коэффициент c для вывода данных в блоке решения

        Алгоритм решения:
            ax²+c=0
            │└ c/a < 0
            │  │└ |a| ≠ 1
            │  │  ax²=-c
            │  │  ax²=-c | ÷ a
            │  │  x²=-(c/a)
            │  │  x=±√(-(c/a))
            │  └─ |a| = 1
            │     x²=-c
            │     x=±√(-c)
            └─ Уравнение не имеет решений!

        '''
        if (coefficient_c/coefficient_a) < 0:
            solution_x1 = (-(coefficient_c/coefficient_a))**(1/2)
            solution_x2 = -(-(coefficient_c/coefficient_a))**(1/2)

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            sol_x1_str = f'{int(solution_x1)}' if solution_x1.is_integer() else f'{solution_x1:.2f}'
            sol_x2_str = f'{int(solution_x2)}' if solution_x2.is_integer() else f'{solution_x2:.2f}'
            auxiliary_c_a = coefficient_c / coefficient_a
            auxiliary_line_1 = f'{int(auxiliary_c_a)}' if auxiliary_c_a.is_integer() else f'{auxiliary_c_a:.2f}'
            auxiliary_line_2 = f'{-coefficient_c}' if coefficient_c < 0 else f'({-coefficient_c})'
            auxiliary_line_3 = f'\n              x = ±√({auxiliary_line_1})' if coefficient_a < 0 else f'\n              x = ±√({-coefficient_c} / {coefficient_a})'
            auxiliary_line_4 = f'\n              x² = {auxiliary_line_1}{auxiliary_line_3}' if coefficient_a < 0 else f'\n              x² = {-coefficient_c} / {coefficient_a}{auxiliary_line_3}'
            auxiliary_line_5 = f'\n              {coef_a_str} = {-coefficient_c} | ÷ {coefficient_a}{auxiliary_line_4}' if coefficient_a > 0 else f'\n              {coef_a_str} = {-coefficient_c} | ÷ ({coefficient_a}){auxiliary_line_4}'
            auxiliary_line = f'{coef_a_str} = {-coefficient_c}{auxiliary_line_5}' if abs(coefficient_a) != 1 else f'x² = ±{auxiliary_line_2}\n              x = ±√{auxiliary_line_2}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+c=0     ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_c_str} = 0')
            print(f'   Решение:   {coef_a_str}{coef_c_str} = 0')
            print(f'              {auxiliary_line}')
            print(f'              x₁ = {sol_x1_str}')
            print(f'              x₂ = {sol_x2_str}')
            print(f'   Ответ:     x₁ = {sol_x1_str}')
            print(f'              x₂ = {sol_x2_str}')
            print('   ──────────────────────────────────────────────')
            print()
        else:
            solution_x = 'Уравнение не имеет решений!'

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+c=0     ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_c_str} = 0')
            print(f'   Решение:   {coef_a_str}{coef_c_str} = 0')
            print(f'              {coefficient_c} / {coefficient_a} > 0')
            print(f'   Ответ:     {solution_x}')
            print('   ──────────────────────────────────────────────')
            print()

    @action_menu_decorator
    def solving_a_quadratic_equation_3(coefficient_a, coefficient_b): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx=0 | c = 0
        '''
        Функция solving_a_quadratic_equation_3 отвечает за решение неполного
        квадратного уравнения вида ax²+bx=0.

        Описание:
            1.  Принимает аргументы.
            2.  Находит решения.
            3.  Генерирует строки для вывода решения в зависимости от коэффициентов.
            4.  Выводит решение.
            5.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a
            coefficient_b: коэффициент b

        Внутренние переменные:
            solution_x1: корень уравнения №1
            solution_x2: корень уравнения №2
            coef_a_str: форматированный коэффициент a для вывода в строке 'Дано'
            coef_b_str: форматированный коэффициент b для вывода в строке 'Дано'
            sol_x1_str: форматированный корень №1 уравнения для вывода в строке с ответом
            sol_x2_str: форматированный корень №2 уравнения для вывода в строке с ответом
            coef_a_sol_1: форматированный коэффициент a для вывода данных в блоке решения
            coef_a_sol_2: форматированный коэффициент a для вывода данных в блоке решения
            coef_b_sol_1: форматированный коэффициент b для вывода данных в блоке решения
            coef_b_sol_2: форматированный коэффициент b для вывода данных в блоке решения
            auxiliary_line_sol_1: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_2: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_3: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol: вспомогательная строка для вывода данных в блоке решения,
                                определяющая дальнейшее действие в зависимости от модуля
                                коэффициента a
            sol_x1_sol: вспомогательная строка для вывода корня №1 в блоке решения

        Алгоритм решения:
            ax²+bx=0
            │└ |a| ≠ 1
            │  ax²+bx=0
            │  x(ax+b)=0
            │  x₁=0
            │  x₂=ax+b=0
            │  x₂=ax=-b
            │  x₂=-b/a
            └─ |a| = 1
                x²+bx=0
                x(x+b)=0
                x₁=0
                x₂=x+b=0
                x₂=x=-b
                x₂=-b

        '''
        solution_x1 = 0
        solution_x2 = -(coefficient_b/coefficient_a)

        coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
        coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else (' + x' if coefficient_b == 1 else ' - x'))
        coef_a_str_1 = f'{coefficient_a}x' if abs(coefficient_a) != 1 else ('x' if coefficient_a == 1 else '-x')
        coef_b_str_1 = f' + {coefficient_b}' if coefficient_b > 0 else f' - {-coefficient_b}'
        sol_x1_str = f'{solution_x1}'
        sol_x2_str = f'{int(solution_x2)}' if solution_x2.is_integer() else f'{solution_x2:.2f}'
        auxiliary_line_1 = f'\n              x₂ = {int(solution_x2)}' if solution_x2.is_integer() else f'\n              x₂ = {solution_x2:.2f}'
        auxiliary_line_2 = f'\n              x₂ = {-coefficient_b} / {coefficient_a}{auxiliary_line_1}'
        auxiliary_line_3 = f'\n              x₂ = {coef_a_str_1} = {-coefficient_b} | ÷ {coefficient_a}{auxiliary_line_2}' if coefficient_a > 0 else f'\n              x₂ = {coef_a_str_1} = {-coefficient_b} | ÷ ({coefficient_a}){auxiliary_line_2}'
        auxiliary_line = f'x₂ = {coef_a_str_1} = {-coefficient_b}{auxiliary_line_3}' if abs(coefficient_a) != 1 else (f'x₂ = {-coefficient_b}' if coefficient_a > 0 else f'x₂ = {coefficient_b}')

        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято квадратное уравнение вида ax²+bx=0    ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coef_a_str}{coef_b_str} = 0')
        print(f'   Решение:   {coef_a_str}{coef_b_str} = 0')
        print(f'              x({coef_a_str_1}{coef_b_str_1}) = 0')
        print(f'              x₁ = {sol_x1_str}')
        print(f'              x₂ = {coef_a_str_1}{coef_b_str_1} = 0')
        print(f'              {auxiliary_line}')
        print(f'   Ответ:     x₁ = {sol_x1_str}')
        print(f'              x₂ = {sol_x2_str}')
        print('   ──────────────────────────────────────────────')
        print()

    @action_menu_decorator
    def solving_a_quadratic_equation_4(coefficient_c): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > c=0 | a и b = 0
        '''
        Функция solving_a_quadratic_equation_4 отвечает за решение равенства
        (линейного уравнения) вида c=0.

        Описание:
            1.  Принимает аргумент.
            2.  Проверяет равен ли коэффициент c нулю и в зависимости от этого
                определяет истинность равенства.
            3.  Выводит решение.
            4.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_c: коэффициент c

        Внутренние переменные:
            solution_x: корень уравнения

        Алгоритм решения:
            c=0
            │└ c≠0
            │  x∈∅
            └─ c=0
                x∈R

        '''
        if coefficient_c != 0:
            solution_x = 'Пустое множество!'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято линейное уравнение вида c=0           ')
            print('   ──────────────────────────────────────────────')
            print(f'   Ошибка! "{coefficient_c} = 0".')
            print('   Данное выражение не имеет смысла!')
            print(f'   Ответ: {solution_x}')
            print('   ──────────────────────────────────────────────')
            print()
            console.print('[italic]Примечание: данное равенство не является уравнением, так как содержит одну неизвестнную величину и очевидно.[/]')
            console.print('[italic]В данном случае, равенство c = 0 ложно, так как c ≠ 0.[/]')
            print()
        else:
            solution_x = 'x может быть любым числом.'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида 0=0         ')
            print('   ──────────────────────────────────────────────')
            print('   Дано:      0 = 0')
            print('   Решение:   x принадлежит R')
            print(f'   Ответ:     {solution_x}')
            print('   ──────────────────────────────────────────────')
            print()
            console.print('[italic]Примечание: данное равенство не является уравнением и очевидно, так как не содержит неизвестных величин и тривиально.[/]')
            console.print('[italic]В данном случае, равенство 0 = 0 верно и является интуитивно понятным и формально обоснованным утверждением, но с другой стороны не имеет смысла.[/]')
            print()

    @action_menu_decorator
    def solving_a_quadratic_equation_5(coefficient_b): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > bx=0 | a и c = 0
        '''
        Функция solving_a_quadratic_equation_5 отвечает за решение линейного
        уравнения вида bx=0.

        Описание:
            1.  Принимает аргумент.
            2.  Выводит решение.
            3.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_b: коэффициент b

        Внутренние переменные:
            solution_x: корень уравнения

        Алгоритм решения:
            0=0

        '''
        solution_x = 0

        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято линейное уравнение вида bx=0          ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coefficient_b}x = 0')
        print(f'   Решение:   x = {solution_x}')
        print(f'   Ответ:     x = {solution_x}')
        print('   ──────────────────────────────────────────────')
        print()
        console.print('[italic]Примечание: данное уравнение не является квадратным, а линейным (первой степени), так как наивысшая степень этого уравнения 1.[/]')
        print()

    @action_menu_decorator
    def solving_a_quadratic_equation_6(coefficient_a): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²=0 | b и c = 0
        '''
        Функция solving_a_quadratic_equation_6 отвечает за решение неполного
        квадратного уравнения вида ax²=0.

        Описание:
            1.  Принимает аргумент.
            2.  Выводит решения.
            3.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a

        Внутренние переменные:
            solution_x: корень уравнения
            auxiliary_line_sol: вспомогательная строка для вывода данных в блоке
            решения

        Алгоритм решения:
            ax²=0
            ax²=0 | ÷ a
            x²=0
            x=√0
            x=0

        '''
        solution_x = 0

        auxiliary_line_sol = f'{coefficient_a}x² = 0 | ÷ {coefficient_a}' if coefficient_a > 0 else f'{coefficient_a}x² = 0 | ÷ ({coefficient_a})'

        print()
        print('   ──────────────────────────────────────────────')
        print('   Принято квадратное уравнение вида ax²=0       ')
        print('   ──────────────────────────────────────────────')
        print(f'   Дано:      {coefficient_a}x² = 0')
        print(f'   Решение:   {coefficient_a}x² = 0')
        print(f'              {auxiliary_line_sol}')
        print('              x² = 0')
        print('              x = √0')
        print('              x = 0')
        print(f'   Ответ:     x = {solution_x}')
        print('   ──────────────────────────────────────────────')
        print()                

    @action_menu_decorator
    def solving_a_quadratic_equation_7(coefficient_a, coefficient_b, coefficient_c):  # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > x²+px+q=0 | a = 1, b и c ≠ 0 
        '''
        Функция solving_a_quadratic_equation_7 предназначена для решения
        приведённого квадратного уравнения вида x²+px+q=0.

        Описание:
            1.  Принимает аргументы.
            2.  Вычисляет приведённый дискриминант и определяет существуют ли решения.
            3.  Находит решения.
            4.  Генерирует строки для вывода решения в зависимости от коэффициентов.
            5.  Выводит решения.
            6.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a
            coefficient_b: коэффициент b
            coefficient_c: коэффициент c

        Внутренние переменные:
            reduced_discriminant: приведённый дискриминант
            x_str: форматированный коэффициент a для вывода в строке 'Дано'
            coef_p_str: форматированный коэффициент b для вывода в строке 'Дано'
            coef_q_str: форматированный коэффициент c для вывода в строке 'Дано'
            coef_p_red_dis: форматированный коэффициент b для вывода в блоке 'Решение',
                            в строке вычисления приведённого дискриминанта
            coef_q_red_dis: форматированный коэффициент b для вывода в блоке 'Решение',
                            в строке вычисления приведённого дискриминанта
            auxiliary_line_dis_1: вспомогательная строка для вывода данных в блоке 
                            нахождения приведённого дискриминанта
            auxiliary_line_dis_11: вспомогательная строка для вывода данных в блоке 
                            нахождения приведённого дискриминанта
            auxiliary_line_dis_2: вспомогательная строка для вывода данных в блоке 
                            нахождения приведённого дискриминанта
            auxiliary_line_dis_22: вспомогательная строка для вывода данных в блоке
                            нахождения приведённого дискриминанта
            reduced_discriminant_dis: форматирование приведённого дискриминанта для
                            вывода данных в блоке решения
            coef_p_sol: форматированный коэффициент b для вывода в блоке 'Решение'
            coef_q_sol: форматированный коэффициент b для вывода в блоке 'Решение'
            auxiliary_line_sol_1: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_sol_11: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_dis_sol_1: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_dis_sol_11: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_dis_sol_2: вспомогательная строка для вывода данных в блоке решения
            auxiliary_line_dis_sol_22: вспомогательная строка для вывода данных в блоке решения
            reduced_discriminant_sol: вывод форматированного приведённого дискриминанта в блоке решения
            sol_x_str: вспомогательная строка для вывода корня в блоке решения при D = 0
            sol_x1_str: вспомогательная строка для вывода корня №1 в блоке решения при D > 0
            sol_x1_str: вспомогательная строка для вывода корня №2 в блоке решения при D > 0

        Алгоритм решения:
            x²+px+q=0
            ││└ D > 0
            ││  D = b²/(4-c)
            ││  x₁ = -b/2+√(b²/(4-c))
            ││  x₂ = -b/2-√(b²/(4-c))
            │└ D = 0
            │  D = b²/(4-c)
            │  x = -b/2
            └ D < 0
            Уравнение не имеет решений!

        '''

        reduced_discriminant = coefficient_b**2 / 4 - coefficient_c

        if reduced_discriminant > 0:
            solution_x1 = -coefficient_b / 2 + (coefficient_b**2 / 4 - coefficient_c)**(1/2)
            solution_x2 = -coefficient_b / 2 - (coefficient_b**2 / 4 - coefficient_c)**(1/2)

            x_str = 'x²' if coefficient_a > 0 else '-x²'
            coef_p_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_q_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_p_str_1 = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_q_str_1 = f' - {coefficient_c}' if coefficient_c > 0 else f' + {-coefficient_c}'
            auxiliary_line_11 = coefficient_b**2
            auxiliary_line_1 = f'{int(auxiliary_line_11)}' if auxiliary_line_11.is_integer() else f'{auxiliary_line_11:.2f}'
            auxiliary_line_22 = coefficient_b**2 / 4
            auxiliary_line_2 = f'{int(auxiliary_line_22)}' if auxiliary_line_22.is_integer() else f'{auxiliary_line_22:.2f}'
            auxiliary_line_33 = -coefficient_b / 2
            auxiliary_line_3 = f'{int(auxiliary_line_33)}' if auxiliary_line_33.is_integer() else f'{auxiliary_line_33:.2f}'
            reduced_discriminant_str = f'{int(reduced_discriminant)}' if reduced_discriminant.is_integer() else f'{reduced_discriminant:.2f}'

            sol_x1_str = f'{int(solution_x1)}' if solution_x1.is_integer() else f'{solution_x1:.2f}'
            sol_x2_str = f'{int(solution_x2)}' if solution_x2.is_integer() else f'{solution_x2:.2f}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида x²+px+q=0   ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {x_str}{coef_p_str}{coef_q_str} = 0')
            print(f'   Решение:   D = {coef_p_str_1}² / 4{coef_q_str_1}')
            print(f'              D = {auxiliary_line_1} / 4{coef_q_str_1}')
            print(f'              D = {auxiliary_line_2}{coef_q_str_1}')
            print(f'              D = {reduced_discriminant_str}')
            print(f'              x = -({coefficient_b} / 2) ± √({coef_p_str_1}² / 4{coef_q_str_1})')
            print(f'              x = {auxiliary_line_3} ± √({auxiliary_line_1} / 4{coef_q_str_1})')
            print(f'              x = {auxiliary_line_3} ± √({auxiliary_line_2}{coef_q_str_1})')
            print(f'              x = {auxiliary_line_3} ± √{reduced_discriminant_str}')
            print(f'   Ответ:     x₁ = {sol_x1_str}')
            print(f'              x₂ = {sol_x2_str}')
            print('   ──────────────────────────────────────────────')
            print()
        elif not reduced_discriminant:
            solution_x = -coefficient_b / 2
            
            x_str = 'x²' if coefficient_a > 0 else '-x²'
            coef_p_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_q_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_p_str_1 = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_q_str_1 = f' - {coefficient_c}' if coefficient_c > 0 else f' + {-coefficient_c}'
            auxiliary_line_11 = coefficient_b**2
            auxiliary_line_1 = f'{int(auxiliary_line_11)}' if auxiliary_line_11.is_integer() else f'{auxiliary_line_11:.2f}'
            auxiliary_line_22 = coefficient_b**2 / 4
            auxiliary_line_2 = f'{int(auxiliary_line_22)}' if auxiliary_line_22.is_integer() else f'{auxiliary_line_22:.2f}'
            reduced_discriminant_str = f'{int(reduced_discriminant)}' if reduced_discriminant.is_integer() else f'{reduced_discriminant:.2f}'

            sol_x_str = f'{int(solution_x)}' if solution_x.is_integer() else f'{solution_x:.2f}'
            
            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида x²+px+q=0   ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {x_str}{coef_p_str}{coef_q_str} = 0')
            print(f'   Решение:   D = {coef_p_str_1}² / 4{coef_q_str_1}')
            print(f'              D = {auxiliary_line_1} / 4{coef_q_str_1}')
            print(f'              D = {auxiliary_line_2}{coef_q_str_1}')
            print(f'              D = {reduced_discriminant_str}')
            print(f'              x = -({coefficient_b} / 2)')
            print(f'   Ответ:     x = {sol_x_str}')
            print('   ──────────────────────────────────────────────')
            print()
        else:
            x_str = 'x²' if coefficient_a > 0 else '-x²'
            coef_p_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_q_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_p_str_1 = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_q_str_1 = f' - {coefficient_c}' if coefficient_c > 0 else f' + {-coefficient_c}'
            auxiliary_line_11 = coefficient_b**2
            auxiliary_line_1 = f'{int(auxiliary_line_11)}' if auxiliary_line_11.is_integer() else f'{auxiliary_line_11:.2f}'
            auxiliary_line_22 = coefficient_b**2 / 4
            auxiliary_line_2 = f'{int(auxiliary_line_22)}' if auxiliary_line_22.is_integer() else f'{auxiliary_line_22:.2f}'
            reduced_discriminant_str = f'{int(reduced_discriminant)}' if reduced_discriminant.is_integer() else f'{reduced_discriminant:.2f}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида x²+px+q=0   ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {x_str}{coef_p_str}{coef_q_str} = 0')
            print(f'   Решение:   D = {coef_p_str_1}² / 4{coef_q_str_1}')
            print(f'              D = {auxiliary_line_1} / 4{coef_q_str_1}')
            print(f'              D = {auxiliary_line_2}{coef_q_str_1}')
            print(f'              D = {reduced_discriminant_str}')
            print(f'              {reduced_discriminant_str} < 0 => ∅')
            print('   Ответ:     Уравнение не имеет решений!')
            print('   ──────────────────────────────────────────────')
            print()
    
    @action_menu_decorator
    def solving_a_quadratic_equation_8(coefficient_a, coefficient_b, coefficient_c): # Главное меню > Решение квадратного уравнения (ax²+bx+c=0) > ax²+bx+c=0 | a и b и c ≠ 0
        '''
        Функция solving_a_quadratic_equation_8 предназначена для решения квадратного уравнения вида ax²+bx+c=0.

        Описание:
            1.  Принимает аргументы.
            2.  Вычисляет дискриминант и определяет существуют ли решения.
            3.  Находит решения.
            4.  Генерирует строки для вывода решения в зависимости от коэффициентов.
            5.  Выводит решения.
            6.  Предлагает продолжить решение или выйти из опции.

        Принимаемые аргументы:
            coefficient_a: коэффициент a
            coefficient_b: коэффициент b
            coefficient_c: коэффициент c

        '''
        discriminant = coefficient_b**2 - 4*coefficient_a*coefficient_c

            

        if discriminant > 0:
            solution_x1 = (-coefficient_b + discriminant**(1/2)) / (2*coefficient_a)
            solution_x2 = (-coefficient_b - discriminant**(1/2)) / (2*coefficient_a)

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_a_dis = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            coef_b_dis = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_c_dis = f'{coefficient_c}' if coefficient_c > 0 else f'({coefficient_c})'
            auxiliary_line_dis_11 = coefficient_b**2
            auxiliary_line_dis_1 = f'{int(auxiliary_line_dis_11)}' if auxiliary_line_dis_11.is_integer() else f'{auxiliary_line_dis_11:.2f}'
            auxiliary_line_dis = f'{int(discriminant)}' if discriminant.is_integer() else f'{discriminant:.2f}'
            a_c_dis = f' - {4 * coefficient_a * coefficient_c}' if 4 * coefficient_a * coefficient_c > 0 else f' + {abs(4*coefficient_a*coefficient_c)}'
            coef_b_sol_1 = f'(-{coefficient_b}' if coefficient_b > 0 else f'(-({coefficient_b})'
            coef_b_sol_2 = f'(-{coefficient_b}' if coefficient_b > 0 else f'({-coefficient_b}'
            discriminant_sol_11 = f'{int(discriminant)}' if discriminant.is_integer() else f'{discriminant:.2f}'
            discriminant_sol_1 = f'√{discriminant_sol_11})' if discriminant > 0 else f'√({discriminant_sol_11}))'
            discriminant_sol_22 = discriminant**(1/2)
            discriminant_sol_2 = f'{int(discriminant_sol_22)}' if discriminant_sol_22.is_integer() else f'{discriminant_sol_22:.2f}'
            coef_a_sol = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            a_2_sol_ = 2*coefficient_a
            a_2_sol =f'{int(a_2_sol_)}' if a_2_sol_.is_integer() else f'{a_2_sol_:.2f}'

            sol_x1_str = f'{int(solution_x1)}' if solution_x1.is_integer() else f'{solution_x1:.2f}'
            sol_x2_str = f'{int(solution_x2)}' if solution_x2.is_integer() else f'{solution_x2:.2f}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+bx+c=0  ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
            print(f'              D = {auxiliary_line_dis_1}{a_c_dis}')
            print(f'              D = {auxiliary_line_dis}')
            print(f'              x = {coef_b_sol_1} ± {discriminant_sol_1} / (2 × {coef_a_sol})')
            print(f'              x = {coef_b_sol_2} ± {discriminant_sol_2}) / ({a_2_sol})')
            print(f'   Ответ:     x₁ = {sol_x1_str}')
            print(f'              x₂ = {sol_x2_str}')
            print('   ──────────────────────────────────────────────')
            print()
        elif not discriminant:
            solution_x = -((coefficient_b) / (2*coefficient_a))

            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_a_dis = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            coef_b_dis = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_c_dis = f'{coefficient_c}' if coefficient_c > 0 else f'({coefficient_c})'
            auxiliary_line_dis_11 = coefficient_b**2
            auxiliary_line_dis_1 = f'{int(auxiliary_line_dis_11)}' if auxiliary_line_dis_11.is_integer() else f'{auxiliary_line_dis_11:.2f}'
            auxiliary_line_dis = f'{int(discriminant)}' if discriminant.is_integer() else f'{discriminant:.2f}'
            a_c_dis = f' - {4 * coefficient_a * coefficient_c}' if 4 * coefficient_a * coefficient_c > 0 else f' + {abs(4*coefficient_a*coefficient_c)}'
            coef_b_sol_1 = f'(-{coefficient_b}' if coefficient_b > 0 else f'(-({coefficient_b})'
            coef_b_sol_2 = f'(-{coefficient_b}' if coefficient_b > 0 else f'({-coefficient_b}'
            coef_a_sol = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            a_2_sol_ = 2*coefficient_a
            a_2_sol =f'{int(a_2_sol_)}' if a_2_sol_.is_integer() else f'{a_2_sol_:.2f}'

            sol_x_str = f'{int(solution_x)}' if solution_x.is_integer() else f'{solution_x:.2f}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+bx+c=0  ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
            print(f'              D = {auxiliary_line_dis_1}{a_c_dis}')
            print(f'              D = {auxiliary_line_dis}')
            print(f'              x = {coef_b_sol_1}) / ( 2 × {coef_a_sol})')
            print(f'              x = {coef_b_sol_2}) / ({a_2_sol})')
            print(f'   Ответ:     x = {sol_x_str}')
            print('   ──────────────────────────────────────────────')
            print()
        else:
            coef_a_str = f'{coefficient_a}x²' if abs(coefficient_a) != 1 else ('x²' if coefficient_a == 1 else '-x²')
            coef_b_str = f' + {coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b > 0 else (f' - {-coefficient_b}x' if abs(coefficient_b) != 1 and coefficient_b < 0 else(' + x' if coefficient_b == 1 else ' - x'))
            coef_c_str = f' + {coefficient_c}' if coefficient_c > 0 else f' - {-coefficient_c}'
            coef_a_dis = f'{coefficient_a}' if coefficient_a > 0 else f'({coefficient_a})'
            coef_b_dis = f'{coefficient_b}' if coefficient_b > 0 else f'({coefficient_b})'
            coef_c_dis = f'{coefficient_c}' if coefficient_c > 0 else f'({coefficient_c})'
            auxiliary_line_dis_11 = coefficient_b**2
            auxiliary_line_dis_1 = f'{int(auxiliary_line_dis_11)}' if auxiliary_line_dis_11.is_integer() else f'{auxiliary_line_dis_11:.2f}'
            auxiliary_line_dis = f'{int(discriminant)}' if discriminant.is_integer() else f'{discriminant:.2f}'

            print()
            print('   ──────────────────────────────────────────────')
            print('   Принято квадратное уравнение вида ax²+bx+c=0  ')
            print('   ──────────────────────────────────────────────')
            print(f'   Дано:      {coef_a_str}{coef_b_str}{coef_c_str} = 0')
            print(f'   Решение:   D = {coef_b_dis}² - 4 × {coef_a_dis} × {coef_c_dis}')
            print(f'              D = {auxiliary_line_dis_1}{a_c_dis}')
            print(f'              D = {auxiliary_line_dis}')
            print('   Ответ:     Уравнение не имеет решений!')
            print('   ──────────────────────────────────────────────')
            print()

    reading_coefficients()


def settings():
    def change_settings():
        os.system('cls')
        console.print(Panel(Text(text='Изменение настроек', justify='center'), title='НАСТРОЙКИ'))

        with open('settings.json', 'r') as json_file:
            settings_data = json.load(json_file)

        table = Table(title='[b]Settings (beta)[/]', expand=True)

        table.add_column('№', justify='center')
        table.add_column('Параметр', justify='center')
        table.add_column('Значение', justify='center')

        table.add_row('1', 'Тема', 'Тёмная')
        table.add_row('2', 'Значёк дискриминанта', 'Базовый')
        table.add_row('3', 'Отображенеи решения', 'Полное')
        table.add_row('4', 'Язык', ' Русский')
        table.add_row('5', 'Размер окна', 'Стандартный')

        console.print(table)

        while True:
            pressed_key = msvcrt.getch().lower()
            if ord(pressed_key) == ord('E'):
                main_menu()
            else:
                console.print('\n[red]Команда некорректна или не существует![/]\n')

    def restoring_settings():
        pass

    os.system('cls')
    console.print(Panel(Text(text='НАСТРОЙКИ', justify='center'), title='Опция №5'))
    settings_options_panel = Panel(
        Text(
            text='''
[1]    Изменение настроек
[2]    Восстановление настроек
[E]    Назад
            '''
        ),
        title='ОПЦИИ',
        subtitle='Пожалуйста, введите идентификатор опции из меню...',
        subtitle_align='left'
    )

    console.print(settings_options_panel)

    while True:
        pressed_key = msvcrt.getch().lower()
        if ord(pressed_key) == ord('1'):
            change_settings()
        elif ord(pressed_key) == ord('2'):
            restoring_settings()
        elif ord(pressed_key) == ord('e'):
            main_menu()
        else:
            console.print('\n[red]Команда некорректна или не существует![/]\n')


if __name__ == '__main__':
    main()
