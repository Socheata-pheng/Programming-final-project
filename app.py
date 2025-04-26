from flask import Flask, render_template, request, redirect, url_for, session, flash
from db import init_db
from models import *


app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database Init
init_db(app)

# Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = check_admin(username, password)
        if admin:
            session['loggedin'] = True
            return redirect('/dashboard')
        else:
            flash('Incorrect username or password')
    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('loggedin'):
        return redirect('/')
    return render_template('dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Book Management

@app.route('/books', methods=['GET', 'POST'])
def books():
    if not session.get('loggedin'):
        return redirect('/')
    if request.method == 'POST':
        action = request.form.get('action')
        book_id = request.form.get('book_id')
        if action == 'add':
            data = (
                request.form['book_id'],
                request.form['title'],
                request.form['author'],
                request.form['year'],
                request.form['price'],
                request.form['status']
            )
            add_book(data)
        elif action == 'update':
            book_id = request.form['book_id']
            data = (
                request.form['title'],
                request.form['author'],
                request.form['year'],
                request.form['price'],
                request.form['status']
            )
            update_book_info(book_id, data)
        elif action == 'delete':
            # book_id = request.form['book_id']
            # print(f"Deleting book with ID {book_id}") 
            delete_book(book_id)  

    books = get_books()
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)

