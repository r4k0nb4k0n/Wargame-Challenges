# Direct3D FPS

## Problem
* [`Direct3D_FPS.zip`](./Direct3D_FPS.zip)
    - `\data`
    - `D3DX9_43.dll`
    - `FPS.exe`

## Tools
* PEStudio
* Cheat Engine
* x32dbg
* HxD

## Explanation
![](./1.PNG?raw=true)
* PEStudio로 `FPS.exe`을 열어보았다.
* 다음과 같은 특징을 알 수 있었다.
    - 32-bit PE
    - GUI
    - C++
    - DirectX 3D API 사용
    - 참조된 문자열들 중 플래그와 연관이 있을 법한 `Game Clear!` 발견

![](./2.PNG?raw=true)
* 직접 실행했다.
* 귀여운 고구마들을 쏘는 재미가 쏠쏠했다.
* 초반 프레임 수가 너무 낮게 나와 게임을 진행하기 어려웠지만, 눈에 보이는 고구마들을 다 쏴죽이니 30 FPS 대로 올라온다.
* **눈에 보이는 고구마들을 다 쏴죽여도 클리어되지 않는다...**
* 고구마에 다가가면 죽는다.

![](./3-0.PNG?raw=true)
* Cheat Engine을 이용하여 분석해보았다.
* 알아낸 정보는 다음과 같다.
    - 플레이어의 HP는 `10`이다.
    - 고구마의 HP는 `100`이다.
    - 총의 공격력은 가변적이지만, 최소 `2` 이상이다.

![](./3-1.PNG?raw=true)
* 해당 PE 파일을 x32dbg로 열어 그래프로 분석을 해보았다.
* Flag와 관련된 핵심 로직은 다음과 같다.
    - 고구마 object를 생성할 때마다 특정 인덱스 부분의 복호화 키를 생성 및 저장함.
    - 고구마 object가 총에 맞아 죽었을 때 해당 object에서 저장한 복호화 키를 이용하여 암호화된 문자열의 특정 인덱스 부분을 복호화한다.
    - 모든 고구마 object가 죽는다면 복호화된 문자열이 MsgBox로 나타난다.

![](./3-2.PNG?raw=true)
* 고구마 object 1개가 저장되는 메모리 크기는 0x210 bytes이다.
* `0xF19194`(`fps.GoGooMa[]`, 고구마 object 배열의 시작 주소)
* `0xF1F8B4`(`fps.GoGooMa[last+1]`)
* `(0xF1F8B4 - 0xF19194) ÷ 0x210 - 0x1 = (고구마 object의 개수) = 0x31 = 49`

![](./3-3.PNG?raw=true)
* `gameClearContentKey`(`0xF19184`부터 `0xF1F694`까지 `0x210`씩 건너뛰어 `0x31` bytes)
* `gameClearContent`(`0xF17028` ~ `0xF17059`, `0x31` bytes)

![](./4-1.PNG?raw=true)
* `gameClearContentKey`(`0xF19184`부터 `0xF1F694`까지 `0x210`씩 건너뛰어 `0x31` bytes)를 덤프한다.

![](./4-2.PNG?raw=true)
* `gameClearContent`(`0xF17028` ~ `0xF17059`, `0x31` bytes)를 덤프한다.

![](./5.PNG?raw=true)
* 위에서 덤프한 것들을 이용하여 다음과 같이 복호화할 수 있다.
* [`decrypt.py`](./decrypt.py)