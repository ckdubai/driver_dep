from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

import driver_backend

def add_command():
    driver_backend.insert(ID_text.get(),name_text.get(),vehicle_text.get(),plate_text.get(),location_text.get(),filename)
    view_command()
    #clear_textfield()
def view_command():
    list1.delete(0,END)
    for row in driver_backend.view():
        list1.insert(END,row)

def delete_command():
    driver_backend.delete(selected_tuple[0])
    view_command()

window=Tk()


window.wm_title("Drivers Details")

l1=Label(window,text="ID No:")
l1.grid(row=0,column=0)

l2=Label(window,text="Name")
l2.grid(row=0,column=2)

l3=Label(window,text="Vehicle")
l3.grid(row=1,column=0)

l4=Label(window,text="Plate:")
l4.grid(row=1,column=2)

l5=Label(window,text="Work Location:")
l5.grid(row=2,column=0)

l6=Label(window,text="Upload Photo")
l6.grid(row=2,column=2)

b1=Button(window,text="view All", width=12,command=view_command)
b1.grid(row=4,column=0)

b2=Button(window,text="Search", width=12)
b2.grid(row=4,column=1)

b3=Button(window,text="Add", width=12,command=add_command)
b3.grid(row=4,column=2)

b4=Button(window,text="Update", width=12)
b4.grid(row=4,column=3)

b5=Button(window,text="Delete", width=12,command=delete_command)
b5.grid(row=4,column=4)

b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=4,column=5)

ID_text=StringVar()
e1=Entry(window,textvariable=ID_text)
e1.grid(row=0,column=1)

name_text=StringVar()
e2=Entry(window,textvariable=name_text)
e2.grid(row=0,column=3)

vehicle_text=StringVar()
e3=Entry(window,textvariable=vehicle_text)
e3.grid(row=1,column=1)

plate_text=StringVar()
e4=Entry(window,textvariable=plate_text)
e4.grid(row=1,column=3)

location_text=StringVar()
e5=Entry(window,textvariable=location_text)
e5.grid(row=2,column=1)

list1=Listbox(window, height=6,width=100)
list1.grid(row=6,column=0,rowspan=6,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=6,column=7,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)




def openfn():
    global filename
    filename = filedialog.askopenfilename(title='open')

def open_img():
    openfn()
    img = Image.open(filename)
    img = img.resize((55, 65), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.grid(row=0,column=4,rowspan=3,columnspan=2)

image_path=StringVar()
btn = Button(window, text='open image', command=open_img).grid(row=2,column=3)

window.mainloop()
