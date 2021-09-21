from flask import Flask, render_template, jsonify
import requests

# IF CSS WONT UPDATE IN CHROME BROWSER HOLD SHIFT AND CLICK RELOAD TO DELETE CACHE


# INIT
app = Flask(__name__, template_folder = 'template')

@app.route('/')

def idnex():
    API_KEY = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=4160714ccefddd8b61c83a198f86a47b'
    city_name = 'Banjaluka'

    # PRINT JSON OF THAT CITY DATA IN CONSOLE
    r = requests.get(API_KEY.format(city_name)).json()
    print(r, '\n')

    # PUT NEEDED DATA IN PYTHON DICTIONARY
    weather_dict = {
        'city': city_name,
        'temperature': round(r['main']['temp'] - 273.15),
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon']
    }

    # TRANSLATE WEATHER DESCRIPTION TO SERBIAN
    if weather_dict['description'] == 'light rain':
        weather_dict['description'] = 'Umjereno kisovito'
        
    elif weather_dict['description'] == 'clear sky':
        weather_dict['description'] = 'Vedro'
    
    def obuci_se():  
        if weather_dict['temperature'] < 18:
            return 'Obucite se toplije.'
        else:
            return 'Obucite se komotnije, vrijeme je toplije.'

    # FORMAT JSON
    print(weather_dict, "\n")
    
    # LOOP THROUGH WEATHER INFO
    better_info = [weather_dict['city'], weather_dict['temperature'], weather_dict['description']]

    #return weather_dict
    return render_template('index.html', city = better_info[0], temp = better_info[1], description = better_info[2], odjeca = obuci_se())

if __name__ == '__main__':
    # WHEN PRODUCTION, debug = False
    app.run(debug = True)  