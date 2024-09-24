import tkinter as tk


class GermanLanguage(tk.Frame):
    def __init__(self, parent, root):
        tk.Frame.__init__(self,parent)

        #self.configure(background='#000000')
        label = tk.Label(self, text="German", font=('Comic',15), foreground='#000000' )
        label.pack(pady=10)

        button = tk.Button(self, text="ü", command=lambda: root.copy_to_clipboard, bd='1')
        button.pack()



