# flag

### Problem
```
Papa brought me a packed present! let's open it.

Download : http://pwnable.kr/bin/flag

This is reversing task. all you need is binary
```

### Background Knowledge
* [man file](https://linux.die.net/man/1/file)
	- 파일 정보를 확인하는 명령어이다.
* [man strip](https://linux.die.net/man/1/strip)
	- strip은 오브젝트 파일에 있는 심볼을 삭제하는 툴이다. 일반적으로 빌드 완료한 실행파일 또는 라이브러리에서 불필요한 심볼을 제거하는데 사용한다.

### Inspection
```
$ file flag
flag: ELF 64-bit LSB  executable, x86-64, version 1 (GNU/Linux), statically linked, stripped
```
* 여기서 `stripped`는 디버그에 도움이 되지만 용량을 차지하는 정보들을 제거했다는 뜻이다. [Link](https://unix.stackexchange.com/questions/2969/what-are-stripped-and-not-stripped-executables-in-unix)

```
$ ./flag
I will malloc() and strcpy the flag there. take it.
```
* 실행 결과에 힌트가 나온다.
	- `malloc()`으로 동적 할당을 받은 곳에 `strcpy()`로 플래그를 남겨놨다.

* `hexdump -C flag`로 보면 2만 줄이 넘는다.