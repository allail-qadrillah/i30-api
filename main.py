from api.api import API
 
from weather.get_weather import Get_Weather

api = API()

print(api.get_input(3).info())
