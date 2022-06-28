
from tkinter import *
from tkinter import messagebox

root =Tk()

def hello():
    messagebox.showinfo("hello world", "hello today")

myButton = Button(root, text="Click Me", padx=10, pady=50, command=hello())

myButton.pack()
root.mainloop()