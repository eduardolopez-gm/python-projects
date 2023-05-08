import tkinter as tk
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text_content = text.get(1.0, tk.END)
        file.write(text_content)
        file.close()


def open_file():
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    if file:
        text_content = file.read()
        text.delete(1.0, tk.END)
        text.insert(tk.INSERT, text_content)


root = tk.Tk()
root.title("Notepad in Python")

text = tk.Text(root)
text.pack()

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

root.mainloop()
