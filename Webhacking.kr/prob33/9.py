import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-6/nextt.php'
cookies = {
	'PHPSESSID': ''
}
payloads = {
	'ans': ''
}

answer = ''
i = 97
while i <= 122:
	answer += chr(i)
	i += 2

payloads['ans'] = answer

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)