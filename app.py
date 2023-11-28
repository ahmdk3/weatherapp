import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp', methods=['POST','GET'])
def get_weatherdata():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {
        'q':request.form.get('city'),
        'appid': 'fbdb9cb6d3ee9d62b0e0ab5461c06981',
        'units': 'metric'
    }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"

if __name__=='__main__':
    app.run(host='0.0.0.0')
