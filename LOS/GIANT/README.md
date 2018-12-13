# GIANT

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
  if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
  $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result[1234]) solve("giant"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(strlen($_GET[shit])>1) exit("No Hack ~_~");`
	- 파라미터로 넘기는 `shit`의 길이가 `1`을 초과하면 걸러진다.
* `if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe");`
	- `` ``(space), `\n`, `\r`, `\t`가 걸러진다. 이는 띄어쓰기와 그 우회방법들이 거의 막힌 것이나 다름없다.
* `select 1234 from{$_GET[shit]}prob_giant where 1`
	- 파라미터로 `shit`을 넘긴다.
	- `shit`에 **띄어쓰기 하나**만 들어가면 쿼리문이 잘 들어갈 것이다.
	
* `if($result[1234]) solve("giant");`
	- 쿼리문의 결과가 나오면 통과한다.

## Solution
* `\t`(horizontal tab)인 `%09`가 아닌 vertical tab인 `%0b`를 사용하면 통과한다.