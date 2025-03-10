import os
import json

from rich.theme import Theme
from rich.console import Console


program_work_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(program_work_directory, 'settings.json')
example_json_path = os.path.join(program_work_directory, 'example_settings.json')


def settings_data_loading():
    global settings_data
    try:
        with open(json_path, 'r') as json_file:
            settings_data = json.load(json_file)
            settings_data_validation()

            light_theme = Theme(settings_data['theme']['light'])
            dark_theme = Theme(settings_data['theme']['dark'])

            global light_console, dark_console
            light_console = Console(theme=light_theme)
            dark_console = Console(theme=dark_theme)
    except Exception as error:
        print(f'\033[31m{error}\033[0m')


def settings_data_validation():
    def check_keys():
        if not all(key in settings_data for key in [
            'box_style',
            'installed_theme',
            'theme',
            'window_size'
        ]):
            print('ОШИБКА [SET-ERR-1001]: Не найден ключ в файле настроек!')
        elif not all(key in settings_data['theme'] for key in [
            'dark',
            'light'
        ]):
            print('ОШИБКА [SET-ERR-1002]: Не найден ключ в файле настроек!')
        elif not all(key in settings_data['theme']['light'] and key in settings_data['theme']['dark'] for key in [
            'alert',
            'background',
            'error',
            'info',
            'success',
            'warning'
        ]):
            print('ОШИБКА [SET-ERR-1003]: Не найден ключ в файле настроек!')
        elif not all(key in settings_data['window_size'] for key in [
            'height',
            'width'
        ]):
            print('ОШИБКА [SET-ERR-1004]: Не найден ключ в файле настроек!')
        else: 
            print('В настройках (ключи) повреждений нет!')

    def check_values():
        if settings_data['box_style'] not in [
            'ascii',
            'ascii2',
            'ascii_double_head',
            'double', 
            'double_edge',
            'heavy',
            'heavy_edge',
            'heavy_head',
            'horizontals',
            'markdown',
            'minimal',
            'minimal_double_head',
            'minimal_heavy_head',
            'rounded',
            'simple',
            'simple_head',
            'simple_heavy',
            'square',
            'square_double_head'
        ]:
            print('ОШИБКА [SET-ERR-1005]: Не верное значение стиля рамки!')
        elif settings_data['installed_theme'] not in ['system', 'light', 'dark']:
            print('ОШИБКА [SET-ERR-1006]: Не верное значение темы!')
        elif not all(
            all(word in [
                'bold',
                'blink',
                'conceal',
                'italic',
                'reverse',
                'strike',
                'underline',
                'on',
                'dim',
                'black',
                'red',
                'green',
                'yellow',
                'blue',
                'magenta',
                'cyan',
                'white'
            ] for word in values.split())
            for key in ['alert', 'background', 'error', 'info', 'success', 'warning']
            for values in (settings_data['theme']['light'][key], settings_data['theme']['dark'][key])
        ):
            print('ОШИБКА [SET-ERR-1007]: Не верное значение темы!')
        elif not isinstance(settings_data['window_size']['height'], int) and not isinstance(settings_data['window_size']['width'], int) and settings_data['window_size']['height'] < 30 and settings_data['window_size']['width'] < 30:
            print('ОШИБКА [SET-ERR-1008]: Не верное значение размера окна!')
        else:
            print('В настройках (значения) повреждений нет!')

    
    check_keys()
    check_values()


def restore_settings():
    print('Восстановление настроек по умолчанию...')


def example():
    print('Light theme'.center(50))
    light_console.print("Это сообщение об ошибке.", style="error")
    light_console.print("Это информационное сообщение.", style="info")
    light_console.print("Это сообщение об успехе.", style="success")
    light_console.print("Это предупреждение.", style="warning")
    light_console.print("Это сообщение по умолчанию.", style="background")
    light_console.print("Это сообщение тревоги.", style="alert")
    print()
    print('Dark theme'.center(50))
    dark_console.print("Это сообщение об ошибке.", style="error")
    dark_console.print("Это информационное сообщение.", style="info")
    dark_console.print("Это сообщение об успехе.", style="success")
    dark_console.print("Это предупреждение.", style="warning")
    dark_console.print("Это сообщение по умолчанию.", style="background")
    dark_console.print("Это сообщение тревоги.", style="alert")


settings_data_loading()
example()

