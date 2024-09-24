import tkinter as tk


class SpanishLanguage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        #self.configure(background='#000000')
        label = tk.Label(self, text="Spanish", font=('Comic', 15), foreground='#000000')
        label.pack(pady=10)