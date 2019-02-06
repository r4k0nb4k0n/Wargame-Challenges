# Advanced RCE Level 01

## Problem
* 이 프로그램은 몇 밀리세컨드 후에 종료 되는가 
* 정답인증은 MD5 해쉬값(대문자) 변환 후 인증하시오

## Tool
* ExeinfoPe
* Exe2Aut

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* AutoIt 스크립트로 작성된 것임을 알 수 있다.

![](./2.PNG?raw=true)
* Exe2Aut로 해당 PE 파일을 열어보았다.
* `MsgBox(0, "CodeEngn Reverse2 L01", "CodeEngn.com by Lee Kang-Soek", 13.179)`
	- [Function MsgBox](https://www.autoitscript.com/autoit3/docs/functions/MsgBox.htm)
	- `MsgBox ( flag, "title", "text" [, timeout = 0 [, hwnd]] )`
	- 13.179초 이후에 종료된다.
* `1 s`는 `1000 ms`이므로,  `13.179 s`는 `13179 ms`이다.

![](./3.PNG?raw=true)
* `13179`의 MD5 결과값이다.