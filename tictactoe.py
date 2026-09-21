from tkinter import*
window=Tk()
window.geometry("600x600")
t=0
def value(buttons):
    global t
    t=t+1
    if t%2==0:
        buttons["text"]="O"
    else:
        buttons["text"]="X"


tl=Button(window,width=20,bd=2,relief="solid",command=lambda:value(tl))
tl.place(x=0,y=0)
tm=Button(window,width=20,bd=2,relief="solid",command=lambda:value(tm))
tm.place(x=200,y=0)
tr=Button(window,width=20,bd=2,relief="solid",command=lambda:value(tr))
tr.place(x=400,y=0)
ml=Button(window,width=20,bd=2,relief="solid",command=lambda:value(ml))
ml.place(x=0,y=200)
mm=Button(window,width=20,bd=2,relief="solid",command=lambda:value(mm))
mm.place(x=200,y=200)
mr=Button(window,width=20,bd=2,relief="solid",command=lambda:value(mr))
mr.place(x=400,y=200)
bl=Button(window,width=20,bd=2,relief="solid",command=lambda:value(bl))
bl.place(x=0,y=400)
bm=Button(window,width=20,bd=2,relief="solid",command=lambda:value(bm))
bm.place(x=200,y=400)
br=Button(window,width=20,bd=2,relief="solid",command=lambda:value(br))
br.place(x=400,y=400)


window.mainloop()