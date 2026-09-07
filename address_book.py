from tkinter import*
from tkinter.filedialog import*

d={}
window=Tk()
window.title=("address book")
window.geometry("600x600")
f=Frame(window)
f.place(x=50,y=100)

s=Scrollbar(f)
l=Listbox(f,yscrollcommand=s.set,width=30,height=20)
s.config(command=l.yview)
s.pack(side="left",fill=Y)
l.pack(side="right")

def wipe():
    openn.delete(0,END)
    opena.delete(0,END)
    openm.delete(0,END)
    openem.delete(0,END)
    openb.delete(0,END)

def u():
    n=openn.get()
    v=(opena.get(),openm.get(),openem.get(),openb.get())
    d[n]=v
    l.insert(END,n)
    print(d)
    wipe()

def delete_dictionary():
    item=l.curselection()
    na=l.get(item)
    del d[na]
    l.delete(item)
    print(d)

def com():
    item=l.curselection()
    na=l.get(item)
    gv=d[na]
    openn.insert(0,na)
    opena.insert(0,gv[0])
    openm.insert(0,gv[1])
    openem.insert(0,gv[2])
    openb.insert(0,gv[3])






edit=Button(window,text="Edit",command=com)
edit.place(x=100,y=450)

delete=Button(window,text="Delete",command=delete_dictionary)
delete.place(x=170,y=450)

save=Button(window,text="Save",width=15)
save.place(x=80,y=520)

title=Label(window,text="My address book")
title.place(x=10,y=10)

open=Button(window,text="Open")
open.place(x=250,y=10)

name=Label(window,text="Name:")
name.place(x=350,y=50)
openn=Entry(window)
openn.place(x=400,y=50)


address=Label(window,text="Address:")
address.place(x=350,y=150)
opena=Entry(window)
opena.place(x=400,y=150)


mobile=Label(window,text="Mobile:")
mobile.place(x=350,y=250)
openm=Entry(window)
openm.place(x=400,y=250)


email=Label(window,text="Email:")
email.place(x=350,y=350)
openem=Entry(window)
openem.place(x=400,y=350)


birthday=Label(window,text="Birthday:")
birthday.place(x=350,y=450)
openb=Entry(window)
openb.place(x=400,y=450)


ua=Button(window,text="Update/Add",command=u)
ua.place(x=400,y=520)



window.mainloop()




