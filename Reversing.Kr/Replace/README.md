# Replace

## Problem
* [`Replace.zip`](./Replace.zip)
	- `Replace.exe`

## Tools
* ExeinfoPe
* PEiD
* x32dbg
* [Cryptii](https://cryptii.com/)

## Background Knowledge
* [GetDlgItemInt function (winuser.h) | Microsoft Docs](https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-getdlgitemint)

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 해당 PE 파일을 열어보았다.
* 다음과 같은 특징을 알 수 있다.
	- Windows GUI
	- Microsoft Visual C++
	- 32bit

![](./2.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* 통과하는 의미의 문자열을 찾아보았다.
* `0x00401073`부터 실행되면 통과할 수 있다.
* 하지만 `0x401071`, `0x401072`가 눈엣가시다.

![](./3.PNG?raw=true)
* 일단 전체 흐름을 파악해본다.
* EntryPoint의 call graph이다.
* `sub_401000`에서 다이얼로그를 띄울 것이다.

![](./4.PNG?raw=true)
* 추측한 대로 다이얼로그를 띄운다.
* `&DialogFunc`를 따라가보자.

![](./5.PNG?raw=true)
* `&DialogFunc`의 call graph이다.
* 어떤 버튼이 눌렀냐에 따른 흐름을 보여준다.
* `Check` 버튼을 눌렀을 때
	- 텍스트 아이템에서 입력을 받아오는데, Unsigned integer만 받아온다.
	- ![](./6.PNG?raw=true)
		+ 아직 변하지 않은 `&self_modified` 에서
		+ `call replace.40467A`에서 `@input`에 `0x2`를 더한다.
		+ `@input`에 `0x601605C7`을 더한다.
		+ 그다음 `&inc_input`을 호출하여 `@input`을 `1`만큼 증가한다.
		+ 그다음 명령어도 결국 `&inc_input`이므로 한번 더 `@input`을 `1`만큼 증가한다.
	- `0x00404690`으로 건너뛴다.
* `0x00404690`에서
	- `eax`에 `@input`을 복사해둔다.
	- `@input`을 `1`만큼 증가하는 함수 `&inc_input`을 두 번 실행한다. **하지만 실제로 사용하는 것은 `eax`에 들어있는 `@input` 값이다.**
	- ![](./7.PNG?raw=true)
		+ `&self_modified`가 특정 byte를 `NOP`(`0x90`)으로 덮어씌우는 코드로 바뀐다.
	- `eax` 안의 주소값에 위치한 byte를 `NOP`로 덮어씌운다.
	- `eax`를 `1` 증가한다.
	- `eax` 안의 주소값에 위치한 byte를 `NOP`로 덮어씌운다.
	- 원래 `&self_modified` 함수로 다시 바꾼다.
* 아까 눈엣가시였던 `0x401071`, `0x401072`를 `NOP`로 덮어씌울 수 있다면 통과할 수 있다.

![](./8.PNG?raw=true)
* `@input + 0x601605C7 + 0x00000004 = 0x00401071`(in DWORD)이어야 눈엣가시인 `0x401071`, `0x401072`를 `NOP`로 덮어씌울 수 있다.
* `@input = 0x00401071 - 0x0000004 - 0x601605C7 = 0xA02A0AA6 = 2687109798`
* `EIP`가 무사히 `0x00401073`에 도달하므로 통과한다.
