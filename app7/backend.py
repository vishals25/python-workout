from numpy import place
import requests

API_KEY="##36ac73438315dd4555ef425f4eb31671##"
def get_data(place,days,view):
    url=f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response=requests.get(url)
    content=response.json()
    filtered_data = content['list']
    filtered_data=filtered_data[:8*days]

    dates=[item['dt_txt'] for item in filtered_data]

    if view=="Temperature":
         filtered_data=[item["main"]["temp"] for item in filtered_data]
    elif view=="Sky":
        filtered_data=[item["weather"][0]["main"] for item in filtered_data]

    return (filtered_data,dates)