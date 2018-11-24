# 1

### First impression
```php
<?
if(!$_COOKIE[user_lv])
{
SetCookie("user_lv","1");
echo("<meta http-equiv=refresh content=0>");
}
?>
<html>
<head>
<title>Challenge 1</title>
</head>
<body bgcolor=black>
<center>
<br><br><br><br><br>
<font color=white>
---------------------<br>
<?

$password="????";

if(eregi("[^0-9,.]",$_COOKIE[user_lv])) $_COOKIE[user_lv]=1;

if($_COOKIE[user_lv]>=6) $_COOKIE[user_lv]=1;

if($_COOKIE[user_lv]>5) @solve();

echo("<br>level : $_COOKIE[user_lv]");

?>
<br>
<pre>
<a onclick=location.href='index.phps'>----- index.phps -----</a>
</body>
</html>
```

### Trial and error
* `if(eregi("[^0-9,.]",$_COOKIE[user_lv])) $_COOKIE[user_lv]=1;`
	- [`eregi()`](http://php.net/manual/en/function.eregi.php) 대소문자를 구분하지 않고 정규표현식에 일치하는 문자열일 때 참을 반환
	- `[^0-9,.]`는 숫자(`0`~`9`), `,`, `.`를 제외한 나머지 문자를 의미한다.
* `if($_COOKIE[user_lv]>=6) $_COOKIE[user_lv]=1;`
	- 정수 `6`보다 크거나 같으면 `1`로 만든다.
* `if($_COOKIE[user_lv]>5) @solve();`
	- 이를 포함한 3개의 조건문을 통과해야 `@solve();`가 실행된다.
* 이를 종합해볼 때, `5 < x <= 6`인 `x`값으로 쿠키값을 변조하면 될 것 같다.
* Chrome의 [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=ko)라는 확장 프로그램을 사용했다. 
* `user_lv` 쿠키를 읽기 전용으로 설정하고 새로고침하니 그냥 풀렸다...
	- 이건 좀 의도하지 않은 답인 것 같다.

### Solution
* 다음과 같은 조건들을 고려해볼 때, `[5, 6)`의 실수를 입력하면 풀린다.
	- 숫자(`0`~`9`), `,`, `.`를 제외한 나머지 문자가 있으면 `1`로 초기화된다. 고로 정수는 물론 **실수**도 된다.
	- `user_lv`은 `[5, 6)`에 포함되는 수이다.