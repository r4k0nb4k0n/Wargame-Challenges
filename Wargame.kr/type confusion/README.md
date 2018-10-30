# type confusion
### First impressions
```
Simple Compare Challenge.

hint? you can see the title of this challenge.

 :D
```

```php
if (isset($_POST['json'])) {
     usleep(500000);
     require("../lib.php"); // include for auth_code function.
    $json = json_decode($_POST['json']);
    $key = gen_key();
    if ($json->key == $key) {
        $ret = ["code" => true, "flag" => auth_code("type confusion")];
    } else {
        $ret = ["code" => false];
    }
    die(json_encode($ret));
}
```
### Trial and error
* `$key = gen_key();`는 무작위 문자열로 알아내기 힘들다.
* `$json->key == $key`는 **느슨한 비교**를 사용한다.
* 여기서 `$json->key`가 숫자 `0`이 된다면 해당 조건문은 `TRUE`가 된다.
* `$json = json_decode($_POST['json']);`을 만족하며 `$json->key`가 숫자 `0`이어야 한다.

### Solution
* [solution.py](./solution.py)
* FLAG 값이 나온다.
