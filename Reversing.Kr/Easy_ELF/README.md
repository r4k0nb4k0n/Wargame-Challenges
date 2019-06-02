# Easy ELF

## Problem
* [`Easy_ELF`](./Easy_ELF)

## Tools
* radare2

## Explanation
```
$ r2 Easy_ELF
[0x0804851b]> aa
[x] Analyze all flags starting with sym. and entry0 (aa)
[0x0804851b]> V
... Add some functions manually ...
[0x0804851b]> afl
0x08048350    1 6            sym.imp.__libc_start_main
0x08048360    1 6            sym.imp.write
0x08048370    1 6            sym.imp.__isoc99_scanf
0x08048380    1 33           entry0
0x08048434    1 29           get_input_flag
0x08048451   14 166          judge_flag
0x080484f7    1 36           print_correct
0x0804851b    4 99           main
[0x0804851b]> agfd main > main.dot
[0x0804851b]> agfd print_correct > print_correct.dot
[0x0804851b]> agfd judge_flag > judge_flag.dot
[0x0804851b]> agfd get_input_flag > get_input_flag.dot
[0x0804851b]> !!dot -Tpng -o main.png main.dot
[0x0804851b]> !!dot -Tpng -o print_correct.png print_correct.dot
[0x0804851b]> !!dot -Tpng -o judge_flag.png judge_flag.dot
[0x0804851b]> !!dot -Tpng -o get_input_flag.png get_input_flag.dot

```

* radare2에서 해당 ELF 파일을 열었다.
* 분석을 마치고 미처 분석이 안된 함수들을 직접 추가하고 흐름도를 그려보았다.

![](./main.png?raw=true)
* 다음과 같은 흐름을 보인다.
	- `"Reversing.Kr Easy ELF\n\n"`를 출력한다.
	- `get_input_flag` 함수를 실행한다.
	- `judge_flag` 함수를 실행한다.
		- 리턴 값이 `0`이면  `"Wrong\n"`을 출력한다.
		- 리턴 값이 `1`이면 `print_correct` 함수를 실행한다.
	- 종료한다.

![](./get_input_flag.png?raw=true)
* `0x804a020` 에 flag를 입력받는다.

![](./print_correct.png?raw=true)
* `"Correct!\n"`을 출력한다.

![](./judge_flag.png?raw=true)
* `&flag = 0x804a020`이라고 하자.
* 다음과 같은 흐름을 보인다.
	- `flag[1] == '1' ; 0x31` 이어야 한다.
	- `flag[4] == 'X' ; 0x58` 이어야 한다.
	- `flag[5] == NULL` 이어야 한다.
	- `flag[2] ^ 0x32 == 0x7C`, 즉 `flag[2] == 'N' ; 0x4E` 이어야 한다.
	- `flag[0] ^ 0x34 == 0x78`, 즉 `flag[0] == 'L' ; 0x4C` 이어야 한다.
	- `flag[3] ^ 0xFFFFFF88 == 0xDD`, 즉 `flag[3] == '?' ; 0x55` 이어야 한다.
* `L1NUX`

