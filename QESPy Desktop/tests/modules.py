import msvcrt
import os
import importlib

# TODO: Значит.
# TODO: Во-первых, функция main() должна быть расформированна, а её функционал должен быть перенесён в другие функции.
# TODO: Во-вторых, функция load_modules() должна быть, как и load_settings(), сделанна отдельной функцией.
# TODO: В-третьих, функция modules() должна работать, как и settings(), уже с готовым списком модулей, да и вообще по томуже принципу:
# TODO: т. е. принять его, вывести и запускать модули по команде (а также выполнять весь остальной возложенный на неё функционал).

program_work_directory = os.path.dirname(os.path.abspath(__file__))

def modules():
    def load_modules():
        modules = {}
        for module_name in os.listdir(modules_dir):
            module_path = os.path.join(modules_dir, module_name)
            if os.path.isdir(module_path):
                try:
                    module = importlib.import_module(f'modules.{module_name}.{module_name}')
                    modules[module_name] = module
                except Exception as e:
                    print(f"Ошибка при загрузке модуля {module_name}: {e}")
        return modules

    def display_menu(modules):
        print("Доступные модули:")
        for i, module_name in enumerate(modules.keys(), 1):
            print(f"{i}. {module_name}")
        print("0. Выход")

    def run_module_with_exit(module):
        print("Нажмите 'q' для выхода из модуля.")
        try:
            while True:
                if msvcrt.kbhit() and msvcrt.getch() == b'q':
                    print("Выход из модуля.")
                    break
                module.run()
        except Exception as e:
            print(f"Ошибка в модуле: {e}")

    def main():
        modules_dir = 'modules'
        modules = load_modules(modules_dir)

        while True:
            display_menu(modules)
            choice = input("Выберите модуль для запуска (0 для выхода): ")

            if choice == '0':
                break
            
            try:
                module_name = list(modules.keys())[int(choice) - 1]
                module = modules[module_name]
                print(f"Запуск модуля: {module_name}")
                run_module_with_exit(module)
            except (IndexError, ValueError):
                print("Неверный выбор. Попробуйте снова.")
    
    modules_dir = os.path.join(program_work_directory, 'modules')

    if not os.path.exists(modules_dir):
        os.makedirs(modules_dir)
    
    main()

if __name__ == "__main__":
    modules()
