from tkinter import*

window=Tk()
window.geometry("600x600")
l=Label(window,text="listboxes, scrolllbars and frames")
f=Frame(window)
s=Scrollbar(f)
l.place(x=40,y=10)
#s.place(x=200,y=0)
s.pack(side=LEFT,fill=Y)
lb=Listbox(f,yscrollcommand=s.set)
s.config(command=lb.yview)
for i in range(100):
  lb.insert(END,"pounds "+str(i))
lb.pack(side=RIGHT)
f.place(x=20,y=40)
window.mainloop()