# foodTasker API Spec

## Get list of restaurants

1. URL: `GET /api/customer/restaurants/`
2. Output: Return a list of restaurants
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
