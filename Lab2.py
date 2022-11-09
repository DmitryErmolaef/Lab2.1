import requests

city = "Nekrasovka,RU"
appid = "e173e2835b248384d08be500b4e16f26"
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print(f'Прогноз погоды на день:\nГород: {city}\nПогодные условия:{data["weather"][0]["description"]}\nТемпература:{data["main"]["temp"]} \nМинимальная температура: {data["main"]["temp_min"]}\nМаксимальная температура: {data["main"]["temp_max"]}')