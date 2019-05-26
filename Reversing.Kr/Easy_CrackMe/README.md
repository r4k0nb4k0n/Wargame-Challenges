# Easy Crack

## Problem
* [Easy_CrackMe.exe](./Easy_CrackMe.exe)

## Tool
* ExeinfoPe
* PEiD
* PEStudio
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe와 PEiD로 해당 PE 파일을 열어보았다.
* 다음과 같이 해당 PE 파일의 특징을 알 수 있다.
	- Win32
	- GUI
	- Visual Studio 5.0-6.0

![](./2.PNG?raw=true)
* PEStudio와 x32dbg에서 해당 PE 파일을 열고, 문자열 참조를 살펴보았다.
* `Congratulation !!`이 Flag 통과 시 나타나는 문자열이라고 유추할 수 있다.

![](./3.PNG?raw=true)
* x32dbg에서 `Congratulation !!`을 참조하는 곳의 call graph를 그려보았다.
* 다음과 같은 규칙을 만족하면 `Congratulation !!`을 띄운다.
	- 2번째 글자는 `a`이어야 한다.
	- 3, 4번째 글자는 `5y`이어야 한다.
	- 그 이후 문자열은 `R3versing`이어야 한다.
	- 1번째 글자는 `E`이어야 한다.

![](./4.PNG?raw=true)
* 통과하는 것을 볼 수 있다.
