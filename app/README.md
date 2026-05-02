# Flask Learning Pack (Beginner Friendly)

This workspace is designed for day-one beginners. Start with tiny, focused examples, then move to a complete mini project.

## Start Here (First 30 Minutes)

1) Open `examples/01_basics` and follow its README.
2) Move to `examples/02_routes` to learn URL patterns and HTTP methods.
3) Try `examples/03_api` to see JSON APIs.

## What Is Inside

- `examples/`: small examples for one topic at a time.
- `mini_project/`: a full Flask app using blueprints, PostgreSQL, session auth, JWT, RBAC, and a separate frontend.

## General Setup (All Examples)

1) Create a virtual environment.
2) Install the dependencies shown in the example README.
3) Run the app with `flask --app app.py run`.

## PostgreSQL

You only need PostgreSQL for the database examples and the mini project. Set:

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@localhost:5432/flask_learning
```

## Mini Project

When you are comfortable with the examples, open `mini_project/README.md`.
