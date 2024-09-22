import tkinter as tk
from menu import MainMenu
from German import GermanLanguage as Gl

class MainGui:
    def __init__(self):
        self.root = ''
        self.language = "German"
        self.init()

    def init(self):
        self.root = tk.Tk()
        self.root.title("Python Languages Codes")
        self.root.geometry("800x500")

        MainMenu(self.root, self.menu_clicked)
        if self.language == "German":
            Gl(self.root)
            print(f"Menu item clicked with parameter: {self.language}")
        elif self.language == "Spanish":
            print(f"Menu item clicked with parameter: {self.language}")
        else:
            print(f"Menu item clicked with parameter: {self.language}")

        self.root.mainloop()

    def menu_clicked(self, name: str)->str:
        print(f"Menu item clicked with parameter: {name}")
        self.language = name
        self.root.destroy()
        self.init()
        return name


if __name__ == "__main__":
    MainGui()