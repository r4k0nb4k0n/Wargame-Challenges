# ORC

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```
## Background Knowledge
* [The basic of Blind SQL Injection](./The_basic_of_Blind_SQL_Injection_PRIDE.pdf)
	- 쿼리가 참 또는 거짓일 때의 서버의 반응으로 데이터를 유추하고 얻는 기술.
	- [`substr()`](https://www.w3schools.com/sql/func_mysql_substr.asp), [`ascii()`](https://www.w3schools.com/sql/func_sqlserver_ascii.asp)
	- 위 두 함수를 이용하여 필요한 정보를 한 글자씩 유추한다. [Parametric Search](http://hongjun7.tistory.com/133)
* `addslashes()`
	- [php.net PHP: addslashes](http://php.net/manual/kr/function.addslashes.php)
		+ 데이터베이스 질의 등에서 처리할 필요가 있는 문자 앞에 백슬래시를 붙인 문자열을 반환합니다. 이 문자들은 홑따옴표(`'`), 겹따옴표(`"`), 백슬래시(`\`), `NUL`(`NULL` 바이트)입니다.
	- [W3Schools PHP addslashes() Function](https://www.w3schools.com/php/func_string_addslashes.asp)
		+ PHP runs addslashes() on all GET, POST, and COOKIE data by default. Therefore you should not use addslashes() on strings that have already been escaped, this will cause **double escaping**. The function get_magic_quotes_gpc() can be used to check this.


## Inspection
* `preg_match`로 거르는 것은 다른 테이블을 건드는 것을 막기 위함이지, 문제에 관한 것은 아니다.
* `select id from prob_orc where id='admin' and pw='{$_GET[pw]}'`
	- 파라미터로 `pw`가 넘겨진다.
	- `AND`, `OR` 연산자 우선순위의 차이를 이용하여 쿼리가 참인 경우를 만들어보자.
		+ `?pw=' or 1=1 -- ` 맨 뒤 띄어쓰기에 유의한다.
	- 쿼리문이 참일 때와 거짓일 때 구분이 가능하다. `Hello admin` 출력 여부로 알 수 있다.
	- **Blind SQLi**를 시도할 수 있다.
* `$_GET[pw] = addslashes($_GET[pw]);`
	- 처리할 필요가 있는 문자 앞에 백슬래시를 붙인다. double escaping 할 수 있다.
* `addslashes()` 처리한 `pw`로 쿼리를 다시 날린다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc");`
	- 쿼리문에 대한 결과가 나오고, 결과의 `pw`가 `addslashes()` 처리한 `pw`와 같으면 통과한다.

## Solution
* [`orc_blind_sqli_parametric_search.py`](./orc_blind_sqli_parametric_search.py)
	- `id`가 `admin`인 `pw`의 길이를 알아낸다.
		+ `' or id='admin' and length(pw) < {X}`
	- 알아낸 길이를 통해 `pw`를 한 글자씩 알아낸다.
		+ `' or id='admin' and ascii(substr(pw,{i},1)) < {x}`

## Review
* `id='admin'`이라는 조건문을 포함시키지 않고 쿼리문을 날렸더니 엉뚱한 `pw`를 알아내었다. 조건문에 유의해야겠다.