from tkinter import*
from tkinter.ttk import*
import time
window=Tk()
window.title=("progress bar")
window.geometry=("100x100")
def start_pb():
    s=store.get()
    nstore=IntVar()
    nstore=0
    while nstore<=100:
      pb["value"]=nstore
      window.update_idletasks()
      nstore=nstore+s
      time.sleep(0.2)
      print(store)

instruction=Label(window,text="how fast do you want the progress bar to move")
store=IntVar()
box=Combobox(window,textvariable=store,width=5)
box["values"]=tuple(range(1,11))
pb=Progressbar(window,orient=HORIZONTAL,length=100)
b=Button(window,text="press to start",command=start_pb)
pb.place(x="10",y="50")
b.place(x="10",y="100")
box.place(x="270",y="10")
instruction.place(x="10",y="10")


window.mainloop()