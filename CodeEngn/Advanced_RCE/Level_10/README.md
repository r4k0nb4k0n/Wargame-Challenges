# Advanced RCE Level 10

## Problem
* Serial이 `WWWCCCJJJRRR` 일때 Name은 무엇인가 
* Hint 1 : 4글자임 
* Hint 2 : 정답으로 나올 수 있는 문자열 중 (0~9, a~z, A~Z) 순서상 가장 먼저 오는 문자열 

## Tool
* ExeinfoPe
* IDA *** 7.0
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* C++, Win Console 임을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* 함수 유추하기엔 개수가 많아 IDA의 힘을 빌렸다.
* IDA에서 생성한 파일을 x32dbg의 SwissArmyKnife플러그인으로 먹여주니 함수 이름이 제대로 나타났다.
* 사실 IDA가 익숙하지 않다...
* 다음은 `main`의 call graph이다.
* Name은 4글자 이상, Key는 12글자이어야 한다.
* 입력을 다 받고 조건을 통과하면 `check_serial`에게 파라미터로 넘겨주고, 나오는 결과에 통과 여부가 갈린다.

![](./3.PNG?raw=true)
* 다음은 `check_serial`의 call graph이다.
* 해당 함수를 아래 코드에서 C++로 나타냈다.

![](./4.PNG?raw=true)
* [namegen.cpp](./namegen.cpp)
* `check_serial` 함수에서 자료형을 잘 통일해줘야 결과가 올바로 나타난다.
* 재귀 함수를 이용하여 모든 경우의 수를 검사해보았다.

![](./5.PNG?raw=true)
* 다음과 같이 통과하는 것을 알 수 있다.