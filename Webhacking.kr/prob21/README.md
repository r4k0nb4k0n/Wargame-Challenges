# 21

### First impression
```
BLIND SQL INJECTION
```
* `no`, `id`, `pw` 총 3개의 필드가 파라미터로 넘어간다.
* `id`, `pw`는 숨겨져 있다.
* `no`에 값을 입력하면 `TRUE`, `FALSE`, ` `의 결과가 나타난다.

### Trial and error
* [The basic of Blind SQL Injection](./The_basic_of_Blind_SQL_Injection_PRIDE.pdf)
	- 쿼리가 참 또는 거짓일 때의 서버의 반응으로 데이터를 유추하고 얻는 기술.
	- [`substr()`](https://www.w3schools.com/sql/func_mysql_substr.asp), [`ascii()`](https://www.w3schools.com/sql/func_sqlserver_ascii.asp)
	- 위 두 함수를 이용하여 필요한 정보를 한 글자씩 유추한다. [Parametric Search](http://hongjun7.tistory.com/133)
	- 일반적으로 DB 관리자가 테이블을 생성하면 `table_name`은 테이블명, `table_type`은 `base table`로 지정된다.
		- 이를 이용하여 계정 정보가 담긴 테이블명을 알아낼 수 있다.
		- `SELECT table_name FROM information_schema.tables
WHERE table_type='base table'`

* `from` 키워드를 대소문자 구분없이 필터링하고 있다.
* `no`에 `1`, `2`를 입력하면 `True`로 나타난다.
* `no`에 따른 `id`, `pw`의 길이와 글자들을 blind sql injection으로 유추할 수 있다.

### Solution
* [blind_sqli_parameric_search.py](./blind_sqli_parametric_search.py)
* `admin`의 `pw`를 Auth로 인증하면 성공한다.