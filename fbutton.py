from tkinter import*

root = Tk()
def myClick():
    myLabel = Label(root, text="Hey you clicked")
    myLabel.pack()

myB = Button(root, text="Click Me!", command=myClick)
myB.pack()

root.mainloop()