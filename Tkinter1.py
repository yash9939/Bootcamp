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
test_button1.grid(column=0, row=2)

test_button2 = Button(windows, text="Reset", activeforeground="blue", activebackground="black", fg="green", bg="orange")
test_button2.grid(column=1, row=2)

#Entry Widget
test_entry = Entry(windows, background="pink", foreground="white")
test_entry.grid(column=1, row=0)

test_entry2 = Entry(windows, background="pink", foreground="white")
test_entry2.grid(column=1, row=1)

#CheckButton Widget
test_chkbtn1 = Checkbutton(windows, text="Done", onvalue=1, offvalue=0, activeforeground="blue", activebackground="black", cursor="arrow")
test_chkbtn1.grid(column=1, row=3)

test_chkbtn2 = Checkbutton(windows, text="Not done", onvalue=1, offvalue=0, activeforeground="blue", activebackground="black", cursor="arrow")
test_chkbtn2.grid(column=2, row=3)

#Radio Widget
#Radio Variables
rad_var = IntVar()

test_rdbtn1 = Radiobutton(windows, text="Done", activeforeground="blue", activebackground="black", variable=rad_var, value=0)
test_rdbtn1.grid(column=1, row=4)

test_rdbtn2 = Radiobutton(windows, text="Not done", activeforeground="blue", activebackground="black", variable=rad_var, value=1)
test_rdbtn2.grid(column=2, row=4)

#Running main window
windows.mainloop()