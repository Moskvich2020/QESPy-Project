commands = {
    "status": show_status,
    "settings": show_settings,
    "help": help_menu,
    "exit": exit_program,
    "change_settings": change_settings
}

def command_line_interface():
    while True:
        command = input("Введите команду: ")
        if command in commands:
            commands[command]()
        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")
