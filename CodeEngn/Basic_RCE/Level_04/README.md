# Basic RCE Level 04

## Problem
* Korean : 
이 프로그램은 디버거 프로그램을 탐지하는 기능을 갖고 있다. 디버거를 탐지하는 함수의 이름은 무엇인가 
* English : 
This program can detect debuggers. Find out the name of the debugger detecting function the program uses. 

## Tool
* PEView
* Ollydbg

## Explanation
![](./1.PNG?raw=true)
* PEView - SECTION .idata - IMPORT Name Table에 이름부터 의심스러운 `IsDebuggerPresent`라는 함수가 있다.
* [`IsDebuggerPresent` function | MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680345.aspx)
	- 호출된 프로세스가 유저-모드 디버거로 디버깅되는지 확인.
* 문제의 정답은 이 함수다.

![](./2.PNG?raw=true)
* 그냥 실행했을 때는 `정상`이라고 출력한다.

![](./3.PNG?raw=true)
* Ollydbg에서 디버그 모드로 실행할 떄는 `디버깅 당함`이라고 출력한다.

## Additional
* [How do I bypass IsDebuggerPresent with OllyDbg - Stack Overflow](https://stackoverflow.com/questions/10330147/how-do-i-bypass-isdebuggerpresent-with-ollydbg)
	- OllyDbg 상에서 실행 파일 내 `IsDebuggerPresent` 위치로 가서 해당 함수 코드들을 `NOP`로 대체한다. 하지만 이는 완전히 고친 것이 아니라, 그저 해당 함수가 위치한 `kernel32.dll`의 복사본을 수정하는 것이다. 실행 파일에서 해당 함수 호출 부분을 변경/삭제하는 것이 완전하다.
	- PEB.BeingDebugged flag 수정.