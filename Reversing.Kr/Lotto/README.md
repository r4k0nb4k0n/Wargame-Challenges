# x64 Lotto

## Problem
* [`Lotto.zip`](./Lotto.zip)
    - `Lotto.exe`

## Tools
* ExeinfoPe
* IDA 7.0

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `ahk.exe`을 열어보았다.
* 64비트 PE 파일임을 알 수 있다.

![](./2-1.PNG?raw=true)
![](./2-2.PNG?raw=true)
* 패킹이 되어 있지 않으므로 IDA로 분석을 진행했다.
* 위 두 사진들은 해당 PE 파일의 main 함수 내용을 수도 코드로 변환한 내용이다.
* 첫 번째 사진에서 정수 6개를 입력받은 뒤 이에 비교할 정수 6개를 난수로 생성하는 것을 확인할 수 있다.
* 두 번째 사진에서 로또일 때(입력한 숫자 조합과 난수 생성된 숫자 조합이 일치할 때) 복호화가 진행되고, 복호화된 문자열이 출력되는 것을 확인할 수 있다.

![](./3.PNG?raw=true)
* 입력 루틴과 난수 생성 루틴을 지나고 난 후 입력 숫자들이 들어가는 스택 메모리를 살펴보았다.
* 빨간색 밑줄이 `input[]`, 파란색 밑줄이 `gen[]`이다.
* 이 두 조합이 서로 일치하도록 스택 메모리를 변경한다.

![](./4.PNG?raw=true)
* 다음과 같이 flag가 출력되는 것을 확인할 수 있다.