from tkinter import*
from tkinter import messagebox
import random
window=Tk()
window.geometry("600x600")
t=1
xscore=0
oscore=0

def clear():
      global t
      tl["text"]=""
      tm["text"]=""
      tr["text"]=""
      ml["text"]=""
      mm["text"]=""
      mr["text"]=""
      bl["text"]=""
      bm["text"]=""
      br["text"]=""
      t=random.randint(0,1)
      messagebox.showinfo("score",("X=",xscore,"O=",oscore))
      




def value(buttons):
    global t
    global xscore
    global oscore
    if t%2==0:
        if buttons["text"]=="":
            buttons["text"]="O"
            t=t+1
    else:
        if buttons["text"]=="":
            buttons["text"]="X"
            t=t+1
    if tl["text"]==tm["text"]==tr["text"]!="":
        messagebox.showinfo("The winner is...",("the winner is "+tl["text"]))
        if tl["text"]=="X":
              xscore=xscore+1
        elif tl["text"]=="O":
              oscore=oscore+1
        clear()

    if tl["text"]==mm["text"]==br["text"]!="":
            messagebox.showinfo("The winner is...",("the winner is "+tl["text"]))
            if tl["text"]=="X":
                xscore=xscore+1
            elif tl["text"]=="O":
                oscore=oscore+1
            clear()

    if ml["text"]==mm["text"]==mr["text"]!="":
            messagebox.showinfo("The winner is...",("the winner is "+mm["text"]))
            if mm["text"]=="X":
                xscore=xscore+1
            elif mm["text"]=="O":
                oscore=oscore+1
            clear()

    if tl["text"]==ml["text"]==bl["text"]!="":
            messagebox.showinfo("The winner is...",("the winner is "+tl["text"]))
            if tl["text"]=="X":
                          xscore=xscore+1
            elif tl["text"]=="O":
                          oscore=oscore+1
            clear()

    if tr["text"]==br["text"]==mr["text"]!="":
            messagebox.showinfo("The winner is...",("the winner is "+tr["text"]))
            if tr["text"]=="X":
                xscore=xscore+1
            elif tr["text"]=="O":
                          oscore=oscore+1
            clear()

    if bl["text"]==bm["text"]==br["text"]!="":
            messagebox.showinfo("The winner is...",("the winner is "+bl["text"]))
            if bl["text"]=="X":
                          xscore=xscore+1
            elif bl["text"]=="O":
                          oscore=oscore+1
            clear()

    if bl["text"]==mm["text"]==tr["text"]!="":
            messagebox.showinfo("The winner is...",("the winner is "+bl["text"]))
            if bl["text"]=="X":
                          xscore=xscore+1
            elif bl["text"]=="O":
                          oscore=oscore+1
            clear()

    if bm["text"]==mm["text"]==tm["text"]!="":
                messagebox.showinfo("The winner is...",("the winner is "+bm["text"]))
                if bm["text"]=="X":
                              xscore=xscore+1
                elif bm["text"]=="O":
                              oscore=oscore+1
                clear()


    if tl["text"]!=""and tm["text"]!=""and tr["text"]!="" and mr["text"]!="" and mm["text"]!="" and ml["text"]!="" and bl["text"]!="" and bm["text"]!="" and br["text"]!="":
          messagebox.showinfo("The winner is...",("It was a draw"))
          clear()
 




tl=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(tl))
tl.place(x=0,y=0,width=200,height=200)
tm=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(tm))
tm.place(x=200,y=0,width=200,height=200)
tr=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(tr))
tr.place(x=400,y=0,width=200,height=200)
ml=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(ml))
ml.place(x=0,y=200,width=200,height=200)
mm=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(mm))
mm.place(x=200,y=200,width=200,height=200)
mr=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(mr))
mr.place(x=400,y=200,width=200,height=200)
bl=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(bl))
bl.place(x=0,y=400,width=200,height=200)
bm=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(bm))
bm.place(x=200,y=400,width=200,height=200)
br=Button(window,bd=2,relief="solid",font=("Arial",100,"bold"),command=lambda:value(br))
br.place(x=400,y=400,width=200,height=200)


window.mainloop()