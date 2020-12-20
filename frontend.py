'''
A program to build a bookstore that stores the information of books:
Title, Author
Year, ISBN

User can:

View all records
Search a record
Add an Entry
UPDATE an Entry
DELETE an Entry
Close the application
'''

from tkinter import *
from backend import Database

database=Database("books.db")

class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("BookStore")

        label_title = Label(window, text="Title")
        label_title.grid(row=0, column=0)

        label_author = Label(window, text="Author")
        label_author.grid(row=0, column=2)

        label_year = Label(window, text="Year")
        label_year.grid(row=1, column=0)

        label_isbn = Label(window, text="ISBN")
        label_isbn.grid(row=1, column=2)

        self.entry_title_value = StringVar()
        self.entry_title = Entry(window, textvariable=self.entry_title_value)
        self.entry_title.grid(row=0, column=1)

        self.entry_author_value = StringVar()
        self.entry_author = Entry(window, textvariable=self.entry_author_value)
        self.entry_author.grid(row=0, column=3)

        self.entry_year_value = StringVar()
        self.entry_year = Entry(window, textvariable=self.entry_year_value)
        self.entry_year.grid(row=1, column=1)

        self.entry_isbn_value = StringVar()
        self.entry_isbn = Entry(window, textvariable=self.entry_isbn_value)
        self.entry_isbn.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=30)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        b_viewall = Button(window, text="View All", width=12, command=self.view_command)
        b_viewall.grid(row=2, column=3)

        b_search = Button(window, text="Search Entry", width=12, command=self.search_command)
        b_search.grid(row=3, column=3)

        b_addentry = Button(window, text="Add Entry", width=12, command=self.addentry_command)
        b_addentry.grid(row=4, column=3)

        b_update = Button(window, text="Update", width=12, command=self.update_command)
        b_update.grid(row=5, column=3)

        b_delete = Button(window, text="Delete", width=12, command=self.delete_command)
        b_delete.grid(row=6, column=3)

        b_close = Button(window, text="Close", width=12, command=window.destroy)
        b_close.grid(row=7, column=3)



    def get_selected_row(self,event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.entry_title.delete(0,END)
            self.entry_title.insert(END,self.selected_tuple[1])
            self.entry_author.delete(0,END)
            self.entry_author.insert(END,self.selected_tuple[2])
            self.entry_year.delete(0,END)
            self.entry_year.insert(END,self.selected_tuple[3])
            self.entry_isbn.delete(0,END)
            self.entry_isbn.insert(END,self.selected_tuple[4])
        except IndexError:
            pass



    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.entry_title_value.get(), self.entry_author_value.get(), self.entry_year_value.get(), self.entry_isbn_value.get()):
            self.list1.insert(END,row)

    def addentry_command(self):
        if(self.entry_title_value.get()!="" and self.entry_author_value.get() != "" and self.entry_year_value.get()!="" and self.entry_isbn_value.get()!=""):
            database.insert(self.entry_title_value.get(), self.entry_author_value.get(), self.entry_year_value.get(), self.entry_isbn_value.get())
            self.list1.delete(0,END)
            self.list1.insert(END,(self.entry_title_value.get(), self.entry_author_value.get(), self.entry_year_value.get(), self.entry_isbn_value.get()))
            self.view_command()
        else:
            self.list1.delete(0,END)
            self.list1.insert(END, ("To make an entry, Please enter all four entries"))


    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        database.update(self.selected_tuple[0],self.entry_title_value.get(), self.entry_author_value.get(), self.entry_year_value.get(), self.entry_isbn_value.get())
        self.view_command()


window=Tk()
Window(window)
window.mainloop()
