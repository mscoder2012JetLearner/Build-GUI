from tkinter import*

window=Tk()
window.geometry=("400x400")
window.title=("spin = box")
sp=Spinbox(window,from_=1,to=10)
sp.place(x="10",y="10")


window.mainloop()