# TROLL

## Problem
```php
<?php  
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  if(@ereg("admin",$_GET[id])) exit("HeHe");
  $query = "select id from prob_troll where id='{$_GET[id]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysql_fetch_array(mysql_query($query));
  if($result['id'] == 'admin') solve("troll");
  highlight_file(__FILE__);
?>
```

## Background Knowledge
* [PHP: `ereg`](http://php.net/manual/en/function.ereg.php)
	- A function do Regular expression match.
	- This function was **DEPRECATED** in PHP 5.3.0, and **REMOVED** in PHP 7.0.0.

## Inspection
* `if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");`
	- `'` 작은따옴표를 쓸 수 없도록 거른다.
* `if(@ereg("admin",$_GET[id])) exit("HeHe");`
	- `admin`이란 문자열을 거른다.
* `select id from prob_troll where id='{$_GET[id]}'`
	- 파라미터로 `id`를 건넨다.
* `if($result['id'] == 'admin') solve("troll");`
	- 쿼리문의 결과의 `id`가 `admin`이어야 통과한다.
	
## Solution
* `AdMiN`, `Admin` 등 `admin`(모두 소문자)가 아니고 대문자를 섞어서 쓴다.
	- 이는 `ereg()`과 DB의 문자열 비교를 우회하여 결국 `id`가 `admin`인 결과를 나타낸다.