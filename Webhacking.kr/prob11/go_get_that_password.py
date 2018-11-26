import requests

url = 'http://webhacking.kr/challenge/codeing/code2.html'
cookies = {}
payload = {}

cookies['PHPSESSID'] = ''
payload['val'] = '1abcde_xxxaxxxaxxxaxxxa\tp\ta\ts\ts'

res = requests.get(url, cookies=cookies, params=payload)

print(res.text)