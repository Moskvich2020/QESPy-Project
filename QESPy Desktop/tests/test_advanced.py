import json
import time

# Открытие файла настроей и запись его данных в переменную settings_data.
with open("settings.json", "r") as json_file:
    settings_data = json.load(json_file)

# Вывод старых настроек.
print('Old settungs:', settings_data["theme"])

# Изменение старых настроек.
settings_data["theme"] = "white"

# Запись новых настроек.
with open("settings.json", "w") as json_file:
    json.dump(settings_data, json_file, indent=4)

# Вывод новых настроек.
print('New settings:', settings_data["theme"])

time.sleep(5)


        # with open("config.json", "r") as json_file:
        #     settings_data = json.load(json_file)
        # if settings_data["discriminant_item"] == "legasy":
        #     dis_item = 'D'
        # else:
        #     dis_item = '∆'


# Для проверки наличия файла в Python, вы можете воспользоваться функцией os.path.exists(). Она возвращает True, если файл существует, и False, если его нет1. Вот пример:

# import os

# file_path = "путь/к/файлу.txt"
# if os.path.exists(file_path):
#     print("Файл существует!")
# else:
#     print("Файл не найден.")

# Если вам нужно записать в файл, который может не существовать (т.е. файл будет создан), откройте его с ключами a+ или w+1. Например:


# file_path = "путь/к/файлу.txt"
# with open(file_path, "a+") as file:
#     # Запись в файл
#     file.write("Новая строка")

# Пожалуйста, замените "путь/к/файлу.txt" на свой путь и имя файла.
