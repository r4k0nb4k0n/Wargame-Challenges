# Advanced RCE Level 09

## Problem
Password는 무엇인가 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* Win Console, C++ 임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 분석해보았다.
* `&main`(추정) 함수의 call graph를 그려보았다.
* 다음과 같이 동작한다.
	+ 25개의 `UINT` 공간을 `88228F`로 초기화한다.
	+ `"Welcome to this software ..."` 문자열을 출력한다. `cout`
	+ `"Username:"`을 출력하고 `string`을 입력받는다.
	+ `"Password:"`을 출력하고 `integer`를 입력받는다.
	+ `&verify`(가칭) 함수에서 판단한다.
	+ 종료한다.

![](./3.PNG?raw=true)
* `&verify`(가칭) 함수의 call graph를 그려보았다.
* 분석 내용은 다음과 같다.
	+ 입력한 `Username`과 `0x0000..`을 비교한다.
	+ 입력한 `Password`와 `0x88228F`을 비교한다.
	+ `Username`이 `0x00..`이고, `Password`가 `0x88228F`이어야 통과한다.
	+ `Username`을 `DonaldDuck`과 비교하는 것은 훼이크다.

![](./4.PNG?raw=true)
* `Username`에 NULL 문자를 입력하면 `Password` 입력을 할 수 없다. 그대로 씹혀버린다.
* 따라서 `Username`에 아무 문자를 입력하고, `Password`에 정확한 숫자를 입력한 다음, 디버거에서 이를 `0x00..`으로 수정하여 통과할 수 있다.
* 또는 코드 패치를 통해 `Username`이 `DonaldDuck`일 때 통과할 수 있도록 바꿀 수 있다.

![](./5.PNG?raw=true)
* 디버거에서 직접 수정했을 때 다음과 같이 통과한다.