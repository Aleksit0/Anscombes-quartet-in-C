from flask import Flask
import requests

# INIT
app = Flask(__name__)

@app.route('/city')

def search_city():
    API_KEY = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid4160714ccefddd8b61c83a198f86a47b'
    city_name = requests.args.get('q') # CITY NAME AS ARGUMENT
    
    # CONVERT RESPONSE TO PY DICTIONARY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}'
    response = requests.get(url).json()
    
    if response.get('cod') != 200:
        return f'Error getting data for {city_name.title()}. Invalid city name.'
        
    # CONVERT TO CELSIUS
    temp = response.get('main', {}).get('temp')
    if temp:
        temp_to_celsius = round(temp - 273.15, 2)    
        return f'The current temp of {city_name.title()} is {temp_to_celsius} &#8451'
    else:
        return f'Error getting data for {city_name.title()}, check your city name.'
    
    
def index():
    return '<h1>Ovo je weather app</h1>'

if __name__ == '__main__':
    # WHEN PRODUCTION, debug = False
    app.run(debug = True)  