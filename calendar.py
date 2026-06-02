from tkinter import*
import calendar

def show_calendar():
    c_window=Tk()
    date=int(typebox.get())
    year_c=calendar.calendar(date)
    label=Label(c_window,text=year_c)
    label.place(x=0,y=0)
    c_window.mainloop()

window=Tk()
window.title("calendar")
window.config(background="white")
window.geometry("400x400")
Exit=Button(window,text="Exit",background="red",command=window.destroy,font=("Airal",10),bd=5)
Exit.place(x=180,y=350)
s_calendar=Button(window,text="Show Calendar",background="red",command=show_calendar,font=("Airal",10),bd=5)
s_calendar.place(x=150,y=310)
calendarl=Label(window,text="Calendar",font=("Airal",73),background="grey")
calendarl.place(x=0,y=10)
typebox=Entry(window,bd=3)
typebox.place(x=135,y=270)



window.mainloop()