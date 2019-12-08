# foodTasker API Spec

### Customer APIs

### Customer gets a list of restaurants

1. URL: `GET /api/customer/restaurants/`
2. Output: Return a list of restaurants to the customer
3. Authentication required: No

Example result body:

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

Example result body:

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
        request form params:
            access_token
            restaurant_id
            address
            order_details (json format), example:
                [{"meal_id": 1, "quantity": 2},{"meal_id": 2, "quantity": 3}]
            stripe_token
    """
```

Example result body:

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
        URL params:
            access_token
    """
```

Example result body:

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

### Get driver location

1. URL: `GET /api/customer/driver/location/?access_token={{access_token}}`
2. Output: Return Driver's location
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        URL params:
            access_token
 """
```

Example result body:

```javascript
{
    "location": "412121,542141"
}
```

<hr>

### Driver APIs

### Driver gets a list of orders that are ready and don't have driver assigned

1. URL: `GET /api/driver/orders/ready/`
2. Output: Return a list of orders ready for driver assignment
3. Authentication required: No

Example result body:

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

### Driver chooses order to deliver

1. URL: `POST /api/driver/orders/ready/`
2. Output: Return confirmation that the order was picked
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        request form params:
            access_token
            order_id
 """
```

Example result body:

```javascript
{
    "status": "success"
}

```

<hr>

### Driver gets last order

1. URL: `GET /api/driver/order/latest/?access_token={{access_token}}`
2. Output: Return confirmation that the order was picked
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        URL params:
            access_token
            order_id
 """
```

Example result body:

```javascript
{
    "order": {
        "id": 4,
        "customer": {
            "id": 1,
            "name": "Halley Berry",
            "avatar": "https://graph.facebook.com/alksh29037/picture?type=large",
            "phone": "",
            "address": ""
        },
        "restaurant": {
            "id": 1,
            "name": "Chicken Licken",
            "phone": "123456789",
            "address": "Randburg, Johannesburg"
        },
        "driver": {
            "id": 1,
            "name": "Ghost Rider",
            "avatar": "https://graph.facebook.com/adjdh286/picture?type=large",
            "phone": "",
            "address": ""
        },
        "order_details": [
            {
                "id": 4,
                "meal": {
                    "id": 1,
                    "name": "Hot Wings",
                    "price": 36
                },
                "quantity": 2,
                "sub_total": 72
            },
            {
                "id": 5,
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
        "status": "On the way",
        "address": "Umbrella Crossing Tokyo"
    }
}

```

### Driver marks order as delivered

1. URL: `POST /api/driver/order/complete/`
2. Output: Return confirmation that the order was delivered
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        request form params:
            access_token
            order_id
 """
```

Example result body:

```javascript
{
    "status": "success"
}

```

<hr>

### Get Driver revenue

1. URL: `GET /api/driver/revenue/?access_token={{access_token}}`
2. Output: Return Driver's revenue for the week
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        URL params:
            access_token
 """
```

Example result body:

```javascript
{
    "revenue": {
        "Mon": 0,
        "Tue": 0,
        "Wed": 0,
        "Thu": 0,
        "Fri": 0,
        "Sat": 366,
        "Sun": 0
    }
}

```

<hr>

### Save Driver location database

1. URL: `POST /api/driver/location/update/`
2. Output: Return confirmation that the location was saved in the database
3. Authentication required: Yes

Example variables included in query parameters:

```javascript
 """
        request form params:
            access_token
            location
 """
```

Example result body:

```javascript
{
    "status": "success"
}

```

# External API's

### Stripe payment API

Example variables included in query parameters:

```javascript
 """
        request form params:
            stripe token_token
 """
```

Example result body:

```javascript
{
    "status": "success"
}

```

<hr>
