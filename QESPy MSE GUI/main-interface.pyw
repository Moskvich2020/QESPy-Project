import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("QESPy Project")
        self.geometry("1366x768")

        # Установка макета сетки 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Подгрузка изображений (для светлой и тёмной тем)
        
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        #self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
                                                     
        # Создание навигационной рамки
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  QESPy MSE", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Главная",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Решение квадратного уравнения (ax²+bx+c=0)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Решение биквадратного уравнения (ax⁴+bx²+c=0)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")
        
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Разложение квадратного уравнения (ax²+bx+c=0)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.logo_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # Создание домашней вкладки
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Щпручка готова! Прошу к столу!", command=self.open_input_dialog_event)
        self.home_frame_button_1.grid(row=1, column=0, padx=5, pady=5)

        # Создание второй вкладки
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Создание третьей вкладки
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # Создание четвёртой вкладки
        self.forth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Выбор стандартной вкладки
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # Установка цвет для выбранной кнопки
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # Отображение выбранной вкладки
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.forth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.forth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
    
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Готовы съесть щпручку?", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.mainloop()

