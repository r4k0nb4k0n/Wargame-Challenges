# AHK2

## Problem
* [`AHK2.zip`](./AHK2.zip)
    - `AHK2.exe`
    - `ReadMe`
```
Reversing.Kr

It should be modified to work properly.

By rianatzz

```

## Tools
* ExeinfoPe
* x32dbg
* UPX 3.95
* IDA 7.0

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `ahk.exe`을 열어보았다.
* AutoHotKey로 제작된 PE 파일임을 알 수 있다.
* [AutoHotKey](https://www.autohotkey.com/)

![](./2.PNG?raw=true)
* [`ReadMe`](./ReadMe)의 내용을 보면, 패치를 해야 해당 파일이 제대로 작동한다는 것을 알 수 있다.
* [`AHK2.exe`](./AHK2.exe)를 실행해보면, 다음과 같이 `EXE corrupted` 메시지가 뜨면서 제대로 작동하지 않는 것을 알 수 있다.

![](./3.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어서 `EXE corrupted`가 뜨는 부분을 찾아보았다.
* `pushad`, `popad`가 있고 이름이 `UPX`로 시작하는 영역이 있는 것을 보고 `UPX`로 패킹된 것을 알 수 있었다.
* stripped binary라고 불러도 되는지 모르겠지만 하여튼 함수들은 엄청 많고 이들이 무슨 역할을 하는지 x32dbg에서는 자세히 알 수 없었다.
* 따라서 [`AHK2.exe`](./AHK2.exe)을 언패킹한 [`AHK2.unpacked.exe`](./AHK2.unpacked.exe)을 IDA로 열어서 자동 분석 후 [`AHK2.unpacked.map`](./AHK2.unpacked.map) 파일을 추출했다.
* 추출한 [`AHK2.unpacked.map`](./AHK2.unpacked.map)을 x32dbg에 불러와 적용하면 다음과 같이 쓰이는 함수들에 라벨링이 되어 알아보기 편해진다.
* 이는 패킹된 상태의 [`AHK2.exe`](./AHK2.exe)에도 적용된다.

![](./4.PNG?raw=true)
* 다음과 같이 `@check_integrity` 함수의 리턴값이 `0`이 아니면 `EXE corrupted` 루틴으로 점프한다.

![](./5-1.PNG?raw=true)
* `@check_integrity` 함수의 call graph를 그려보았다.
    - 실행한 exe 파일을 `fopen` 함수로 열어 file pointer를 딴다.
    - **미리 저장된 체크섬?CRC?값을 복사한다.**
    - 파일을 이것저것 읽어본다. 파일의 맨 끝 4바이트도 읽어본다. 사실 이 부분은 없어도 상관없다.
    - **파일의 특정 위치에서 읽어온 16 바이트가 미리 복사해둔 체크섬?CRC?값과 일치하는지 확인한다.**
    - 이후 1바이트씩 2,3 바이트들이 일치하는지 확인하고 맞으면 `0`을 리턴한다.
* 파일의 맨 끝 4바이트를 확인하는 구간은 건너뛰어도 상관없다.
* 하지만 미리 복사해둔 체크섬?CRC?값을 확인하는 구간에서 파일의 특정 위치에서 16바이트를 읽어오기 위해 `fseek` 함수로 이동을 하는데, `offset` 인자가 엉뚱한 값이 넘겨지는 것을 확인할 수 있다. 이 부분을 찾아야 한다.

![](./5-2.PNG?raw=true)
* 다음은 미리 저장된 체크섬?CRC?값을 복사한 값을 보여준다.
* 해당 16바이트를 exe 파일에서 찾는다면, 올바른 `offset`을 구할 수 있다.

![](./5-3.PNG?raw=true)
* [`AHK2.exe`](./AHK2.exe), [`AHK2.unpacked.exe`](./AHK2.unpacked.exe)에서 각각 체크섬?CRC?값을 검색해보았다.
* 위치는 각각 `0x32800`, `0x66E00`이다.
* 어떤 파일을 패치할 것인지에 따라 어떤 오프셋으로 패치할 지 달라진다.
    - 언패킹한 파일에서 패치하면 `0x66E00`,
    - 패킹한 파일에서 패치하면 `0x32800`이다. 주의할 점은 패치도 패킹되어야 한다는 것이다.

![](./6.PNG?raw=true)
* 파일의 맨 끝 4바이트를 확인하는 구간과 `fseek` 함수의 인자 `origin`, `offset`을 스택에 push하는 구간을 `nop`로 채운 뒤 다음과 같이 변경했다.
* 이는 파일의 맨 처음부터 오프셋 `0x32800`에 해당하는 부분으로 이동하라는 의미이다.
* 이는 패킹된 파일 기준으로 한 패치다.
* 언패킹된 파일을 패치한 것은 [`AHK2.unpacked.patched.exe`](./AHK2.unpacked.patched.exe)이다.

![](./7.PNG?raw=true)
* 파일 패치 후 실행하면 다음과 같이 수수께끼가 담긴 창이 뜬다.
* 잘 모르지만 이는 드라마 왕자의 게임에 관련된 내용이고, 위키피디아에서 검색을 잘 하면 **ㅈㅅㄴㅇ**임을 유추할 수 있다.
* 이를 영어 소문자로 제출하면 끝이다.
