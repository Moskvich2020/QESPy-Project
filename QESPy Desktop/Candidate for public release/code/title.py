import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()
clear = lambda: os.system('cls')

def title(func):
    def wrapper():
        clear()
        console.print(Panel(Text(text='', justify=''), title=''))
        func()
    return wrapper
