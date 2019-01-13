# 30

## Problem
```

Military - Download

 
 
해커가 김장군의 PC에 침투한 흔적을 발견하였다.
사고 직후 김장군의 PC에서 획득한 메모리 덤프를 제공받은 당신은 해커가 한 행동을 밝혀내야한다.

1. 김장군 PC의 IP 주소는?
2. 해커가 열람한 기밀문서의 파일명은?
3. 기밀문서의 주요 내용은? 내용속에 "Key"가 있다.

인증키 형식 : lowercase(MD5(1번답+2번답+3번키))

======================================================================================

General Kim's PC was hacked by Hacker
Here is a Memory Dump at that time, You should find what Hacker did

Q1 : IP Address of General Kim's PC
Q2 : Which secret document did Haker read?
Q3 : What is content of secret document? There is a "Key"

Auth Key = lowercase(MD5(Answer of Q1+Answer of Q2+Key of Q3))
```

## Background Knowledge
* [Memory Forensics - Wikipedia](https://en.wikipedia.org/wiki/Memory_forensics)
	- 메모리 덤프 분석.
* [Volatility Command Reference](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)

## Tool
* [Volatility](https://www.volatilityfoundation.org/releases)

## Inspection and Solution
![](./1.PNG?raw=true)
* Volatility를 이용하여 해당 메모리 덤프에서 운영체제 및 시간 정보를 알아낸다.
* 프로필 제안으로 `Win7SP?x86`이 뜬다.

![](./2.PNG?raw=true)
* `volatility.exe -f MemoryDump(SuNiNaTaS) --profile=Win7SP1x86 netscan`
	- 제안받은 프로필 중 하나인 `Win7SP1x86`를 적용한다.
	- `netscan`으로 네트워크 아티팩트를 조사한다.
* `Local address`인 `192.168.197.138` 에서 `Foreign address`로 나가는 연결이 많다.
* `1. 김장군 PC의 IP 주소는?`의 답은 `192.168.197.138`.

![](./3.PNG?raw=true)
* `volatility.exe -f MemoryDump(SuNiNaTaS) --profile=Win7SP1x86 psxview`
	- `psxview`로 숨겨진 프로세스까지 조사한다.
* `v1tvr0.exe`은 29번 문제에서 본 키로거 파일과 똑같다. 문제 푸는 것과는 관련이 적다.
* `cmd.exe`가 열려있다. `cmdscan`을 이용해 명령 실행 기록을 확인해봐야 한다.
* `notepad.exe`, `iexplorer.exe` 같이 문서를 읽을만한 프로세스가 있다.
	- 브라우저 방문 기록, 메모리에 남은 파일들을 조사해봐야 한다.


![](./4.PNG?raw=true)
* `volatility.exe -f MemoryDump(SuNiNaTaS) --profile=Win7SP1x86 cmdscan`
	- `cmdscan`으로 명령 실행 기록을 확인한다.
* `notepad C:\Users\training\Desktop\SecreetDocumen7.txt`을 보아 메모장으로 비밀문서같이 보이는 `SecreetDocumen7.txt`를 열었다는 것을 알 수 있다.

![](./5.PNG?raw=true)
* `volatility.exe -f MemoryDump(SuNiNaTaS) --profile=Win7SP1x86 iehistory`
	- `iehistory`로 브라우저 방문 기록을 확인한다.
* `1408`번 `explorer.exe`에서 `SecreetDocumen7.txt`를 열람한 기록이 있다.

![](./6.PNG?raw=true)
* `volatility.exe -f MemoryDump(SuNiNaTaS) --profile=Win7SP1x86 filescan > filescan.txt`
	- `filescan`으로 물리 메모리에 있는 파일 오브젝트들을 찾는다.
* Offset `0x3df2ddd8`에 `SecreetDocumen7.txt`가 위치한다는 것을 알 수 있다.

![](./7.PNG?raw=true)
* `volatility.exe -f MemoryDump(SuNiNaTaS) --profile=Win7SP1x86 dumpfiles --physoffset 0x3df2ddd8 --dump-dir .\`
	- `dumpfiles`로 오프셋을 직접 지정하여 파일을 덤프 뜰 수 있다.

![](./8.PNG?raw=true)
* 덤프 뜬 파일을 확인해보니 flag가 나타난다.
* `2. 해커가 열람한 기밀문서의 파일명은?`, `3. 기밀문서의 주요 내용은? 내용속에 "Key"가 있다.`의 답은 각각 `SecreetDocumen7.txt`, `4rmy_4irforce_N4vy`.


* `lowercase(MD5("192.168.197.138"+"SecreetDocumen7.txt"+"4rmy_4irforce_N4vy"))`를 제출하면 통과한다.