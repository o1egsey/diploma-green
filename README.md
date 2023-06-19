# Ecommerce Store

This is a Django-based ecommerce store project that utilizes SQLite as its database. It provides a platform for managing products, orders, and customer information.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/o1egsey/diploma-green
```

2. **Create a virtual environment:**
```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**

On macOS and Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

4. **Install the project dependencies:**
```bash
pip install -r requirements.txt
```

5. **Apply database migrations:**
```bash
python manage.py migrate
```
6. **Load database data:**
```bash
python manage.py loaddata data.json
```

7. **Create a superuser (admin) account:**
```bash
python manage.py createsuperuser
```
8. **Start the development server:**
```bash
python manage.py runserver
```
**Access the application:**

Open a web browser and go to http://localhost:8000 to access the ecommerce store.

**Configuration**

The project's settings can be found in the settings.py file. You may need to configure certain settings such as database connections, static files, and email settings depending on your deployment environment.
