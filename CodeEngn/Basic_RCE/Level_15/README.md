# Basic RCE Level 15

## Problem
* Name이 CodeEngn일때 Serial을 구하시오

## Tool
* ExeinfoPe
* x32dbg
* IDA - HexRay

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보니 Delphi로 만들어진 것을 확인할 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 열어서 어느 문자열들이 호출되었는지 확인해보니, Serial 통과/미통과 시 나타나는 문자열들이 보인다.
* 해당 문자열들이 호출되는 위치로 디스어셈블러에서 따라가본다.

![](./3.PNG?raw=true)
* 해당 문자열들이 호출되고, Name에 따른 Serial 인증 확인 함수의 call graph를 그려보았다.
* `407774` 함수 호출 이후의 `EAX`와 `*45B844`이 같아야 통과한다.
* 이는 `45B844`에 Name에 따른 Serial이 저장된다는 것을 알 수 있다.

![](./4.PNG?raw=true)
* `45B844`를 주시해보니, `458760` 함수를 실행한 이후에 값이 변경되는 것을 확인할 수 있다.
* `458760` 함수가 Name에 따른 Serial를 만든다는 것을 알 수 있다.

![](./5.PNG?raw=true)
* `458760` 함수의 call graph를 그려보았다.

![](./6.PNG?raw=true)
* `458760` 함수의 내용을 pseudo code로 작성해보았다. (with IDA-HexRay)
* Serial은 다음과 같이 생성된다.
	- `(Name의 각 글자의 ascii code 값) * 8`을 모두 더한다.
	- 위 값에 `(Name의 문자열 길이) * 8`을 더한다.
	- 위 값에 `4`를 곱한다.

![](./7.PNG?raw=true)
* `407774` 함수는 입력받은 Serial의 문자열을 그대로 10진수로 인식하고 정수값으로 변환한다.
* 생성된 Serial의 16진수 표현은 `6160`이다.
* 이의 10진수 표현을 입력하면 통과한다.
