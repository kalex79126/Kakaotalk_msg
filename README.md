# Kakaotalk_Message
This program is designed to send messages to yourself by using KAKAOTALK API.

## Sign up as a kakaotalk Developer
By accessing the url below, sign up for kakotalk developers. It provides kakao API that gives you access to many different functions such as kakotalk login, send messages, friend API, AI API, etc. 
url: https://developers.kakao.com/ 
![image](https://github.com/kalex79126/Kakaotalk_msg/assets/122379584/454f18ec-d09d-4d75-999c-ac5b919faa5a)

## Application
Add an application after logging in by clicking my application then add.
![image](https://github.com/kalex79126/Kakaotalk_msg/assets/122379584/585e5314-d8a0-497c-833c-ca3bda15096b)

## REST API KEY
BY clikcing the application that you have created, it shows the application properties. You need to use the REST API KEY value later on.

## Kakaotalk Login Settings
Login to your own kakaotalk ID to be used in the program. Set your redirect url then allow to send message in kakaotalk in consent items section.
![image](https://github.com/kalex79126/Kakaotalk_msg/assets/122379584/e3ad91a6-6f2d-4085-ace2-5278eab24211)

![image](https://github.com/kalex79126/Kakaotalk_msg/assets/122379584/70e6c3d4-ef54-449a-a1a2-7e93cb233199)

## Check Your Code Value
By using the REST API KEY value and the Redirect URL that you have set for and access a new tab using the URL below.
https://kauth.kakao.com/oauth/authorize?client_id=YOUR REST KEY VALUE&redirect_uri=YOUR REDIRECT VALUE&response_type=code 

## Create Your Token
Open kakaotalk.py then create your certify token that allows you to send kakaotalk messages. It saves the token as a json file. This token expires every 24 hours and have to be renewed.

## Send Messages
Open send_kakaotalk_msg.py. Customize your own message then send it to yourself.
