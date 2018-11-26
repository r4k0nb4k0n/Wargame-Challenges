# 11

### First impression
```
Wrong


$pat="/[1-3][a-f]{5}_.*999.999.999.999.*\tp\ta\ts\ts/";

if(preg_match($pat,$_GET[val])) { echo("Password is ????"); }
```
* 파라미터 `val`이 저 regex를 통과해야 문제를 맞출 수 있는 것 같다.

### Trial and error
* [https://regexr.com/](https://regexr.com/) 에서 해당 regex를 붙여놓고 이런 저런 문자열들을 검사해봤다.
* 정규표현식을 대충 공부할 수 있었다.
	- `[1-3]` : `1`~`3` 중 한 글자.
	- `[a-f]{5}` : `a`~`f` 중 다섯 글자.
	- `.` : 아무 글자 하나.
	- `.*` : 아무 글자 0개 이상.
	- 글자 그대로 있는 건 정말 그 글자를 그대로 엮어줘야 한다.

### Solution
* 다음 값을 `val` 파라미터로 넘겨준다.
	- `1abcde_AAAaBBBbCCCcDDDd\tp\ta\ts\ts`
	- `AAA`, `BBB`, `CCC`, `DDD` 는 각각 IP의 A, B, C, D클래스 숫자다.
* 이를 스크립트로 작성했다. [go_get_that_password.py](./go_get_that_password.py)