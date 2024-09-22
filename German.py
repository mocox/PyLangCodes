import tkinter as tk


class GermanLanguage:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.initialise()

    def initialise(self):
        g_frame = tk.Frame(self.root, height=100, width=100, bd=2, background='#ff0000')
        g_frame.pack()

        label = tk.Label(g_frame, text="German", font=('Comic',15), foreground='#00ff00' )
        label.pack()

