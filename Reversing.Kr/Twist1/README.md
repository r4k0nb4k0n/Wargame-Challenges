# Twist1

## Problem

* [`Twist1.zip`](./Twist1.zip)
  * [`Twist1.exe`](./Twist1.exe)
  * [`ReadMe.txt`](./ReadMe.txt)
```text

Twist1.exe is run in x86 windows.

```

## Tools

* ExeinfoPe
* 010 Editor
* IDA 7.0

## Explanation

* ExeinfoPe로 [`Twist1.exe`](./Twist1.exe)를 분석해보았다.
  * ![1-1](./1-1.png?raw=true)
    * 패킹 및 자가 변조가 적용된 것을 유추할 수 있다.
* IDA 7.0 및 기타 디버거에서 디버깅을 시도했으나 실패했다.
  * ![1-2](./1-2.png?raw=true)
    * 안티 디버깅 기법이 적용된 것을 유추할 수 있다.
* 이를 우회하기 위해 프로세스 덤프 파일에서 PE 파일을 추출한다.
  * ![2-1](./2-1.png?raw=true)
    * [`Twist1.exe`](./Twist1.exe)를 실행한 뒤 해당 프로세스의 덤프 파일을 생성한다.
  * ![2-2](./2-2.png?raw=true)
    * [`Twist1.DMP`](./Twist1.DMP)를 010 Editor로 열어서 분석해보았다.
    * Module 중 원하는 PE 파일의 `BaseOfImage`와 `SizeOfImage`를 알아낸다.
  * ![2-3](./2-3.png?raw=true)
    * [`Twist1.DMP`](./Twist1.DMP)의 `RawData` 섹션 중 PE 파일 부분을 `BaseOfImage`와 `SizeOfImage`에 기반하여 선택한 후 복사한다.
  * ![2-4](./2-4.png?raw=true)
    * 복사한 값들을 새로운 파일인 [`Twist1.DMP.extracted.exe`](./Twist1.DMP.extracted.exe)에 저장한다.
* 프로세스 덤프 파일에서 추출한 PE 파일을 분석하여 플래그를 얻는다.
  * ![3-1](./3-1.png?raw=true)
    * `check_input` 함수의 결과값이 `0`이 아니어야 `Correct!` 문자열이 출력되는 루틴으로 빠진다.
  * ![3-2](./3-2.png?raw=true)
    * `check_input` 함수를 분석해보았다.
    * `input[6] xor 0x36`의 결과값이 `0x36`일 때 정상 루틴으로 진행된다.
    * `input[6] = 0x00 (null byte)`, 즉 플래그는 6글자임을 알 수 있다.
  * ![3-3](./3-3.png?raw=true)
    * `input[0] ror 0x6`의 결과값이 `0x49`일 때 정상 루틴으로 진행된다.
    * `input[0] = 0x52 ('R')`임을 알 수 있다.
  * ![3-4](./3-4.png?raw=true)
    * `input[2] xor 0x77`의 결과값이 `0x35`일 때 정상 루틴으로 진행된다.
    * `input[2] = 0x42 ('B')`임을 알 수 있다.
  * ![3-5](./3-5.png?raw=true)
    * `input[1] xor 0x20`의 결과값이 `0x69`일 때 정상 루틴으로 진행된다.
    * `input[1] = 0x49 ('I')`임을 알 수 있다.
  * ![3-6](./3-6.png?raw=true)
    * `input[0] xor 0x10`의 결과값이 **`0x43`이 아니어야** 정상 루틴으로 진행된다. 이미 `input[0] = 0x52 ('R')`임을 알기 때문에 쉽게 알 수 있다.
    * `input[3] xor 0x21`의 결과값이 `0x64`일 때 정상 루틴으로 진행된다.
    * `input[3] = 0x45 ('E')`임을 알 수 있다.
  * ![3-7](./3-7.png?raw=true)
    * `input[4] xor 0x46`의 결과값이 `0x8`일 때 정상 루틴으로 진행된다.
    * `input[4] = 0x4e ('N')`임을 알 수 있다.
  * ![3-8](./3-8.png?raw=true)
    * 중간의 코드 자가 변조 부분을 직접 패치하고 디스어셈블했다.
    * `input[5] rol 0x4`의 결과값이 `0x14`일 때 정상 루틴으로 진행된다.
    * `input[5] = 0x41 ('A')`임을 알 수 있다.
* [Wikipedia - Ribena](https://en.wikipedia.org/wiki/Ribena)

## Review
* `Twist1` 이름 그대로 꼬일 대로 꼬인 문제다.
* 패킹 및 각종 안티 디버깅 기법들, 코드 자가 변조까지 리버서를 괴롭히기 정말 좋은 문제다.
* 내 방식은 꼼수의 꼼수를 부려 푼 것이다. 깔끔하게 풀 수 있는 방법을 찾아봐야겠다.
