from logging import error
import constants as keys
import json
import requests

def get_weather():
    apiUrl = "http://api.openweathermap.org/data/2.5/weather"
    request = requests.post(url = apiUrl, params ={'q':'Montevideo', 'APPID': keys.OPENWEATHERMAP_API_KEY, 'units':'metric'})
    if request.status_code == 200:
        response = json.loads(request.content)
        temp = float(response['main']['temp'])
        temp = round(temp)
        return 'La temperatura en Montevideo es de ' + str(temp)+'°'
    else: 
        return 'No se pudo obtener la temperatura, intente nuevamente más tarde'

def get_forecast():
    apiUrl = "http://api.openweathermap.org/data/2.5/forecast"
    request = requests.post(url = apiUrl, params ={'q':'Montevideo', 'APPID': keys.OPENWEATHERMAP_API_KEY, 'units':'metric'})
    if request.status_code == 200:
        response = json.loads(request.content)
        msg = ["Pronóstico del tiempo: \n"]
        for item in response['list']:
            date_response = str(item['dt_txt'])
            date = get_date(date_response)
            hour = get_hour(date_response)
            if(hour == "09hs" or hour == "15hs" or hour == "21hs"): 
                msg.append("*"+date+"*")
                for data_item in item['weather']:
                    weather = data_item['main']
                    description = data_item['description']
                    ic = icon(data_item['icon'])
                    msg.append(f"{ic}  {weather}  ({description})")
                if hour == "09hs" : msg.append("*"+" Mañana\n"+"*")
                if hour == "15hs" : msg.append("*"+" Tarde\n"+"*")
                if hour == "21hs" : msg.append("*"+" Noche\n\n"+"*")
        message = ''.join(msg)   
        return message
    else: 
        return 'No se pudo obtener el pronóstico, intente nuevamente más tarde'

def get_date(string):
    date = string.split() #[0]fecha, [1]hora
    date = date[0].split('-') #fecha
    date = ''.join(date[2]+'/'+date[1]) #fecha dd/mm
    return date

def get_hour(string):
    hour = string.split() #[0]fecha, [1]hora
    hour = hour[1].split(":") #hora
    hour = hour[0]+"hs" #hora 00hs
    return hour

def icon(string):
    s = str(string)
    if s == "01d": return "🌤"
    if s == "01n": return "🌤"
    if s == "02d": return "⛅"
    if s == "02n": return "⛅"
    if s == "03d": return "🌥"
    if s == "03n": return "🌥"
    if s == "04d": return "☁"
    if s == "04n": return "☁"
    if s == "09d": return "🌦"
    if s == "09n": return "🌦"
    if s == "10d": return "🌧"
    if s == "10n": return "🌧"
    if s == "11d": return "⛈"
    if s == "11n": return "⛈"
    if s == "13d": return "🌨"
    if s == "13n": return "🌨"
    if s == "50d": return "🌫"
    if s == "50n": return "🌫"