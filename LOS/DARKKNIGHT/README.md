# DARKKNIGHT

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_darkknight where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_darkknight where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("darkknight"); 
  highlight_file(__FILE__); 
?>
```
## Background Knowledge
* [`mid()`](https://www.w3resource.com/mysql/string-functions/mysql-mid-function.php)
	- `MID(str, pos, len)`
	- MySQL MID() extracts a substring from a string. The actual string, position to start extraction and length of the extracted string - all are specified as arguments.
* [`ord()`](https://www.w3resource.com/mysql/string-functions/mysql-ord-function.php)
	- MySQL ORD() returns the code for the leftmost character if that character is a multi-byte (sequence of one or more bytes) one. 
	- **If the leftmost character is not a multi-byte character, ORD() returns the same value as the ASCII() function.**

## Inspection
* `if(preg_match('/\'/i', $_GET[pw])) exit("HeHe");`
	- 파라미터의 `pw`에 `'`(작은따옴표)를 거른다.
* `if(preg_match('/\'|substr|ascii|=/i', $_GET[no])) exit("HeHe");`
	- 파라미터의 `no`에 `'`, `substr`, `ascii`, `=`를 거른다.
* `select id from prob_darkknight where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}`
	- 첫번째 쿼리문이다.
	- 파라미터로 `pw`와 `no`를 받는다.
	- `no`에는 `'`가 보이지 않아서 주입이 수월할 것이다.
* `if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; `
	- 쿼리문의 결과가 참일 때 나타나는 것이다.
	- 쿼리문의 결과의 참/거짓 여부를 구분할 수 있으므로, **Blind SQLi**를 시도할 수 있다.
* `select pw from prob_darkknight where id='admin' and pw='{$_GET[pw]}`
	- 두번째 쿼리문이다.
	- 파라미터로 `pw`를 받는다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("darkknight")`
	- `admin`의 `pw`를 넣어야 통과한다.

## Solution
* [darkknight_blind_sqli_parametric_search.py](./darkknight_blind_sqli_parametric_search.py)
	- `admin`의 `pw`의 길이를 알아낸다.
		+ `1 or id like "admin" and length(pw) < {X}`
		+ 걸러지는 `'`(작은따옴표) 대신 `"`(큰따옴표)를 사용했다.
	- `admin`의 `pw`를 한 글자씩 알아낸다.
		+ `1 or id like "admin" and ord(mid(pw,{i},1)) < {X}`
		+ 걸러지는 `'`(작은따옴표) 대신 `"`(큰따옴표)를 사용했다.
		+ 걸러지는 `substr`, `substring` 대신 `mid`를 사용했다.
		+ 걸러지는 `ascii` 대신 `ord`를 사용했다.
	- 알아낸 `admin`의 `pw`를 파라미터로 넘겨주면 통과한다.