# Basic RCE 08

## Problem
* Korean : OEP를 구하시오
	- Ex) 00400000
* English : Find the OEP
	- Ex) 00400000 

## Tool
* ExeinfoPe
* CFF Explorer

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe에서 열어보니 UPX로 패킹되어있다.

![](./2.PNG?raw=true)
* CFF Explorer에서 열어서 언패킹한 후 따로 저장한다.

![](./3.PNG?raw=true)
* 언패킹한 PE 파일을 ExeinfoPe에서 열어봤다.
* OEP는 `00012475`임을 알 수 있다.
* C++로 작성된 것을 알 수 있다.