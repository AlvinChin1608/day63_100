import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

# NOT NULL means it must have a value and cannot be left empty. max 250 characters
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# comment the create table comment or you will get an error that table already exist
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K Rowling', '9.3' )")
db.commit()
# in order to view it, we need to download a specialised software
#  https://sqlitebrowser.org/dl/