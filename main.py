from flask import Flask
import requests

# INIT
app = Flask(__name__)

@app.route('/')

def idnex():
    API_KEY = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=4160714ccefddd8b61c83a198f86a47b'
    city_name = 'Moscow'
    
    # PRINT JSON OF THAT CITY DATA IN CONSOLE
    r = requests.get(API_KEY.format(city_name)).json()
    print(r)
    return '<h1>Ovo je weather app</h1>'

if __name__ == '__main__':
    # WHEN PRODUCTION, debug = False
    app.run(debug = True)  