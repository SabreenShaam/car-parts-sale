# Technologies Used
* Python 3.10 or 3.9
* PostgreSQL Relational database
* Django Framework
* Django Database ORM

### Development is done based on following user stories from the backlog

* As a company, I want all my products in a database, so I can offer them via our new platform to customers
* As a client, I want to add a product to my shopping cart, so I can order it at a later stage
* As a client, I want to remove a product from my shopping cart, so I can tailor the order to what I actually need
* As a client, I want to order the current contents in my shopping cart, so I can receive the products I need to repair my car
* As a client, I want to select a delivery date and time, so I will be there to receive the order
* As a client, I want to see an overview of all the products, so I can choose which product I want
* As a client, I want to view the details of a product, so I can see if the product satisfies my needs


**Want to run the project in Docker?**

- ```docker-compose up```
* login to the container with following command
- ```docker exec -it car-parts-sale_web_1 /bin/sh```
* ```car-parts-sale_web_1``` is the container name
* create a superuser by running following commands to add and manage the products
- ```python manage.py createsuperuser```
- Navigate to ```http://127.0.0.1/8000``` or ```http://localhost:8000/```

**Request to Add a Product**

http://127.0.0.1:8000/product

method:POST

`{
    "product_code": "Product001",
    "product_name": "Park Light",
    "unit_price": 1000,
    "stock": 10,
    "description": "car park light",
    "type": "Lights",
    "company": "Suzuki"
}`

**Request to Add a Product into Cart**

http://127.0.0.1:8000/cart

method:POST

`{
    "product_code": "Product001",
    "quantity": 3
}`

**Request to Place an Order**

http://127.0.0.1:8000/order

method:POST

`{
    "customer" : "abc",
    "email" : "abc@gmail.com",
    "phone" : "0212121221",
    "address" : "Colombo",
    "delivery_date" : "2022-07-29",
    "delivery_time" : "10:30:00.000000",
    "items" :[
        {
            "id": 2,
            "product_code": "Product002",
            "unit_price": 5000,
            "quantity": 5,
            "total_cost": 25000,
            "user": 2
        },
        {
            "id": 3,
            "product_code": "Product001",
            "unit_price": 1000,
            "quantity": 2,
            "total_cost": 2000,
            "user": 2
        }
    ]
}`