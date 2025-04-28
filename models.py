from db import mysql
from datetime import datetime
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
    
    # Check if the book already exists in the database
    cur.execute("SELECT * FROM books WHERE book_id = %s", (book[0],))
    existing_book = cur.fetchone()

    if existing_book:
        cur.close()
        return "Book with this ID already exists."
    
    # If not, insert the new book
    cur.execute("""INSERT INTO books (book_id, title, author, year, price, status) VALUES (%s, %s, %s, %s, %s, %s)""", book)
    mysql.connection.commit()
    cur.close()
    return "Book added successfully!"


def update_book_info(book_id, data):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE books 
        SET title=%s, author=%s, year=%s, price=%s, status=%s
        WHERE book_id=%s
    """, (data[0], data[1], data[2], data[3], data[4], book_id))
    mysql.connection.commit() 
    cur.close()


def delete_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    mysql.connection.commit()
    cur.close()


# Borrowers
def get_borrowers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM borrowers")
    borrowers = cur.fetchall()
    cur.close()
    return borrowers

def add_borrower(borrower):
    cur = mysql.connection.cursor()

    # Check if book exists
    cur.execute("SELECT * FROM books WHERE book_id = %s", (borrower['book_id'],))
    book = cur.fetchone()

    if not book:
        cur.close()
        return "Book ID does not exist."

    # Check if book is available
    if book['status'] != 'available':
        cur.close()
        return "Book is not available."

    # Add borrower
    cur.execute("""
        INSERT INTO borrowers 
        (member_id, member_type, first_name, last_name, address, mobile_number, book_id, book_status, borrow_date, due_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (borrower['member_id'], borrower['member_type'], borrower['first_name'], borrower['last_name'], borrower['address'], borrower['mobile_number'], borrower['book_id'], borrower['book_status'], borrower['borrow_date'], borrower['due_date']))

    # Update book status to unavailable
    cur.execute("UPDATE books SET status = 'unavailable' WHERE book_id = %s", (borrower['book_id'],))

    mysql.connection.commit()
    cur.close()
    return "Success"

def update_borrower(member_id, data):
    cur = mysql.connection.cursor()

    # Update borrower info
    cur.execute("""
        UPDATE borrowers
        SET member_type=%s, first_name=%s, last_name=%s, address=%s, mobile_number=%s, book_id=%s, book_status=%s, borrow_date=%s, due_date=%s, return_date=%s
        WHERE member_id=%s
    """, (data['member_type'], data['first_name'], data['last_name'], data['address'], data['mobile_number'], data['book_id'], data['book_status'], data['borrow_date'], data['due_date'], data['return_date'], member_id))

    # Calculate late return and fine if returning
    if data['book_status'] == 'return':
        sql = """
            UPDATE borrowers
            SET 
                late_return_days = GREATEST(DATEDIFF(return_date, due_date), 0),
                late_return_fine = GREATEST(DATEDIFF(return_date, due_date), 0) * 0.5
            WHERE member_id = %s
        """
        cur.execute(sql, (member_id,))
        # Make book available again
        cur.execute("UPDATE books SET status = 'available' WHERE book_id = %s", (data['book_id'],))

    mysql.connection.commit()
    cur.close()

def delete_borrower(member_id):
    cur = mysql.connection.cursor()
    
    # First, find the book_id associated with this borrower
    cur.execute("SELECT book_id FROM borrowers WHERE member_id = %s", (member_id,))
    result = cur.fetchone()

    if result:
        book_id = result['book_id']  # or result[0] if fetchone() returns a tuple
        
        # Delete the borrower
        cur.execute("DELETE FROM borrowers WHERE member_id = %s", (member_id,))
        
        # Make the book available again
        cur.execute("UPDATE books SET status = 'available' WHERE book_id = %s", (book_id,))
        
        mysql.connection.commit()
    
    cur.close()
