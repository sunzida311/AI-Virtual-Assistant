import requests
from keys import *

api_address="https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid="+weather_key
json_data = requests.get(api_address).json()

def temp():
    tempo= round(json_data['main']['temp']-273,1)
    desc=json_data['weather'][0]['description']
    s=str(tempo)+" degree celcius "+desc
    return s
