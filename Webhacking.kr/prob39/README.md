# 39

## Problem
```php
<?

$pw="????";

if($_POST[id])
{
$_POST[id]=str_replace("\\","",$_POST[id]);
$_POST[id]=str_replace("'","''",$_POST[id]);
$_POST[id]=substr($_POST[id],0,15);
$q=mysql_fetch_array(mysql_query("select 'good' from zmail_member where id='$_POST[id]"));

if($q[0]=="good") @solve();

}

?>
```

## Inspection
* `$_POST[id]=str_replace("\\","",$_POST[id]);`
	- `\`를 없앤다.
* `$_POST[id]=str_replace("'","''",$_POST[id]);`
	- `'`를 `''`로 바꾼다.
* `$_POST[id]=substr($_POST[id],0,15);`
	- 길이를 15글자로 줄인다.
	
## Solution
* 가독성을 위해 space를 `+`로 표시한다.
* 길이를 15글자로 줄이는 것을 이용하여 늘어난 single quote 한 개를 없앨 수 있다.
	- `good+++++++++'`(15글자)
	- `good+++++++++''`(16글자)
