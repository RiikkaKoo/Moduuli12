# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma,
# joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan
# Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

api_key = f"avain"

paikkakunta = input("Syötä paikkakunnan nimi: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric&lang=fi"

vastaus = requests.get(url)
json = vastaus.json()

sää = json["weather"][0]
lämpötila = json["main"]

print(f"{paikkakunta} sää tällä hetkellä:\n"
      f"\n"
      f"{sää['description'].capitalize()}.\n"
      f"Lämpötila {int(lämpötila['temp'])} Celsius-astetta, tuntuu kuin {int(lämpötila['feels_like'])} Celcius-astetta.")