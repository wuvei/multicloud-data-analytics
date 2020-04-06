import requests
import json
import random
access_token = "pk.eyJ1IjoienljMTk5NzAwIiwiYSI6ImNrOGswdTZqZzAyem0zbW54Y3g3ZTFzOHEifQ.dn5LAHxO-O95GCQd8FJctg"

r = requests.get('https://api.mapbox.com/geocoding/v5/mapbox.places/Northern%20Virginia.json', params = {'access_token':access_token})

print(r.content)
print(random.choice(r.json()['features'])['center'])