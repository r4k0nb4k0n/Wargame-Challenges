# HateIntel

## Problem
* [`HateIntel.zip`](./HateIntel.zip)
    - `HateIntel.exe`
    - `ReadMe`

```
Reversing.Kr

Find The Password

By ezbeat

```
## Background Knowledges
* [Mach-O - Wikipedia](https://en.wikipedia.org/wiki/Mach-O)
    - Multi-architecture binaries
        - Under NeXTSTEP, OPENSTEP, macOS, and iOS, multiple Mach-O files can be combined in a multi-architecture binary.
        - For example, a multi-architecture binary for iOS can have 6 instruction set architectures, namely ARMv6 (for iPhone, 3G and 1st / 2nd generation iPod touch), ARMv7 (for iPhone 3GS, 4, 4S, iPad, 2, 3rd generation and 3rd–5th generation iPod touch), ARMv7s (for iPhone 5 and iPad (4th generation)), ARMv8 (for iPhone 5S), x86 (for iPhone simulator on 32-bit machines) and x86_64 (64-bit simulator).
## Tools
* ExeinfoPe
* IDA 7.0

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `HateIntel`을 열어보았다.
* Mach-O 파일임을 알 수 있다.

![](./2-1.PNG?raw=true)
![](./2-2.PNG?raw=true)
![](./2-3.PNG?raw=true)
* 패킹이 되어 있지 않으므로 IDA로 분석을 진행했다.
* 위 세 사진들은 해당 파일의 main 함수 내용을 수도 코드로 변환한 내용이다.
* 첫 번째 사진은 `main()`의 내용을 담고 있다. 
* 두 번째 사진은 `encode_key_n_times()`의 내용을 담고 있다.
* 세 번째 사진은 `encode_character_n_times()`의 내용을 담고 있다.
* 전체 작동을 요약하자면 다음과 같다.
    - 29바이트가 담긴 `byte_3004[]`은 메시지가 암호화된 데이터를 담고 있다.
    - 암호화되기 전의 메시지 데이터를 입력하여 이를 암호화한 후, 기존 암호화된 데이터와 같다면 통과한다.
    - 암호화 루틴은 각 글자마다 다음과 같은 연산을 `4`번 거치는 것이다.
        - `ch = (각 글자)`
        - `ch *= 2`
        - `if (ch & 0x100) ch |= 1u`

![](./3.PNG?raw=true)
* 위 암호화 루틴을 사용하여 무작위 대입을 통해 암호화되기 전의 메시지를 구할 수 있다.
* 다음과 같이 flag가 출력되는 것을 확인할 수 있다.

## Rewind
* 해당 문제의 요점은 `Mach-O와 ARM 명령어들을 아는가`라고 생각한다.
* Mach-O와 ARM 명령어들에 익숙해질 수 있었던 좋은 기회였다.
