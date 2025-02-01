# EvalEasy MS Auth

MS Auth is a Django-based microservice for handling authentication and user management. It provides APIs for creating institutions and representatives, along with user authentication functionalities.

## Features
- User authentication and management
- Institution creation and management
- Institution Representative creation and management

## Endpoints
- `POST /api/create/institution/` - Create a new institution
- `POST /api/create/representative/` - Create a new representative
- `POST /api/login/` - Login and obtain JWT token

## Requirements
- Python 3.8+
- Django 5.1.5
- PostgreSQL

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/1javid/evaleasy-ms-auth.git
    ```
2. Navigate to the project directory:
    ```sh
    cd evaleasy-ms-auth/ms_auth
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```sh
    python manage.py migrate
    ```
5. Seed the database with initial data:
    ```sh
    python manage.py seed_db
    ```

## PostgreSQL Setup
1. Create a new PostgreSQL database:
    ```sql
    CREATE DATABASE ms-auth;
    ```
2. Update your Django settings to use the new database and user:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'ms-auth',
            'USER': 'postgres',
            'PASSWORD': '1234',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

## Usage
1. Run the development server:
    ```sh
    python manage.py runserver
    ```
2. Access the API at `http://127.0.0.1:8000/api/`