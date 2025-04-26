from db import mysql

#Admin Login
def check_admin(username, password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
    admin = cur.fetchone()
    cur.close()
    return admin

#Books
def get_books():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    cur.close()
    return books

def add_book(book):
    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO books (book_id, title, author, year, price, status) VALUES (%s, %s, %s, %s, %s, %s)""", book)
    mysql.connection.commit()
    cur.close()

def update_book_info(book_id, data):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE books 
        SET title=%s, author=%s, year=%s, price=%s, status=%s
        WHERE book_id=%s
    """, (data[0], data[1], data[2], data[3], data[4], book_id))
    mysql.connection.commit() 
    cur.close()

def update_book_status(book_id, status):
    cursor = db.cursor()
    sql = "UPDATE books SET status = %s WHERE book_id = %s"
    cursor.execute(sql, (status, book_id))
    db.commit()


def delete_book(book_id):
    cur = mysql.connect.cursor()
    cur.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    mysql.connection.commit()
    cur.close()

