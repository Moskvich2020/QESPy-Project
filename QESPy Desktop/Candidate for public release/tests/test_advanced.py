# import os
# import sys
import json
# from msvcrt import getch
from time import sleep

# from rich.console import Console
# from rich.panel import Panel
# from rich.text import Text


# console = Console()
# clear = lambda: os.system('cls')

with open('test_settings.json', 'r') as settings:
    # mod = json.load(settings)
    mod = settings.read()

set_red = json.loads(mod)

if set_red["theme"] == "white":
    print('светлая!')
else:
    print('тёмная!')

# print(set_red["theme"])
# print(f'theme {config['theme']}')
# print(f'')
sleep(5)
