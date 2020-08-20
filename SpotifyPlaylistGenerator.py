import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = 'BQCa3vCq3cwUm-KOkloahocq41TBsmEuvQPIdlpU8onJwAEoHXsvFEJFT3MQY2diy0tTzGwwTtIVowIQX8v0a3KsTI2tT9-S6a0KcNg2AOA_nVOufAFqL8R3o-Z-P9I_z0zsXXxqiJQiGcy2pkYA4yJhhmjc1mB7BUVp_bFpq0SeE75uaSHE'
uris = []

# FILTERS
limit = 10      # number of songs
market = "AU"   # country
seed_genres = "pop"     # genres
target_danceability = 0.2
seed_artists = '4MCBfE4596Uoi2O4DtmEMz'

# QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&seed_artists={seed_artists}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")