# 26

### First impression
```php
if(eregi("admin",$_GET[id])) { echo("<p>no!"); exit(); } 

$_GET[id]=urldecode($_GET[id]); 

if($_GET[id]=="admin") 
{ 
@solve(26,100); 
} 
```

### Trial and error
* `?id=` 파라미터로 `admin`이 있어야 통과한다.
* 그 전에 `urldecode()`로 내용을 수정한다.
* `?id=admin`은 `eregi()`에서 걸러져서 `no!`를 출력한다.
* `admin`을 urlencode하면 `%61%64%6D%69%6E`이다. [Link](https://www.w3schools.com/tags/ref_urlencode.asp)
* 이를 `id` 파라미터로 넘겨준다.

### Solution
* `?id=%61%64%6D%69%6E`
* 브라우저 대신 파이썬 requests로 한다. [`urlencode.py`](./urlencode.py)