# Basic RCE Level 03

## Problem
* Korean : 
비주얼베이직에서 스트링 비교함수 이름은? 
* English : 
What is the name of the Visual Basic function that compares two strings?

## Tool
* PEView
* x32dbg

## Explanation
![](./1.PNG?raw=true)  
* 독일어로 작성된 것 같다. 실행 시 모습은 다음과 같이 등록 코드를 입력하는 다이얼로그가 뜬다.

![](./2.PNG?raw=true)  
* 이를 PEView로 열어본 결과 `SECTION .idata`에 `__vbaStrCmp`를 쓴다는 것을 알 수 있다.
* 해당 프로그램은 Visual Basic으로 작성한 것을 알 수 있다.
* 해당 섹션이 남아있는 것을 보니 디버그가 가능하도록 컴파일한 것 같다.

![](./3.PNG?raw=true)  
* x32dbg에서 모든 문자열 호출을 살펴보니 등록 코드로 추측되는 문자열과, 일치/불일치 시 나타나는 독일말들(Danke! / Error!)이 나타났다.

![](./4.PNG?raw=true)  
* x32dbg에서 모든 함수 호출을 살펴보니 `__vbaStrCmp`가 있어서 해당 함수가 호출되는 곳을 모두 Breakpoint로 잡았다.

![](./5.PNG?raw=true)  
* 다음과 같이 `___vbaStrCmp`의 인자로 등록 코드로 추측되는 문자열을 넣는 것으로 보아 등록 코드가 거의 확실하다는 것을 알 수 있다.

![](./6.PNG?raw=true)
* 등록 코드로 추측되는 문자열을 입력한 결과 통과하는 것을 알 수 있다.