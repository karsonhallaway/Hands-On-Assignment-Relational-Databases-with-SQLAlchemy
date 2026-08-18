# HOA: Relational Databases with SQLAlchemy

## Objective

Practice creating and managing a relational database using Python and SQLAlchemy. You will define tables, set up relationships, and perform basic CRUD operations.

## Instructions

- [x] Use Python and SQLAlchemy to complete this assignment.
- [x] Make sure you have SQLAlchemy installed (`pip install SQLAlchemy`).
- [x] Use SQLite for simplicity (`sqlite:///example.db`).
- [ ] Submit your Python script (`.py`) with all the steps completed.

## Part 1: Setup

Import necessary modules from SQLAlchemy:

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
```

Create an engine and base:

```python
engine = create_engine('sqlite:///shop.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
```

## Part 2: Define Tables

Create a `User` table with:
- [x] `id` (primary key)
- [x] `name` (string)
- [x] `email` (string, unique)

Create a `Product` table with:
- [x] `id` (primary key)
- [x] `name` (string)
- [x] `price` (integer)

Create an `Order` table with:
- [x] `id` (primary key)
- [x] `user_id` (foreign key referencing `User.id`)
- [x] `product_id` (foreign key referencing `Product.id`)
- [x] `quantity` (integer)

Set up relationships:
- [x] A `User` can have many `Order`s
- [x] A `Product` can appear in many `Order`s

Hint: Use `relationship()` in the tables to define these connections.

## Part 3: Create Tables

Use `Base.metadata.create_all(engine)` to create the tables in the SQLite database.

## Part 4: Insert Data

- [x] Add at least 2 users, 3 products, and 4 orders with different quantities.
- [x] Use `session.add()` and `session.commit()` to save data.

## Part 5: Queries

Write Python code to:

- [x] Retrieve all users and print their information.
- [x] Retrieve all products and print their name and price.
- [x] Retrieve all orders, showing the user's name, product name, and quantity.
- [x] Update a product's price.
- [x] Delete a user by ID.

## Part 6: Bonus (Optional)

- [x] Add a `status` column to the `Order` table (Boolean to represent shipped or not).
- [x] Query all orders that are not shipped.
- [x] Count the total number of orders per user.
