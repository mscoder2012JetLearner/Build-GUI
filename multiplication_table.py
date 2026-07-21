from tkinter import*
from tkinter.ttk import*
import tkinter as tk


def multiplication_grid():
    s=store.get()
    r=rstore.get()
    result=""
    for i in range(1,r):
        a=s*i
        result=result+str(s)+"*"+str(i)+"="+str(a)+"\n"
    mgrid.config(text=result)




window=Tk()
window.title("multiplication")
window.config(backgroun="white")
window.geometry("500x500")
title=Label(window,text="Multiplication Square")
title.grid(row=0,column=2,padx=10,pady=25)
sr=Label(window,text="Number and Range",background="grey")
sr.grid(row=2,column=0)
store=IntVar()
box=Combobox(window,textvariable=store,width=5)
box.grid(row=2,column=1)
box["values"]=tuple(range(0,101))
rstore=IntVar()
ten=Radiobutton(window,text="10",variable=rstore,value=10)
twenty=Radiobutton(window,text="20",variable=rstore,value=20)
thirty=Radiobutton(window,text="30",variable=rstore,value=30)
ten.grid(row=3,column=3)
twenty.grid(row=4,column=3)
thirty.grid(row=5,column=3)
show_grid=tk.Button(window,text="show multiplication table",bd=4,backgroun="green",command=multiplication_grid)
show_grid.place(x=130,y=200)
mgrid=Label(window)
mgrid.place(x=400,y=10)
rstore.set(10)
window.mainloop()