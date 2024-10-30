# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa:
# https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests

url = f"https://api.chucknorris.io/jokes/random"

vitsi = requests.get(url)
json = vitsi.json()


print(f"Satunnainen Chuck Norris -vitsi:\n\n{json['value']}")