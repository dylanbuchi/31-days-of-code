import requests
import os

from twilio.rest import Client
# loads .env secret variables
from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

# city location longitude and latitude
LON = -43.9378
LAT = -19.9208

# weather API url
URL = f"https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}"


def send_message_with_twilio(weather_msg):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    sender_number = os.environ['SENDER_PHONE_NUMBER']
    receiver_number = os.environ['RECEIVER_PHONE_NUMBER']

    client = Client(account_sid, auth_token)
    message = client.messages.create(body=f'{weather_msg}',
                                     from_=sender_number,
                                     to=receiver_number)


def get_12_hours_weather_ids_data():
    """get only the 12 hours of weather data of the day"""

    response = requests.get(URL)
    weather_data = response.json()
    weather_data_12_hours = weather_data["hourly"][:12]
    weather_ids = [i['weather'][0]['id'] for i in weather_data_12_hours]
    return weather_ids


def get_weather_string_message_from(id_num, weather_status):

    if id_num == 801:
        weather_status['is_clear'] = True
        return "Today will be a clear day! ☀︎"

    elif 800 <= id_num <= 804:
        weather_status['is_cloudy'] = True
        return "Today will be a cloudy day! ☁️"

    elif 600 <= id_num <= 622:
        weather_status['is_snow'] = True
        return "It's going to snow today! ❄️"

    elif 500 <= id_num <= 531:
        weather_status['is_rain'] = True
        return "It's going to rain today! ☔"

    elif 300 <= id_num <= 321:
        weather_status['is_drizzle'] = True
        return 'Today will be a drizzle day! 💧'

    elif 200 <= id_num <= 232:
        weather_status['is_thunderstorm'] = True
        return 'Today we will have a thunderstorm! ⛈'


def main():
    weather_status = {
        'is_clear': False,
        'is_cloudy': False,
        'is_snow': False,
        'is_rain': False,
        'is_drizzle': False,
        'is_thunderstorm': False
    }

    weather_string_msg = None

    for weather_id in get_12_hours_weather_ids_data():
        weather_string_msg = get_weather_string_message_from(
            weather_id, weather_status)
        if True in weather_status.values():
            break

    send_message_with_twilio(weather_string_msg)


if __name__ == "__main__":
    main()
