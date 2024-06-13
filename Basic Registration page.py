#Importing tkinter Library
import tkinter
from tkinter import *

#Creating main Window
reg_pg = tkinter.Tk()

#Setting geometry
reg_pg.geometry("500x500")

#Giving Title name
reg_pg.title("Registration Page")

#Heading Widget
head = Label(reg_pg, text="Registration Page", font=("bold", 30), fg="red", bg="black")
head.place(x=90, y=53)

#Nmae Widget
name1 = Label(reg_pg, text="Name : ", font=("bold"), fg="orange", bg="yellow")
name1.place(x=80, y=130)

data1 = StringVar()

name2 = Entry(reg_pg, textvariable=data1, background="pink", foreground="black")
name2.place(x=150, y=130)

#Email Widget
email1 = Label(reg_pg, text="Email Id : ", font=("bold"), fg="orange", bg="yellow")
email1.place(x=68, y=180)

data2 = StringVar()

email2 = Entry(reg_pg, textvariable=data2, background="pink", foreground="black")
email2.place(x=150, y=180)

#Gender widget
gender1 = Label(reg_pg, text="Gender : ", font=("bold"), fg="orange", bg="yellow")
gender1.place(x=70, y=220)

var = IntVar()

gender2 = Radiobutton(reg_pg, text="Male", variable=var, activebackground="black", activeforeground="blue", value=1)
gender2.place(x=150, y=220)

gender3 = Radiobutton(reg_pg, text="Female", variable=var, activebackground="black", activeforeground="blue", value=2)
gender3.place(x=210, y=220)

#Menu Widget
menu = Menu(reg_pg)

file = Menu(menu, tearoff=0)
file.add_command(label="Open")
file.add_command(label="New")
file.add_command(label="Save")
file.add_command(label="Save as...")

file.add_separator()

file.add_command(label="Exit", command=reg_pg.quit)
menu.add_cascade(label="File", menu=file)

edit = Menu(reg_pg, tearoff=0)
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")
menu.add_cascade(label="Edit", menu=edit)

help = Menu(reg_pg, tearoff=0)
help.add_command(label="About")

help.add_separator()

help.add_command(label="Help")
menu.add_cascade(label="Help", menu=help)

reg_pg.config(menu=menu)

#Submit Button Widget
def submit():
    main = Tk()
    main.geometry("500x500")
    new = Label(main)
    new.config(text="Thak you for submitting", font=("bold", 25), fg="black", bg="pink")
    new.place(x=80, y=130)

Submit = Button(reg_pg, text="Submit", command=submit, fg="blue")
Submit.place(x=150, y=260)

#Running Main Window
reg_pg.mainloop()