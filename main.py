import tkinter as tk
import menu


def main_gui():
    root = tk.Tk()
    root.title("Python Languages Codes")
    root.geometry("800x500")

    menu.init_menu(root, menu_clicked)
    root.mainloop()


def menu_clicked(name: str)->str:
    print(f"Menu item clicked with parameter: {name}")
    return name

if __name__ == "__main__":
    main_gui()