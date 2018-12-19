# DRAGON

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_dragon where id='guest'# and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("dragon");
  highlight_file(__FILE__); 
?>
```

## Inspection
* `select id from prob_dragon where id='guest'# and pw='{$_GET[pw]}'`
	- 파라미터의 `pw`를 받는다.
	- `#`이후로 주석처리된다.
* `if($result['id']) echo "<h2>Hello {$result[id]}</h2>";`
	- 쿼리문의 결과가 뜨면 출력된다.
* `if($result['id'] == 'admin') solve("dragon");`
	- 쿼리문의 결과의 `id`가 `admin`이면 통과한다.
	
## Solution
* [`bypass_sharp_comment.py`](./bypass_sharp_comment.py)
	- `#`은 그 줄의 끝까지만 주석처리하므로, 이를 개행으로 우회한다.
	- `\r\n` = `%0D%0A`
	