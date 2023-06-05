import requests

api_key = "ef7bfb3cad53847f9b4f765e99565bb8" # API key OpenWeaterMap
city = "Pamekasan" # Nama kota yang ingin dilihan cuacanya

# URL untuk mengambil data cuaca
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Mengambil data cuaca dari OpenWeatherMap API
resposes = requests.get(url)

if resposes.status_code == 200:
    weater_data = resposes.json()

    # mendapat data suhu
    temperature = weater_data['main']['temp'] - 273.15

    # mendapat deskripsi cuaca
    weather_description = weater_data['weather'][0]['description']

    # mebuat translate deskripsi cuaca ke bahasa indonesia
    translation_dict = {
        'clear sky' : 'Cerah',
        'few clouds' : 'Sedikit Awan',
        'scattered clouds' : 'Berawan',
        'broken clouds' : 'Berawan',
        'shower rain' : 'Hujan Lokal',
        'rain' : 'Hujan',
        'thunderstrom' : 'Hujan Petir',
        'snow' : 'Salju',
        'mist' : 'Kabut'
    }

    # Mengubah deskripsi cuaca ke bahasa indonesia
    translation_description = translation_dict.get(weather_description, weather_description)

    print("Weather : ", translation_description)
    print("Temperature : ", round(temperature, 1), "°C")

else:
    print("Unable to retrieve weather information.")



