import requests

url = 'http://webhacking.kr/challenge/bonus/bonus-6/'
ip_url = 'http://ifconfig.me'
cookies = {
	'PHPSESSID': ''
}

res = requests.get(url, cookies=cookies)
res = requests.get(ip_url)
ip = res.text.rstrip().lstrip()

for i in range(0, len(ip)+1):
	si = str(i)
	si = si if len(si) <= 1 else si[:-1]
	print('ip : Replace',si,'with',str(ord(si)))
	ip = ip.replace(si, str(ord(si)))
	print(ip)
	
ip = ip.replace('.', '')
print('Remove . in ip',ip)

ip = ip[:10+1]
print('Shorten',ip)

answer = int(ip)*2
answer = int(ip)/2
answer = str(answer)
print('ip/2',answer)
answer = answer.replace('.', '')
print('Remove . in answer',answer)

url += 'answerip/' + ip + '/' + answer + '.' + ip
res = requests.get(url, cookies=cookies)
print(res.text)