from tkinter import*


root = Tk()





def myClick():
    myLabel = Label(root, text="Hey you clicked", fg="red", bg="#00FFFF")
    myLabel.pack()

myB = Button(root, text="Click Me!", command=myClick, fg="blue", bg="black")
myB.pack()

root.mainloop()