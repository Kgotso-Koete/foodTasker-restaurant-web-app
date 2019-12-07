# foodTasker API Spec

---

### Customer APIs

### Customer gets a list of restaurants

1. URL: `GET /api/customer/restaurants/`
2. Output: Return a list of restaurants to the customer
3. Authentication required: No

Example request body:

```javascript
{
    "restaurants": [
        {
            "id": 3,
            "name": "MacDonalds",
            "phone": "19429832232",
            "address": "Corner Hill Street and Malibongwe",
            "logo": "http://localhost:8000/media/restaurant_logo/macDlogo.png"
        },
        {
            "id": 2,
            "name": "KFC",
            "phone": "1493626291",
            "address": "Braamfishcer, Braamfontein",
            "logo": "http://localhost:8000/media/restaurant_logo/kfcLogo.png"
        },
        {
            "id": 1,
            "name": "Chicken Licken",
            "phone": "123456789",
            "address": "Randburg, Johannesburg",
            "logo": "http://localhost:8000/media/restaurant_logo/chickenLickenLogo_3je6faL.jpeg"
        }
    ]
}
```

<hr>

### Customer gets a restaurant menu

1. URL: `GET /api/customer/meals/?restaurant_id/`
2. Output: Return a menu meals offered by each restaurant
3. Authentication required: No

Example request body:

```javascript
{
    "meals": [
        {
            "id": 2,
            "name": "Big John Burger",
            "short_description": "2 Chicken Bresteaks and lettuce",
            "image": "http://localhost:8000/media/meal_images/PI_JustChickenBurgers_Big-John-Burger_DWtb8ic.png",
            "price": 37
        },
        {
            "id": 1,
            "name": "Hot Wings",
            "short_description": "Fire fire tasty wings",
            "image": "http://localhost:8000/media/meal_images/hotWings.jpeg",
            "price": 36
        }
    ]
}
```

<hr>

### Customer creates order

1. URL: `POST /api/customer/order/add/`
2. Output: Return confirmation that the order was placed
3. Authentication required: Yes

Example variables included in a form:

```javascript
 """
        form params:
            access_token
            restaurant_id
            address
            order_details (json format), example:
                [{"meal_id": 1, "quantity": 2},{"meal_id": 2, "quantity": 3}]
            stripe_token
    """
```

Example request body:

```javascript
 {"status": "success"}
```

<hr>

### Customer gets last order placed

1. URL: `GET /api/customer/order/latest/?access_token={{access_token}}`
2. Output: Return confirmation that the order was placed
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        params:
            access_token
    """
```

Example request body:

```javascript
{
    "order": {
        "id": 6,
        "customer": {
            "id": 1,
            "name": "Optimus Prime",
            "avatar": "https://graph.facebook.com/12139r847372901039dhdg/picture?type=large",
            "phone": "",
            "address": ""
        },
        "restaurant": {
            "id": 1,
            "name": "Chicken Licken",
            "phone": "123456789",
            "address": "Randburg, Johannesburg"
        },
        "driver": null,
        "order_details": [
            {
                "id": 8,
                "meal": {
                    "id": 1,
                    "name": "Hot Wings",
                    "price": 36
                },
                "quantity": 2,
                "sub_total": 72
            },
            {
                "id": 9,
                "meal": {
                    "id": 2,
                    "name": "Big John Burger",
                    "price": 37
                },
                "quantity": 3,
                "sub_total": 111
            }
        ],
        "total": 183,
        "status": "Cooking",
        "address": "125 Fancy Complex, Sunninghill Johanesburg"
    }
}
```

<hr>

---

### Driver APIs

### Driver gets a list of orders that are ready and dont have driver assigned

1. URL: `GET /api/driver/orders/ready/`
2. Output: Return a list of orders ready for driver assignment
3. Authentication required: No

Example request body:

```javascript
{
    "orders": [
        {
            "id": 6,
            "customer": {
                "id": 1,
                "name": "Kylo Ren",
                "avatar": "https://graph.facebook.com/aldsd19837/picture?type=large",
                "phone": "",
                "address": ""
            },
            "restaurant": {
                "id": 1,
                "name": "Chicken Licken",
                "phone": "123456789",
                "address": "Randburg, Johannesburg"
            },
            "driver": null,
            "order_details": [
                {
                    "id": 8,
                    "meal": {
                        "id": 1,
                        "name": "Hot Wings",
                        "price": 36
                    },
                    "quantity": 2,
                    "sub_total": 72
                },
                {
                    "id": 9,
                    "meal": {
                        "id": 2,
                        "name": "Big John Burger",
                        "price": 37
                    },
                    "quantity": 3,
                    "sub_total": 111
                }
            ],
            "total": 183,
            "status": "Ready",
            "address": "125 Fancy Complex, Sunninghill Johanesburg"
        }
    ]
}
```

<hr>
