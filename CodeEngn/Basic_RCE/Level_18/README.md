# Basic RCE Level 18

## Problem
Name이 CodeEngn일때 Serial은 무엇인가 

## Tool
* ExeinfoPe
* PEiD
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 열어보았다.
* 패킹된 것 같진 않지만, 어느 언어로 작성된 것인지는 모르겠다.
* Win GUI이다.

![](./2.PNG?raw=true)
* x32dbg로 PE 파일을 열어보았다.
* Serial 검증 부분을 call graph로 그려보았다.
* 이런저런 Serial 생성 부분이 있지만, `lstrcmpi` 함수 호출 부분에서 Serial이 그대로 드러나버린다.

![](./3.PNG?raw=true)
* 드러난 Serial을 입력해보니 통과한다.