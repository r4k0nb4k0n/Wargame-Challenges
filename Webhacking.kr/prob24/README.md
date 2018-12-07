# 24

### First impression
```
client ip	**********
agent	Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36
Wrong IP!
```

```php
extract($_SERVER);
extract($_COOKIE);

if(!$REMOTE_ADDR) $REMOTE_ADDR=$_SERVER[REMOTE_ADDR];

$ip=$REMOTE_ADDR;
$agent=$HTTP_USER_AGENT;


if($_COOKIE[REMOTE_ADDR])
{
$ip=str_replace("12","",$ip);
$ip=str_replace("7.","",$ip);
$ip=str_replace("0.","",$ip);
}

echo("<table border=1><tr><td>client ip</td><td>$ip</td></tr><tr><td>agent</td><td>$agent</td></tr></table>");

if($ip=="127.0.0.1")
{
@solve();
}

else
{
echo("<p><hr><center>Wrong IP!</center><hr>");
}
```

### Trial and error
* 쿠키값으로 `REMOTE_ADDR`을 보낸 것이 `127.0.0.1`과 같으면 통과한다.
* 하지만 중간에 `str_replace()`가 방해한다.
* 이를 우회하는 방법을 찾아야 한다.

### Solution
* `$ip=str_replace("12","",$ip);`는 `1122`을 입력하면 `12`가 나와서 우회할 수 있다.
* [fxxx_da_ip.py](./fuck_da_ip.py)