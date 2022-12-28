import requests

API_KEY = "145d826b13a5a9b9df94bf4fec7dc474"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("This app is for checking the weather")

city = input("Enter name of city: ")
request_url = (f"{BASE_URL}?appid={API_KEY}&q={city}")
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    print(weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(temperature)
else:
    print("An error occured")
