import tkinter as tk
from menu import MainMenu
from German import GermanLanguage as Gl
from Spanish import SpanishLanguage as Sl

class MainGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Languages Codes")
        self.root.geometry("800x500")

        self.language = "German"
        # menu
        MainMenu(self.root, self.menu_clicked)
        self.init()
        self.root.mainloop()

    def init(self):
        # language frame
        if self.language == "German":
            Gl(self.root).initialise()
            print(f"Menu item clicked with parameter: {self.language}")
        elif self.language == "Spanish":
            Sl(self.root).initialise()
            print(f"Menu item clicked with parameter: {self.language}")
        else:
            print(f"Menu item clicked with parameter: {self.language}")

        self.root.update()

    def menu_clicked(self, name: str)->str:
        print(f"Menu item clicked with parameter: {name}")
        self.language = name
        self.init()
        return name


if __name__ == "__main__":
    MainGui()