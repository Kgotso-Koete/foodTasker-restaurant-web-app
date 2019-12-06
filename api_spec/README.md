# foodTasker API Spec

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
