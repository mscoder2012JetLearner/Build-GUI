from tkinter import*
from tkinter import messagebox

window=Tk()

messagebox.showinfo("information box","information")

messagebox.showwarning("WARNING!","warning")

messagebox.showerror("Error","There is an error")

messagebox.askquestion("question","would you like to continue")

messagebox.askokcancel("ok/cancel","print")

messagebox.askyesno("yes no","would you like to save")

messagebox.askretrycancel("retry cancel","there was an error")