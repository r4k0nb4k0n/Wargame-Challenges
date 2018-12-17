import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-6/md555.php'

cookies = {
	'PHPSESSID': '',
	'imcookie': 'true'
}

params = {
	'impost': 'true'
}

url += '?imget=true'

res = requests.post(url, cookies=cookies, data=params)
print(res.text)