# ╭─────────────────────────────────╮
# │ Name: QESPy CFPR                │ 
# │ Version: 1.0                    │ 
# │ Build: 01032024                 │ 
# │ Build Date: 01-03-2024 9:00 PM  │ 
# │ Author: Moskvich2020            │ 
# │ License: BSD 3-Clause License   │ 
# ╰─────────────────────────────────╯

import os
from time import sleep
from main_menu import main_menu

clear = lambda: os.system('cls')
# os.system('mode 125, 30')


def main():
    clear()
    print('Quadratic Equation Solver in Python CFPR [Version 1.0]')
    print('(c) Cristi Constantin (Moskvich2020) QESPy Project. Все права защищены.')
    sleep(0.5)
    main_menu()

if __name__ == "__main__":
    main()
