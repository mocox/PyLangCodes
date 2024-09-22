import tkinter as tk
from menu import MainMenu

class MainGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Languages Codes")
        self.root.geometry("800x500")

        MainMenu(self.root, self.menu_clicked)

        self.root.mainloop()

    @staticmethod
    def menu_clicked(name: str)->str:
        print(f"Menu item clicked with parameter: {name}")
        return name


if __name__ == "__main__":
    MainGui()