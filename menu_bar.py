from tkinter import*

window=Tk()
window.title("menu")
window.geometry("500x500")
m=Menu(window)
file=Menu(m,tearoff=0)
edit=Menu(m,tearoff=0)
help=Menu(m,tearoff=0)

m.add_cascade(label="File",menu=file)
m.add_cascade(label="Edit",menu=edit)
m.add_cascade(label="Help",menu=help)
file.add_command(label="new file",command=None)
file.add_separator()
file.add_command(label="open file",command=None)
file.add_command(label="open folder",command=None)
file.add_separator()
file.add_command(label="save",command=None)
file.add_command(label="save as...",command=None)
window.config(menu=m)
window.config
window.mainloop()