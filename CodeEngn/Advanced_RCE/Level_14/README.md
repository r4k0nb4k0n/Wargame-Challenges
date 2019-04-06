# Advanced RCE Level 14

## Problem
* Serial : `NH6-0-0091008D0052` 일때 Name은 무엇인가 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* Windows GUI임을 알 수 있다.
* Delphi로 작성되었음을 알 수 있다.

![](./2.PNG?raw=true)
* Entry Point에 진입한 후 문자열 참조를 탐색해보았다.
* 다음과 같이 시리얼 통과 여부를 나타내는 문자열들이 보인다.

![](./3.PNG?raw=true)
* 다음 문자열들이 참조되는 곳을 보니 해당 위치는 입력된 시리얼을 검증하기 전에 여러가지 조건을 확인하는 곳임을 알 수 있다.
* 주황색
	- Name과 Serial의 길이는 `0`보다 커야 한다.
	- Name은 무조건 `3` 글자 이상이어야 한다.
	- Serial의 첫 6글자는 다음 정규표현식과 같다. `NH6-[0-9]{1}-`
* 첫번째 빨간색
	- 입력된 Serial을 `-`로 파싱했을 때의 세번째 토큰과 입력된 Name에서 생성한 토큰을 비교한다.
	- 같으면 초록색, 다르면 두번째 빨간색으로 이동.
* 초록색
	- 통과.
* 두번째 빨간색
	- 통과못함.

![](./4.PNG?raw=true)
* `&GenerateSerialThirdToken` 함수의 call graph를 그려보았다.
* 다음과 같이 작동한다. [`./keygen.py`](./keygen.py)
	+ 입력받은 Name과 Seed string(`NH6 KeyGenMe6`)을 스택으로 가져온다.
	+ 입력받은 Name의 길이가 `12` 글자가 되도록 만든다.
		- 길면 `13`번째 글자부터 지운다.
		- 짧으면 이를 반복해서 뒤에 붙인다.
	+ 가공된 Name과 Seed string에서 한 글자씩 가져와서 ascii 값으로 더한 다음, 이를 `4 bytes` 형식의 문자열을 계속해서 뒤에 붙인다.
		- `C`(`0x43`) + `N`(`0x4E`) = `0x91`
		- `0091`
	+ 여기서 첫 `12`글자들을 떼어서 리턴한다.

![](./5.PNG?raw=true)
* 다음과 같이 통과하는 것을 볼 수 있다.
* `NH6-0-0091008D0052`의 Name은 첫 3글자가 `CE2` 이면 된다.