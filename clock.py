from tkinter import*

window=Tk()

from time import strftime

def ti():
  
  t=strftime("%H:%M:%S %p")
  clock_time.config(text=t)
  clock_time.after(1000,ti)


clock_time=Label(window)
clock_time.place(x=0,y=0)
ti()
window.mainloop()