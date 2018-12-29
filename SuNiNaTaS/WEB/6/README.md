# 6

## Problem
* 3번째 글 README를 열어보면 다음과 같은 패스워드 입력창이 뜬다.

```
|___________________| |확인|

"select szPwd from T_Web13 where
  nIdx = '3' and szPwd = '"&pwd&"'"
```

## Inspection
* 해당 폼의 `passwd`가 POST로 전송된다는 것을 알 수 있다.
* `select szPwd from T_Web13 where nIdx = '3' and szPwd = '"&pwd&"'`
    + 폼의 `passwd`가 쿼리문에서 `pwd`라는 것을 알 수 있다.
    + SQLi를 시도할 수 있다.
* `%`, `and`, `=`, `  `(space) 등이 걸러진다.

## Solution
* `'/**/or/**/'1'<'2`
    + 논리연산자의 우선순위(`and`가 `or`보다 우선적)를 이용하여 조건을 참으로 만든다.
    + 띄어쓰기를 `/**/`로 우회한다.
    + `=`를 `<`로 우회한다.