# Advanced RCE Level 02

## Problem
정답은 무엇인가 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* C++, CLI 기반으로 작성된 것임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg에서 해당 PE 파일을 열어보았다.
* `main` 함수의 call graph를 그려보았다.
* `scanf` 함수로 password를 입력받고, 계산된 주소에 있는 `ComparePassword` 함수로 이동한다.

![](./3.PNG?raw=true)
* `ComparePassword` 함수의 call graph를 그려보았다.
* `**********`와 비교하는 것을 볼 수 있다.
* 일치하면 `WELL DONE!`이라는 Dialog를 띄우는 것을 알 수 있다.

![](./4.PNG?raw=true)
* 알아낸 password을 입력하면 통과하는 것을 볼 수 있다.