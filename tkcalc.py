from tkinter import*


root = Tk()
entry = ""
root.title("simple calculator")
def press(num):
    global entry
    entry += str(num)
    linear.set(entry)

def equal():
    sol=str(eval(entry))
    linear.set(sol)

def clear():
    global entry
    entry=""
    linear.set(entry)

linear = StringVar()

expression = Entry(root, text=linear)
expression.grid(columnspan=4, ipadx=70)

b1 = Button(root, text="1", command=lambda:press(1), height=1, width=7 )
b1.grid(row=1, column=0)

b2 = Button(root, text="2", command=lambda:press(2), height=1, width=7 )
b2.grid(row=1, column=1)

b3 = Button(root, text="3", command=lambda:press(3), height=1, width=7 )
b3.grid(row=1, column=2)

bplus= Button(root, text="+", command=lambda:press("+"), height=1, width=7 )
bplus.grid(row=1, column=3)

b4 = Button(root, text="4", command=lambda:press(4), height=1, width=7 )
b4.grid(row=2, column=0)

b5 = Button(root, text="5", command=lambda:press(5), height=1, width=7 )
b5.grid(row=2, column=1)

b6 = Button(root, text="6", command=lambda:press(6), height=1, width=7 )
b6.grid(row=2, column=2)

b7 = Button(root, text="7", command=lambda:press(7), height=1, width=7 )
b7.grid(row=3, column=0)

b8 = Button(root, text="8", command=lambda:press(8), height=1, width=7 )
b8.grid(row=3, column=1)

b9 = Button(root, text="9", command=lambda:press(9), height=1, width=7 )
b9.grid(row=3, column=2)

b0 = Button(root, text="0", command=lambda:press(0), height=1, width=7 )
b0.grid(row=4, column=1)

bequal = Button(root, text="=", command=lambda:equal(), height=1, width=7 )
bequal.grid(row=4, column=3)

bmult = Button(root, text="*", command=lambda:press("*"), height=1, width=7 )
bmult.grid(row=2, column=3)

bsub = Button(root, text="-", command=lambda:press("-"), height=1, width=7 )
bsub.grid(row=3, column=3)

bdiv = Button(root, text="/", command=lambda:press("/"), height=1, width=7 )
bdiv.grid(row=4, column=2)

bclear = Button(root, text="clear", command=lambda:clear(), height=1, width=7 )
bclear.grid(row=4, column=0)

root.mainloop()