# Basic RCE Level 19

## Problem
이 프로그램은 몇 밀리세컨드 후에 종료 되는가 

## Tool
* ExeinfoPe
* PEiD
* Exe2Aut

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 해당 PE파일을 열어보았다.
* AutoIt 스크립트라는 분석 결과가 보인다.

![](./2.PNG?raw=true)
* Exe2Aut로 해당 PE파일을 열어보았다.
* `MsgBox(0, "CodeEngn Reversing L19", "CodeEngn.com by Lee Kang-Seok", 11.12)`
	- [Function MsgBox](https://www.autoitscript.com/autoit3/docs/functions/MsgBox.htm)
	- `MsgBox ( flag, "title", "text" [, timeout = 0 [, hwnd]] )`
	- 11.12초 이후에 종료된다.
* `1 s`는 `1000 ms`이므로,  `11.12 s`는 `11120 ms`이다.