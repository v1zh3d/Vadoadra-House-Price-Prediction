import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={'h_type': 0,
                             'location': 15,
                             'size': 2,
                             'bathroom': 3,
                             'balcony': 1,
                             'total_sqft': 1550})

print(r.json())
