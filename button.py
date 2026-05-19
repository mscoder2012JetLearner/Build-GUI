from tkinter import*

window=Tk()
window.title("Button")
window.config(background="black")
window.geometry("400x400")
button=Button(window,text="Don't click me or I will die a painful death",background="red",command=window.destroy,bd="20")
button.pack(side="top")
l=Label(window,text="Don't click me",background="blue",foreground="white")
l.pack(side="bottom")
typebox=Entry(window)
typebox.place(x=130,y=200)
window.mainloop()
