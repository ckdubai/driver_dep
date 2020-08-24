from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import os

import driver_backend

namelist=''
filename=''
save_dir='driver_images/'
save_img=''
image_path=''

namelist = driver_backend.getDriverName()





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

tab_parent = ttk.Notebook(window)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab3 = ttk.Frame(tab_parent)


tab_parent.add(tab1, text="Driver Details")
tab_parent.add(tab2, text="Duty Schedule")
tab_parent.add(tab3, text="vacation")

tab_parent.grid(row=0,column=0)

l1=Label(tab1,text="ID No:")
l1.grid(row=0,column=0)

l2=Label(tab1,text="Name")
l2.grid(row=0,column=2)

l3=Label(tab1,text="Vehicle")
l3.grid(row=1,column=0)

l4=Label(tab1,text="Plate:")
l4.grid(row=1,column=2)

l5=Label(tab1,text="Work Location:")
l5.grid(row=2,column=0)

l6=Label(tab1,text="Upload Photo")
l6.grid(row=2,column=2)

b1=Button(tab1,text="view All", width=12,command=view_command)
b1.grid(row=4,column=0)

b2=Button(tab1,text="Search", width=12,command=search_command)
b2.grid(row=4,column=1)

b3=Button(tab1,text="Add", width=12,command=add_command)
b3.grid(row=4,column=2)

b4=Button(tab1,text="Update", width=12,command=update_command)
b4.grid(row=4,column=3)

b5=Button(tab1,text="Delete", width=12,command=delete_command)
b5.grid(row=4,column=4)

b6=Button(tab1,text="Close", width=12,command=window.destroy)
b6.grid(row=4,column=5)

ID_text=StringVar()
e1=Entry(tab1,textvariable=ID_text)
e1.grid(row=0,column=1)

name_text=StringVar()
e2=Entry(tab1,textvariable=name_text)
e2.grid(row=0,column=3)

vehicle_text=StringVar()
e3=Entry(tab1,textvariable=vehicle_text)
e3.grid(row=1,column=1)

plate_text=StringVar()
e4=Entry(tab1,textvariable=plate_text)
e4.grid(row=1,column=3)

location_text=StringVar()
e5=Entry(tab1,textvariable=location_text)
e5.grid(row=2,column=1)

""" Treeview """
tree= ttk.Treeview(tab1, column=("ID","Employee ID", "Name", "Vehicle"," Plate No:","Work Location"), show='headings')
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
    panel = Label(tab1, image=img)
    panel.image = img
    panel.grid(row=0,column=4,rowspan=3,columnspan=2)

def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((55, 65), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(tab1, image=img)
    panel.image = img
    panel.grid(row=0,column=4,rowspan=3,columnspan=2)


def getImagePath(filename):
    global filena
    filena = filename.split('/')[-1]
    new_path = save_dir+filena
    return new_path


btn = Button(tab1, text='open image', command=open_img).grid(row=2,column=3)


""" tab2 - duty Schedule """
""""

def match_string():
    hits = []
    got = auto.get()
    for item in new_list:
        if item.startswith(got):
            hits.append(item)
    return hits

def get_typed(event):
    if len(event.keysym) == 1:
        hits = match_string()
        show_hit(hits)

def show_hit(lst):
    if len(lst) == 1:
        auto.set(lst[0])
        detect_pressed.filled = True

def detect_pressed(event):
    key = event.keysym
    if len(key) == 1 and detect_pressed.filled is True:
        pos = autofill.index(INSERT)
        autofill.delete(pos, END)

detect_pressed.filled = False
"""

def get_driver_id(event):
    temp_name = duty_combo.get()
    print(temp_name)
    driver_id =driver_backend.getDriverId(temp_name)
    print(driver_id)

duty_l1=Label(tab2,text="Select Name:")
duty_l1.grid(row=0,column=0)

duty_name_text=StringVar()

duty_combo=ttk.Combobox(tab2,width=30, height=20,textvariable=duty_name_text)
duty_combo.grid(row=0,column=3)
duty_combo['values'] = namelist
duty_combo.focus_set()
duty_combo.bind("<<ComboboxSelected>>", get_driver_id)
"""
auto = StringVar()

autofill = Entry(tab2,textvariable=auto)
autofill.grid(row=0,column=3)
autofill.focus_set()
autofill.bind('<KeyRelease>', get_typed)
autofill.bind('<Key>', detect_pressed)
"""

# label
duty_l2=Label(tab2, text = "Select the Month :",
          font = ("Times New Roman", 10)).grid(column = 4,
          row = 0, padx = 10, pady = 25)

# Combobox creation
duty_month_text = StringVar()
monthchoosen = ttk.Combobox(tab2, width = 10, textvariable = duty_month_text)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column = 5, row = 0)
monthchoosen.current()

# label
duty_l3=Label(tab2, text = "Select Time :",
          font = ("Times New Roman", 10)).grid(column = 6,
          row = 0, padx = 10, pady = 25)
# Combobox creation
duty_time_text = StringVar()
timechoosen = ttk.Combobox(tab2, width = 10, textvariable = duty_time_text)

# Adding combobox drop down list
timechoosen['values'] = (' 7 AM - 4 PM',
                          ' 8 AM - 5 PM',
                          ' 10 AM - 7 PM',
                          ' 3 PM - 12 AM',
                          ' 10 PM - 7 AM')

timechoosen.grid(column = 7, row = 0)
timechoosen.current()

# label
duty_l4=Label(tab2, text = "Select OFF Day :",
          font = ("Times New Roman", 10)).grid(column = 8,
          row = 0, padx = 10, pady = 25)
# Combobox creation
offday_text = StringVar()
offchoosen = ttk.Combobox(tab2, width = 10, textvariable = offday_text)

# Adding combobox drop down list
offchoosen['values'] = (' Sunday',
                          ' Monday',
                          ' Tuesday',
                          ' Wednesday',
                          ' Thursday',
                          ' Friday')

offchoosen.grid(column = 9, row = 0)
offchoosen.current()

window.mainloop()
