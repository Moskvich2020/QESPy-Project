import customtkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title('My app!')
        self.geometry('350x200')
        self.grid_columnconfigure((0, 1), weight=1)

        customtkinter.set_appearance_mode('System') # Todo: Установка темы по умолчанию ('System', 'Dark', 'Light')
        customtkinter.set_default_color_theme("blue") # Todo: Установка цветовой темы по умолчанию ("blue" (standard), "green", "dark-blue")

        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=15)
        # self.sidebar_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Todo: создаём кнопку в окне App()
        self.button = customtkinter.CTkButton(self, text='CTkButton', command=self.button_command)
        
        # Todo: grid и pack - это менеджеры геометрии.
        # Todo: Они оба принимают аргументы padx и pady, но grid фиксирует элемент на заданных координатах, в то время как pack является адаптивным.
        
        # Todo: Тестовая конопка
        self.button.grid(row=0, column=1, padx=0, pady=(0, 10))
        # self.button.pack(padx=40, pady=10)
        # self.button.grid_columnconfigure(1, weight=1)

        # Todo: Кнопка закрытия окна
        self.close_button = customtkinter.CTkButton(self, text='Close this window', command=self.close_window)
        self.close_button.grid(row=1, column=1, padx=0, pady=(0, 0))
        # self.close_button.pack(padx=40, pady=20)

        # Todo: Надпись "Тема"
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Тема:")
        self.appearance_mode_label.grid(row=0, column=0, padx=10, pady=(0, 0))
        
        # Todo: Выпадпющий список "Тема"
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=0, padx=10, pady=(0, 0))
        
        # Todo: Надпись "Масштаб элементов"
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="Масштаб элементов:")
        self.scaling_label.grid(row=2, column=0, padx=10, pady=(20, 0))
        
        # Todo: Выпадпющий список "Масштаб элементов"
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=3, column=0, padx=10, pady=(0, 0))

    def button_command(self):
        print()
        print('Buttton is clicked!')
        print()

    def close_window(self):
        quit()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def chage_default_color_theme(self, new_default_color_theme: str):
        customtkinter.set_default_color_theme(new_default_color_theme)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

app = App()
app.mainloop()

