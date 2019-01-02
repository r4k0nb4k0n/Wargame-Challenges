# 9

## Problem
http://suninatas.com/Part_one/web09/SuNiNaTaS.zip

## Tool
* CFF Explorer
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* CFF Explorer로 확인한 결과 Delphi로 작성된 프로그램일 확률이 높다.

![](./2.PNG?raw=true)
* 실행해보면 다음과 같이 무언가 입력하여 통과해야하는 것처럼 생겼다.

![](./3.PNG?raw=true)
* x32dbg로 열어서 문자열 호출들을 살펴보니 `"Congratulation!"`이라는 의심 문자열을 발견했다.
* 해당 문자열 호출이 발생하는 곳을 중심으로 그래프를 그려보았다.
* `"913465"`와 입력 문자열을 비교하는 것을 알 수 있다.

![](./4.PNG?raw=true)
* `913465`를 입력하고 클릭 버튼을 누르면 축하한다는 안내가 뜬다.
* 이후 확인 버튼을 누르면 프로그램이 종료된다.

* 이는 Auth값이다.