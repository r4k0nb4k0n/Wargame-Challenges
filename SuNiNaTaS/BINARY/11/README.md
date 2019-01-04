# 11

## Problem
http://suninatas.com/Part_one/web11/Unregister.zip

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보았다. Delphi로 만들어졌고, 패킹되어있지 않다는 것을 알 수 있다.

![](./2.PNG?raw=true)
* x32dbg로 열어서 모든 문자열 호출을 살펴보았다. `"Congratulation!"`과 `"Authkey: "`라는 매우 의심스러운 문자열들이 보이길래 디스어셈블러로 따라가봤다.

![](./3.PNG?raw=true)
* `jne` 에서 통과 여부가 결정되는 것을 알 수 있다. 그래서 여기에 중단점을 설정하고 디버깅을 시작했다.

![](./4.PNG?raw=true)
* 먼저 F9로 EntryPoint를 찾은 뒤, 시험 목적으로 `12345678` 문자열을 입력한 뒤 `Register` 버튼을 클릭한다.

![](./5.PNG?raw=true)
* 설정했던 중단점에서 멈춘다. 시험 목적 문자열 `12345678`과 `2VB6H1XS0F`의 동일 여부가 곧 통과 여부임을 알 수 있다.
* `"Congratulation!"` 다음에 Authkey로 의심되는 문자열을 볼 수 있다.

![](./6.PNG?raw=true)
* 다시 EntryPoint를 찾은 뒤 `2VB6H1XS0F`를 입력하고 `Register` 버튼을 클릭하니 다음과 같이 Authkey를 얻을 수 있다.