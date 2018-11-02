# pyc decompile
### First impressions
```
bughela.pyc

:D
```
* 제목에서 말하듯 일단 디컴파일해봐야겠다.

### Trial and error
* `uncompyle6` 모듈을 이용하여 디컴파일했다.
* [`bughela.py`](./bughela.py)
```python
def GIVE_ME_FLAG(flag):
    if flag[:43] != 'http://wargame.kr:8080/pyc_decompile/?flag=':
        die()
    flag = flag[43:]
    now = time.localtime(time.time())
    seed = time.strftime('%m/%d/HJEJSH', time.localtime())
    hs = sha512(seed).hexdigest()
    start = now.tm_hour % 3 + 1
    end = start * (now.tm_min % 30 + 10)
    ok = hs[start:end]
    if ok != flag:
        die()
    print 'GOOD!!!'
```
* flag 검사 코드인 것 같다.
* 페이지에서 주어진 서버 시간을 `now`와 `seed`에 대입한다면 올바른 flag를 전송할 수 있을 것이다.

### Solution
* `uncompyle6 bughela.pyc > bughela.py`
* `GIVE_ME_FLAG()`를 참조하여 올바른 flag를 생성하는 코드를 작성한다. [`solution.py`](./solution.py)
* `http://wargame.kr/pyc_decompile/?flag=[올바른 flag]`에 접속하면 FLAG가 나타난다.