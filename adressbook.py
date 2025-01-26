from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.ttk import *
import os
import json

window = Tk()
window.title('Adress book')
window.geometry('500x500')
# OR
#window.minsize(500, 500)


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
    clear_all()
    index = book_list.curselection()
    if index:
        nameentry.insert(0, book_list.get(index))
        details = myAddressBook[nameentry.get()]
        adressentry.insert(0, details[0])
        phoneentry.insert(0, details[1])
        emailentry.insert(0, details[2])
        birthdayentry.insert(0, details[3])
    else:
        messagebox.showinfo('error','You need to select a name')

def delete():
    index = book_list.curselection()
    if index:
        del myAddressBook[book_list.get(index)]# delete from dict.
        book_list.delete(index) # to delete from list box
        clear_all() # to delete the textboxes
    else:
        messagebox.showinfo('error', 'You need to select a entry')

def display(event):
    newWindow = Toplevel(window)
    index = book_list.curselection()
    content = ' '
    if index:
        key = book_list.get(index)
        contact = 'NAME : '+key+'\n\n'
        details = myAddressBook[key]
        contact += 'ADRESS : '+details[0]+'\n'
        contact += 'PHONE NUMBER : '+details[1]+'\n'
        contact += 'EMAIL : '+details[2]+'\n'
        contact += 'BIRTHDAY : '+details[3]+'\n'

    # Levels for new window
    
    lbl = Label(newWindow)
    lbl.grid(row = 0, grid = 0)
    lbl.configure(text = contact)

def reset():
    clear_all()
    book_list.delete(0, END)
    myAddressBook.clear()
    bookName.configure(text = 'My adress book')

def save():
    fout=asksaveasfile(defaultextension='.txt')
    if fout:
        print(myAddressBook, file = fout)
        reset()
    else:
        messagebox.showinfo('warning', 'Address book not found')

def open_file():
    global myAddressBook
    reset()
    fin=askopenfile(title='Open file')
    if fin:
        eval()
        with open(fin.name, 'r') as file:
            myAddressBook = json.load(file)
        for key in myAddressBook.keys():
            book_list.insert(END,key)
        bookName.configure(text = os.path.basename(fin.name))
    else:
        messagebox.showinfo('Error', 'No adress book open')


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

add_update_btn = Button(window, text = 'Add/Update', command = update)
add_update_btn.grid(row = 7, column = 3)

delete_btn = Button(window, text = 'Delete', command = delete)
delete_btn.grid(row = 7, column = 2)

edit_btn = Button(window, text = 'Edit', command = edit)
edit_btn.grid(row = 7, column = 1)

open_btn = Button(window, text = 'Open', command = open)
open_btn.grid(row = 8, column = 3)

save_btn = Button(window, text = 'Save', command = save)
save_btn.grid(row = 8, column = 2)



window.mainloop()
