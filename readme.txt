# E-Commerce Portal API

A simple REST API for an e-commerce backend built with FastAPI, SQLAlchemy, and MySQL.
Supports managing products, customers, and orders, including stock tracking.

## Features

- Product management (create, read, update, delete, filter by category)
- Customer management (create, read, delete)
- Order management (create, read, update status, delete)
- Automatic stock deduction when an order is placed
- Insufficient-stock validation on order creation

## Tech Stack

- FastAPI - web framework
- SQLAlchemy - ORM
- MySQL (via PyMySQL) - database
- Pydantic - request/response validation

## Project Structure

- main.py       - FastAPI app and route definitions
- models.py     - SQLAlchemy ORM models (Product, Customer, Order)
- schemas.py    - Pydantic schemas for request/response validation
- crud.py       - Database access functions (create/read/update/delete)
- database.py   - Database engine and session configuration

## Setup

1. Install dependencies:
   pip install fastapi uvicorn sqlalchemy pymysql pydantic

2. Create a MySQL database:
   CREATE DATABASE ecommerce_db;

3. Update the database connection string in database.py:
   DATABASE_URL = "mysql+pymysql://<user>:<password>@localhost:3306/ecommerce_db"

4. Run the app:
   uvicorn main:app --reload

5. The API will be available at:
   http://localhost:8000

   Interactive docs (Swagger UI):
   http://localhost:8000/docs

## API Endpoints

### Products
- POST   /products                      Create a product
- GET    /products                      List all products
- GET    /products/{product_id}         Get a product by ID
- PUT    /products/{product_id}         Update a product
- DELETE /products/{product_id}         Delete a product
- GET    /category/{category_name}      List products by category

### Customers
- POST   /customers                     Create a customer
- GET    /customers                     List all customers
- GET    /customers/{customer_id}       Get a customer by ID
- DELETE /customers/{customer_id}       Delete a customer

### Orders
- POST   /orders                        Create an order (validates stock)
- GET    /orders                        List all orders
- GET    /orders/{order_id}             Get an order by ID
- GET    /customers/{customer_id}/orders  List orders for a customer
- PUT    /orders/{order_id}/status      Update order status
- DELETE /orders/{order_id}             Delete an order

## Notes

- Order status values: pending, shipped, delivered, cancelled
- Placing an order automatically reduces the corresponding product's stock
- Orders on products with insufficient stock return a 400 error