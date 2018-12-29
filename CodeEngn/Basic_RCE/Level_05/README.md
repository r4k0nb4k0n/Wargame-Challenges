# Basic RCE Level 05

## Problem
* Korean : 
이 프로그램의 등록키는 무엇인가 
* English : 
The registration key of this program is? 

## Tool
* CFF Explorer
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* CFF Explorer로 열어본 결과, GUI 기반인 것을 알 수 있다.

![](./2.PNG?raw=true)
* 실행하면 다음과 같이 기본값 문자열들이 채워져있고, 이대로 `Register now !` 버튼을 누르면 `Wrong serial`이라는 창이 뜬다.
* 기본값 문자열들을 모두 지우고 `Register now !` 버튼을 누르면  차례대로 `Enter a Name!`, `Enter a Serial!`, `Wrong serial` 창이 뜬다.

* 실행 파일 안에 등록키와 관련된 문자열이 저장되어있을 거라는 추측을 했다.

![](./3.PNG?raw=true)
* x32dbg에서 실행 파일을 불러오고, 모든 모듈에서의 문자열 참조들을 찾은 뒤, 정규식 검색으로 등록키와 같은 형식인 문자열을 찾아냈다.
* 기본값 문자열 : `754-GFX-IER-954`
* 정규표현식 : `[0-9A-Za-z]{3}-[0-9A-Za-z]{3}-[0-9A-Za-z]{3}-[0-9A-Za-z]{3}`
* 찾아낸 문자열 : `GFX-754-IER-954`

![](./4.PNG?raw=true)
* 찾아낸 문자열 참조가 일어난 곳으로 따라가보니, 다음 그래프와 같은 순서도로 진행된다는 것을 알 수 있다.
* 맥락상 `Registered User`,`GFX-754-IER-954`이어야 통과하는 것을 알 수 있다.

![](./5.PNG?raw=true)
* `Registered User`,`GFX-754-IER-954`을 입력했을 때 통과하는 것을 볼 수 있다.