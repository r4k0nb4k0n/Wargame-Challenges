# 27

## Problem
```
Can you speak x86

 
 
NSA has intercepted a chatter between mafia organization members from an IRC server.
investigators are certain that the message has some secret, however they can't find any clue.
your mission is to help the NSA investigators and reveal the secret of this message.

down

Thanks to : daehee
```
## Tool
* wc
* Bless
* gdb-peda
* xxd

## Inspection
* [`message.txt`](./message.txt)
    * 러시아 마피아 조직원의 잡담이 영문으로 담겨 있다.
* 제목 `Can you speak x86`을 보니 [`message.txt`](./message.txt)에서 의심스러운 문자열들을 x86 어셈블리어로 디스어셈블해보면 어떨까 생각했다.
* 관찰 결과
	- 의심스러운 문자열들
		+ `$A$"4k`
		+ `DDDDDHHHHHHPDDDDD`
		+ `@@@@@@@@@@@@@@@@@@@@`
		+ `DDDD`
		+ `HHHHHHHHHHHHHHHHHHHHHHHHHH`
		+ `11111DDDDD@@@@@@@@@@PDDDDD@@@@@@@@@@PDDDDDHHHHHHHHHHHHHHHHHHHH`
		+ `@@PDDDDDPDDDDDHPDDDDD@@@@@PDDDDDPDDDDD@@@PDDDDD`
		+ `kNz3i!Bs4jP`
	- 디스어셈블링 결과, `eax`에 특정 값을 넣어놓고 이를 증가 및 감소하면서 스택에 `push`하는 코드들로 보인다. 
	- 이를 실행해보면서 스택을 보니 `key`, `_`, `is`가 보였다.
	- 이 파일을 통째로 실행하면 스택에 `key`값이 보일 것이다.

## Solution
* 요약 : 정상 ELF 파일에 [`message.txt`](./message.txt)를 주입한 후, 디버거에서 실행하여 스택을 살펴본다.

```
$ cat message.txt | wc -m
3412
```
* [`message.txt`](./message.txt)는 총 `3412 bytes`이다.
* `wc -m`은 글자 수를 센다.

```
$ python -c 's=""
for i in range(3413):
  s+="\"nop;\"\n"
print("int main(){__asm__(%s); return 0;}" % s)
' > dummy.c

$ gcc -m32 -o dummy.out dummy.c
```
* 아무 ELF에 그냥 주입하면 ELF가 망가진다.
* C의 inline assembly를 이용하여 `nop(0x90)`을 [`message.txt`](./message.txt)의 크기만큼 채워놓아야 이를 [`message.txt`](./message.txt)의 내용으로 대체할 수 있고, ELF가 망가지지 않는다.

![](./1.PNG?raw=true)
* Bless에서 [`message.txt`](./message.txt)를 열고 전체를 선택해보니 `0xd54 bytes`, 즉 `3412 bytes`이다.

![](./2.PNG?raw=true)
* Bless에서 [`dummy.out`](./dummy.out)을 열고 `nop(0x90)`이 많은 곳을 찾아보았다.
* `55`, `89 E5` 이후에 `nop`이 많다.
* 이는 `push %ebp`, `move %esp, %ebp`로, `main` 함수의 prolog 코드이다. 

![](./3.PNG?raw=true)
* `55 89 E5` 이후의 `NOP` 코드부터 `3412 bytes`만큼 선택한다.

![](./4.PNG?raw=true)
* 이를 [`message.txt`](./message.txt)로 대체한 후, [`filled.out`](./filled.out)으로 저장한다.

![](./5.PNG?raw=true)
* `gdb-peda filled.out`
* `pdisas main`
* 만약 잘못 처리했다면 ELF 파일이 깨졌다고 뜰 것이다. 다시 잘 붙여야 한다.
* [`message.txt`](./message.txt) 코드가 다 끝난 후 `main` 함수가 종료하기 전인 `*main+3415`에 breakpoint를 잡는다.

![](./6.PNG?raw=true)
* `run`
* `*main+3415`에 멈춘다.
* `EBP`에 `"ccbggj"`라는 의심스러운 문자열이 보인다. 스택을 덤프떠봐야 한다.

![](./7.PNG?raw=true)
* `xxd`라는 명령을 정의한다.
	- `define xxd`
	- `dump binary memory dump.bin $arg0 $arg0+$arg1`
	- `shell xxd dump.bin`
	- `end`
* `xxd (EIP에서 몇십 바이트 뺀 위치) (읽을 바이트 개수)`
* `key`가 나타난다.
* 