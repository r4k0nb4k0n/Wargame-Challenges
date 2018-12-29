# UMARU

## Problem
```php
<?php
  include "./config.php";
  login_chk();
  dbconnect();

  function reset_flag(){
    $new_flag = substr(md5(rand(10000000,99999999)."qwer".rand(10000000,99999999)."asdf".rand(10000000,99999999)),8,16);
    $chk = @mysql_fetch_array(mysql_query("select id from prob_umaru where id='{$_SESSION[los_id]}'"));
    if(!$chk[id]) mysql_query("insert into prob_umaru values('{$_SESSION[los_id]}','{$new_flag}')");
    else mysql_query("update prob_umaru set flag='{$new_flag}' where id='{$_SESSION[los_id]}'");
    echo "reset ok";
    highlight_file(__FILE__);
    exit();
  }

  if(!$_GET[flag]){ highlight_file(__FILE__); exit; }

  if(preg_match('/prob|_|\./i', $_GET[flag])) exit("No Hack ~_~");
  if(preg_match('/id|where|order|limit|,/i', $_GET[flag])) exit("HeHe");
  if(strlen($_GET[flag])>100) exit("HeHe");

  $realflag = @mysql_fetch_array(mysql_query("select flag from prob_umaru where id='{$_SESSION[los_id]}'"));

  @mysql_query("create temporary table prob_umaru_temp as select * from prob_umaru where id='{$_SESSION[los_id]}'");
  @mysql_query("update prob_umaru_temp set flag={$_GET[flag]}");

  $tempflag = @mysql_fetch_array(mysql_query("select flag from prob_umaru_temp"));
  if((!$realflag[flag]) || ($realflag[flag] != $tempflag[flag])) reset_flag();

  if($realflag[flag] === $_GET[flag]) solve("umaru");
?>
```

## Inspection
* `if(!$_GET[flag]){ highlight_file(__FILE__); exit; }`
	- 파라미터로 `flag`를 넘겨받는데, 이게 없으면 파일 내용이 출력하고 종료한다.
* `if(preg_match('/prob|_|\./i', $_GET[flag])) exit("No Hack ~_~");`
	- 파라미터 `flag`에서 `prob`, `_`, `.`를 거른다.
* `if(preg_match('/id|where|order|limit|,/i', $_GET[flag])) exit("HeHe");`
	- 파라미터 `flag`에서 `id`, `where`, `order`, `limit`를 대소문자 구분없이 거른다.
* `if(strlen($_GET[flag])>100) exit("HeHe");`
	- 파라미터 `flag`의 길이가 `100`을 넘으면 거른다.
* ` $realflag = @mysql_fetch_array(mysql_query("select flag from prob_umaru where id='{$_SESSION[los_id]}'"));`
	- 세션의 `los_id`에 맞는 진짜 `flag`를 DB에서 받아오고, 이를 `$realflag`에 담는다.
* `@mysql_query("create temporary table prob_umaru_temp as select * from prob_umaru where id='{$_SESSION[los_id]}'");`
* `@mysql_query("update prob_umaru_temp set flag={$_GET[flag]}");`
* `$tempflag = @mysql_fetch_array(mysql_query("select flag from prob_umaru_temp"));`
	- 임시 테이블을 만들고 파라미터로 넘긴 `flag`를 저장한 다음, 이를 `$tempflag`에 담는다.
* `if((!$realflag[flag]) || ($realflag[flag] != $tempflag[flag])) reset_flag();`
	- `$realflag`가 비어있거나(쿼리문의 결과가 나오지 않았을 때), `$realflag`와 `$tempflag`가 다를 경우(서버에서 생성한 `flag`와 파라미터로 넣은 `flag`가 서로 다를 때), `reset_flag()`를 실행한다.
* `if($realflag[flag] === $_GET[flag]) solve("umaru");`
	- 서버에서 생성된 `flag`와 파라미터로 넘긴 `flag`가 Strict comparison으로 같을 경우 통과한다.
* `function reset_flag()`
	- `$new_flag = substr(md5(rand(10000000,99999999)."qwer".rand(10000000,99999999)."asdf".rand(10000000,99999999)),8,16);`
		+ 새로운 `flag`를 생성한다.
		+ 임의의 숫자가 섞인 문자열을 `md5()`로 처리한 결과의 `8`번째 글자부터 `16`개의 글자들을 합친 문자열이다.
	- `$chk = @mysql_fetch_array(mysql_query("select id from prob_umaru where id='{$_SESSION[los_id]}'"));`
    - `if(!$chk[id]) mysql_query("insert into prob_umaru values('{$_SESSION[los_id]}','{$new_flag}')");`
    - `else mysql_query("update prob_umaru set flag='{$new_flag}' where id='{$_SESSION[los_id]}'");`
		+ 기존에 생성한 `flag` 존재 여부를 확인한다.
		+ 만약 이전에 생성했다면, 새로운 플래그로 갱신하는 쿼리를 보낸다.
		+ 만약 생성한 적이 없다면, 새로운 플래그를 삽입하는 쿼리를 보낸다.
	- `echo "reset ok";`
		+ `reset ok`를 출력한다.

## Trial and error
* `function reset_flag()`에서 `flag`의 길이를 유추할 수 있다.
	- `$new_flag = substr(md5(rand(10000000,99999999)."qwer".rand(10000000,99999999)."asdf".rand(10000000,99999999)),8,16);`
	- `16`글자.
* `@mysql_query("update prob_umaru_temp set flag={$_GET[flag]}");`
	- SQLi를 시도할 수 있다.
	- 쿼리가 실행되면 알아야 하는 flag가 갱신되어버린다.
	- 쿼리 실행을 지연하거나 안되게 하는 방법을 생각해내야 한다.
	- **`sleep()`과 의도적 오류를 이용한다**.
* `?flag=0`일 때 그냥 소스가 떴던 것은 `if(!$_GET[flag]){ highlight_file(__FILE__); exit; }` 때문이다...

## Solution
* [`umaru_blind_sqli_brute_force.py`](./umaru_blind_sqli_brute_force.py)
	- **Time-based Blind SQLi**.
	- `SELECT 1 UNION SELECT 2`로 의도적인 오류를 일으켜 `reset_flag()` 실행을 막고(`flag` 변경 방지), `sleep()`으로 조건의 참/거짓을 판단한다(응답 시간 계산).
	- `?flag=sleep({t} * (flag like '{s}%'))^(SELECT 1 UNION SELECT 2)`
		+ `(flag like '{s}%')` 조건문을 먼저 검사한다. 만약 참이면 `sleep({t})`이 실행되어 `t`초만큼 시간 지연이 발생하고, 거짓이면 `sleep(0)`이 실행되어 시간 지연이 발생하지 않는다.
		+ `sleep()`의 리턴값과 `(SELECT 1 UNION SELECT 2)`를 `^`로 연산을 시도하지만, 오류를 일으켜 `reset_flag()`가 실행되지 않도록 한다. `^` 이외에 다른 연산자도 가능할 수 있지만, 찾아보진 않았다.
	- `flag`는 PHP의 `md5()`의 결과값에서 나오는데, 숫자(`0`-`9`)와 소문자 알파벳(`a`-`z`)만 나온다. SQLi를 이용해 알아낸 것은 대문자가 나오므로 이를 소문자로 바꿔준다.