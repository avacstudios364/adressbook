from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.ttk import *
import os

window = Tk()
window.title('Adress book')
window.geometry('500x500')


myAddressBook = {}

# Functions

def clear_all():
    nameentry.delete(0,END)
    adressentry.delete(0,END)
    emailentry.delete(0,END)
    phoneentry.delete(0,END)
    birthdayentry.delete(0,END)

def update():
    key = nameentry.get()
    if key == ' ':
        messagebox.showinfo('ERROR', 'Name cannot be empty')
    else:
        if key not in myAddressBook.key():
            bookName.insert(END, key)
        myAddressBook[key] = adressentry.get(), phoneentry.get(), emailentry.get(), birthdayentry.get()
        clear_all() #clears text boxes

def edit():
    pass

def delete():
    pass

def display(event):
    pass

def reset():
    pass

def save():
    pass

def open_file():
    pass




# design main window

bookName = Label(window, text = 'My Adress Book')
bookName.grid(row = 0, column = 1)

book_list = Listbox(window, height = 20, width = 40)
book_list.grid(row = 2, column = 1)

namelabel = Label(window, text = 'Name:')
namelabel.grid(row = 2, column = 3, padx = 6)

adresslabel = Label(window, text = 'Adress:')
adresslabel.grid(row = 3, column = 3, padx = 6)

emaillabel = Label(window, text = 'Email:')
emaillabel.grid(row = 4, column = 3, padx = 6)

phonelabel = Label(window, text = 'Phone:')
phonelabel.grid(row = 5, column = 3, padx = 6)

birthdaylabel = Label(window, text = 'Birthday')
birthdaylabel.grid(row = 6, column = 3, padx = 6)

nameentry = Entry(window)
nameentry.grid(row = 2, column = 4, padx = 10)

adressentry = Entry(window)
adressentry.grid(row = 3, column = 4, padx = 10)

emailentry = Entry(window)
emailentry.grid(row = 4, column = 4, padx = 10)

phoneentry = Entry(window)
phoneentry.grid(row = 5, column = 4, padx = 10)

birthdayentry = Entry(window)
birthdayentry.grid(row = 6, column = 4, padx = 10)

add_update_btn = Button(window, text = 'Add/Update', command = None)
add_update_btn.grid(row = 7, column = 3)

delete_btn = Button(window, text = 'Delete', command = None)
delete_btn.grid(row = 7, column = 2)

edit_btn = Button(window, text = 'Edit', command = None)
edit_btn.grid(row = 7, column = 1)

open_btn = Button(window, text = 'Open', command = None)
open_btn.grid(row = 8, column = 3)



window.mainloop()
