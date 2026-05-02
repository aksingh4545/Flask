# Flask Learning Pack (Examples + Mini Project)

This workspace contains:
- `examples/`: small, focused examples for each topic.
- `mini_project/`: a full Flask project using blueprints, PostgreSQL, session auth, JWT, RBAC, and a separate frontend.

## Quick Start

1) Create a virtual environment and install dependencies for the example you want.
2) Set PostgreSQL connection string in `DATABASE_URL`.
3) Run the example with `flask --app app.py run`.

Each example has its own README with setup notes.

## PostgreSQL

Use a local PostgreSQL database and set:

```
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@localhost:5432/flask_learning
```

## Mini Project

See `mini_project/README.md` for a full walkthrough.
