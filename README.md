# HOA: Relational Databases with SQLAlchemy

A small SQLAlchemy project modeling a shop's users, products, and orders using a SQLite database, with relationships, CRUD operations, and a couple of aggregate queries.

## Overview

The script ([relational-database.py](relational-database.py)) uses SQLAlchemy's modern ORM (`DeclarativeBase` / `Mapped` / `mapped_column`) to:

- Define `User`, `Product`, and `Order` tables with relationships between them
- Create the tables in a SQLite database (`shop.db`)
- Insert sample data
- Query, update, and delete records
- Run bonus queries: filtering unshipped orders and counting orders per user

See [project.md](project.md) for the original assignment instructions.

## Schema

- **User** — `id`, `name`, `email` (unique); has many `Order`s
- **Product** — `id`, `name`, `price`; appears in many `Order`s
- **Order** — `id`, `user_id` (FK → `users.id`), `product_id` (FK → `products.id`), `quantity`, `status` (Boolean, shipped/not shipped)

## Requirements

- Python 3
- SQLAlchemy

```bash
pip install SQLAlchemy
```

## Setup

A virtual environment is expected at `venv/`. Activate it and install dependencies:

```bash
source venv/bin/activate
pip install SQLAlchemy
```

## Usage

Run the script from the project directory:

```bash
python relational-database.py
```

On first run, `Base.metadata.create_all(engine)` creates `shop.db` and its tables. The data-insertion, update, and delete statements are commented out after initial use to avoid duplicate inserts or errors on re-run — uncomment the relevant block in **Part 4** if you want to reseed or modify data.

Running the script prints:

- All users (name, email)
- All products (name, price)
- All orders (user name, product name, quantity)
- All unshipped orders
- Total order count per user

## Project Structure

```
.
├── relational-database.py   # Main script: models, setup, CRUD, queries
├── project.md                # Assignment instructions/checklist
├── shop.db                   # SQLite database (generated)
└── venv/                     # Virtual environment
```
