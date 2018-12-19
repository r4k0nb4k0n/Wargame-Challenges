# XAVIS

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis"); 
  highlight_file(__FILE__); 
?>
```

## Inspection
* `if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");`
	- 파라미터의 `pw` 안의 `prob`, `_`, `.`, `(`, `)`를 거른다.
* `if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe");`
	- 파라미터의 `pw` 안의 `regex`, `like`를 거른다. 대소문자 구분 없이.
* `select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'`
	- 첫번째 쿼리문.
	- `pw`를 파라미터로 받는다.
* `if($result['id']) echo "<h2>Hello {$result[id]}</h2>";`
	- 첫번째 쿼리문의 결과가 뜨면 출력된다.
	- Blind SQLi 시도를 할 수 있다.
* `select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'`
	- 두번째 쿼리문.
	- 첫번째 쿼리문과는 달리 `pw`를 뽑는다.
* `if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis");`
	- 두번째 쿼리문의 결과인 `pw`와 파라미터의 `pw`가 같으면 통과한다.

## Solution
* [`xavis_blind_sqli_parametric_search.py`](./xavis_blind_sqli_parametric_search.py)
	- `admin`의 `pw`의 길이를 알아낸다.
		+ `' or id='admin' and length(pw) < {x} -- `
	- `admin`의 `pw`의 길이를 4로 나눈다.
		+ 정확히 무슨 문자셋인지는 모르겠지만, 한 글자당 4 byte를 차지하는 multi-byte character라고 추측했다.
	- 알아낸 길이를 통해 `admin`의 `pw`를 한 글자씩 알아낸다.
		+ `' or id='admin' and ord(substring(pw,{i},1)) < {x} -- `

## Review
* 처음엔 이전 문제들처럼 ascii 인코딩으로 풀려고 했더니 length는 `40`이 뜨고 모든 글자가 아스키코드로 `0`으로 떴다.
* `LENGTH()`가 글자 수가 아닌 바이트 수를 센다는 것을 상기하고 multi-byte character로 생각해봤다.
* 왜 1글자 당 4bytes씩 쓰면서 0~255 범위인지는 잘 모르겠다. 서버 부담을 줄이려고 그랬는지도 모르겠다.
* 자꾸 정답 검색을 하고 싶은 생각이 들었는데, 충분히 모든 가능성을 염두에 두어야겠다.
