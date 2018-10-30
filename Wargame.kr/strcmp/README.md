# strcmp
### First impressions
```
if you can bypass the strcmp function, you get the flag.
```
`strcmp` 함수를 우회할 수 있다면, flag를 얻는다.   
```php
if (strcmp($_POST['password'], $password) == 0) {
    echo "Congratulations! Flag is <b>" . auth_code("strcmp") ."</b>";
    exit();
} else {
    echo "Wrong password..";
}
```
### Trial and error
* [PHP `strcmp()` vulnerability](https://hydrasky.com/network-security/php-string-comparison-vulnerabilities/)
* Loose comparison인 `==`을 사용하면 둘 중 하나가 `NULL`이면 `TRUE`을 반환한다.
* 문제는 `$_POST['password']`를 어떻게 `NULL`로 만드냐는 거다.
* `requests` 모듈에서 `data={'password':None}`으로 하여 post 해봤지만 반응이 없었다...

### Solution
* DevTools에서 input의 name 속성을 `password[]`로 바꾼다.
* 이는 php에서 `null`로 계산되어 `strcmp()`를 우회한다.
* Flag 값이 뜬다.