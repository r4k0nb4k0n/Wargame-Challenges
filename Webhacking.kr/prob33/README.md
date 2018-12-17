# 33

## Codes & Solutions
* Challenge 33-1 [`1.php`](./1.php) 
	- `?get=hehe` 접속 후 `Next` 클릭.
* Challenge 33-2 [`2.php`](./2.php) [`2.py`](./2.py)
	- `?post=hehe&post2=hehe2` 넘김.
* Challenge 33-3 [`3.php`](./3.php) 
	- `?myip=xxx.xxx.xxx.xxx` 넘김.
	- 네이버에 "내 아이피" 검색하면 뜨는 것 넘긴다.
* Challenge 33-4 [`4.php`](./4.php) [`4.py`](./4.py)
	- 파이썬 스크립트로 현재 시간 값 구한 후 `md5.hexdigest()` 한 값을 `password` 파라미터로 넘겨줌.
	- 서버와의 시간차이가 미묘하게 1초 이내이므로 보통 5번 중 한두번 성공함.
* Challenge 33-5 [`5.php`](./5.php) [`5.py`](./5.py)
	- GET 파라미터, POST 파라미터, 쿠키값을 동시에 넘긴다.
	- `url`에 `?imget=true`을 붙인다.
	- `params`에 `impost`를 `true`로 넣어준다.
	- `cookies`에 `imcookie`를 `true`로 넣어준다.
* Challenge 33-6 [`6.php`](./6.php) [`6.py`](./6.py)
	- `ifconfig.me`에 접속하여 IP를 알아낸다.
	- 헤더를 조작하여 `User-Agent`를 내 맘대로 바꾼다.
* Challenge 33-7 [`7.php`](./7.php) [`7.py`](./7.py)
	- `.`가 제거된 IP값을 이름으로 하는 파라미터에 `.`가 제거된 IP값을 넘겨준다.
* Challenge 33-8 [`8.php`](./8.php)
	- `?addr=127.0.0.1` 넘겨준다.
* Challenge 33-9 [`9.php`](./9.php) [`9.py`](./9.py)
	- 아스키코드 `97`부터 `122`까지 홀수번째 코드들만 이어붙인 값을 `ans` 파라미터에 넘겨준다.
* Challenge 33-10 [`10.php`](./10.php) [`forfor.php`](./forfor.php)
	- 그냥 접속 IP 알아내고 php 스크립트에 넣고 돌리면 위치 알아낼 수 있다.
	- 뜨는 비밀번호로 인증하면 통과.