# 7

### First impression
* `/index.php?val=1`일 때 다음과 같은 주석이 있다.

```
<!-- admin mode : val=2 -->
<!--

index.phps

-->
```

* `/index.phps` 접속 시 `index.php`의 내용을 알 수 있다.

```php
<html>
<head>
<title>Challenge 7</title>
</head>
<body>
<!--
db에는 val=2가 존재하지 않습니다.

union을 이용하세요
-->
<?
$answer = "????";

$go=$_GET[val];

if(!$go) { echo("<meta http-equiv=refresh content=0;url=index.php?val=1>"); }

$ck=$go;

$ck=str_replace("*","",$ck);
$ck=str_replace("/","",$ck);


echo("<html><head><title>admin page</title></head><body bgcolor='black'><font size=2 color=gray><b><h3>Admin page</h3></b><p>");


if(eregi("--|2|50|\+|substring|from|infor|mation|lv|%20|=|!|<>|sysM|and|or|table|column",$ck)) exit("Access Denied!");

if(eregi(' ',$ck)) { echo('cannot use space'); exit(); }

$rand=rand(1,5);

if($rand==1)
{
$result=@mysql_query("select lv from lv1 where lv=($go)") or die("nice try!");
}

if($rand==2)
{
$result=@mysql_query("select lv from lv1 where lv=(($go))") or die("nice try!");
}

if($rand==3)
{
$result=@mysql_query("select lv from lv1 where lv=((($go)))") or die("nice try!");
}

if($rand==4)
{
$result=@mysql_query("select lv from lv1 where lv=(((($go))))") or die("nice try!");
}

if($rand==5)
{
$result=@mysql_query("select lv from lv1 where lv=((((($go)))))") or die("nice try!");
}

$data=mysql_fetch_array($result);
if(!$data[0]) { echo("query error"); exit(); }
if($data[0]!=1 && $data[0]!=2) { exit(); }


if($data[0]==1)
{
echo("<input type=button style=border:0;bgcolor='gray' value='auth' onclick=
alert('Access_Denied!')><p>");
echo("<!-- admin mode : val=2 -->");
}

if($data[0]==2)
{
echo("<input type=button style=border:0;bgcolor='gray' value='auth' onclick=
alert('Congratulation')><p>");
@solve();
} 




?>

<!--

index.phps

-->



</body>
</html>
```

### Trial and error
* `/index.php?val=1+1` -> `cannot use space`.
	- `eregi()`에서 걸려서 통과 못함.
* `/index.php?val=6/3` -> `query error`.
	- `/`도 `str_replace()`를 통하여 사라지므로 통과 못함.
* [`UNION`](https://zetawiki.com/wiki/SQL_UNION,_UNION_ALL_%EC%97%B0%EC%82%B0%EC%9E%90)
	* 두 SQL 쿼리문의 결과를 합치는 연산자.
* 의도적으로 쿼리 결과에 `2`를 나타내야 한다.
* 기존 작성된 쿼리에 엉뚱한 조건을 넣어 아무런 결과도 뜨지 않게 하고, 여기에 UNION으로 결과가 `2`가 뜨는 쿼리문을 엮어줘야 하는 듯 싶다.
* `/index.php?val=-9)\nUNION\nSELECT\n(6-4`
	- 랜덤 수가 `1`에 걸릴 경우를 생각하여 괄호를 하나만 넣었다.
	- 걸러지는 띄어쓰기 대신 개행문자(`\n`)을 넣었다.
	- 걸러지는 `2` 대신 `6-4`를 넣어 산술 연산 결과로 나타냈다.
* `406 Not Acceptable` 오류가 뜬다...