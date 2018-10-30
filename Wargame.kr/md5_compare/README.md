# md5_compare
### First impressions
```
JUST COMPARE ONLY.

with the other value :D
```

```php
$chk = true;
$v1 = $_GET['v1'];
$v2 = $_GET['v2'];

if (!ctype_alpha($v1)) {$chk = false;}
if (!is_numeric($v2) ) {$chk = false;}
if (md5($v1) != md5($v2)) {$chk = false;}
```

### Trial and error
* `$v1`은 알파벳, `$v2`는 숫자여야 한다.
* `md5($v1)`과 `md5($v2)`의 값이 같아야 한다.
* [magic hash](https://www.whitehatsec.com/blog/magic-hashes/)
* `0e`로 시작하는 md5 값은 숫자로 보면 0이다. 이는 0에 거듭제곱을 하는 거나 다름 없다.
* 따라서 의도적으로 `0e`로 시작하는 값이 나오도록 하는 Magic Number/String을 입력한다.
* [Why `md5('240610708')` is equal to `md5('QNKCDZO')?`](https://stackoverflow.com/questions/22140204/why-md5240610708-is-equal-to-md5qnkcdzo)

### Solution
* VALUE 1에 `QNKCDZO`, VALUE 2에 `240610708`을 입력 후 전송한다.
* FLAG 값이 나타난다.