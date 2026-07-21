from tkinter import*
from tkinter.ttk import*
import time
window=Tk()
window.title=("progress bar")
window.geometry=("400x400")
def start_pb():
    for i in range(100):
      pb["value"]=i
      window.update_idletasks()
      time.sleep(0.2)




pb=Progressbar(window,orient=HORIZONTAL,length=100)
b=Button(window,text="press to start",command=start_pb)
pb.place(x="10",y="10")
b.place(x="50",y="50")


window.mainloop()