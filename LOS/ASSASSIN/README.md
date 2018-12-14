# ASSASSIN

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("assassin"); 
  highlight_file(__FILE__); 
?>
```

## Background Knowledges
* [SQL Wildcard Characters](https://www.w3schools.com/sql/sql_wildcards.asp)
	- `%`
		+ The percent sign represents zero, one, or multiple characters.
	- `-`
		+ The underscore represents a **single** character.


## Inspection
* `if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); `
	- 파라미터의 `pw`의 `'`(작은따옴표, single quote)를 거른다.
* `select id from prob_assassin where pw like '{$_GET[pw]}'`
	- 파라미터로 `pw`를 넘긴다.
	- `pw` 양옆을 single quote가 감싼다.
* `if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; `
	- 쿼리문의 결과가 뜨면 출력된다.
	- 쿼리문의 결과가 참인지 거짓인지 구분할 수 있다.
	- **Blind SQLi**를 시도할 수 있다.
* `if($result['id'] == 'admin') solve("assassin"); `
	- 결과의 `id`가 `admin`이면 통과한다.

## Solution
* [`assassin_blind_sqli.py`](./assassin_blind_sqli.py)
	- `pw`의 길이를 알아낸다.
		+ `_`를 이용한다.
	- `pw`를 한 글자씩 유추한다.
		+ `(알아낸 글자들)` + `(유추하는 한 글자)` + `..%%%`(남는 길이만큼 채우기) -> 총 길이는 알아낸 `pw`의 길이이다.
		+ `Hello`가 뜰 때 `admin`도 뜨면 통과한다.