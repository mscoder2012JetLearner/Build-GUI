from tkinter import*
import calendar

def show_calendar():
    c_window=Tk()
    c_window.title("calendar_year")
    d=int(typebox.get())
    year_c=calendar.calendar(d)
    label=Label(c_window,text=year_c,font=("Airal",10),padx=3,pady=3)
    label.place(x=20,y=20)
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