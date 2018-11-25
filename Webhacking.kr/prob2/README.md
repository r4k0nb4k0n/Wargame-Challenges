# 2

### First impression
beist lab homepage

### Trial and error
* Found.
	+ `/index.php`
		- Line 19 : `<area shape="rect" coords="851,7,890,65" href="admin/" target="" alt="">` 찾음.
		- Line 33 : `<!--2018-11-24 04:26:55--></td>` 찾음.
			- 쿠키의 `time` 값에 따라 변함.
	+ `/bbs/read.php?No=1`
		- 비밀번호가 걸린 글 찾음.
		- 주석처리된 css 찾음.
	+ `/admin`
		- `/index.php`로 전송하는 비밀번호 폼 찾음.

* 쿠키의 `time` 값에 그냥 `TRUE`나 `FALSE`를 넣고 새로고침하면, 적용이 되지 않고 예전에 처리가 잘 되었던 쿠키가 나타난다.
* 쿠키의 `time` 값 끝에 `& 조건문`을 넣어주고 새로고침하면, 주석값이 달라진다.
	- 참일 때, `2070-01-01 09:00:01`.
	- 거짓일 때, `2070-01-01 09:00:00`.
* SQL 문법의 조건문으로 넣어줘야 할 것 같다.
	- `1 == 2`는 처리가 되지 않는다.
	- `1 = 2`는 거짓으로 처리가 된다.
	- `1 = -(-1)`은 참으로 처리가 된다.
* **Blind SQL Injection**
* 이를 통해 숨겨진 정보를 알아내야 한다.
* 도저히 들어있는 테이블 명을 알 수 없어서 검색을 통해 예전 힌트에 테이블 `admin`, `FreeB0aRd`가 있다는 것을 알게 되었다. 

* 다음과 같이 길이를 유추할 수 있다.
	- `1543122851 & (select length(password) from admin) = 10` -> 참.
	- `1543122851 & (select length(password) from FreeB0aRd) = 9` -> 참.
	- `admin`의 비밀번호 길이는 `10`자리.
	- `FreeB0aRd`의 비밀번호 길이는 `9`자리.
	
* 비밀번호는 ASCII 문자로 구성되어 있다는 가정 하에, 이를 선형 탐색하는 스크립트를 짰다. 
	- [linear-search.py](./linear_search.py)
	- 구름IDE에서 대략 20-30분 소요함.

* FreeB0aRd의 비밀번호를 통해 들어가서 매뉴얼 압축 파일을 다운로드한다.
* admin의 비밀번호를 통해 들어가서 매뉴얼 압축 파일의 비밀번호를 알아낸다.
* 입축 파일에 들어있는 파일에 auth 키가 들어있다.