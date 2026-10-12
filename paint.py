from tkinter import*
from tkinter.colorchooser import askcolor
window=Tk()
window.geometry("500x500")

defaultcolour="white"
startpointx=None
startpointy=None


def buttondown(bname):
    global dab
    dab.config(relief=RAISED)
    bname.config(relief=SUNKEN)
    dab=bname


def penactive():
    buttondown(pen)

def brushactive():
    buttondown(brush)

def eraserdown():
    buttondown(eraser)

def choosecolour():
    global defaultcolour
    defaultcolour=askcolor(defaultcolour)[1]

def draw(event):
    global startpointx
    global startpointy
    lw=s.get()
    if startpointx and startpointy:
        c.create_line(startpointx,startpointy,event.x,event.y,width=lw,fill=defaultcolour)
    startpointx=event.x
    startpointy=event.y

def stopdraw(event):
    global startpointx,startpointy
    startpointx=None
    startpointy=None


pen=Button(window,text="Pen",command=penactive)
pen.place(x=10,y=10)

brush=Button(window,text="Brush",command=brushactive)
brush.place(x=110,y=10)

colour=Button(window,text="Colour",command=choosecolour)
colour.place(x=210,y=10)

eraser=Button(window,text="Eraser",command=eraserdown)
eraser.place(x=310,y=10)

s=Scale(window,from_=1,to=10,orient=HORIZONTAL)
s.place(x=380,y=0)

c=Canvas(window,bg="Black",width=500,height=470,bd=3,highlightbackground="Black")
c.place(x=0,y=100)
c.bind("<B1-Motion>",draw)
c.bind("<ButtonRelease-1>",stopdraw)

dab=pen

window.mainloop()