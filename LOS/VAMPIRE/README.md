# VAMPIRE

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~"); 
  $_GET[id] = str_replace("admin","",$_GET[id]); 
  $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id'] == 'admin') solve("vampire"); 
  highlight_file(__FILE__); 
?>
```

## Background Knowledge
* [PHP: `str_replace`](http://php.net/manual/kr/function.str-replace.php)

## Inspection
* `if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~"); `
	- `'` 작은따옴표를 거른다.
* `$_GET[id] = str_replace("admin","",$_GET[id]); `
	- 파라미터로 넘어가는 `id`의 내용 중 `admin`을 빈칸으로 치환한다.
* `select id from prob_vampire where id='{$_GET[id]}'`
	- 파라미터로 `id`가 넘어간다.
* `if($result['id'] == 'admin') solve("vampire");`
	- 쿼리문의 결과의 `id`가 `admin`이라면 통과한다.
	
## Solution
* `str_replace()`는 재귀적이 아닌 최초 1회 탐색을 하기 때문에, 다음과 같이 겹쳐서 쓴다.
	- `adadminmin`
	- `str_replace("admin","","adadminmin");` -> `"admin"`