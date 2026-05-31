import tkinter as tk
from tkinter import filedialog

filename = None

def new_file():
    global filename
    filename = 'Untitled'
    text.delete(0,0,tk.END)


def savAs():
    f = tk.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0,0,tk.END)
    try:
        f.write(t.rstrip())
    except Exception:
        tk.showerror(title="opps", message="Unable to save file")

def save_file():
    global filename
    t = text.get(0,0,tk.END)
    f = open(filename, 'w')
    f.write(t)
    f.close()


def openfile():
    f = tk.askopenfile(mode='r')
    t = f.read()
    text.delete(0,0,tk.END)
    text.insert(0.0, t)

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
filemenu.add_command(label="Save As", command=savAs)
menubar.add_separator
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()