from tkinter import*
from tkinter import messagebox
import random
window=Tk()
window.geometry("400x400")
realnumber=random.randint(0,20)
def nmessage():
    name=na.get()
    messagebox.showinfo("Helllo",("Hello "+name+" Welcome to the number guesser game"))

def usserguess():
    num=int(nu.get())
    if num==realnumber:
        messagebox.showinfo("Correct",("Correct, the number was "+str(realnumber)))
    if num>realnumber:
        messagebox.showinfo("Incorrect",("Wrong, the number is less than "+str(num)))
    if num<realnumber:
        messagebox.showinfo("Incorrect",("Wrong, the real number is more than "+str(num)))



title=Label(window,text="Welcome to the number guesser game ")
title.place(x=80,y=50)

whatname=Label(window,text="What is your name?")
whatname.place(x=10,y=100)

na=Entry(window)
na.place(x=10,y=120)

enter=Button(window,text="enter",command=nmessage)
enter.place(x=200,y=120)

q=Label(window,text="What do you think the number is")
q.place(x=10,y=250)

nu=Entry(window)
nu.place(x=200,y=250)

g=Button(window,text="guess",command=usserguess)
g.place(x=350,y=250)



window.mainloop()