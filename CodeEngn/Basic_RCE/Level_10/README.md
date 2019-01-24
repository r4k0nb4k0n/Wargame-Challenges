# Basic RCE Level 10

## Problem
* Korean : OEP를 구한 후 "등록성공"으로 가는 분기점의 OPCODE를 구하시오. 정답인증은 OEP + OPCODE 
	- EX) `00400000EB03` 
* English : After finding the OEP, find the OPCODE of the branch instruction going to the "goodboy routine" The solution should be in this format : OEP + Serial 
	- EX) `00400000EB03`

## Tool
* ExeinfoPe
* AspackDie
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보니 Aspack로 패킹되었다는 것을 알 수 있다.

![](./2.PNG?raw=true)
* AspackDie로 언패킹한다. `unpacked.ExE`로 추출된다.

![](./3.PNG?raw=true)
* x32dbg로 언패킹한 PE 파일을 연다.
* OEP를 찾을 수 있다. `00445834`
* 현재 구역에서 문자열 호출을 찾아보니 `Registered... well done!`이라는 게 보인다.
* 등록 성공과 관련된 문자열이다.

![](./4.PNG?raw=true)
* 프로그램 GUI가 뜨고 난 후 `Registered... well done!` 문자열 호출을 찾아보았다.
* 여기로 가는 분기점의 OPCODE를 구한다. `75 55`