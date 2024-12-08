import os
import json

from rich.theme import Theme
from rich.console import Console


script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'config.json')


def load_settings():
    try:
        with open(json_path, 'r') as json_file:
            settings_data = json.load(json_file)
            settings_validation(settings_data)

            light_theme = Theme(settings_data['theme']['light'])
            dark_theme = Theme(settings_data['theme']['dark'])

            global light_console, dark_console
            light_console = Console(theme=light_theme)
            dark_console = Console(theme=dark_theme)
    except Exception as error:
        error_handling(error, 'load_settings_process')


def settings_validation(settings_data):
    def check_keys():
        try:
            if not all(key in settings_data for key in [
                'box_style',
                'discirminant_sign',
                'installed_theme',
                'solution_type',
                'theme',
                'precision'
            ]):
                raise KeyError
            elif not all(key in settings_data['theme'] for key in [
                'light',
                'dark'
            ]):
                raise KeyError
            elif not all(key in settings_data['theme']['light'] and key in settings_data['theme']['dark'] for key in [
                'alert',
                'background',
                'error',
                'info',
                'success',
                'warning'
            ]):
                raise KeyError
            else: 
                print(f'\033[32m{'В настройках (ключи) повреждений нет!'}\033[0m')
        except Exception as error:
            error_handling(error, 'settings_validation')

    def check_values():
        try:
            if settings_data['installed_theme'] not in ['system', 'light', 'dark']:
                raise ValueError
            elif not all(
                all(word in [
                    'bold', 'blink', 'conceal', 'italic', 'reverse', 'strike', 'underline', 'on',
                    'dim', 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
                ] for word in values.split())
                for key in ['alert', 'background', 'error', 'info', 'success', 'warning']
                for values in (settings_data['theme']['light'][key], settings_data['theme']['dark'][key])
            ):
                raise ValueError
            elif settings_data['discirminant_sign'] not in ['default', 'custom']:
                raise ValueError
            elif settings_data['solution_type'] not in ['complete', 'shortened']:
                raise ValueError
            elif not isinstance(settings_data['precision'], int) or (settings_data['precision'] < 0 or settings_data['precision'] > 10):
                raise ValueError
            elif settings_data['box_style'] not in [
                'box.ASCII',
                'box.ASCII2',
                'box.ASCII_DOUBLE_HEAD',
                'box.DOUBLE', 
                'box.DOUBLE_EDGE',
                'box.HEAVY',
                'box.HEAVY_EDGE',
                'box.HEAVY_HEAD',
                'box.HORIZONTALS',
                'box.MARKDOWN',
                'box.MINIMAL',
                'box.MINIMAL_DOUBLE_HEAD',
                'box.MINIMAL_HEAVY_HEAD',
                'box.ROUNDED',
                'box.SIMPLE',
                'box.SIMPLE_HEAD',
                'box.SIMPLE_HEAVY',
                'box.SQUARE',
                'box.SQUARE_DOUBLE_HEAD'
            ]:
                raise ValueError
            else:
                print(f'\033[32m{'В настройках (значения) повреждений нет!'}\033[0m')
        except Exception as error:
            error_handling(error, 'settings_validation')
    
    check_keys()
    check_values()


def error_handling(error, position):
    if isinstance(error, ValueError):
        match position:
            case 'settings_validation':
                print('ОШИБКА: Файл настроек повреждн!\nНеверное значение ключа!\n\nВыполните восстановление настроек!')
    elif isinstance(error, FileNotFoundError):
        match position:
            case 'load_settings_process':
                print('ОШИБКА: Файл настроек не найден!\n\nВыполните восстановление настроек!')
    elif isinstance(error, KeyError):
        match position:
            case 'settings_validation':
                print('ОШИБКА: Файл настроек повреждн!\nКлюч не найден!\n\nВыполните восстановление настроек!')
    else:
        print(f'Неизвестная ошибка. Тип ошибки: {type(error).__name__}.')


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


load_settings()
example()

