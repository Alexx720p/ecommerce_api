# ecommerce_api

https://roadmap.sh/projects/ecommerce-api


A RESTful e-commerce backend built with Django and Django REST Framework following a monolithic architecture  
The API provides user authentication, product catalog browsing, shopping cart management and product administration features.

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
- Search products by keywords

### Cart
- Add products to cart
- Update cart quantities
- Remove products from cart
- View current cart contents
- Checkout

### Admin
- Create products
- Update products
- Delete products
- Create categories
- Manage catalog data

## Architecture
This project follows a monolithic architecture where all functionality is contained within a single Django application and all modules share the same database, business logic and application layer.

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
```git clone https://github.com/Alexx720p/ecommerce_api```

Navigate to the project directory:  
```cd ecommerce_api```

Create a virtual environment and activate it:  
```python -m venv venv_name```

Install dependencies:  
```pip install -r requirements.txt```

Apply migrations:  
```python manage.py migrate```

Run the server:  
```python manage.py runserver```

### Environment variables
Create a .env file in the project root with your Stripe API key:  
`STRIPE_SECRET_KEY='your_actual_Stripe_key'`  

# API Documentation
## Authentication
Logout and account deletion requires authentication:  
> Bearer `<access_token>`   
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
- 200 OK
- 401 Unauthorized

### Logout  
> HTTP `POST /logout/`  

Request:  
> JSON `{"refresh": "refresh_jwt"}`   

Response:  
> JSON `{"message": "Logged out successfully"}`  

Status codes:  
- 200 OK
- 400 Bad Request
- 401 Unauthorized

### Refresh
Request:  
> HTTP POST `/refresh/`
> JSON `{"refresh": "refresh_token"}`  

Response:  
> JSON `{"access": "access_jwt", "refresh": "refresh_jwt"}`

Status codes:
- 200 OK
- 401 Unauthorized

### Delete account
Request:  
> HTTP DELETE `/delete/`

Response:  
> JSON `{"detail":"User deleted successfully"}`  

Status codes:  
- 200 OK
- 401 Unauthorized

## Products
### Search Products
> HTTP GET `/products/?search=hat`
### Get all products
> HTTP GET `/products`

Response:  
> JSON `{"count": 1, "next": "null", "previous": "null", "results": [{"id": 1, "title": "hat", "description": "Black hat for men", "price": 3.99, "Category": 1}]}`

You can filter by Category too using the category's id:  
> HTTP GET `/products/?Category=1`  

Status codes:  
- 200 OK
- 400 Bad Request

## Cart
**Authentication required in all views:**  
> Bearer `<access_token>`  
### View cart
Request:    
> HTTP GET `/cart`  

Response:    
> JSON `{"count":0,"next":null,"previous":null,"results":[]}`  

Status codes:  
- 200 OK
- 401 Unauthorized

### Add product to cart
> HTTP POST `/add/product_id/`  

Response:  
> JSON `[{"product":{"id":2,"title":"T shirt women","description":"T shirt for women L size","price":"14.99","Category":2},"quantity":1,"added_at":"2026-11-06T04:29:07.499647Z"}]`  

Status codes:  
- 200 OK
- 401 Unauthorized

### Update cart item
> HTTP PATCH `/rest/product_id/`  

Status codes:  
- 200 OK
- 401 Unauthorized

### Remove product from cart
> HTTP DELETE `/remove/product_id/`  

Response:  
> JSON `{"message":"Product removed from cart","cart":[]}`  

Status codes:  
- 200 OK
- 401 Unauthorized

### Checkout
> POST `/checkout/`  

*No JSON body required in the request*  

Response:  
> JSON `{"checkout_url": "Stripe_checkout_url"}`

After a successfil payment, Stripe redirects the user to the configured success URL.  
If the checkout process is cancelled, Stripe redirects the user to the configured cancel URL.  

Status Codes:  
- 200 OK
- 401 Unauthorized
- 400 Bad Request


## Admin
**Requires authentication and admin permissions:**  
> Authorization bearer `<admin_access_token>`  

### Get all products
> HTTP GET `/admin-products`  

Response:  
> JSON `{"count": 1, "next": "null", "previous": "null", "results": [{"id": 1, "title": "hat", "description": "Black hat for men", "price": 3.99, "Category": 1}]}`  

Status codes:
- 200 OK
- 401 Unauthorized
- 403 Forbidden    

### Create a product
> HTTP POST `/admin-products/`  

Request:  
> JSON: "{"title": "Hoodie", "description": "Hoodie for woman, Large size", "price": 4.99, "inventory": 3, "Category": 2}"   

Response:  
> JSON `{"id":7,"title":"Hoodie","description":"Hoodie for woman, Large size","price":"4.99","inventory":3,"created":"2026-11-06T07:04:08.394951Z","updated":"2026-11-06T07:04:08.394951Z","Category":2}`

Status codes:
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden  

### Update product
> HTTP PATCH `/admin-products/product_id/`   

Request:  
> JSON: `{"price": 5.99}`  

Response:  
> JSON `{"id":7,"title":"Hoodie","description":"Hoodie for woman, Large size","price":"5.99","inventory":3,"created":"2026-11-06T07:04:08.394951Z","updated":"2026-11-06T07:11:01.940312Z","Category":2}`

Status codes:
- 201 OK
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found  

### Delete Product
> HTTP DELETE `/admin-products/product_id/`  

Response:  
  None  

Status codes:  
- 204 No Content
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found

### Get all categories
> HTTP GET `/admin-categories`  

Response:  
> JSON `{"count":3,"next":null,"previous":null,"results":[{"id":1,"name":"Men","slug":"men"},{"id":2,"name":"Women","slug":"women"},{"id":3,"name":"Kids","slug":"kids"}]}`  

Status codes:
- 200 OK
- 401 Unauthorized
- 403 Forbidden

### Create a new Category
> HTTP POST `/admin-categories/`  

Request:  
> JSON `{"name": "Toys", "slug": "toys"}`  

Response:  
> JSON `{"id":5,"name":"Toys","slug":"toys"}`  

Status codes:  
- 201 Created
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
