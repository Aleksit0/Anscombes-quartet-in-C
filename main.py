from flask import Flask
from flask.wrappers import Request
from flask_restful import Resource, Api

# INIT
app = Flask(__name__)
api = Api(app)

@app.route('/city')

def search_city():
    API_KEY = 'd141b18866b7ea2b9bfe61b870e4e6e9'
    city_name = requests.args.get('q') # CITY NAME AS ARGUMENT
    
    # CONVERT RESPONSE TO PY DICTIONARY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={API_KEY}'
    response = requests.get(url).json()
    
    if response.get('cod') != 200:
        return f'Error getting data for {city_name.title()}. Invalid city name.'

    
    
def index():
    return '<h1>Ovo je weather app</h1>'

if __name__ == '__main__':
    # WHEN PRODUCTION, debug = False
    app.run(debug = True)  