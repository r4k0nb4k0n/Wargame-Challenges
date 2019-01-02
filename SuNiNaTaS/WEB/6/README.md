# 6

## Inspect and Solve...
* SkyHacker가 쓴 1번째 글 Hint를 열어보면 `Reading suninatas's Writing!^^`이라고 써있다.
* suninatas가 쓴 3번째 글 README를 열어보면 다음과 같은 패스워드 입력창이 뜬다.

```
|___________________| |확인|

"select szPwd from T_Web13 where
  nIdx = '3' and szPwd = '"&pwd&"'"
```

* 해당 폼의 `passwd`가 POST로 전송된다는 것을 알 수 있다.
* `select szPwd from T_Web13 where nIdx = '3' and szPwd = '"&pwd&"'`
    + 폼의 `passwd`가 쿼리문에서 `pwd`라는 것을 알 수 있다.
    + SQLi를 시도할 수 있다.
    + `%`, `and`, `=`, `  `(space) 등이 걸러진다.
* `'/**/or/**/'1'<'2`로 우회한다.
    + 논리연산자의 우선순위(`and`가 `or`보다 우선적)를 이용하여 조건을 참으로 만든다.
    + 띄어쓰기를 `/**/`로 우회한다.
    + `=`를 `<`로 우회한다.
* 통과 후 다음과 같은 확인창이 뜬다.

```
Congratulation!!
auth_key is suninatastopofworld!

Now, you can read this article.
```

* 확인을 누르면, 이후 `http://suninatas.com/Part_one/web06/view.asp?idx=3&num=3&passcode=wkdrnlwnd`로 리다이렉트하지만, `접근권한이 없습니다!`라는 창이 뜬다.
* 쿠키에 다음 값이 있다.
    - `auth%5Fkey` : `%3F%3F%3F%3F%3F`
    - URL Decode 하면 `?????`이다.

* Manager가 쓴 2번째 글 reference!를 열어보면 다음과 같은 힌트가 있다.
    - `https://md5hashing.net/`
* 쿠키의 `auth%5Fkey`에 `suninatastopofworld!`를 `MD5()`로 해싱한 값을 넣으면 통과한다.

* 제목 KeyFinding / 내용 KeyFinding^^
* 소스를 보면 `<form method="post" name="KEY_HINT" action="Rome's First Emperor"></form>`이 있다.
* 아우구스투스.
