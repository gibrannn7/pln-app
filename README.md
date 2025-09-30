# PLN Application

A comprehensive web application for managing operational, reporting, and monitoring modules built with Flask, MySQL, and Tailwind CSS.

## Features

- Role-based access control (Admin, Coordinator, Field Officer)
- Dashboard with data visualization
- Master data management
- Reporting and monitoring modules
- Talangan (advance fund) management
- Customer information lookup
- HO Anomaly module
- Export functionality (Excel/PDF)
- Captcha verification at login
- Dark mode support
- Visual alerts for outdated data rows

## Tech Stack

- Backend: Flask + Flask-Login + SQLAlchemy ORM
- Database: MySQL
- Frontend: Jinja2 templates + Tailwind CSS
- Charts: Chart.js
- Export: openpyxl for Excel
- PDF: weasyprint

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL Server
- Git (optional, for cloning)

### Installation

1. Clone the repository (or extract the files):
   ```
   git clone <repository-url>
   cd pln_app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   - Import the schema.sql file into your MySQL server using phpMyAdmin or command line:
     ```
     mysql -u username -p database_name < schema.sql
     ```
   - If the database doesn't exist, create it first:
     ```
     CREATE DATABASE pln_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```

6. Update the database configuration in `app/__init__.py` if needed:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/pln_db'
   ```

7. Run the application:
   ```
   set FLASK_APP=run.py
   set FLASK_ENV=development
   flask run
   ```
   Or on Windows PowerShell:
   ```
   $env:FLASK_APP = "run.py"
   $env:FLASK_ENV = "development"
   flask run
   ```

### Default Credentials

After importing the schema, you'll need to set passwords for the default users. The schema.sql file contains example password hashes.

To set up passwords for the default users:

1. Start the Python shell in your virtual environment:
   ```
   python
   ```

2. Generate password hashes:
   ```python
   from werkzeug.security import generate_password_hash
   print(generate_password_hash("admin123"))  # Replace with your desired password
   print(generate_password_hash("coordinator123"))  # Replace with your desired password
   print(generate_password_hash("officer123"))  # Replace with your desired password
   ```

3. Update the users table in your database with the new password hashes, or create a simple script to update them:
   ```sql
   UPDATE users SET password_hash = 'your_new_hash_here' WHERE username = 'admin';
   UPDATE users SET password_hash = 'your_new_hash_here' WHERE username = 'coordinator1';
   UPDATE users SET password_hash = 'your_new_hash_here' WHERE username = 'officer1';
   ```

Default usernames:
- Admin: `admin`
- Coordinator: `coordinator1` 
- Field Officer: `officer1`

### Sample Data

The schema.sql file includes sample data for demonstration purposes.

## Directory Structure

```
pln_app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── utils.py             # Utility functions
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   ├── main.py          # Main routes
│   │   ├── dashboard.py     # Dashboard routes
│   │   ├── master_data.py   # Master data routes
│   │   ├── reports.py       # Reports routes
│   │   ├── talangan.py      # Talangan routes
│   │   ├── information.py   # Information routes
│   │   └── anomaly.py       # Anomaly routes
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── auth/
│       ├── dashboard/
│       ├── master_data/
│       ├── reports/
│       ├── talangan/
│       ├── information/
│       ├── anomaly/
│       └── errors/
├── app/static/
│   ├── css/
│   │   └── main.css        # Custom CSS
│   ├── js/
│   └── uploads/            # File uploads
├── schema.sql              # Database schema
├── requirements.txt        # Python dependencies
└── run.py                  # Application entry point
```

## Running in Production

For production deployments, make sure to:

1. Change the SECRET_KEY in `app/__init__.py`
2. Update database credentials
3. Configure a production-ready WSGI server like Gunicorn
4. Set up a reverse proxy like Nginx
5. Configure proper logging

## License

This project is created for educational purposes.