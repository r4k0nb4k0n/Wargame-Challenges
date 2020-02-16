# PEPassword

## Problem

* [`PEPassword.zip`](./PEPassword.zip)
  * [`Original.exe`](./Original.exe)
  * [`Packed.exe`](./Packed.exe)

## Background Knowledges

* [PE Password Unpack](http://www.jiniya.net/tt/entry/PE-Password-Unpack)

## Tools

* CFF Explorer VIII
* IDA 7.0

## Explanation

* [`Original.exe`](./Original.exe)와 [`Packed.exe`](./Packed.exe)의 차이점을 분석해보았다.
  * ![1-1](./1-1.png?raw=true)
    * Entry point의 위치가 서로 다른 것을 알 수 있다.
      * [`Original.exe`](./Original.exe) - `.text` 영역
      * [`Packed.exe`](./Packed.exe) - `SMT//SMF` 영역
  * ![1-2](./1-2.png?raw=true)
    * `SMT//SMF`라는 영역이 [`Packed.exe`](./Packed.exe)에 추가되어 있다.
    * PE Password 패커의 코드가 들어있는 것으로 추측할 수 있다.
  * ![1-3](./1-3.png?raw=true)
    * `.text` 영역을 비교해보면, 크기와 위치는 동일하나 그 내용은 서로 다르다.
    * 암호화된 것으로 추측할 수 있다.
* [`Packed.exe`](./Packed.exe)를 IDA 7.0으로 열어서 분석해보았다.
  * ![2-1](./2-1.png?raw=true)
    * `Password Check`라는 제목을 가진 Dialog를 생성하고 띄운다. 여기에는 패스워드를 입력할 수 있는 필드가 주어진다.
  * ![2-2](./2-2.png?raw=true)
    * `0x434F4445`(`CODE`)와 입력한 패스워드의 첫번째 글자를 XOR 연산한 결과값을 `generate_hash()` 함수에 넣어 도출한 해시값이 `0x0E98F842A`와 같으면 통과한다. 이는 단순히 우회하여 통과만 하면 다음 루틴으로 진행할수 있다.
  * ![2-3](./2-3.png?raw=true)
    * `Unpack()` 함수는 다음과 같이 작동한다.
      * 복호화에 쓰일 `p`와 `q`를 생성한다.
        * `0x48415348`(`HASH`)와 입력한 패스워드의 첫번째 글자를 XOR 연산한 결과값을 `generate_hash()` 함수에 넣어 도출한 해시값이 `p`다. 
        * `p = generate_hash(input[0] ^ 0x48415348)`
        * `0x48415348`(`HASH`)와 입력한 패스워드의 두번째 글자를 XOR 연산한 결과값을 `generate_hash()` 함수에 넣어 도출한 해시값이 `q`다. 
        * `q = generate_hash(input[1] ^ 0x48415348)`
      * 한번에 4바이트씩 복호화를 진행한다.
        * `unpacked[i] = packed[i] ^ p`
      * 복호화 후 새로운 `p''`와 `q''` 값을 계산한다.
        * `q' = q rol p[0]`
        * `p' = p ^ q'`
        * `p'' = p' ror q'[1]`
        * `q'' = p'' + q'`
* [`Original.exe`](./Original.exe)를 IDA 7.0으로 열어서 분석해보았다.
  * ![3-1](./3-1.png?raw=true)
    * `WinMain()` 함수를 pseudo-code로 변환해보았다.
    * `"Congratulation!\r\n\r\nPassword is "` 문자열 뒤에 `"???????????"`로 가짜 패스워드를 채워놓았다.
* 암호화 키를 구하고 복호화까지 진행한다.
  * ![4-1](./4-1.png?raw=true)
    * 위 분석 내용을 기반으로 [`Original.exe`](./Original.exe)와 [`Packed.exe`](./Packed.exe)의 `.text` 영역을 비교해보면, 영역 구분을 위해 채워놓은 `0x00` 바이트들이 암호화 당시 XOR 연산으로 인해 `p` 값들로 바뀐 것을 알 수 있다.
  * 여기서부터 위로 거슬러 올라가서 `p`와 `q`의 규칙을 파악하여 맨 처음 `p`와 `q`를 파악하는 것도 좋다.
  * 하지만 맨 처음 3-4개 정도의 dword들이 일치하기 때문에, 거슬러 올라갈 필요 없이 맨 처음 `p`에 대한 올바른 `q`를 구한 후, 복호화 루틴에 이를 집어넣으면 그만이다.
  * ![4-2](./4-2.png?raw=true)
    * [`getkey.c`](./getkey_c/getkey.c)
    * key p(`b7aac296 5a5a7e05 99c51d27`)에 key q(`c263a2cb 0d4b16ed 4327fac8`)로 나타나는 것을 확인할 수 있다.
  * 맨 처음 `p`인 `b7aac296`과 맨 처음 `q`인 `c263a2cb`를 복호화 루틴 진입 전에 각각 레지스터 `eax`와 `ebx`에 집어놓고 진행한다.
  * 복호화가 성공적으로 진행되고 플래그가 나타나는 것을 확인할 수 있다.
