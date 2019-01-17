# 25

## Problem
```
LAST NUMBER
3767
DownLoad
```

## Tool
* [jadx](https://github.com/skylot/jadx)

## Inspection and Solution
![](./1.PNG?raw=true)
* 압축을 풀어보니 24번 문제처럼 .jar 파일 내부랑 비슷하길래 jadx를 이용해서 통째로 열어보려니 인식이 잘 안된다.
* 파일명을 자세히 보니 대소문자 구분이라던가 몇 글자를 빼먹어서 일부러 틀리게 만들었다.
* 이를 옳은 형식으로 바꾸고 다시 압축한다음 jadx로 열어보았다.

![](./2.PNG?raw=true)
* 보라색 강조
	- `getContacts()`
		+ `displayName`이 `SuNiNaTaS`일 경우
			- `arg`가 `sb`이면 이를 그대로 리턴.
			- `arg`가 `id`이면 해당 `contactId`를 리턴.
	- `conName`에는 `SuNiNaTaS`가 저장됨.
* 초록색 강조
	- `getTel()`
		+ `getContacts()` 함수가 돌려주는 `contactId`를 이용해서 전화번호를 String 형태로 돌려줌.
	- `conNum`에는 `SuNiNaTaS`의 전화번호가 저장됨.
* 빨간색 강조
	- `http://www.suninatas.com/Part_one/web24/chk_key.asp`에 `id`, `pw`, `Name`, `Number`를 넘긴다.
	- `Name`은 `SuNiNaTaS`.
	- `Number`는 문제에도 나오듯이 LAST NUMBER가 `3767`인 전화번호.

![](./3.PNG?raw=true)
* Chrome 모바일 모드를 이용했다.
* `Number`는 `01012343767`로 마지막 4자리만 문제에서 원하는 것으로 했다.
* 물론 `+82 10 1234 3767`도 된다. (URL Encoding 필수)
* 안드로이드의 연락처에 전화번호가 어떤 형식으로 저장되었을지 잘 생각이 안나서 둘다 해보았다.