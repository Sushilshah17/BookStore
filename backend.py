import sqlite3

class Database():

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT,year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        if(isbn!=""):
            self.cur.execute("SELECT * FROM book WHERE isbn=?",(isbn,))
            rows=self.cur.fetchall()
        else:
            self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=?", (title,author,year))
            rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

    def delete_table(self):
        self.cur.execute("DROP TABLE book")

    def __del__(self):
        self.conn.close()

#connect()
#insert("Dreams Come True", "Bhumi Shah", 2021, 3774577887)
#print(view())
#print(search(author="Bhumi Shah"))
#print("After Updating")
#update(3, "Blooming Day", "Bhumi Shah")
#print(view())
