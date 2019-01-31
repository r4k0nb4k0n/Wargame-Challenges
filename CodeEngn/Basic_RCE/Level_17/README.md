# Basic RCE Level 17

## Problem
* Key 값이 `BEDA-2F56-BC4F4368-8A71-870B` 일때 Name은 무엇인가 
* 힌트 : Name은 한자리인데.. 알파벳일수도 있고 숫자일수도 있고.. 
* 정답인증은 Name의 MD5 해쉬값(대문자) 

## Tool
* ExeinfoPe
* PEiD
* x32dbg
* g++

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe와 PEiD로 열어보았다.
* Delphi로 작성된 것을 알 수 있다.
* GUI임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg에서 Key를 생성하는 함수의 call graph를 그려보았다.
* Key값이 `AAAA-BBBB-CCCCCCCC-DDDD-EEEE`일 때
	- `a` 루프에서 생성된 Hex값의 앞 4자리가 `AAAA`이다.
	- `b` 루프에서 생성된 Hex값의 앞 4자리가 `BBBB`이다.
	- `c` 함수에서 생성된 Hex값의 앞 8자리가 `CCCCCCCC`이다.
	- `d` 루프에서 생성된 Hex값의 앞 4자리가 `DDDD`이다.
	- `e` 루프에서 생성된 Hex값의 앞 4자리가 `EEEE`이다.

![](./3.PNG?raw=true)
* [`first_token_brute_force.cpp`](./first_token_brute_force.cpp)
* `a` 루프를 C 코드로 구현한 후, 문제에서 준 조건(한 자리, 알파벳 또는 숫자)을 이용하여 브루트 포스한다.

![](./4.PNG?raw=true)
* 브루트 포스를 통해 찾아낸 Name을 넣고 돌려보면 똑같은 Key가 나타나는 것을 알 수 있다.