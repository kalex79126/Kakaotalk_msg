import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = 'REPLACE WITH YOUR REST KEY VALUE' #REPLACE WITH YOUR REST KEY VALUE
redirect_uri = 'https://example.com/oauth'
code = 'REPLACE WITH YOUR CODE' #REPLACE WITH YOUR CODE

data = {
    'grant_type':'authorization_code',
    'client_id':client_id,
    'redirect_uri':redirect_uri,
    'code': code,
    }

response = requests.post(url, data=data)
tokens = response.json()

#save issued token into json file
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)