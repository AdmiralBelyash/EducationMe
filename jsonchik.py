import requests
import json

client_id = '92da7c2c4bbf3a0b49c1'
client_secret = '45eb5ccc967664bc1eccd5a2e5449bd8'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
#artists
artists = []
#didjay
with open('cum.txt', encoding='UTF-8') as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = 'https://api.artsy.net/api/artists/{}'.format(artist_id)
        params = {'xapp_token': token}
        resp = requests.get(url, params=params).text
        data = json.loads(resp)
        if data.get('sortable_name') is not None:
            artists.append({'name': data.get('sortable_name'), 'birthday': data.get('birthday')})

for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])
