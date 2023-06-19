# Ecommerce Store

This is a Django-based ecommerce store project that utilizes SQLite as its database. It provides a platform for managing products, orders, and customer information.

## Installation

1. **Clone the repository:**

```bash
git clone [<repository-url>](https://github.com/o1egsey/diploma-green)

2. **Navigate to the project directory:**

```bash

cd ecommerce-store

3. **Create a virtual environment:**
```bash

python3 -m venv venv
Activate the virtual environment:
On macOS and Linux:

bash

source venv/bin/activate
On Windows:

bash

venv\Scripts\activate
Install the project dependencies:
bash

pip install -r requirements.txt
Apply database migrations:
bash

python manage.py migrate
Create a superuser (admin) account:
bash

python manage.py createsuperuser
Start the development server:
bash

python manage.py runserver
Access the application:
Open a web browser and go to http://localhost:8000 to access the ecommerce store.

Configuration
The project's settings can be found in the settings.py file. You may need to configure certain settings such as database connections, static files, and email settings depending on your deployment environment.
