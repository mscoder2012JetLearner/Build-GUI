from tkinter import*
window=Tk()
window.geometry("600x600")
t=1
def value(buttons):
    global t
    if t%2==0:
        if buttons["text"]=="":
            buttons["text"]="O"
            t=t+1
    else:
        if buttons["text"]=="":
            buttons["text"]="X"
            t=t+1


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