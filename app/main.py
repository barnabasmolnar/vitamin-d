from flask import Flask
from flask import render_template
import requests
import json
import datetime
import itertools
from forms import MyForm
from timezonefinder import TimezoneFinder
import pendulum
from iso3166 import countries
from credentials import API_KEY, SECRET_KEY

API_KEY = API_KEY
API_URL = "https://api.openweathermap.org/data/2.5/forecast"

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

tf = TimezoneFinder()

def get_data(form):
    payload = {"q": form.city.data, "APPID": API_KEY, "units": "metric" }
    r = requests.get(API_URL, params=payload)
    res = r.json()

    city_data = res["city"]
    weather_list = res["list"]

    data = []

    for item in weather_list:
        if item["weather"][0]["icon"] == "01d":
            city_lat = city_data["coord"]["lat"]
            city_lon = city_data["coord"]["lon"]
            city_tz = tf.timezone_at(lng=city_lon, lat=city_lat)
            
            local_date = pendulum.from_timestamp(item["dt"], tz=city_tz)
            local_day = local_date.format("YYYY-MM-DD")
            local_hours = local_date.format("HH:mm")
            wind = item["wind"]
            wind_speed_kmh = round(wind["speed"] * 3.6, 1)

            my_dict = {
                "date": local_date,
                "day": local_day,
                "hour": local_hours,
                "temp": item["main"]["temp"],
                "wind_speed": wind_speed_kmh,
            }

            data.append(my_dict)

    grouped_data = [list(g) for k, g in itertools.groupby(data, key=lambda d: d["date"].date())]

    city_info = {
        "name": city_data["name"],
        "country": countries.get(city_data["country"]).name
    }

    return render_template('index.html', days=grouped_data, city_data=city_info, form=form)

@app.route("/", methods=("GET", "POST"))
def start():
    form = MyForm()
    if form.validate_on_submit():
        return get_data(form)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)