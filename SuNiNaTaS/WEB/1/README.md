# 1

## Problem
```asp
<%
    str = Request("str")

    If not str = "" Then
        result = Replace(str,"a","aad")
        result = Replace(result,"i","in")
        result1 = Mid(result,2,2)
        result2 = Mid(result,4,6)
        result = result1 & result2
        Response.write result
        If result = "admin" Then
            pw = "????????"
        End if
    End if
%>
```

## Inspection
* 언어는 [ASP](https://en.wikipedia.org/wiki/Active_Server_Pages)일 것이다.
* `GET` 파라미터 `str`를 받는다.
* `str`에서 `a`를 `aad`로 바꾼 문자열을 `result`에 넣는다.
* `result`에서 `i`를 `in`으로 바꾼다.
* `result1`에 `result`의 `2`번째 글자부터 `2`개 글자들을 넣는다.
* `result2`에 `result`의 `4`번째 글자부터 `6`개 글자들을 넣는다.
* `result`에 `result1`과 `result2`를 이어붙인 문자열을 넣는다.
* `result`가 `admin`이면 플래그를 받는다.

## Solution
* `ami`
	- `result = Replace(str,"a","aad")`
		+ `result = aadmi`
	- `result = Replace(result,"i","in")`
		+ `result = aadmin`
	- `result1 = Mid(result,2,2)`
		+ `result1 = ad`
	- `result2 = Mid(result,4,6)`
		+ `result2 = min`
	- `result = result1 & result2`
		+ `result = "admin"`
