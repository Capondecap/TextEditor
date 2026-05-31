import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
filename = None

def new_file():
    global filename
    filename = 'Untitled'
    text.delete(1.0,tk.END)


def saveAs():
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(1.0,tk.END)
    try:
        f.write(t.rstrip())
    except Exception:
        messagebox.showerror(
            title="Oops",
            message="Unable to save file"
        )
def save_file():
    global filename
    if filename:
        saveAs()
        return
    t = text.get(1.0,tk.END)
    with open(filename, 'w') as f:
        f.write(t.rstrip())

def openfile():
    f = filedialog.askopenfile(mode='r')
    t = f.read()
    text.delete(1.0,tk.END)
    text.insert(1.0, t)

root = tk.Tk()

root.title("Notepad")

root.geometry("400x400")

text = tk.Text(root, width=400, height=400)
text.pack()

menubar = tk.Menu(root)
filemenu= tk.Menu(menubar)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As", command=saveAs)
menubar.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()