# Flask Microblog App 🚀

This is my web application built using **Python** and the **Flask framework**.

---

## 📌 Project Overview

This project is a simple microblog application built using **Flask**.
It demonstrates how to create dynamic web pages, handle user input, and build structured backend logic using Python.

---

## ⚙️ Features

### ✅ Chapter 1

* Flask project setup
* Virtual environment usage
* Basic routing
* "Hello, World!" web app

---

### ✅ Chapter 2

* HTML Templates (Jinja2)
* Dynamic data rendering
* Loops for displaying posts
* Template variables
* Separation of logic and UI

---

### ✅ Chapter 3

* Implemented web forms using Flask-WTF
* Created login form (username, password, remember me)
* Added CSRF protection using SECRET_KEY
* Handled GET and POST requests
* Implemented form validation using WTForms
* Displayed validation error messages
* Used flash messages for user feedback
* Implemented redirection after form submission
* Used url_for() for dynamic routing (best practice)

---

### ✅ Chapter 4

* Integrated database using Flask-SQLAlchemy
* Configured SQLite database (app.db)
* Created User and Post models
* Implemented relationships between models
* Used Flask-Migrate for database migrations
* Generated and applied migrations
* Performed basic database operations using Flask shell

---

## 📂 Project Structure

```
microblog/
│── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│── migrations/
│── config.py
│── microblog.py
│── .gitignore
│── venv/
│── app.db
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/Gayathri-0809/flask-microblog.git
cd flask-microblog
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install flask flask-wtf flask-sqlalchemy flask-migrate
```

### 5. Set environment variable

```
set FLASK_APP=microblog.py
```

### 6. Setup database (first time only)

```
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 7. Run the application

```
flask run
```

---

## 🌐 Output

Open browser:

```
http://localhost:5000/
```

### 🔥 Features in UI:

* Displays user greeting
* Shows dynamic posts
* Login form with validation
* Error messages for invalid input
* Flash messages after login

---

## 🎯 Learning Outcome

* Learned Flask basics
* Understood Jinja templating
* Built dynamic web pages
* Implemented form handling in Flask
* Learned CSRF protection
* Implemented validation and user input handling
* Integrated database with Flask
* Managed project using Git & GitHub

---

💡 This project is part of my journey to become a skilled developer in Python, web development, and cybersecurity.
