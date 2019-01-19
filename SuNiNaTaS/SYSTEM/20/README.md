# 20

## Problem
```
New No. 20 : Find it - Download

 
 

설명이 필요 없는 키값 찾는 리버싱!

힌트1 : “correct 함수가 호출될 수 있는 input 중 가장 짧은 것을 구하시오”
힌트2 : “이 문제는 프로그램이 실행되는 어떠한 시스템에서도 동일하게 풀려야합니다”

Just Reversing for finding a Key!
```

## Tool
* radare2
* graphviz
* gdb-peda

## Inspection
```
$ r2 reverseme
WARNING: Cannot initialize dynamic strings
 -- We are surrounded by the enemy. - Excellent, we can attack in any direction!
[0x08048db8]> aa
[[anal.jmptbl] Missing cjmp bb in predecessor at 0x08078978
[anal.jmptbl] Missing cjmp bb in predecessor at 0x08078940
[anal.jmptbl] Missing cjmp bb in predecessor at 0x080b3d18
Truncated instruction of 1 bytes at 0x8049bef
[anal.jmptbl] Missing cjmp bb in predecessor at 0x080b3d18
[anal.jmptbl] Missing cjmp bb in predecessor at 0x080b77d3
[anal.jmptbl] Missing cjmp bb in predecessor at 0x080b77b3
[anal.jmptbl] Missing cjmp bb in predecessor at 0x080b77f3
[anal.jmptbl] Missing cjmp bb in predecessor at 0x080b7813
[x] Analyze all flags starting with sym. and entry0 (aa)
[0x08048db8]> agfd main > callgraph.main.dot
[0x08048db8]> !!dot -Tpng -o callgraph.main.png callgraph.main.dot
[0x08048db8]>
```
* radare2에서 `reverseme`를 불러와 분석을 한 후 call graph를 그리고 이를 이미지 파일로 변환한다.

![](./callgraph.main.png?raw=true)
```
0x08049327 cmp dword [arg_8h], 1
0x0804932b jg 0x8049346
```
* `if (argc > 1) return;`
* 실행 시 받은 인자의 개수가 1개보다 더 많다면 `main` 함수가 종료되는 곳으로 `jmp`한다.

```
...
0x08049332 mov dword [local_4h], str.. suninatas
0x0804933a mov dword [esp], eax
0x0804933d call strcmp
...
```
* `if (!strcmp(argv[0], "./suninatas")) continue;`
* 그 1개의 인자가 `./suninatas`와 같으면 계속 진행하고, 아니면 `main` 함수가 종료되는 곳으로 `jmp` 한다.
* 이는 해당 ELF의 이름을 `suninatas`로 바꾸고, `./suninatas`로 실행해야 한다는 것을 알 수 있다.

```
0x080493c1 mov dword [esp], str.Authenticate_:
0x080493c8 call sym.__printf
...
0x080493d5 mov dword [esp], str.30s
0x080493dc call sym.__isoc99_scanf
...
0x08049414 call sym.Base64Decode
...
0x0804941d cmp dword [local_34h], 0xc
0x08049422 ja 0x8049456
```
* `printf("Authenticate: ");`
* `scanf("%30s", input);`
* `if(strlen(Base64Decode(input)) > 12) return;`
* 입력받은 문자열을 Base64Decode 한 후의 리턴값의 길이가 12글자를 넘을 경우 종료한다.
* 여기서 `input`은 `0x811c9ec`를 가리킨다.  

```
...
0x0804942c mov dword [local_8h], edx
0x08049430 mov dword [local_4h], eax
0x08049434 mov dword [esp], obj.input(0x811c9ec)
0x0804943b call sym.memcpy
...
0x08049447 call sym.auth
0x0804944c cmp eax, 1
0x0804944f jne 0x8049456
...
0x08049451 call sym.correct
```
* `Base64Decode`한 문자열을 특정 위치에 복사한 후 `auth` 함수를 호출한다.
* 호출한 `auth` 함수의 결과값이 `1`이면 `correct` 함수를 호출한다.

![](./callgraph.auth.png?raw=true)
* `Base64Decode`한 문자열이 입력으로 들어온다.
* 이를 md5 해싱한 값이 `f87cd601aa7fedca99018a8be88eda34`와 같으면 `1`를 리턴한다. 즉 `correct` 함수를 호출하는 곳으로 갈 수 있게 된다.

