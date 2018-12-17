import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-6/wtff.php'
ip_url = 'http://ifconfig.me'
cookies = {
	'PHPSESSID': ''
}
payloads = {}

res = requests.get(ip_url)
ip = res.text.rstrip().lstrip().replace('.','')

payloads[ip] = ip

print(ip, payloads)

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)