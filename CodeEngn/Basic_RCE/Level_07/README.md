# Basic RCE Level 07

## Problem
* Korean : 
컴퓨터 C 드라이브의 이름이 CodeEngn 일경우 시리얼이 생성될때 CodeEngn은 "어떤것"으로 변경되는가 
* English : 
Assuming the drive name of C is CodeEngn, what does CodeEngn transform into in the process of the serial construction 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 살펴보니 어셈블리로 만들었다는 것을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg에서 모든 문자열 참조를 탐색해보니 시리얼로 의심되는 문자열들과 시리얼이 통과할 떄와 그렇지 않을 때 출력되는 문자열들이 나온다.
* 해당 문자열들 참조 위치를 살펴본다.

![](./3.PNG?raw=true)
* 시리얼을 검증하는 부분을 그래프로 뽑았다.
* `GetVolumeInformationA`에서 C 드라이브의 이름을 가져온다. 이미 C 드라이브의 이름을 `CodeEngn`으로 바꿔놓았다.
* 여기에 임의의 처리를 통과한 문자열을 입력값과 비교한다. `lstrcat`, `loop`, `lstrcmpi`
* 비교한 결과값이 나타나는 부분에 중단점을 설정한다.

![](./4.PNG?raw=true)
* 디버깅을 시작하고 입력값을 넣은 뒤 `Check` 버튼을 누른다.

![](./5.PNG?raw=true)
* C 드라이브 이름인 `CodeEngn`과 `4562-ABEX`를 붙인다. `s1 => 'CodeEngn4562-ABEX'`
* `s1`의 앞 4자리의 문자들의 ASCII Code값을 1씩 더하는 것을 2번 반복한다.
	- 1번 반복 -> `s1 => 'DpefEngn4562-ABEX'`
	- 2번 반복 -> `s2 => 'EqfgEngn4562-ABEX'`
* `s2 => ''`과 `L2C-5781`를 붙인다. `s2 => 'L2C-5781'`
* `s2`와 `s1`을 붙인다. `s2 => 'L2C-5781EqfgEngn4562-ABEX'`
* `L2C-5781EqfgEngn4562-ABEX`이 최종 시리얼이다.
* 여기서 `CodeEngn`은 `EqfgEngn`으로 바뀐다.