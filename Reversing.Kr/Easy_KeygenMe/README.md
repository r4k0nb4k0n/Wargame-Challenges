# Easy Keygen

## Problem
* [Easy_KeygenMe.zip](./Easy_KeygenMe.zip)
	- Easy Keygen.exe
	- ReadMe.txt
		+ ReversingKr KeygenMe
		+ Find the Name when the Serial is `5B134977135E7D13`

## Tools
* ExeinfoPe
* PEiD
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 해당 PE 파일을 열어보았다.
* PE 파일에 대해 다음과 같은 특징을 알 수 있다.
	- Win32
	- Console
	- Visual Studio 5.0-6.0

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열고, 프로그램의 전반적인 call graph를 그려보았다.
	- Input Name을 입력받는다.
	- Input Name과 `[0x10, 0x20, 0x30]`의 반복을 XOR 연산한 후 이를 16진수로 출력한다. 이는 Input Name으로부터 생성된 Serial이다.
	- Input Serial을 입력받는다.
	- 생성된 Serial과 Input Serial을 비교한다.
		- 일치하면 `Correct!`를 출력한다.
		- 일치하지 않으면 `Wrong`을 출력한다.

![](./3.PNG?raw=true)
* [namegen.py](./namegen.py)
	- Serial을 입력받아서 역으로 Name을 알아낸다.
	- XOR 연산은 특정 비트의 반전이므로, **2회 반복하면 원래대로 돌아온다**.

![](./4.PNG?raw=true)
* 다음과 같이 통과하는 것을 알 수 있다.
