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

### ✅ Chapter 5

* Implemented secure user authentication system
* Password hashing using Werkzeug
* Added login functionality with validation
* Integrated Flask-Login for session management
* Implemented logout functionality
* Protected routes using @login_required
* Added user session persistence ("remember me")
* Displayed dynamic navigation (Login / Logout)
* Handled invalid login attempts with flash messages

---

## 📂 Project Structure

```
microblog/
│── app/
│   ├── __init__.py        # App factory & Flask-Login setup
│   ├── routes.py          # Routes (login, logout, protected pages)
│   ├── forms.py           # WTForms (Login form)
│   ├── models.py          # User model with password hashing
│   ├── templates/
│       ├── base.html      # Layout + navigation (Login/Logout)
│       ├── index.html
│       ├── login.html
│── migrations/
│── instance/
│   ├── app.db             # SQLite database
│── config.py
│── run.py
│── .gitignore
│── venv/
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
pip install flask flask-wtf flask-sqlalchemy flask-migrate flask-login email-validator
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
* User login and logout functionality
* Protected pages (requires login)
* Persistent login session

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
* Implemented secure user authentication system
* Learned password hashing and verification
* Integrated Flask-Login for session handling
* Built protected routes with authentication

---

💡 This project is part of my journey in technologies.
