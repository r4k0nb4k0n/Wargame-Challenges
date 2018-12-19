# DARK_EYES

## Problem
```php
<?php
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(mysql_error()) exit();
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  
  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");
  highlight_file(__FILE__);
?>
```

## Inspection
* `if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");`
	- 파라미터의 `pw`에서 `col`, `if`, `case`, `when`, `sleep`, `benchmark`를 거른다.
* `select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'`
	- 첫번째 쿼리다.
	- 파라미터로 `pw`를 받는다.
* `if(mysql_error()) exit();`
	- 첫번째 쿼리문의 오류가 있다면 종료한다.
	- 참 또는 거짓일 때 오류가 뜬다면 Blind SQLi를 시도할 수 있다.
	- 오류 상세내용을 보여주지 않으므로 제한적이다.
* `select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'`
	- 두번째 쿼리다.
	- 첫번째 쿼리와는 달리 `pw`를 뽑는다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");`
	- 두번째 쿼리문의 결과가 나타나고, 이의 `pw`가 파라미터의 `pw`와 같다면 통과한다.
	
## Solution
* [`dark_eyes_blind_sqli_parametric_search.py`](./dark_eyes_blind_sqli_parametric_search.py)
	- `IRON_GOLEM`과 같은 방식으로 오류를 일으킨다.
	- [How to conditionally raise an error in mysql without stored procedure](https://dba.stackexchange.com/questions/78594/how-to-conditionally-raise-an-error-in-mysql-without-stored-procedure)
		+ 여러개의 레코드들을 돌려주는 서브쿼리를 작성한다.
	- [What is the difference between `union` and `union all`](https://stackoverflow.com/questions/49925/what-is-the-difference-between-union-and-union-all)
		+ `union`은 중복을 제거한 결과를 나타낸다.
		+ `union all`은 중복 레코드들도 모두 나타낸다.
	- `SELECT 1 UNION (subquery)`
		+ `union`이 중복을 제거한 결과를 나타내는 것을 이용한다.
		+ `(subquery)`가 참이면 `1`과 중복되어 `1` 레코드 한 개만 나타낸다.
		+ `(subquery)`가 거짓이면 `1`과 중복되지 않고 `1`과 `0` 레코드 두 개를 나타낸다.
	- `admin`의 `pw`의 길이를 알아낸다.
		+ `' or id = 'admin' and (select 1 union select (length(pw) < {x})) -- `
		+ 거짓일 경우 오류가 발생한다.
	- `admin`의 `pw`를 한 글자씩 유추한다.
		+ `' or id = 'admin' and (select 1 union select(ord(mid(pw,{i},1)) < {x})) -- `
		+ 거짓일 경우 오류가 발생한다.

## Review
* `if`, `case`, `when`을 걸러내어 조건문을 사용할 수 없어서 이를 우회할 방법을 생각해야 했다.
* 처음에는 이산 수학의 propositional logic을 떠올렸다. 하지만 이를 이용하면 참이든 거짓이든 오류가 뜬다.