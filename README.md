# ToDo App - Django Task Manager

A full-featured task management web application built with Django and PostgreSQL, featuring user authentication, task CRUD operations, and a modern Bootstrap UI.

## ✨ Features

- **User Authentication**
  - User registration with email
  - Secure login/logout functionality
  - Password validation and security

- **Task Management**
  - Create, read, update, and delete tasks
  - Mark tasks as completed
  - Task priority levels (Low, Medium, High)
  - Due date tracking
  - Task descriptions
  - User-specific task isolation

- **Modern UI**
  - Responsive Bootstrap 5 design
  - Clean and intuitive interface
  - Mobile-friendly layout
  - Success/error message notifications

## 🛠️ Technologies Used

- **Backend:** Django 6.0.2
- **Database:** PostgreSQL
- **Frontend:** Bootstrap 5, HTML5, CSS3
- **Python:** 3.12+

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- PostgreSQL
- pip (Python package manager)
- virtualenv (recommended)

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv

# On Linux/Mac
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database

**Create database and user:**
```bash
sudo -u postgres psql
```

**Inside PostgreSQL prompt:**
```sql
CREATE USER mydatabaseuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydatabase OWNER mydatabaseuser;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO mydatabaseuser;
\q
```

### 5. Update Database Settings
Edit `todo/settings.py` and update the database credentials if needed:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files
```bash
python manage.py collectstatic
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## 📱 Usage

1. **Register:** Create a new account at `/register/`
2. **Login:** Sign in at `/login/`
3. **Home:** View all your tasks at `/home/`
4. **Add Task:** Click "Add New Task" to create a task
5. **Complete Task:** Mark tasks as done with the "Complete" button
6. **Delete Task:** Remove tasks with the "Delete" button
7. **Logout:** Sign out from the navigation menu

## 📂 Project Structure

```
ToDo/
├── task/                    # Main task app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── index.html
│   │   ├── add_task.html
│   │   ├── login.html
│   │   └── register.html
│   ├── models.py           # Task model
│   ├── views.py            # View functions
│   ├── forms.py            # Form definitions
│   ├── urls.py             # URL routing
│   └── admin.py            # Admin configuration
├── todo/                    # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL config
│   └── wsgi.py
├── templates/               # Shared templates
│   └── base.html           # Base template
├── static/                  # Static files
│   └── css/
│       └── style.css
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## 🔒 Security Notes

- Never commit your `SECRET_KEY` to version control
- Use environment variables for sensitive data in production
- Keep `DEBUG = False` in production
- Use HTTPS in production
- Regularly update dependencies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Your Name**
- GitHub: [Shahriar-Hasan123](https://github.com/Shahriar-Hasan123)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Team
- PostgreSQL Community

---
**Happy Task Managing! 📝✨**
