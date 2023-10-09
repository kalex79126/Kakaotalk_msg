import requests
import json

# recall the token issued
with open("token.json","r") as kakao:
    tokens = json.load(kakao)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data = {
       'object_type': 'text',
       'text': 'Hello World.',
       'link': {
           'web_url': 'https://developers.kakao.com',
           'mobile_web_url': 'https://developers.kakao.com'
       },
       'button_title': 'keyword'
   }
   
data = {'template_object': json.dumps(data)}
response = requests.post(url, headers=headers, data=data)
response.status_code