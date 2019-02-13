# Advanced RCE Level 08

## Problem
* Key 값이 `5D88-53B4-52A87D27-1D0D-5B09` 일때 Name은 무엇인가 
* 힌트 : Name은 두자리인데.. 알파벳일수도 있고 숫자일수도 있고.. 
* 정답인증은 Name의 MD5 해쉬값(대문자) 

## Tool
* ExeinfoPe
* x32dbg

## Solution
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다. 
* Win32 GUI, Delphi임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* 성공/실패 내용의 문자열을 찾아보았다.
* `Congratulation!` 문자열이 있는 곳으로 디스어셈블러에서 따라간다.

![](./3.PNG?raw=true)
* `Check it!` 버튼을 눌렀을 때 실행되는 코드들을 call graph로 그려보았다.
* 유추 가능한 함수의 이름을 달았다.
* 의미가 유추 가능한 명렁에 주석을 달았다.
* `08.&GenerateSerial` 함수에서 Name을 유추할 수 있을 것이다.

![](./4.PNG?raw=true)
* `08.&GenerateSerial`을 call graph로 그려보았다.
* 4개의 루프, 1개의 함수에서 5개의 토큰 시드값을 만들어낸다.
* 토큰 시드값에서 앞 4자리 또는 8자리 Hex값을 가져와 토큰을 만들고, 이를 합쳐 Serial을 생성한다.

![](./5.PNG?raw=true)
* [`first_token_brute_force.cpp`](./first_token_brute_force.cpp)
* 길이가 2인 알파벳과 숫자 조합의 문자열을 생성하여 브루트 포싱한다.

![](./6.PNG?raw=true)
* 통과함을 알 수 있다.

## Review
* [Basic RCE Level 17](../Basic_RCE/Level_17)과 비슷하나, 알아내야 할 문자열의 길이가 다르다.