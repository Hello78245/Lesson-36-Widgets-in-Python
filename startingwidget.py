from tkinter import *
from datetime import date
root=Tk()
root.title('Getting started with Widgets')
root.geometry('400x300')
lbl=Label(text="Hello There!", fg="white",bg="#0FA3B1", height=1, width=300)
name_lbl=Label(text="Full name", bg="#F1D302")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to the Application! \nToday's Date is:"
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())
text_box=Text(height=3)
btn=Button(text="Begin", command=display, height=1, bg="#AE8E1C", fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()