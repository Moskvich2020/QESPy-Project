import json
# import msvcrt
import time
import winreg
import os

from rich.box import ASCII, ASCII2, ASCII_DOUBLE_HEAD, DOUBLE, DOUBLE_EDGE, HEAVY, HEAVY_EDGE, HEAVY_HEAD, HORIZONTALS, MARKDOWN, MINIMAL, MINIMAL_DOUBLE_HEAD, MINIMAL_HEAVY_HEAD, ROUNDED, SIMPLE, SIMPLE_HEAD, SIMPLE_HEAVY, SQUARE, SQUARE_DOUBLE_HEAD
from rich.theme import Theme
from rich.console import Console
# from rich.errors import StyleSyntaxError
from rich.panel import Panel


program_work_directory = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(program_work_directory, 'settings.json')


def settings_data_loading():
    def get_windows_theme():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
            value, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')
            winreg.CloseKey(key)

            if value == 0:
                return True # Тёмная тема
            else:
                return False # Светлая тема
        except FileNotFoundError:
            print('ОШИБКА [REG-ERR-1001]: Не удалось определить системную тему Windows!')
            print(r'В кусте реестра "HKEY_CURRENT_USER" по пути "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" не найден ключь "AppsUseLightTheme".')
        except PermissionError:
            print('ОШИБКА [REG-ERR-1002]: Не удалось определить системную тему Windows!')
            print('Отсутствуют права доступа к кусту реестра "HKEY_CURRENT_USER" или ключу "AppsUseLightTheme".')
        except OSError:
            print('ОШИБКА [REG-ERR-1003]: Не удалось определить системную тему Windows!')
            print('Не удалось открыть и прочесть куст реестра "HKEY_CURRENT_USER" или ключ "AppsUseLightTheme".')
        except KeyError:
            print('ОШИБКА [REG-ERR-1004]: Не удалось определить системную тему Windows!')
            print(r'Попытка чтения ключа "AppsUseLightTheme" из куста реестра "HKEY_CURRENT_USER" по пути "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" завершилась неудачно.')
        except TypeError:
            print('ОШИБКА [REG-ERR-1005]: Не удалось определить системную тему Windows!')
            print(r'Значение ключа "AppsUseLightTheme" из куста реестра "HKEY_CURRENT_USER" по пути "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" возвращенно в неожиданном формате или типе.')
        except ValueError:
            print('ОШИБКА [REG-ERR-1006]: Не удалось определить системную тему Windows!')
            print(r'Значение ключа "AppsUseLightTheme" из куста реестра "HKEY_CURRENT_USER" по пути "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" не соответствует ожидаемому типу.')
        except Exception as error:
            print(f'ОШИБКА [REG-ERR-1000]: Не удалось определить системную тему Windows!')
            print('Произошла неизвестная ошибка при попытке определить системную тему Windows:\n{error}')

    global settings_data

    try:
        with open(json_path, 'r') as json_file:
            settings_data = json.load(json_file)
    except FileNotFoundError:
        print('ОШИБКА [FILE-ERR-1001]: Файл настроек не найден!')
        print('Файл настроек "settings.json" не найден в рабочей директории программы.')
    except PermissionError:
        print('ОШИБКА [FILE-ERR-1002]: Ошибка доступа к файлу настроек!')
        print('Отсутствуют права доступа к файлу настроек "settings.json".')
    except UnicodeDecodeError:
        print('ОШИБКА [FILE-ERR-1003]: Ошибка декодирования файла настроек!')
        print('Не удалось декодировать файл настроек "settings.json" в кодировку UTF-8.')
    except json.JSONDecodeError:
        print('ОШИБКА [FILE-ERR-1004]: Файл настреек не является корректным JSON!')
        print('Файл настроек "settings.json" не является корректным JSON-файлом.')
    except OSError:
        print('ОШИБКА [FILE-ERR-1005]: Ошибка при открытии файла настроек!')
        print('Не удалось открыть файл настроек "settings.json" в режиме чтения.')
    except Exception as error:
        print(f'ОШИБКА [FILE-ERR-1000]: Не удалось загрузить файл настроек!')
        print(f'Произошла неизвестная ошибка при попытке загрузить файл настроек "settings.json":\n{error}')
    
    # settings_data_validation()

    box_styles = {
        'ascii': ASCII,
        'ascii2': ASCII2,
        'ascii_double_head': ASCII_DOUBLE_HEAD,
        'double': DOUBLE,
        'oduble_edge': DOUBLE_EDGE,
        'heavy': HEAVY,
        'heavy_edge': HEAVY_EDGE,
        'heavy_head': HEAVY_HEAD,
        'horizontals': HORIZONTALS,
        'markdown': MARKDOWN,
        'minimal': MINIMAL,
        'minimal_double_head': MINIMAL_DOUBLE_HEAD,
        'minimal_heavy_head': MINIMAL_HEAVY_HEAD,
        'rounded': ROUNDED,
        'simple': SIMPLE,
        'simple_head': SIMPLE_HEAD,
        'simple_heavy': SIMPLE_HEAVY,
        'square': SQUARE,
        'square_double_head': SQUARE_DOUBLE_HEAD
    }

    box_style = settings_data['box_style']
    if box_style in box_styles:
        global box
        box = box_styles[box_style]

    if settings_data['installed_theme'] == 'dark':
        theme = Theme(settings_data['theme']['dark'])
    elif settings_data['installed_theme'] == 'light':
        theme = Theme(settings_data['theme']['light'])
    else:
        if get_windows_theme():
            theme = Theme(settings_data['theme']['dark'])
        else:
            theme = Theme(settings_data['theme']['light'])

    global console
    console = Console(theme=theme)

    os.system(f'mode con: lines={str(settings_data['window_size']['height'])} cols={str(settings_data['window_size']['width'])}')


def example():
    console.print(Panel("Hello, World!", box=box))
    console.print('Это тревожный текст', style="alert")
    console.print('Это обычный текст', style="background")
    console.print("Это сообщение об ошибке", style="error")
    console.print('Это информационный текст', style="info")
    console.print("Это сообщение об успехе", style="success")
    console.print("Это предупреждающее сообщение", style="warning")
    time.sleep(5)

settings_data_loading()
example() # Проверка
