'''
pyc decompile solution
Written by github.com/r4k0nb4k0n
Written in python 2
'''

import bughela
import time
import requests
import sys
from hashlib import sha512

def main():
	url = 'http://wargame.kr:8080/pyc_decompile/'
	
	sys.stdout.write('Get time from server... -> ')
	server_time = get_time_from_server(url)
	sys.stdout.write(server_time + '\n')
	
	sys.stdout.write('Generate proper flag... -> ')
	flag = gen_flag(server_time)
	sys.stdout.write(flag + '\n')
	
	sys.stdout.write('Send flag and get result... \n')
	result = send_flag_and_get_result(url, flag)
	sys.stdout.write(result + '\n')
	
def gen_flag(server_time):
	server_time = time.strptime(server_time, '%Y/%m/%d %H:%M:%S')
	seed = time.strftime('%m/%d/HJEJSH', server_time)
	hs = sha512(seed).hexdigest()
	start = server_time.tm_hour % 3 + 1
	end = start * (server_time.tm_min % 30 + 10)
	flag = hs[start:end]
	return flag
	
def get_time_from_server(url):
	return requests.get(url).text[82:101]
	
def send_flag_and_get_result(url, flag):
	url_with_flag = url + '?flag=' + flag
	res = requests.get(url_with_flag)
	return res.text

if __name__ == '__main__':
	main()