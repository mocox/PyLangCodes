import tkinter as tk


def init_menu(root: tk.Tk, action: lambda name: str):
    main_menu = tk.Menu(root)
    f_size: int = 10

    file_menu = tk.Menu(main_menu, tearoff=0, font=('Tahoma', f_size))
    file_menu.add_command(label="New", font=('Tahoma', f_size))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit, font=('Tahoma', f_size))
    main_menu.add_cascade(label="File", menu=file_menu, font=('Tahoma', f_size))

    file_menu = tk.Menu(main_menu, tearoff=0)
    file_menu.add_command(label="German", font=('Tahoma', f_size), command=lambda: action('German'))
    file_menu.add_command(label="Spanish", font=('Tahoma', f_size), command=lambda: action('Spanish'))
    file_menu.add_command(label="French", font=('Tahoma', f_size), command=lambda: action('French'))
    main_menu.add_cascade(label="Language", menu=file_menu, font=('Tahoma', f_size))

    root.config(menu=main_menu)

