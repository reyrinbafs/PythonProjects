import requests

parameters = {
    "lat": 28.754914,
    "lag": 77.249282,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
