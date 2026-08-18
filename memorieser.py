from tkinter import*
from tkinter.filedialog import*

window=Tk()
window.title=("memorieser")
window.geometry("600x450")
f=Frame(window)
f.place(x=50,y=100)

s=Scrollbar(f)
l=Listbox(f,yscrollcommand=s.set)
s.config(command=l.yview)
s.pack(side="left",fill=Y)
l.pack(side="right")

for i in range(100):
    l.insert(END, "List "+str(i))


def savef():
    fn=asksaveasfile(defaultextension=".txt")
    for i in l.get(0,END):
        print(i,file=fn)
    l.delete(0,END)


def addv():
    eg=e.get()
    l.insert(END,eg)
    e.delete(0,END)


open=Button(window,text="open")
open.place(x=250,y=50)

delete=Button(window,text="Delete")
delete.place(x=350,y=50)

save=Button(window,text="save",command=savef)
save.place(x=450,y=50)

add=Button(window,text="add",command=addv)
add.place(x=300,y=200)


e=Entry(window)
e.place(x=280,y=150)



window.mainloop()