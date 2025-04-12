print("-"* 40)
print("Weather Application")
print("-"* 40)
import requests


api_key = "3a1f35193ccc559dd956aee9c4020367"
base_url ="https://api.openweathermap.org/data/2.5/weather"

city = input("Enter Your city name :")

url = f"{base_url}?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200 :
    data = response.json()
    print(f"\n Weather report for {city}: \n")
    print(f"Temperature:{data['main']['temp']} Centigrade")
    print(f"Weather : {data['weather'][0]['main']} - {data['weather'][0]['description']}")
    print(f"Humidity : {data['main']['humidity']}%")
    print(f"Wind Speed :{data['wind']['speed']}m/s")
else:
    print("City not found or invalid API key")
print("\n Thank you! for using the weather app")
print("\n Stay Updated . Stay Safe . Good Bye ;)")