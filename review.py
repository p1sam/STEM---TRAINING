from tkinter import*


root = Tk()
entry1 = Entry(root, )
entry2 = Entry(root, )


def myCLick():
    global entry1
    str_ = entry1.get()
    if "*" in str_:
        y = str_.index("*")
        f_no = str_[:y]
        s_no = str_[y+1:]
        ans = int(f_no) * int(s_no)
        
        entry1 = ans



myB = Button(root, text="=", command=myCLick, fg="blue", bg="black")

entry1.pack()
myB.pack()
root.mainloop()