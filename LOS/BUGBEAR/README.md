# BUGBEAR

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/\'/i', $_GET[pw])) exit("HeHe");`
	- 파라미터의 `pw`에서 `'`(작은따옴표)를 거른다.
* `if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe");`
	- 파라미터의 `pw`에서 `'`(작은따옴표), `substr`, `ascii`, `=`, `or`, `and`, `` ``(space), `like`, `0x`를 거른다.
* `select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}`
	- 첫번째 쿼리문이다.
	- 파라미터로 `pw`, `no`를 넘긴다.
	- `no` 쪽엔 따옴표가 없다.
* `if($result['id']) echo "<h2>Hello {$result[id]}</h2>";`
	- 첫번째 쿼리문이 참이면 `Hello {id}`가 뜬다.
	- 쿼리문의 참/거짓 여부를 판단할 수 있다.
	- **Blind SQLi**를 시도할 수 있다.
* `select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'`
	- 두번째 쿼리문이다.
	- 파라미터로 `pw`를 넘긴다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear");`
	- `admin`의 `pw`를 넘겨야 통과한다.

## Solution
* [`bugbear_blind_sqli_parametric_search.py`](./bugbear_blind_sqli_parametric_search.py)
	- `admin`의 `pw`의 길이를 알아낸다.
		+ `1 or id = "admin" and length(pw) < {X}`
			+ `` ``(space)는 Tab(`\t`), Line Feed(`\n`), Carriage Return(`\r`), `/**/`, `()`, `+`로 우회할 수 있다.
			+ `or`, `and`는 `||`, `&&`로 우회할 수 있다. `&`의 URL encoded 값은 `%26`이다.
			+ `=`, `like`을 쓸 수 없는 상황에서  `id = "admin"`을 나타내려면 `id <> "guest"` 같이 일종의 이중 부정을 해야 한다. 
		+ `1	||	id	<>	"guest"	&&	length(pw)	<	{X}`
		+ `1%09||%09id%09<>%09"guest"%09%26%26%09length(pw)%09<%09{X}`
			+ url창에 `&&`을 직접 치면 인식이 안된다. `%26`으로 직접 넣어줘야 한다. 물론 스크립트에서는 상관없다.
	- `admin`의 `pw`를 한 글자씩 알아낸다.
		+ `1	||	id	<>	"guest"	&&	hex(mid(pw,{i},1))	<	hex({X})`
			+ `or` 때문에 `ord()`도 걸러지므로 `hex()`를 사용했다.
	- 알아낸 `admin`의 `pw`를 파라미터로 넘겨주면 통과한다.