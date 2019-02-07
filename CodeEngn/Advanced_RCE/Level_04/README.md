# Advanced RCE Level 04

## Problem
Name이 CodeEngn 일때 Serial은 무엇인가 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* Windows GUI임을 알 수 있다.
* Self Write Code임을 보니, 실행 중 인코딩된 코드를 디코딩할 것이다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* 특정 점프까지 실행해보니, 인코딩된 코드들이 디코딩 된 것을 알 수 있다.

![](./3.PNG?raw=true)
* `Main`(추정) 함수의 call graph를 그려보았다.
* `Test` 버튼을 누르면,
	+ 입력받은 Name과 Serial을 가지고 `&GenAndCheckSerial` 함수를 실행한다.

![](./4.PNG?raw=true)
* `&GenAndCheckSerial` 함수의 call graph를 그려보았다.
* 동작 과정은 다음과 같다.
	- `Name`의 앞 8글자를 이용하여 2개의 Serial token을 생성한다.
	- `LOD-%lu-%lx` 형식으로 2개의 Serial token을 출력하여 Serial을 생성한다.
	- 생성된 Serial과 입력받은 Serial을 비교한다.
		+ 통과하지 못하면 `Invalid Serial` 창을 띄우고, 확인을 누르면 프로그램이 종료된다.
		+ 통과하면 `Valid Serial` 창을 띄운다. 확인을 눌러도 프로그램이 종료되지 않는다.

![](./5.PNG?raw=true)
* `lstrcmp` 함수의 인자로 생성된 Serial이 드러난다.
* 다음과 같이 통과하는 것을 알 수 있다.