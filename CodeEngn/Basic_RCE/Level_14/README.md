# Basic RCE Level 14

## Problem
* Korean : 
	- Name이 `CodeEngn` 일때 Serial을 구하시오 
	- (이 문제는 정답이 여러개 나올 수 있는 문제이며 5개의 숫자로 되어있는 정답을 찾아야함, bruteforce 필요) 
	- Ex) 11111 
* English : 
	- Find the Serial when the Name of `CodeEngn` 
	- (This problem has several answers, and the answer should be a 5 digit number. Brute forcing is required.) 
	- Ex) 11111 

## Tool
* ExeinfoPe
* CFF Explorer
* x32dbg
* IDA

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보니 UPX로 패킹된 것을 알 수 있다.

![](./2.PNG?raw=true)
* CFF Explorer를 이용하여 언패킹하고 이를 `14.unpacked.exe`로 저장한다.

![](./3.PNG?raw=true)
* x32dbg에서 `14.unpacked.exe`를 열어 Serial 생성 및 확인 코드를 그래프로 그려보았다.
* Name을 활용하여 생성한 Serial(정수값)을 입력받은 Serial(문자열)을 10진수의 정수로 변환한 값과 비교한다. 같으면 통과.
	- `14.unpacked.401383`은 정수 형태의 문자열을 10진수 정수값으로 변환하는 함수이다.

![](./4.PNG?raw=true)
* `ESI`에 `129A1`이라는 Serial 값이 저장되어있다.
* 이를 10진수로 변환한 값이 곧 Serial이다.

## ...
* 왜 정답이 여러개 나올 수 있는 문제이고 brute force가 필요한지 궁금하다.
* 좀더 알아볼 필요가 있는 문제이다.