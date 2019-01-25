# Basic RCE 13

## Problem
* Korean : 정답은 무엇인가 
* English : Find the answer 

## Tool
* ExeinfoPe
* dnSpy

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보니 C#으로 작성된 것을 알 수 있다.

![](./2.PNG?raw=true)
* dnSpy로 열어보니 `Main` 함수의 내용이 나타난다.
* `cipherText`를 `RijndaelSimple.Decrypt`로 처리한 결과를 `text`에 저장한 후, 입력값과 비교하는데 같으면 통과한다.

![](./3.PNG?raw=true)
* 입력값을 받기 전에 중단점을 설정한 후, 디버깅을 시작한다.
* 지역 변수에서 `text`의 내용을 볼 수 있다.