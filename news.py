import requests
from keys import *

api_address="https://newsapi.org/v2/top-headlines?country=us&apiKey="+news_key
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(2):
        ar.append("number " + str(i+1) + json_data['articles'][i]['title'])

    return ar
