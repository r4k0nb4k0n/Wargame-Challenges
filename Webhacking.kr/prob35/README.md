# 35

## Problem
```php
<?
if($_GET[phone])
{
if(eregi("%|\*|/|=|from|select|x|-|#|\(\(",$_GET[phone])) exit("no hack");

@mysql_query("insert into challenge35_list(id,ip,phone) values('$_SESSION[id]','$_SERVER[REMOTE_ADDR]',$_GET[phone])") or die("query error");
echo("Done<br>");
}

$admin_ck=mysql_fetch_array(mysql_query("select ip from challenge35_list where id='admin' and ip='$_SERVER[REMOTE_ADDR]'"));

if($admin_ck[ip]==$_SERVER[REMOTE_ADDR])
{
@solve();
@mysql_query("delete from challenge35_list");
}
$phone_list=@mysql_query("select * from challenge35_list where ip='$_SERVER[REMOTE_ADDR]'");

echo("<!--");

while($d=@mysql_fetch_array($phone_list))
{
echo("$d[id] - $d[phone]\n");
}

echo("-->");

?>
```

## Inspection
* `if($_GET[phone])`
	- `GET` 파라미터 `phone`의 값을 받았을 때.
	- `if(eregi("%|\*|/|=|from|select|x|-|#|\(\(",$_GET[phone])) exit("no hack");`
		+ `%`, `*`, `/`, `=`, `from`, `select`, `x`, `-`, `#`, `((`를 거른다.
		+ [RegExr](https://regexr.com/)에서는 `/`이 탈출이 잘 안되었다고 뜨는데, 여기서도 문제가 되는지는 잘 모르겠다.
	- `@mysql_query("insert into challenge35_list(id,ip,phone) values('$_SESSION[id]','$_SERVER[REMOTE_ADDR]',$_GET[phone])") or die("query error");`
		+ 레코드 하나를 삽입한다.
		+ `$_GET[phone]` 부분에서 또다른 레코드를 하나 더 삽입할 수 있는 SQLi를 시도할 수 있다.
* `$admin_ck=mysql_fetch_array(mysql_query("select ip from challenge35_list where id='admin' and ip='$_SERVER[REMOTE_ADDR]'"));`
	- `id`가 `admin`이고 `ip`가 접속 IP인 레코드의 `ip`를 불러온다.
* `if($admin_ck[ip]==$_SERVER[REMOTE_ADDR])`
* `@solve();`
* `@mysql_query("delete from challenge35_list");`
	- 쿼리로 불러온 IP와 접속 IP가 동일하면 통과한다.

## Solution
* [`insert_more.py`](./insert_more.py)
	- `1),('admin','xxx.xxx.xxx.xxx',2`
	- `'`를 막는 무언가가 있다.
	- 이를 우회하기 위해 `char()` 함수를 사용한다.