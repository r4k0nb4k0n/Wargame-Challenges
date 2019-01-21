# Basic RCE Level 06

## Problem
* Korean : 
Unpack을 한 후 Serial을 찾으시오. 정답인증은 OEP + Serial 
	- Ex) 00400000PASSWORD 
* English : 
Unpack, and find the serial. The solution should be in this format : OEP + Serial 
	- Ex) 00400000PASSWORD 

## Background Knowledge
* OEP
	- Original Entry Point

## Tool
* ExeinfoPe
* CFF Explorer
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보니 UPX로 패킹된 것을 알 수 있다.

![](./2.PNG?raw=true)
* CFF Explorer에서 이를 언패킹하고 `06.unpacked.exe`로 저장한다.

![](./3.PNG?raw=true)
* 언패킹된 PE파일을 ExeinfoPe로 열어보니 C++로 만들어진 것을 알 수 있다.

![](./4.PNG?raw=true)
* x32dbg에서 F9로 실행을 해보니 EntryPoint가 나타난다.
* 언패킹한 PE 파일에서의 Entry Point이므로 Original Entry Point, OEP가 맞다.
* `00401360`

![](./5.PNG?raw=true)
* x32dbg에서 모든 문자열 참조를 탐색했다.
* Serial로 매우 의심가는 문자열이 보인다.
* Serial이 맞았을 때와 틀렸을 때 보이는 문자열도 보인다.

![](./6.PNG?raw=true)
* 해당 문자열이 참조되는 함수의 그래프이다.
* 해당 문자열과 일치해야 통과한다.
* `AD46DFS547`