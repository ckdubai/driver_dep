from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import os


import driver_backend

filename=''
save_dir='driver_images/'
save_img=''
image_path=''

""" check for folder exist otherwise create it """
if not os.path.exists('driver_images'):
    os.makedirs('driver_images')

def save_image():
   #if not str(os.path.exists(filena)):
    #print("image path is"+image_path)
    save_img.save(image_path,'JPEG')



def add_command():
    #print("image path = "+image_path)
    driver_backend.insert(ID_text.get(),name_text.get(),vehicle_text.get(),plate_text.get(),location_text.get(),image_path)
    view_command()
    save_image()
    clear_textfield()

def view_command():
    tree.delete(*tree.get_children())
    for row in driver_backend.view():
        tree.insert("",END,values=row)
        tree.column("#1", width=0)

def get_selected_row(event):

    clear_textfield()
    global selected_tuple
    for selected_tuple in tree.selection():
        global id
        id,emp_id,name,vehicle,plate_no,work_location,image_path = tree.item(selected_tuple, 'values')
        e1.insert(END, emp_id)
        e2.insert(END, name)
        e3.insert(END, vehicle)
        e4.insert(END, plate_no)
        e5.insert(END, work_location)
        display_image(image_path)

def clear_textfield():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

def update_command():
    #print(image_path)
    driver_backend.update(id,ID_text.get(),name_text.get(),vehicle_text.get(),plate_text.get(),location_text.get(),image_path)
    save_image()
    view_command()
    clear_textfield()


def search_command():
    tree.delete(*tree.get_children())
    for row in driver_backend.search(ID_text.get(),name_text.get(),vehicle_text.get(),plate_text.get(),location_text.get()):
        tree.insert("",END,values=row)

def delete_command():
    driver_backend.delete(id)
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

b2=Button(window,text="Search", width=12,command=search_command)
b2.grid(row=4,column=1)

b3=Button(window,text="Add", width=12,command=add_command)
b3.grid(row=4,column=2)

b4=Button(window,text="Update", width=12,command=update_command)
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

""" Treeview """
tree= ttk.Treeview(window, column=("ID","Employee ID", "Name", "Vehicle"," Plate No:","Work Location"), show='headings')
tree.heading("#1", text="ID")
tree.heading("#2", text="Employee ID")
tree.heading("#3", text="Name")
tree.heading("#4", text="Vehicle")
tree.heading("#5", text="Plate No:")
tree.heading("#6", text="Work Location")
tree.grid(row=6,column=0,rowspan=6,columnspan=7)

tree.bind("<<TreeviewSelect>>",get_selected_row)

""" upload image"""
def openfn():
     global filename
     filename= filedialog.askopenfilename(title='open')


def open_img():
    openfn()
    global image_path, save_img
    image_path = getImagePath(filename)
    #print("image path = "+image_path)
    save_img=Image.open(filename)
    img = Image.open(filename)
    #img.save(image_name,'JPEG')
    img = img.resize((55, 65), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.grid(row=0,column=4,rowspan=3,columnspan=2)

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((55, 65), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.image = img
    panel.grid(row=0,column=4,rowspan=3,columnspan=2)


def getImagePath(filename):
    global filena
    filena = filename.split('/')[-1]
    new_path = save_dir+filena
    return new_path


btn = Button(window, text='open image', command=open_img).grid(row=2,column=3)

window.mainloop()
