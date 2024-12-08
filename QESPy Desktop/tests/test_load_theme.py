import json
import msvcrt
import winreg
import os

from rich.theme import Theme
from rich.console import Console
from rich.errors import StyleSyntaxError


script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'config.json')


def error_handling(e, position):
    if isinstance (e, FileNotFoundError):
        match position:
            case 'load_settings_process':
                error_message = f"Произошла ошибка: {e}"

                print(error_message)
                print()
                print('Файл настроек не найден!!!')
                print()
                print()
                print()
                print('Для прерывания загрузки нажмите любую клавишу...')
                msvcrt.getch()
                quit()
    elif isinstance(e, StyleSyntaxError):
        print(f'Произошла ошибка загрузки настроек! {e}')
        print()
        print()
        print()
        print('Для прерывания загрузки нажмите любую клавишу...')
        msvcrt.getch()
        quit()
    else:
        error_message = f"Произошла неизвестная ошибка: {e}"


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
    
    try:
        with open(json_path, 'r') as json_file:
            settings_data = json.load(json_file)
    except Exception as error:
        error_handling(error, 'load_settings_process')

    try:
        if settings_data['set_theme'] == 'system':
            if get_windows_theme():
                theme = Theme(settings_data['theme']['dark'])
            else:
                theme = Theme(settings_data['theme']['light'])
        elif settings_data['set_theme'] == 'dark':
            theme = Theme(settings_data['theme']['dark'])
        elif settings_data['set_theme'] == 'light':
            theme = Theme(settings_data['theme']['light'])
        else:
            error_handling(error=NameError, position='set_theme')

        global console
        console = Console(theme=theme)
    except Exception as error:
        error_handling(error, 'load_settings')

    example() # Проверка


def example():
    print('\nЕсли вы видите это сообжение, значит всё прошло успешно!!!\n')
    console.print('Это обычный текст', style="default")
    console.print("Это сообщение об успехе", style="success")
    console.print("Это сообщение об ошибке", style="error")
    console.print("Это предупреждающее сообщение", style="warning")

load_settings()
