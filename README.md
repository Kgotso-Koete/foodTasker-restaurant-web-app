# About the project

Foodtasker is an UberEats clone in which customers can order takeaway food on through the customer mobile app, restaurants can accept and track orders

---

### Click here for the [demo](https://arcane-spire-07518.herokuapp.com/restaurant/)

---

### Screen shot of the application

![](/screenshots/FoodtaskerWeb_screenshot_1.png)
![](/screenshots/FoodtaskerWeb_screenshot_2.png)

---

### Technology stack

Python Django, SQLite 3, Bootstrap 3 and Stripe for payments

---

### Application overview and link to related code bases

The combined application consists of 4 components:

1. Back-end (part of this code base): A back end that handles CRUD operations with an api specified in the `api_spec folder`.
2. Restaurant Front-end (part of this code base): A web-based administrative front-end for restaurant employees to manage orders
3. Customer Front-end [separate repository](https://github.com/Kgotso-Koete/foodTasker-customer-driver-mobile-app): An android mobile app for customers to use to place and pay for orders
4. Driver Front-end [separate repository](https://github.com/Kgotso-Koete/foodTasker-customer-driver-mobile-app): An android mobile app for drivers to use to accept and deliver orders

---

### What this code base covers

This code is for the back end which includes databases and APIs, and web based administration site for restaurant employees.

---

### Tutorial used

[Code4Startup](https://code4startup.com/) tutorial on building an UberEats clone based on the [foodTasker app tutorial](https://coderealprojects.com/projects/create-ubereats-api-server-side-with-python).

---

### Description and features

### General functionality

- Authenticate users using JWT
- CRU\* users (sign up & settings page - no deleting required)
- CRUD on Restaurants and Meals

### The general page breakdown is as follows:

### User pages

- Sign in page (URL: `api_baseURL/restaurant/sign-in`)
- Sign up page (URL: `api_baseURL/restaurant/sign-up`)
- Settings page (URL: `api_baseURL/restaurant/account`)

### Restaurant pages

- Home page (URL: `api_baseURL/restaurant/order/`)
  - List of orders and their status
  - Restaurants can change the status of orders from 'Cooking' to 'Ready'
- Meals page to view/create/edit meals (URL: `api_baseURL/restaurant/meal/`)
  - View the menu of meals
  - Add meals to the menu (URL: `api_baseURL/restaurant/meal/add`)
  - Edit meals after clicking on a meal name (URL: `api_baseURL/restaurant/meal/edit/`)
- Report page where restaurants can view revenue and other statistics (URL: `api_baseURL/restaurant/report/`)
- Customers page where restaurants can view customers by order volume (URL: `api_baseURL/restaurant/customers/`)
- Drivers page where restaurants can view drivers by order volume (URL: `api_baseURL/restaurant/drivers/`)

---

### How to run the code

The back end API is deployed on Heroku, and the front end is deployed on ??. Here is the [demo](https://arcane-spire-07518.herokuapp.com/restaurant/), and here is the production api link `https://arcane-spire-07518.herokuapp.com/` that can be used with any front end for requests

### 1: Create virtual environment

1. Create a top level (1) folder called foodTasker
2. Create a second level (2) folder called foodtasker and download this repository code into this folder
3. To set up a virtual environment, run `python3 -m venv myvirtualenv/foodtasker-virtualenv`
4. Install dependencies by moving (cd) into the foodtasker folder and running `pip install -r requirements.txt`

### 2: Run Django virtual environment

Navigate(cd) to the top level (1) foodTasker folder and run `source foodtasker-virtualenv/bin/activate`

### 3: Run Django server

Run `python manage.py runserver`

### 4: View application

Open up `http://localhost:8000/` in your browser

---

### Application Structure

- `foodtasker/` where key settings are specified
  - `settings/` where all the key settings have been specified
  - `urls/` handles application routing
- `foodtaskerapp/` for the main application
  - `migrations/` for all the database migrations
  - `models.py` for all the database table/collection models
  - `views.py` for key views and related data
  - `templates/` for html templates and static assets such as Bootstrap 3 files and custom css
  - `runtime.txt` specify which version of python to use in runtime
  - `requirements.txt` specify all packages/dependencies to be downloaded before running the application
- `db.sqlite3` database

---

### Authentication

Requests are authenticated using the `Authorization` header with a valid JWT. Authentication is handled by djangoauth and django-rest-framework-social-oauth2

---

### Payments

Stripe payment API was used (using test keys and test tokens)

---

### Timesheet log

- Back end

  - Version 1 (Code4Startup Tutorial): 31 hours
  - Version 2 (personal modifications): 5 hours

---

### Acknowledgements

Special thanks to Leo Trieu's [Code4Startup](https://code4startup.com/projects) for a great tutorial. I had been looking for a tutorial for a real world 2 sided market application with geo-location features and I found one with thanks to Code4Startup. We need more of this kind of tutorial and less of 'Foo Bar'.

---

### License

The codebase is MIT licensed unless otherwise specified.

---

To be modified further by Kgotso Koete
<br/>
Johannesburg, South Africa
