import requests


def get_weather_forecast(city):
    # Ganti dengan API key yang Anda dapatkan dari OpenWeather
    api_key = "11a5ba73255cfa55831c342c4a9cceee"
    base_url = "http://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "cnt": 1  # Mengambil prediksi cuaca satu minggu ke depan (7 hari)
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)

    if data["cod"] == "200":
        print("Prediksi cuaca untuk", data["city"]["name"])

        for forecast in data["list"]:
            date = forecast["dt_txt"]
            temperature = forecast["main"]["temp"]
            weather_desc = forecast["weather"][0]["description"]

            print(
                f"Tanggal: {date}, Temperatur: {temperature}°C, Deskripsi Cuaca: {weather_desc}")
    else:
        print("Gagal memperoleh data cuaca.")


# Memanggil fungsi get_weather_forecast dengan kota yang diinginkan
# get_weather_forecast("Banda Aceh")

import csv
import requests

def get_weather_data(city):
    api_key = ""  # Ganti dengan API key yang Anda dapatkan dari OpenWeather

    base_url = "http://api.openweathermap.org/data/2.5/weather"

    start_date = "2023-01-01"
    end_date = "2023-05-31"

    date = start_date
    with open("weather_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Temperature (°C)", "Weather Description"])

        while date <= end_date:
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric",
                "dt": date
            }

            response = requests.get(base_url, params=params)
            data = response.json()

            if data["cod"] == 200:
                temperature = data["main"]["temp"]
                weather_desc = data["weather"][0]["description"]
                writer.writerow([date, temperature, weather_desc])

            date = increment_date(date)
            print(date)

    print("Data cuaca berhasil disimpan dalam weather_data.csv")

def increment_date(date):
    year, month, day = map(int, date.split("-"))
    next_day = day + 1

    # Handle end of month
    if next_day > 31 or (month == 2 and next_day > 28):
        next_day = 1
        month += 1

    # Handle end of year
    if month > 12:
        month = 1
        year += 1

    return f"{year:04d}-{month:02d}-{next_day:02d}"

# Memanggil fungsi get_weather_data dengan kota yang diinginkan
get_weather_data("Banda Aceh")

