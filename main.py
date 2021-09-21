from flask import Flask, render_template
import requests


# IF CSS WONT UPDATE IN CHROME BROWSER HOLD SHIFT AND CLICK RELOAD TO DELETE CACHE


# INIT
app = Flask(__name__, template_folder = 'template')

# TODO: PREVESTI OPISE VREMENA NA SRPSKI

@app.route('/')

def idnex():
    API_KEY = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=4160714ccefddd8b61c83a198f86a47b'
    city_name = 'Banjaluka'

    #! PRINT JSON OF THAT CITY DATA IN CONSOLE
    r = requests.get(API_KEY.format(city_name)).json()
    print(r, '\n')

    #! PUT NEEDED DATA IN PYTHON DICTIONARY
    weather_dict = {
        'city': city_name,
        'temperature': round(r['main']['temp'] - 273.15),
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    if weather_dict['description'] == 'light rain':
        weather_dict['description'] = 'umjereno kisovito'
    
    def obuci_se():  
        if weather_dict['temperature'] < 18:
            return 'Obucite se toplije.'
        else:
            return 'Obucite se komotnije, vrijeme je toplije.'

    print(weather_dict)

    #return weather_dict
    return render_template('index.html', content = weather_dict, odjeca = obuci_se())

if __name__ == '__main__':
    #! WHEN PRODUCTION, debug = False
    app.run(debug = True)  