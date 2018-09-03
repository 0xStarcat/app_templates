Very rudimentary Flask app template

- with sqlite, SQLAlechemy & migrations

1) run `flask db init`
2) Adjust the models to your preference and run migrations with `flask db migrate -m "<migration name>"`
  - comes with a related user and post example
3) Comes with a few view templates
4) Also comes with `flask shell` configured and a `.flaskenv` file. be sure to add it to `.gitignore`
