#Importing Tkinter library
import tkinter
#Importing everything from tkinter
from tkinter import *

#Creating main window
windows = tkinter.Tk()

#Setting the title in Tkinter
windows.title("Test")

#Widgets

#Label Widget
test_label1 = Label(windows, text="First Name : ")
test_label1.grid(column=0, row=0)

test_label2 = Label(windows, text="Last Name : ")
test_label2.grid(column=0, row=1)

#Button Widget
test_button1 = Button(windows, text="Submit", activeforeground="blue", activebackground="black", fg="red", bg="yellow")
test_button1.grid(column=0, row=6)

test_button2 = Button(windows, text="Reset", activeforeground="blue", activebackground="black", fg="green", bg="orange")
test_button2.grid(column=1, row=6)

#Entry Widget
test_entry = Entry(windows, background="pink", foreground="white")
test_entry.grid(column=1, row=0)

test_entry2 = Entry(windows, background="pink", foreground="white")
test_entry2.grid(column=1, row=1)

#CheckButton Widget
test_chkbtn1 = Checkbutton(windows, text="Male", onvalue=1, offvalue=0, activeforeground="blue", activebackground="black", cursor="arrow")
test_chkbtn1.grid(column=0, row=4)

test_chkbtn2 = Checkbutton(windows, text="Female", onvalue=1, offvalue=0, activeforeground="blue", activebackground="black", cursor="arrow")
test_chkbtn2.grid(column=1, row=4)

#Radio Widget
#Radio Variables
rad_var = IntVar()

test_rdbtn1 = Radiobutton(windows, text="Done", activeforeground="blue", activebackground="black", variable=rad_var, value=0)
test_rdbtn1.grid(column=0, row=5)

test_rdbtn2 = Radiobutton(windows, text="Not done", activeforeground="blue", activebackground="black", variable=rad_var, value=1)
test_rdbtn2.grid(column=1, row=5)

#Listbox Widget
#Listbox Label
list_label = Label(windows, text="Country : ", bg="red", fg="yellow")

test_lstbox = Listbox(windows, bg="red", fg="yellow")
test_lstbox.insert(1, "India")
test_lstbox.insert(2, "Pakistan")
test_lstbox.insert(3, "Russian")
test_lstbox.insert(4, "U.S.A")
test_lstbox.insert(5, "Canada")
test_lstbox.insert(6, "Anyother...")
list_label.grid(column=0, row=2)
test_lstbox.grid(column=0, row=3)

#Menu Widget
test_menu = Menu(windows)

file = Menu(test_menu, tearoff=0)
file.add_command(label="Open")
file.add_command(label="New")
file.add_command(label="Save")
file.add_command(label="Save as...")

file.add_separator()

file.add_command(label="Exit", command=windows.quit)
test_menu.add_cascade(label="file", menu=file)

edit = Menu(windows, tearoff=0)
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")
test_menu.add_cascade(label="edit", menu=edit)

help = Menu(windows, tearoff=0)
help.add_command(label="About")

help.add_separator()

help.add_command(label="Help")
test_menu.add_cascade(label="help", menu=help)

windows.config(menu=test_menu)

#Running main window
windows.mainloop()