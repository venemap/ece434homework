#!/usr/bin/env python3
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('57e1695e7aa1b72e3dd06f353b7dbecf')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('fahrenheit')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

reg = owm.city_id_registry()
list_of_tuples = reg.ids_for("Terre Haute")
currWeather = mgr.weather_at_place('Terre Haute')
print(list_of_tuples)
print(currWeather.weather.detailed_status)
print(currWeather.weather.temperature('fahrenheit'))

