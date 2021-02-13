# Note! For the code to work you need to replace all the placeholders with
# Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "18ae73b69e99c1fc53d8f9aa0fbee985"
account_sid = "ACefc13f0984cd61257fa4af773950a8d9"
auth_token = "fd0320deda8e1c96a2ef4791fe9f1502"

weather_params = {
    "lat": "-22.906847",
    "lon": "-43.172897",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19495233795",
        to="+15203310035"
    )
    print(message.status)
