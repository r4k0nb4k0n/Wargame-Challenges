# Basic RCE Level 02

## Problem
* Korean : 
패스워드로 인증하는 실행파일이 손상되어 실행이 안되는 문제가 생겼다. 패스워드가 무엇인지 분석하시오 
* English : 
The program that verifies the password got messed up and ceases to execute. Find out what the password is. 

## Tool
* PEView

## Explanation
![](./1.PNG?raw=true)  
* 실행 시 불가하다고 뜬다.
![](./2.PNG?raw=true)  
* PE 파일임을 나타내는 대표적인 시그니처인 `MZ`만 있고 별다른 헤더나 섹션들이 없다. 손상된 것이다.
![](./3.PNG?raw=true)
* 파일을 아스키값으로 읽어보면 사용하는 API 이름들과 정적 할당된 문자열들이 나타난다.
* 여기서 패스워드로 의심되는 문자열을 추측할 수 있다.