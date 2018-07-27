from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
root.title("calculator")
root.resizable(False,False)

operator=""
textin=StringVar()
def clickbut(numbers):
    global operator
    operator=operator+str(numbers)
    textin.set(operator)

def equlbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''



def equlbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''


def equlbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''


def equlbut():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=''




def clear():
    textin.set('')


topframe=Frame(root)
topframe.pack(side=TOP)
txtDisplay=Entry(frame,textvariable=textin,bd=20,insertwidth=1,font=30,bg="cyan")
txtDisplay.pack(side=TOP)

button1=Button(topframe,padx=18,pady=16,bd=8,text="1",fg="black",command=lambda: clickbut(1),bg="cyan")
button1.pack(side=LEFT)
button2=Button(topframe,padx=18,pady=16,bd=8,text="2",fg="black",command=lambda: clickbut(2),bg="cyan")
button2.pack(side=LEFT)
button3=Button(topframe,padx=18,pady=16,bd=8,text="3",fg="black",command=lambda: clickbut(3),bg="cyan")
button3.pack(side=LEFT)
button4=Button(topframe,padx=18,pady=16,bd=8,text="/",command=lambda: clickbut("/"),fg="black",bg="cyan")
button4.pack(side=LEFT)

frame1=Frame(root)
frame1.pack(side=TOP)

button1=Button(frame1,padx=18,pady=16,bd=8,text="4",fg="black",command=lambda: clickbut(4),bg="cyan")
button1.pack(side=LEFT)
button2=Button(frame1,padx=18,pady=16,bd=8,text="5",fg="black",command=lambda: clickbut(5),bg="cyan")
button2.pack(side=LEFT)
button3=Button(frame1,padx=18,pady=16,bd=8,text="6",fg="black",command=lambda: clickbut(6),bg="cyan")
button3.pack(side=LEFT)
button4=Button(frame1,padx=18,pady=16,bd=8,text="-",fg="black",command=lambda: clickbut("-"),bg="cyan")
button4.pack(side=LEFT)

frame2=Frame(root)
frame2.pack()
button1=Button(frame2,padx=17,pady=16,bd=8,text="7",fg="black",command=lambda: clickbut(7),bg="cyan")
button1.pack(side=LEFT)
button2=Button(frame2,padx=18,pady=16,bd=8,text="8",fg="black",command=lambda: clickbut(8),bg="cyan")
button2.pack(side=LEFT)
button3=Button(frame2,padx=18,pady=16,bd=8,text="9",fg="black"
  ,command=lambda: clickbut(9),bg="cyan")
button3.pack(side=LEFT)
button4=Button(frame2,padx=17,pady=16,bd=8,text="+",command=lambda: clickbut("+"),fg="black",bg="cyan")
button4.pack(side=LEFT)

frame3=Frame(root)
frame3.pack()
button1=Button(frame3,padx=18,pady=16,bd=8,text="C",command=lambda: clear(),fg="black",bg="cyan")
button1.pack(side=LEFT)
button2=Button(frame3,padx=18,pady=16,bd=8,text="0",fg="black",command=lambda: clickbut(0),bg="cyan")
button2.pack(side=LEFT)
button3=Button(frame3,padx=18,pady=16,bd=8,text=".",command=lambda: clickbut("."),fg="black",bg="cyan")
button3.pack(side=LEFT)
button4=Button(frame3,padx=18,pady=16,bd=8,text="x",command=lambda: clickbut("*"),fg="black",bg="cyan")
button4.pack(side=LEFT)

frame4=Frame(root)
frame4.pack()
button1=Button(frame4,padx=109,pady=10,bd=8,text="=",command=equlbut,fg="black",bg="cyan")
button1.pack(side=LEFT)

root.mainloop()