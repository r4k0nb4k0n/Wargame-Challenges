# 25

### First impression
```
합계 12
-rw-r--r-- 1 oldzombie users   12  5월 14 00:57 hello.txt
-rw-r--r-- 1 oldzombie users 1158  9월  5 01:24 index.php
-rw-r--r-- 1 oldzombie users   57  5월 14 00:57 password.php

hello world

```
```
http://webhacking.kr/challenge/bonus/bonus-5/?file=hello
```

### Trial and error
* `http://webhacking.kr/challenge/bonus/bonus-5/`로 접속해도 `?file=hello`라는 파라미터가 계속 따라붙는다.
* `http://webhacking.kr/challenge/bonus/bonus-5/password.php`로 접속하면 빈 화면만 뜬다.
```
<html><head></head><body></body></html>
```
* `합계 12`인데 뜨는 파일은 3개인 것을 봐서는 더 있는데 안보여주는 것 같다.
* 분명 `?file=` 파라미터로 넘겨서 원하는 파일을 보는 것이라고 생각하는데, 계속 `hello.txt`만 보여준다.
* `?file=hello`를 넘겼을 때 `hello.txt`를 출력하는 것을 보아, 자동으로 `.txt`를 붙여주는 것 같다.
* `?file=password.php%00`로 끝에 `NULL`을 먹이면, 뒤에 `.txt`는 무시할 것이다.

### Solution
* `?file=password.php%00`