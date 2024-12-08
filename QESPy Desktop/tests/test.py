import os
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()

dictionar = {
    "theme": "3"
}

def settings():
    
    table = Table(title='Параметры', expand=True)

    table.add_column('Параметр', justify="right", no_wrap=True)
    table.add_column('Индитификатор')
    table.add_column('Значение')

    table.add_row('Стиль рамок', '1', dictionar['theme'])
    table.add_row('Значок дискриминанта', '2')
    table.add_row('Тема интерфейса', '3')
    table.add_row('Полнота решения', '4')
    table.add_row('Точность решения', '5')

    os.system('cls')
    console.print(Panel(Text(text='НАСТРОЙКИ', justify='center'), title='Опция №N'))
    console.print(table)

settings()
