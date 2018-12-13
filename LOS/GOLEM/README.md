# GOLEM

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe");`
	- `or`, `and`, `substr(`, `=`를 거른다.
* `select id from prob_golem where id='guest' and pw='{$_GET[pw]}'`
	- 파라미터로 `pw`를 넘긴다.
* `if($result['id']) echo "<h2>Hello {$result[id]}</h2>";`
	- 쿼리문이 참일 때만 뜨므로 Blind SQLi를 시도할 수 있다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem");`

## Solution
* [golem_blind_sqli_parametric_search.py](./golem_blind_sqli_parametric_search.py)
	- `=`는 `LIKE`로 대체한다.
	- `or`, `and`는 `||`, `&&`로 대체한다. `&&`는 URL에 직접 쓸 때 `%27`로 URL encoded로 입력한다.
	- `substr(`는 `substring(`로 대체한다.
	- `left`, `right`, `charindex`같은 함수들도 있다.