import requests

url1 = 'http://suninatas.com/Part_one/web07/web07.asp'
url2 = 'http://suninatas.com/Part_one/web07/web07_1.asp'
cookies = {
	'ASPSESSIONIDQAAQSBQS': '',
	'auth_Fkey': '?????'
}
payloads = {
	'web07': 'Do U Like girls?'
}

res = requests.get(url1, cookies=cookies)
print(res)
res = requests.post(url2, cookies=cookies, data=payloads)
print(res.text)