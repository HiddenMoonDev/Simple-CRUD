# This is simple CRUD app on Flask and SQLite database

## Installation
First of all u need to download this to make this app work:

```bash
pip install flask
pip install flask-SQLAlchemy
pip install SQLAlchemy
```

# To create SQLite database use this command in main.py:
```python
with app.app_context():
  db.create_all()
```
Delete Database if u wanna use clean database
