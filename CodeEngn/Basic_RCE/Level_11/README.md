# Basic RCE 11

## Problem
* Korean : 
	- OEP를 찾으시오. Ex) `00401000 `
	- Stolenbyte 를 찾으시오. Ex) `FF35CA204000E84D000000`
	- 정답인증은 OEP+ Stolenbyte 
	- Ex ) `00401000FF35CA204000E84D000000`
* English : 
	- Find the OEP. Ex) `00401000`
	- Find the Stolenbyte. Ex) `FF35CA204000E84D000000` 
	- The solution should be in this format : OEP + Serial 

## Tool
* ExeinfoPe
* CFF Explorer
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe에서 열어봤다.
* UPX로 패킹된 것을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg에서 패킹된 PE파일을 열어보았다.
* `pushad`에 Entry Point가 잡혀있다.
* UPX로 패킹된 PE파일에서 Stolen bytes는 주로 `popad` 이후 특정 주소로 점프하기 전에 나타난다.

![](./3.PNG?raw=true)
* 현재 구역에서 `popad`를 찾은 후 디스어셈블러에서 해당 위치로 가본다.
* Stolen bytes가 나타난다.
* `jmp 11.40100C`를 보니 `0x0040100C`에 OEP 이후의 코드들이 있다는 것을 알 수 있다.
* 덤프에서 `40100C` 주변을 보니 `401000`부터 12개의 NOP 코드가 채워져 있는 것을 볼 수 있다.
* Stolen bytes는 총 12 bytes.