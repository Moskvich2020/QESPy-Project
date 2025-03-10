import copy
import os
import json
import msvcrt

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


os.system('title QESPy Desktop - Настройки')

def load_settings():
    global console, settings_data, json_path
    program_work_directory = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(program_work_directory, 'settings.json')

    console = Console()

    with open(json_path, 'r') as json_file:
        settings_data = json.load(json_file)


def settings():
    def output_settings():
        if settings_data['box_style'] == 'ascii':
            box_style_str = 'ASCII'
        elif settings_data['box_style'] == 'ascii2':
            box_style_str = 'ASCII 2'
        elif settings_data['box_style'] == 'ascii_double_head':
            box_style_str = 'ASCII Double Head'
        elif settings_data['box_style'].count('_') == 0:
            box_style_str = settings_data['box_style'].capitalize()
        else:
            box_style_str = settings_data['box_style'].replace('_', ' ').capitalize()
        installed_theme_str = 'Системная' if settings_data['installed_theme'] == 'system' else ('Тёмная' if settings_data['installed_theme'] == 'dark' else 'Светлая')
        window_size_str = f'{str(settings_data['window_size']['height'])} × {str(settings_data['window_size']['width'])}'

        if settings_data['box_style'] != new_settings['box_style']:
            if new_settings['box_style'] == 'ascii':
                new_box_style_str = 'ASCII'
            elif new_settings['box_style'] == 'ascii2':
                new_box_style_str = 'ASCII 2'
            elif new_settings['box_style'] == 'ascii_double_head':
                new_box_style_str = 'ASCII Double Head'
            elif new_settings['box_style'].count('_') == 0:
                new_box_style_str = new_settings['box_style'].capitalize()
            else:
                new_box_style_str = new_settings['box_style'].replace('_', ' ').title()
        else:
            new_box_style_str = '---'
        if settings_data['installed_theme'] != new_settings['installed_theme']:
            new_installed_theme_str = 'Системная тема' if new_settings['installed_theme'] == 'system' else ('Тёмная тема' if new_settings['installed_theme'] == 'dark' else 'Светлая тема')
        else:
            new_installed_theme_str = '---'
        if settings_data['window_size']['height'] != new_settings['window_size']['height'] or settings_data['window_size']['width'] != new_settings['window_size']['width']:
            new_window_size_str = f'{str(new_settings["window_size"]["height"])} × {str(new_settings["window_size"]["width"])}'
        else:
            new_window_size_str = '---'

        table = Table(title='Параметры', expand=True)

        table.add_column('Индитификатор', justify="center", no_wrap=True)
        table.add_column('Параметр', no_wrap=True)
        table.add_column('Текущее значение', no_wrap=True)
        table.add_column('Новое значение', no_wrap=True)
        table.add_column('Значение по умолчанию', no_wrap=True)

        table.add_row('1', 'Стиль рамок', box_style_str, new_box_style_str, 'Square')
        table.add_row('2', 'Тема интерфейса', installed_theme_str, new_installed_theme_str, 'Системная тема')
        table.add_row('3', 'Размер окна', window_size_str, new_window_size_str, '30 × 120')

        os.system('cls')
        console.print(Panel(Text(text='НАСТРОЙКИ', justify='center'), title='Опция №N'))
        console.print(table)
        print('\n[1] Изменить настройки   [2] Применить настройки   [3] Вернуть все значения по умолчанию   [E] Выйти (Отмена)')
        while True:
            cmd = msvcrt.getch().lower()
            if ord(cmd) == ord('1'):
                changing_settings()
            elif ord(cmd) == ord('2'):
                cmd = input('\nВы уверены, что хотите применить новые настройки? [Y/N]: ').lower()
                if cmd == 'y':
                    with open(json_path, 'w') as json_file:
                        json.dump(new_settings, json_file, indent=4)
                    load_settings()
                    os.system('cls')
                    output_settings()
                elif cmd == 'n':
                    os.system('cls')
                    output_settings()
                else:
                    print('\nКоманда некорректна или не существует!')
            elif ord(cmd) == ord('3'):
                cmd = input('\nВы уверены, что хотите вернуть все значения по умолчанию? [Y/N]: ').lower()
                if cmd == 'y':
                    new_settings['box_style'] = 'square'
                    new_settings['discriminant_sign'] = 'default'
                    new_settings['installed_theme'] = 'system'
                    new_settings['solution_type'] = 'complete'
                    new_settings['precision'] = 2
                    new_settings['window_size']['height'] = 30
                    new_settings['window_size']['width'] = 120
                    with open(json_path, 'w') as json_file:
                        json.dump(new_settings, json_file, indent=4)
                    load_settings()
                    os.system('cls')
                    output_settings()
                elif cmd == 'n':
                    os.system('cls')
                    output_settings()
                else:
                    print('\nКоманда некорректна или не существует!')
            elif ord(cmd) == ord('e'):
                quit()
            else:
                print('\nКоманда некорректна или не существует!')

    def changing_settings():
        indetificator = input('\nВведите индетификатор параметра: ').lower()
        if indetificator == 'e':
            os.system('cls')
            output_settings()
        elif indetificator == '1':
            print('\nИзменение стиля рамок')
            print('[1] ASCII                  [2] ASCII 2          [3] ASCII Double Head')
            print('[4] Double                 [5] Double Edge      [6] Heavy')
            print('[7] Heavy Edge             [8] Heavy Head       [9] Horizontal')
            print('[10] Markdown              [11] Mininal         [12] Minimal Double Head')
            print('[13] Minimal Heavy Head    [14] Rounded         [15] Simple')
            print('[16] Simple Head           [17] Simple Heavy    [18] Square')
            print('[19] Square Double Head')
            box_styles = [
                'ascii', 'ascii2', 'ascii_double_head', 'double', 'double_edge', 'heavy', 'heavy_edge',
                'heavy_head', 'horizontal', 'markdown', 'minimal', 'minimal_double_head', 'minimal_heavy_head',
                'rounded', 'simple', 'simple_head', 'simple_heavy', 'square', 'square_double_head'
            ]
            while True:
                new_value = input('\nВведите индетификатор нового значения: ').lower()
                if new_value == 'e':
                    break
                elif 0 < int(new_value) < 20:
                    new_settings['box_style'] = box_styles[int(new_value) - 1]
                    break
                else:
                    print('Такого параметра не существует!')
        elif indetificator == '2':
            print('\nИзменение темы интерфейса')
            print('[1] Системная тема   [2] Тёмная тема   [3] Светлая тема')
            while True:
                new_value = input('\nВведите индетификатор нового значения: ').lower()
                if new_value == 'e':
                    break
                elif new_value == '1':
                    new_settings['installed_theme'] = 'system'
                    break
                elif new_value == '2':
                    new_settings['installed_theme'] = 'dark'
                    break
                elif new_value == '3':
                    new_settings['installed_theme'] = 'light'
                    break
                else:
                    print('Такого параметра не существует!')
        elif indetificator == '3':
            print('\nИзменение размера окна')
            print('Высота и ширина окна должны быть целыми числами, не меньших 30!')
            while True:
                new_height = input('Введите новую высоту окна: ').lower()
                if new_height == 'e':
                    break
                new_width = input('Введите новую ширину окна: ').lower() 
                if new_width == 'e':
                    break
                if new_height.isdigit() and new_width.isdigit() and int(new_height) >= 30 and int(new_width) >= 30:
                    new_settings['window_size']['height'] = int(new_height)
                    new_settings['window_size']['width'] = int(new_width)
                    break
                else:
                    print('Не верное значение высоты или ширины окна!')
        else:
            print('Такого параметра не существует!')

        os.system('cls')
        output_settings()

    new_settings = copy.deepcopy(settings_data)
    output_settings()    


load_settings()
settings()
