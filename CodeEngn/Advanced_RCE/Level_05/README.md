# Advanced RCE Level 05

## Problem
Serial 을 구하시오 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE파일을 열어보았다.
* Visual Basic, Windows GUi임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE파일을 열어보았다.
* Serial 관련 함수의 call graph를 그려보았다.
	+ 하늘색 사각형
		+ Serial 생성.
	+ 빨간색 사각형
		+ 생성된 Serial과 입력받은 Serial 비교 및 다를 시 점프.
	+ 주황색 사각형
		+ 생성된 Serial과 입력받은 Serial이 같을 시, `Bien!` 창 띄워줌. 스페인어로 좋아요.
* `&__vbaStrCmp` 함수의 인자로 들어가는 문자열에 그대로 Serial이 드러난다.

![](./3.PNG?raw=true)
* 드러난 Serial을 입력해보니 다음과 같이 통과 창이 뜬다.