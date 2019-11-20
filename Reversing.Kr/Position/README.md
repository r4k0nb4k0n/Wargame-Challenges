# Position

## Problem
* [`Position.zip`](./Position.zip)
	- `Position.exe`
    - `ReadMe.txt`

```
ReversingKr KeygenMe


Find the Name when the Serial is 76876-77776
This problem has several answers.

Password is ***p
```

## Tools
* ExeinfoPe
* IDA 7.0

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* 다음과 같은 특징을 알 수 있다.
	- Windows GUI
	- Microsoft Visual C++
	- 32bit

![](./2.PNG?raw=true)
* IDA로 해당 PE 파일을 열어보았다.
* Name, Serial과 관련된 문자열을 찾아보았다.
* `Input Name`, `Input Serial`, `Correct!`, `Wrong`

![](./3.PNG?raw=true)
* `Correct!`, `Wrong`이 참조되는 함수 `@print_genuine`의 call graph를 그려보았다.
* `@judge_genuine` 함수의 결과에 따라 설정될 문자열이 정해진다.

![](./4.PNG?raw=true)
* `@judge_genuine` 함수의 call graph 를 그려보았다.
* 이를 요약하면 다음과 같다.
	1. 입력받은 `Name`의 유효성을 확인한다.
		+ 길이가 4글자이다.
		+ 영어 알파벳 소문자이다.
		+ 4글자 모두 서로 다른 글자이다.
	2. 입력받은 `Serial`의 유효성을 확인한다.
		+ 길이가 11글자이다.
		+ 6번째 글자가 `-`이다.
		+ 여기서 나머지 글자가 숫자인지 확인은 안하지만, 이후 과정을 보면 숫자여야 한다.
	3. 입력받은 `Name`을 이용하여 이에 맞는 `Serial`을 생성한다.
	4. 생성한 `Serial`이 입력받은 `Serial`과 일치하는지 확인한다.
		+ 만약 일치한다면, `1`을 리턴한다.
		+ 만약 일치하지 않는다면, `0`을 리턴한다.
* 해당 함수의 로직을 python script로 구현해보았다.

![](./5.PNG?raw=true)
* [`Position.py`](./Position.py)
	+ `Name`과 `Serial`의 유효성을 검증할 수 있다.
	+ `Name`과 `Serial` 둘 중 하나만 주어졌을 때, 그에 맞는 나머지를 구할 수 있다.
* `76876-77776`에 맞는 `Name`을 구했을 때 여러가지 문자열이 나온다.
* 이중 `***p`에 맞는 문자열을 제출한다.