import tkinter as tk


class GermanLanguage:
    def __init__(self, root: tk.Tk()):
        self.root: tk.Tk = root

    def initialise(self):

        #self.root.frame = tk.Frame(self.root, height=100, width=100, bd=2, background='#ff0000')
        #self.root.frame.pack()

        label = tk.Label(self.root.frame, text="German", font=('Comic',15), foreground='#00ff00' )
        label.pack()


