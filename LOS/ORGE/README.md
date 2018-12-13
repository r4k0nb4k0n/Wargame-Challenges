# ORGE

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_orge where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orge where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orge"); 
  highlight_file(__FILE__); 
?>
```

## Background Knowledge
* [The difference between 'AND' and '&&' in SQL](https://stackoverflow.com/questions/4105658/the-difference-between-and-and-in-sql)
	- `AND` 연산자는 표준 SQL.
	- `&&` 연산자는 proprietary syntax(독점적인 구문...?)

## Inspection
* 저번 [`ORC`](https://github.com/r4k0nb4k0n/Wargame-Challenges/tree/master/LOS/ORC) 문제와 거의 똑같지만, 다음 문장이 추가되었다.
	- `if(preg_match('/or|and/i', $_GET[pw])) exit("HeHe");`
		+ `OR`, `AND` 연산자를 대소문자 구분없이 모두 거른다.
		+ 이를 우회할 방법을 찾아야 한다.

## Solution
* [orge_blind_sqli_parametric_search.py](./orge_blind_sqli_parametric_search.py)
	- `id`가 `admin`인 `pw`의 길이를 알아낸다.
		+ `' || id='admin' && length(pw) < {X}`
	- 알아낸 길이를 통해 `pw`를 한 글자씩 알아낸다.
		+ `' or id='admin' && ascii(substr(pw,{i},1)) < {X}`
* `or`을 `||`로, `and`를 `&&`로 치환한다.