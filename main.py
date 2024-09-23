import tkinter as tk
from menu import MainMenu
from German import GermanLanguage as Gl
from Spanish import SpanishLanguage as Sl
from French import FrenchLanguage as Fr

class MainGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Python Languages Codes")
        self.geometry("800x500")

        self.language = "German"

        self.root = tk.Frame(self)
        self.root.pack(side="top", fill="both", expand = True)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # menu
        MainMenu(self, self.menu_clicked)

        self.frames = {}

        for F in (Gl, Sl, Fr):
            frame = F(self.root)
            #frame.pack()
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Gl)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def menu_clicked(self, name: str):
        print(f"Menu item clicked with parameter: {name}")

        if name == "German":
            self.show_frame(Gl)
        elif name == "Spanish":
            self.show_frame(Sl)
        else:
            self.show_frame(Fr)


if __name__ == "__main__":
    app = MainGui()
    app.mainloop()