![](./callgraph.correct.png?raw=true)
* 들어온 값의 앞 4bytes가 `0xdeadbeef`와 같다면 `Congratulations! you are good!`를 출력하고 종료한다.

![](./1.PNG?raw=true)
```
$ mv reverseme suninatas
$ echo "776t3hEiM0RVZneI" | ./suninatas
Authenticate : hash : e7de0e668f2a0a9e0567709d328ee2b7
[1]    2919 done                              echo "776t3hEiM0RVZneI" |
       2920 segmentation fault (core dumped)  ./suninatas
$
```
* `Base64Decode`했을 때, 앞 4bytes가 Big-endian으로 읽었을 때 `0xdeadbeef`이고 나머지 8bytes는 `11 22 33 44 55 66 77 88`로 채운, 총 12bytes가 나오는 Base64Encode된 문자열을 생성했다.
* 이를 ELF에 입력값으로 줬을 때 어딘가 터진다. 이를 디버거로 살펴봐야겠다.

![](./2.PNG?raw=true)
* gdb-peda로 돌려보았다.
* Breakpoints
    - `*main`
    - `*main+60` : `argv[0]`이 `./suninatas`인지 확인하기 전.
    - `*main+326` : `auth` 함수 들어가기 전.
    - `*main+336` : `correct` 함수 들어가기 전.
* `*main+60`에서 스택에 있는 `argv[0]`을 `./suninatas`로 덮어씌어줘야 디버거에서 돌릴 수 있다.
* `*main+326`에서 스택을 봤을 때, `Base64Decode` 했을 때 앞 4bytes인 `0xdeadbeef`가 들어있는 걸 볼 수 있다. 이는 `Base64Decode` 했을 때 앞 4bytes를 `auth`가 인자로 받는다는 것이다.
* `auth`를 다 빠져나오고 나서 얼마 지나지 않아 `EBP`가 `0x88776655`(Little-endian)로 터진 것을 볼 수 있다. `Base64Decode` 했을 때 뒤 4bytes인 `0x55667788`이 `EBP`에 덮어씌워지는 것을 알 수 있다.
* **뒤 4bytes를 실행마다 변하지 않고, `0xdeadbeef`와 `correct` 함수의 주소를 담고 있는, 원하는 곳의 주소를 쓴다면 스택을 바꿔치기하여 프로그램의 흐름을 원하는대로 바꿀 수 있다.**

## Solution
![](./3.PNG?raw=true)
* 앞 4bytes는 `correct` 함수를 통과하기 위해 넘겨주는 인자값인 `0xdeadbeef`이다.
* 가운데 4bytes는 `correct` 함수의 첫 명령어의 주소인 `0x0804925f`이다.
* 뒤 4bytes는 해당 payloads가 들어가는 주소이고, `EBP`로 들어갈 주소인 `0x0811c9ec`이다.
* `EBP`가 `0x0811c9ec`로 바뀌면, 이후 `main` 함수가 종료할 때 `leave`, `ret`에 의해 `EIP`가 `correct` 함수의 첫 명령어의 주소인 `0x0804925f`로 바뀌어 여기로 흐름이 바뀌고, `0xdeadbeef`가 `correct` 함수의 인자로 들어가진다.

```
$ echo "776t3l+SBAjsyREI" | ./suninatas
Authenticate : hash : 105bd49a03f52b964ea4f0b3014b29e6
Congratulation! you are good!
```
* 다음과 같이 통과한다.


## Review
* 처음에는 `EBP`가 입력값의 일부분으로 덮어씌워지는 것, 즉 터지는 것도 모르고 md5hashing.net이나 뒤적거리고 있었다...
* `EBP`가 터지는 것을 알고 프로그램의 흐름을 바꾸고 싶었는데, BSS영역을 생각하지 못하고 `EBP`에 `correct` 함수 주소나 덮어씌우고 있었다...
* @ddddh의 조언과 도움을 받아 Solution에 가깝게 왔는데, Auth에서 막혔다.
* 알고보니 가운데 4bytes를 `main`에서 `correct` 함수를 호출하는 곳의 주소(`*main+336`)가 아닌, `correct` 함수의 첫 명령어 주소를 써야 했던 것이다.