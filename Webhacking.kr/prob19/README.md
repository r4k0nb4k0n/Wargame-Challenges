# 19

### First impression
```
id: admin 제출

you are not admin
```

### Trial and error
* `admin`을 제출하면 다음과 같은 응답이 나타난다.
```
you are not admin
```
* Response Headers
```
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 29 Nov 2018 06:23:23 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
P3P: CP='NOI CURa ADMa DEVa TAIa OUR DELa BUS IND PHY ONL UNI COM NAV INT DEM PRE'
X-Powered-By: PHP/5.2.17p1
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Encoding: gzip
```

* `admin`이 아닌 것을 제출하면 다음과 같은 오류가 나타난다.
```
Warning: Cannot modify header information - headers already sent by (output started at 
/home/hosting_users/webhacking/www/challenge/javascript/js6.html:11) 
in /home/hosting_users/webhacking/www/challenge/javascript/js6.html on line 29
```
	- 이미 헤더를 보냈기 때문에 헤더 정보를 수정할 수 없다고 한다.
* Request Headers
```
GET /challenge/javascript/js6.html?id=test HTTP/1.1
Host: webhacking.kr
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://webhacking.kr/challenge/javascript/js6.html
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: PHPSESSID=XXXXXXXXXXXXXXXXXXXXXXXXXXX
```
	- 쿠키로 `PHPSESSID`를 보낸다.

* Response Headers
```
HTTP/1.1 200 OK
Server: nginx
Date: Thu, 29 Nov 2018 06:10:58 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
P3P: CP='NOI CURa ADMa DEVa TAIa OUR DELa BUS IND PHY ONL UNI COM NAV INT DEM PRE'
X-Powered-By: PHP/5.2.17p1
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Encoding: gzip
```
	- `Expires: Thu, 19 Nov 1981 08:52:00 GMT`를 보면 무려 37년 전에 만료된 페이지다.
	- `Cache-Control`과 `Pragma`를 보아하니 정보를 안남게 하고 만료된 것이라고 뜨게 하려고 한 것 같다.

* `admin`의 양 옆에 다음과 같은 글자들은 삽입 가능하다.
	- Tab : `%09`
	- Line Feed (`\n`): `%0a`
	- Carrage Return(`\r`) : `%0d`
	- 더하기 : `+`
* 이는 양 옆 trim을 해주는 것 같다.
* 현재 다른 솔루션들을 찾아본 결과 `admin`이 아닌 다른 값을 전송할 경우 오류가 나타나지 않아야 한다.
* 현재 오류가 나타나는 것 같다.