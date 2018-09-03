Boilerplate flask app w/ user auth and sqlite

1) enter venv and `pip install requirements.txt`
2) add database URL to `.flaskenv`
3) init db with `flask db init`
4) adjust models.py, create migrations, etc with `flask db migrate -m "migration message"`
5) migrate with `flask db upgrade`
