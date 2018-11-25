# 6

### First impression
```
HINT : base64  
index.phps

ID : guest
PW : 123qwe
```

```php
<?php 
if(!$_COOKIE[user]) 
{ 
    $val_id="guest"; 
    $val_pw="123qwe"; 

    for($i=0;$i<20;$i++) 
    { 
        $val_id=base64_encode($val_id); 
        $val_pw=base64_encode($val_pw); 

    } 

    $val_id=str_replace("1","!",$val_id); 
    $val_id=str_replace("2","@",$val_id); 
    $val_id=str_replace("3","$",$val_id); 
    $val_id=str_replace("4","^",$val_id); 
    $val_id=str_replace("5","&",$val_id); 
    $val_id=str_replace("6","*",$val_id); 
    $val_id=str_replace("7","(",$val_id); 
    $val_id=str_replace("8",")",$val_id); 

    $val_pw=str_replace("1","!",$val_pw); 
    $val_pw=str_replace("2","@",$val_pw); 
    $val_pw=str_replace("3","$",$val_pw); 
    $val_pw=str_replace("4","^",$val_pw); 
    $val_pw=str_replace("5","&",$val_pw); 
    $val_pw=str_replace("6","*",$val_pw); 
    $val_pw=str_replace("7","(",$val_pw); 
    $val_pw=str_replace("8",")",$val_pw); 

    Setcookie("user",$val_id); 
    Setcookie("password",$val_pw); 

    echo("<meta http-equiv=refresh content=0>"); 
} 
?> 

<html> 
<head> 
<title>Challenge 6</title> 
<style type="text/css"> 
body { background:black; color:white; font-size:10pt; } 
</style> 
</head> 
<body> 

<? 

$decode_id=$_COOKIE[user]; 
$decode_pw=$_COOKIE[password]; 

$decode_id=str_replace("!","1",$decode_id); 
$decode_id=str_replace("@","2",$decode_id); 
$decode_id=str_replace("$","3",$decode_id); 
$decode_id=str_replace("^","4",$decode_id); 
$decode_id=str_replace("&","5",$decode_id); 
$decode_id=str_replace("*","6",$decode_id); 
$decode_id=str_replace("(","7",$decode_id); 
$decode_id=str_replace(")","8",$decode_id); 

$decode_pw=str_replace("!","1",$decode_pw); 
$decode_pw=str_replace("@","2",$decode_pw); 
$decode_pw=str_replace("$","3",$decode_pw); 
$decode_pw=str_replace("^","4",$decode_pw); 
$decode_pw=str_replace("&","5",$decode_pw); 
$decode_pw=str_replace("*","6",$decode_pw); 
$decode_pw=str_replace("(","7",$decode_pw); 
$decode_pw=str_replace(")","8",$decode_pw); 


for($i=0;$i<20;$i++) 
{ 
    $decode_id=base64_decode($decode_id); 
    $decode_pw=base64_decode($decode_pw); 
} 

echo("<font style=background:silver;color:black>&nbsp;&nbsp;HINT : base64&nbsp;&nbsp;</font><hr><a href=index.phps style=color:yellow;>index.phps</a><br><br>"); 
echo("ID : $decode_id<br>PW : $decode_pw<hr>"); 

if($decode_id=="admin" && $decode_pw=="admin") 
{ 
    @solve(6,100); 
} 


?> 

</body> 
</html> 
```

### Trial and error
* 쿠키에 `user`가 없으면, 다음과 같은 절차를 수행한다.
	- `guest`, `123qwe`를 각각 base64로 20번 인코딩 한다.
	- `1` -> `!`, `2` -> `@`, `3` -> `$`, `4` -> `^`, `5` -> `&`, `6` -> `*`, `7` -> `(`, `8` -> `)` 로 교체한다.
	- 이를 각각 쿠키의 `user`, `password`에 저장한다.
* 위 과정을 역으로 수행했을 때 나오는 `user`와 `password`가 `admin`이어야 통과한다.

### Solution
* [generate.py](./generate.py)로 인코딩 값을 생성한다.
* 이를 쿠키의 `user`, `password`의 값으로 설정한다.
* 통과한다.