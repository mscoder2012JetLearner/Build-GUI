from tkinter import*

def convert_it():
    a=int(typebox.get())
    b=a*9
    c=b/5
    d=c+32
    answerbox.config(text=d)



window=Tk()
window.title("converter")
window.config(background="white")
window.geometry("400x400")
convert=Button(window,text="convert",background="red",font=("Airal",30),bd=10,command=convert_it)
convert.place(x=120,y=250)
title=Label(window,text="Celsius to Fahrenheit",font=("Airal",31),background="grey")
title.place(x=0,y=10)
typebox=Entry(window,bd=3)
typebox.place(x=140,y=220)
answerbox=Label(window,text=" ",background="green")
answerbox.place(x=140,y=180)

window.mainloop()