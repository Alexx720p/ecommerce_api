# ecommerce_api

https://roadmap.sh/projects/ecommerce-api

I used mainly Django Rest Framework and Sqlite3 for this project

If you want to test it you will need to clone this repo and install the requirements bash: pip install -r requirements.txt
Also you may need to start a Stripe account in order to get the api key. After you have created your account, get your stripe api key and set it in a .env file in the same level as the manage.py file <p> STRIPE_SECRET_KEY = 'your actual secret key' </p>


# Commands:
## Products:
- See all products: GET /products
- Search products: GET /products?search=*key word in the title*
- Filter products by category: GET /products/Category=*category_id*

## Admin panel:
Is very similar to the products one but in this one you can modify, delete and add products and categories
- See all products: GET /admin-products
- Add a new product: send a POST request to this url /admin-products/  and a JSON with a title, description, price, inventory and the category id. E.g. <p>{'title': 't-shirt',  'description': 't-shirt size m for men', 'price': 14.99, Category': 3}</p>
- Update a product: PATCH /admin-products/*product_id*/ and a JSON with the attribute you want to modify. Eg: <p>{'title': 'T-shirt men'}</p>
- Delete a product: DELETE  /admin-products/*product_id*/


## Auth:
I used JWT for authentication, the core main functions are register, login, logout and delete the account:
- Register: POST /register/ JSON: <p>{"username": "your_username", "password": "your_password"}</p>
- Login: POST /login/ JSON: <p>{"username": "your_username", "password": "your_password"}</p>
- Logout: POST /logout/ JSON: <p>{"username": "your_username", "password": "your_password", "refresh": "the_refresh_token"}</p>
- Delete your user: DELETE /delete/ (needs authentication)

## Cart (needs authentication):
- See the cart: GET /cart
- Add a product to the cart: POST /add/*productid*/
- Rest from the cart: PATCH /rest/*product_id*/
- Delete all pieces of one product in the cart: DELETE /remove/*product_id*/
- Clear the cart: DELETE /clear/
- Checkout: POST /checkout/
