import tkinter as tk


class FrenchLanguage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #self.configure(background='#000000')
        label = tk.Label(self, text="French", font=('Comic', 15), foreground='#00ff00')
        label.pack(pady=10)