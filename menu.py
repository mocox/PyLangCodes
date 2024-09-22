import tkinter as tk

class MainMenu:
    def __init__(self, root: tk.Tk, action: lambda name: str):
        self.f_size: int = 10
        self.root = root
        self.action = action
        self.main_menu = tk.Menu(root)
        self.create_file_menu()
        self.create_language_menu()
        self.root.config(menu=self.main_menu)

    def create_file_menu(self):
        file_menu = tk.Menu(self.main_menu, tearoff=0, font=('Tahoma', self.f_size))
        file_menu.add_command(label="New", font=('Tahoma', self.f_size))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit, font=('Tahoma', self.f_size))
        self.main_menu.add_cascade(label="File", menu=file_menu, font=('Tahoma', self.f_size))

    def create_language_menu(self):
        language_menu = tk.Menu(self.main_menu, tearoff=0)
        language_menu.add_command(label="German", font=('Tahoma', self.f_size), command=lambda: self.action('German'))
        language_menu.add_command(label="Spanish", font=('Tahoma', self.f_size), command=lambda: self.action('Spanish'))
        language_menu.add_command(label="French", font=('Tahoma', self.f_size), command=lambda: self.action('French'))
        self.main_menu.add_cascade(label="Language", menu=language_menu, font=('Tahoma', self.f_size))



