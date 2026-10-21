# Code editor app

import tkinter as tk
from tkinter import filedialog , messagebox

#Main window code
root = tk.Tk()
root.title("My text editor")
root.geometry("500x300")

# Create text area
text = tk.Text(root,wrap=tk.WORD, font=("Helvetica",12))

text.pack(expand=True,fill=tk.BOTH)

# Main logic starting
# Function - to create a new file

def new_file():
    text.delete(1.0,tk.END)

# Function to open a file:

def open_file():
    file_path = filedialog.askopenfile(
        defaultextension=".txt",
        filetypes={("Text Files","*.txt")}
    )

    if file_path:
        #OPen file
        with open(file_path, "r")as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

# File saving code 

def save_file():
    #Open save file dialogue
    file_path = filedialog.asksaveasfilename(defaultextension="*.txt",filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info", "File saved succesfully")

# MENU

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)

# New , open file , save , exit
# Add file to menu bar
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

menu.add_cascade(label="Edit",menu=file_menu)

# it starts and keeps the window open
root.mainloop()

