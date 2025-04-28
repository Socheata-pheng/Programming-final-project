---

📚 Library Management System (Flask App)

A simple and modern Library Management System built with **Flask** and **MySQL**.  
It includes features like **Admin Login**, **Book Management**, **Borrower Management**.

---

## 🚀 Features
- Admin login and logout
- Manage Books (Add / Update / Delete)
- Manage Borrowers (Add / Update / Delete)
- Borrow and return books
- Flash messages for feedback
- MySQL database integration

---

## 🛠️ Tech Stack
- Python (Flask Framework)
- MySQL (Database)
- HTML, Bootstrap (Frontend styling)
- Flask-MySQLdb (Database connection)

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/library-management-flask.git
   cd library-management-flask
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**  
   ```bash
   pip install -r requirements.txt
   ```
   **Example `requirements.txt`** (create one if needed):
   ```
   Flask
   Flask-MySQLdb
   ```

4. **Set up MySQL Database**
   - Create a database (e.g., `library_db`).
   - Create necessary tables (`admins`, `books`, `borrowers`).
   - You can define your `db.py` to connect to your local database like:
     ```python
     def init_db(app):
         app.config['MYSQL_HOST'] = 'localhost'
         app.config['MYSQL_USER'] = 'root'
         app.config['MYSQL_PASSWORD'] = 'yourpassword'
         app.config['MYSQL_DB'] = 'library_db'
         mysql = MySQL(app)
         return mysql
     ```

5. **Run the Flask App**
   ```bash
   python app.py
   ```
   Then open `http://127.0.0.1:5000/` in your browser.

---

## 📋 Usage

- Go to the **login page**.
- Log in with admin credentials (stored in your `admins` table).
- Access:
  - **Dashboard** 
  - **Manage Books** (add, update, delete)
  - **Manage Borrowers** (add, update, delete, return books)
- **Logout** when done.

---




