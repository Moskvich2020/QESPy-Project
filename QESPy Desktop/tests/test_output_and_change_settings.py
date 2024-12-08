import os
import json

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def load_settings():
    global console, settings_data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'config.json')

    console = Console()

    with open(json_path, 'r') as json_file:
        settings_data = json.load(json_file)


def settings():
    table = Table(title='Параметры', expand=True)

    table.add_column('Параметр', justify="right", no_wrap=True)
    table.add_column('Индитификатор')
    table.add_column('Значение')

    table.add_row('Стиль рамок', '1', settings_data['box_style'])
    table.add_row('Значок дискриминанта', '2', settings_data['discirminant_sign'])
    table.add_row('Тема интерфейса', '3', settings_data['installed_theme'])
    table.add_row('Полнота решения', '4', settings_data['solution_type'])
    table.add_row('Точность решения', '5', str(settings_data['precision']))

    os.system('cls')
    console.print(Panel(Text(text='НАСТРОЙКИ', justify='center'), title='Опция №N'))
    console.print(table)

load_settings()
settings()
