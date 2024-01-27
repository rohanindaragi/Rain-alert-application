# importing the libraries
import requests
# this library is used for sending messages
from twilio.rest import Client

# Open weather map endpoint
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api key for fetching the weather data
api_key = "c12aded28448c80f20246c1d146fd4d6"

# this information is used for sending sms
account_sid = "ACa70f70f75c0ad66f32a87332b1d3feb5"
auth_token = "15cd1632cffc6ccfe8f45d1624c22bdc"



weather_params = {
    "lat": -6.175110,
    "lon": 106.865036,
    "appid": api_key,
}

# passing the endpoint using get method
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "It's going to rain today.Remember to bring an umbrella",
        from_= "+12255628422",
        to= "+918494903736"
    )
    print(message.status)