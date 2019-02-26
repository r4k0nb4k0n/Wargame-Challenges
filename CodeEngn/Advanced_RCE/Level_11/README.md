# Advanced RCE Level 11

## Problem
* Serial이 `94E7DB1B` 일때 Name은 무엇인가 
* 해당 Serial에 대한 정답이 여러개 나오는 문제이며 Contact로 보내주시면 인증키를 보내드리겠습니다 
* 해당 Serial에 대해서 'Serial accepted' 메시지가 나와야 합니다. 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE파일을 열어보았다.
* Windows GUI임을 알 수 있다.
* 어떤 언어로 작성되었는지는 알 수 없었다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE파일을 열어보았다.
* 모든 문자열들을 탐색하여 의미있는 것을 살펴보았다.
* `"Serial accepted."`이 나타나는 곳으로 가본다.

![](./3.PNG?raw=true)
* 다음은 `main` 함수와 비슷한 함수의 call graph를 그려보았다.
* `About` 버튼을 누르면 `"Pineware_001..."` 문자열이 있는 MessageBox가 뜬다.
* Name과 Serial을 모두 입력하고 `Ok` 버튼을 누르면 `CheckSerial` 함수를 호출한다.

![](./4.PNG?raw=true)
* 다음은 `CheckSerial` 함수의 call graph를 그려보았다.
* `GenerateSerial` 함수를 호출하여 Name으로부터 Serial을 생성한다.
* 이와 입력받은 시리얼을 비교한다.
    + 같으면 `Serial Accepted` MessageBox를 띄운다.
    + 다르면 `Invalid Serial Number` MessageBox를 띄운다.

![](./5.PNG?raw=true)
* 다음은 `GenerateSerial` 함수의 call graph를 그려보았다.
* 다음과 같이 동작한다.
    + Name을 한 글자씩 가져온다.
    + 해당 글자의 아스키 값에 특정 값을 곱한 값을 계속 합한다.
    + 이 합의 값을 특정 값으로 나눈 몫과 나머지를 이용하여 Serial을 생성한다.

![](./6.PNG?raw=true)
* [Namegen.cpp](./Namegen.cpp)
* 위 `GenerateSerial` 함수를 C++로 그대로 재현해보았다.
* 순차적인 Brute-force는 시간이 오래 걸려, 무작위 문자열을 생성하여 대입해보았다.
* 다음과 같이 통과하는 것을 알 수 있다.