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
    # If already logged in, redirect to dashboard
    if session.get('loggedin'):
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = check_admin(username, password)
        if admin:
            session['loggedin'] = True
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username or password', 'danger')
    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
    
# Book Management
@app.route('/books', methods=['GET', 'POST'])
def books():
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    
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
            result = add_book(data)
            if result == "Book with this ID already exists.":
                flash(result, 'warning')
            else:
                flash(result, 'success')
        
        elif action == 'update':
            data = (
                request.form['title'],
                request.form['author'],
                request.form['year'],
                request.form['price'],
                request.form['status']
            )
            update_book_info(book_id, data)
            flash('Book updated successfully!', 'success')
        
        elif action == 'delete':
            delete_book(book_id)
            flash('Book deleted successfully!', 'success')

    books = get_books()
    return render_template('books.html', books=books)

# Borrower Management
@app.route('/borrowers', methods=['GET', 'POST'])
def borrowers():
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        action = request.form.get('action')
        member_id = request.form.get('member_id')
        if action == 'add':
            borrower = {
                'member_id': request.form['member_id'],
                'member_type': request.form['member_type'],
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'address': request.form['address'],
                'mobile_number': request.form['mobile_number'],
                'book_id': request.form['book_id'],
                'book_status': request.form['book_status'],
                'borrow_date': request.form['borrow_date'],
                'due_date': request.form['due_date'],
            }
            result = add_borrower(borrower)
            if result == 'Success':
                flash('Borrower added successfully!', 'success')
            else:
                flash(result, 'warning')
        elif action == 'update':
            data = {
                'member_type': request.form['member_type'],
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'address': request.form['address'],
                'mobile_number': request.form['mobile_number'],
                'book_id': request.form['book_id'],
                'book_status': request.form['book_status'],
                'borrow_date': request.form['borrow_date'],
                'due_date': request.form['due_date'],
                'return_date': request.form.get('return_date') or None
            }
            update_borrower(member_id, data)
            flash('Updated successfully!', 'success')
        elif action == 'delete':
            delete_borrower(member_id)
            flash('Deleted successfully!', 'success')

    borrowers = get_borrowers()
    return render_template('borrowers.html', borrowers=borrowers)

if __name__ == '__main__':
    app.run(debug=True)
