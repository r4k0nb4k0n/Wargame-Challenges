# Basic RCE Level 16

## Problem
Name이 CodeEngn일때 Serial을 구하시오 

## Tool
* ExeinfoPe
* PEiD
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 해당 PE 파일을 확인해보았다.
* 언팩 상태이고, C++로 작성한 것을 알 수 있다.
* Win Console임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 열어보았다.
* Name에 `CodeEngn`을 입력하고, Password에 여러 입력을 넣어보았다. `[A-Za-z0-9]`
* `main` 함수의 call graph를 그려보았다.
	- `Name`을 입력받는다. 
	- `Name`의 문자열 길이를 `x`라고 하자.
	- `(((x+x+x)*4)^3)+23 = first_touch`
	- `Password`를 입력받고, 이를 숫자값으로 변환한다. 이를 `input_password`라고 하자.
	- `first_touch * 0x000ACE80`를 DWORD로 계산한 값이 곧 Name에 따른 Password이다. 이를 `gen_password`라고 하자.
	- `input_password`와 `gen_password`가 같아야 통과한다.