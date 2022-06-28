from tkinter import*


root = Tk()



e = Entry(root, width=50, bg="black", fg="red")

def myClick():
    hello="Hello " + e.get()
    myLabel = Label(root, text=hello, fg="red", bg="#00FFFF")
    myLabel.pack()

myB = Button(root, text="Enter your name", command=myClick, fg="blue", bg="black")
myB.pack()
e.pack()
e.insert(1, "Enter your name here")

root.mainloop()


def myClick():
    