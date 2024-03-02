import os
import sys
import json
# from msvcrt import getch
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


console = Console()
clear = lambda: os.system('cls')

with open('test_settings.json', 'r') as settings:
    config = json.load(settings)

print(f'thtme {config['theme']}')
print(f'')
