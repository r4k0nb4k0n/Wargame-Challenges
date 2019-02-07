# Advanced RCE Level 03

## Problem
Name이 CodeEngn 일때 Serial은 무엇인가 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* Windows GUI임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* 다음은 `Main`(추정) 함수의 call graph이다.
* `Check` 버튼을 눌렀을 때,
	+ 입력한 `Name`을 읽어온다.
	+ `GenKey` 함수에서 입력받은 `Name`을 이용하여 `Key`를 만든다.
	+ unsigned integer 형식인 `%u` 로 `Key`를 출력한 것을 문자열로 저장한다.
	+ 입력한 `Serial`을 읽어온다.
	+ 입력받은 `Serial`과 문자열로 저장된 `%u` 형식으로 출력한 `Key`를 비교한다. `lstrcmpA`
	+ 비교 결과값을 비교 결과값으로 나눈다. `idiv eax`
		- `1`이라면 정상적으로 처리가 되어 밑의 통과 못함 메시지 출력을 처리한다.
		- `0`이라면 `divide by zero` 예외가 발생하여 통과 메시지 출력을 처리한다.

![](./3.PNG?raw=true)
* `GenKey` 함수의 call graph를 그려보았다.
* `403000`에 `Key`를 생성한다.
* 재귀함수이다.

![](./4.PNG?raw=true)
* `lstrcmpA`의 인자로 `Key`가 그대로 드러나기 때문에, 쉽게 `Key`를 알아낼 수 있다.

## Reference
* [wsprintfA function | Microsoft Docs](https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-wsprintfa)
* [X86-assembly/Instructions/idiv](https://www.aldeid.com/wiki/X86-assembly/Instructions/idiv)
* [X86-assembly/Instructions/cdq](https://www.aldeid.com/wiki/X86-assembly/Instructions/cdq)