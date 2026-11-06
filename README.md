# ecommerce_api

https://roadmap.sh/projects/ecommerce-api


A RESTful e-commerce backend built with Django and Django REST Framework following a monolithic architecture  
The API provides user authentication, product catalog browsing, shopping cart management adn administrative product management functionality.

## Features
### Authentication
- User registration
- User login
- User logout
- Account deletion
- JWT-based authentication

### Products
- Browse product catalog
- Retrieve individual product details
- Filter products by category
- Search products by key words

### Cart
- Add products to cart
- Update cart quantities
- Remove products from cart
- View current cart contents

### Admin
- Create products
- Update products
- Delete products
- Create categories
- Manage catalog data

## Architecture
This project follows a monolithic architecture where all functionality is contained within a single Django application and all modules share the same database, application and business logic.

### Modules
- Auth
- Products
- Cart
- Admin

## Tech stack
- Python
- Django
- Django REST Framework
- SQLite3
- JWT Authentication
- Stripe (Payments)

## Installation
Clone the repository:  
> bash: git clone https://github.com/Alexx720p/ecommerce_api

Navigate to the project directory:  
>bash: cd ecommerce_api

Create a virtual environment and activate it:  
> bash: python -m venv venv_name

Install dependencies:  
> bash: pip install -r requirements.txt

Apply migrations:  
> bash: python manage.py migrate

Run the server:  
> bash: python manage.py runserver

### Environmente variables
Create a .env file in the project root with your Stripe API key:  
`SECRET_KEY = 'your_actual_Stripe_key'`  

# API Documentation
## Authentication
### Register User  
> HTTP `POST register/`
  
Request:  
> JSON `{"username": "John", "email": "johndoe@email.com", "password": "securepassword"}`    

Response:  
> JSON `{"username": "john"}`  

Status codes:  
- 201 Created
- 400 Bad Request

### Login   
> HTTP `POST /login/`
Request:
> JSON `{"username": "john", "password": "securepassword"}`

Response:  
> JSON `{"refresh": "refresh_jwt", "access": "access_jwt"}`

Status codes:  
- 200 Ok
- 401 Unauthorized

### Logout  
> HTTP `POST /logout/`  

Authorization required  
Request:  
> Bearer `<token>`  
> JSON `{"refresh": "refresh_jwt"}`  

Response:  
> JSON `{"message": "Logged out successfully"}`  

Status codes:  
- 200 Ok
- 400 Bad Request
- 401 Unauthorized

## Products
### Search one product
> HTTP `/products/?search=hat`
### Get all products
> HTTP `GET /products`

Response:  
> JSON `{"count": 1, "next": "null", "previous": "null", "results": [{"id": 1, "title": "hat", "description": "Black hat for men", "price": 3.99, "Category": 1}]}`

You can filter by Category too using the category's id:  
> HTTP `/products/?Category=1`  

Status codes:  
- 200 ok
- 400 Bad Request

## Cart
### View cart
Authentication required    
Request:    
> HTTP GET `/cart`  
> Bearer `<token>`

Response:    
> JSON `{"count":0,"next":null,"previous":null,"results":[]}`  

Status codes:  
- 200 Ok
- 401 Unauthorized

### Add product to cart
> HTTP POST `/add/product_id/`
Authentication required:
> Bearer `<access_token>`

Response:  
> JSON `[{"product":{"id":2,"title":"T shirt women","description":"T shirt for women L size","price":"14.99","Category":2},"quantity":1,"added_at":"2026-11-06T04:29:07.499647Z"}]`

Status codes:  
- 200 Ok
- 402 Unauthorized

### Update cart item
> HTTP PATCH `/rest/product_id/`  

Status codes:  
- 200 Ok
- 401 Unauthorized

### Remove product from cart
Authentication required  
> HTTP DELETE `/remove/product_id/`
> Bearer `<access_token>`

Response:  
> JSON `{"message":"Product removed from cart","cart":[]}`

Status codes:  
- 200 Ok
- 401 Unauthorized



