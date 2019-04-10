# Advanced RCE Level 15

## Problem
* Name : 'CodeEngn.com' 일때 Serial은 무엇인가 
* Ex) AAAAAAAAAAAAAAA

## Tool
* ExeinfoPe
* PEiD
* PEStudio
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 해당 PE 파일을 열어보았다.
* Win32 GUI 임을 알 수 있다.
* 하지만 어떤 언어로 작성되었는지는 알아낼 수 없었다.

![](./2.PNG?raw=true)
* PEStudio에서 해당 PE 파일을 열어보았다.
* Serial 판별과 관련된 문자열들이 보인다.

![](./3.PNG?raw=true)
* x32dbg에서 해당 PE 파일을 열었다.
* 현재 모듈에서 문자열 참조을 찾아보았다.
* Serial 판별과 관련된 문자열들이 보인다.

![](./4.PNG?raw=true)
* 프로그램에서 About 버튼을 클릭해보았다.
* 제대로 된 Unlock Code를 찾으면 Serial 생성 코드의 난독화가 해제된다고 한다.

![](./5.PNG?raw=true)
* 프로그램의 전체적인 흐름을 볼 수 있는 call graph를 그려보았다.
* 특정 이벤트 코드에 따라 흐름이 바뀌는 것을 볼 수 있다.
* About 클릭 버튼을 눌렀을 때, Unlock Code 버튼을 눌렀을 때, Check 버튼을 눌렀을 때 등등 여러 로직이 있다.

![](./6.PNG?raw=true)
* Unlock Code를 입력하고 Unlock Code 버튼을 눌렀을 때 실행되는 함수 `@GenerateKeyByUnlockCode`의 call graph를 그려보았다.
* 난독화를 해제하는 Key를 생성한다.
	+ `l = 0x10`
	+ `key = 0x00`
	+ `for(i=0; i<l; i++)`
		- `a = (l * l)의 결과의 상위 2 바이트와 하위 2 바이트를 더한 값.`
		- `b = UnlockCode[i]`
		- `c = (a * b)의 결과의 상위 2 바이트와 하위 2 바이트를 더한 값.`
		- `key += c (2 바이트를 넘어가는 나머지 바이트들은 무시)`
	+ 글자 수를 초과하면 그냥 `0x00` 바이트로 계산한다.

![](./7.PNG?raw=true)
* Unlock Code를 입력하고 Unlock Code 버튼을 눌렀을 때 실행되는 함수 `@DeobfuscateCodeByKey`의 call graph를 그려보았다.
* 난독화된 코드의 시작 주소와 끝 주소가 나타난다. `0x004011C1` ~ `0x0040123C` 총 124 bytes.
* 난독화된 코드의 한 바이트와 Key 바이트를 XOR 연산하고 이를 다시 그 자리에 기록하여 난독화를 해제한다.

![](./8.PNG?raw=true)
* 난독화된 코드에 분명 함수 프롤로그 과정(`push ebp`, `mov ebp,esp`)이 있을거라 추측했다.
* Key는 1 byte로 0~255까지다. 충분히 브루트 포스를 시도할 수 있다고 생각했다.
* [`brute_obfuscate.py`](./brute_obfuscate.py)
* 다음과 같이 Key 바이트와 난독화가 해제된 어셈블리를 볼 수 있다.

```
Found key => 37 (0x25)
//// &GenerateKeyByName(0x004011C1)
   0:   55                      push   ebp
   1:   8b ec                   mov    ebp,esp
   3:   be 19 33 40 00          mov    esi,0x403319
   8:   8b 4d 08                mov    ecx,DWORD PTR [ebp+0x8]
   b:   8b c1                   mov    eax,ecx
   d:   f6 e1                   mul    cl
   f:   02 c4                   add    al,ah
  11:   8a d8                   mov    bl,al
  13:   8a 06                   mov    al,BYTE PTR [esi]
  15:   f6 e3                   mul    bl
  17:   02 c4                   add    al,ah
  19:   00 05 39 33 40 00       add    BYTE PTR ds:0x403339,al
  1f:   46                      inc    esi
  20:   49                      dec    ecx
  21:   75 e8                   jne    0xb
  23:   c9                      leave  
  24:   c2 04 00                ret    0x4
//// &GenerateSerialByName(0x004011E8)
  27:   55                      push   ebp
  28:   8b ec                   mov    ebp,esp
  2a:   83 c4 fc                add    esp,0xfffffffc
  2d:   c6 05 39 33 40 00 00    mov    BYTE PTR ds:0x403339,0x0
  34:   ff 75 08                push   DWORD PTR [ebp+0x8]
  37:   e8 c4 ff ff ff          call   0x0
  3c:   bf 3a 33 40 00          mov    edi,0x40333a
  41:   b9 10 00 00 00          mov    ecx,0x10
  46:   c6 45 ff 00             mov    BYTE PTR [ebp-0x1],0x0
  4a:   a0 39 33 40 00          mov    al,ds:0x403339
  4f:   02 c1                   add    al,cl
  51:   f6 e0                   mul    al
  53:   02 c4                   add    al,ah
  55:   8a 5d ff                mov    bl,BYTE PTR [ebp-0x1]
  58:   80 fb 01                cmp    bl,0x1
  5b:   7c 07                   jl     0x64
  5d:   24 f0                   and    al,0xf0
  5f:   c0 e8 04                shr    al,0x4
  62:   eb 02                   jmp    0x66
  64:   24 0f                   and    al,0xf
  66:   f6 db                   neg    bl
  68:   88 5d ff                mov    BYTE PTR [ebp-0x1],bl
  6b:   3c 09                   cmp    al,0x9
  6d:   7e 02                   jle    0x71
  6f:   04 07                   add    al,0x7
  71:   04 30                   add    al,0x30
  73:   88 07                   mov    BYTE PTR [edi],al
  75:   47                      inc    edi
  76:   46                      inc    esi
  77:   49                      dec    ecx
  78:   75 d0                   jne    0x4a
  7a:   c9                      leave  
  7b:   e7                      .byte 0xe7


------------------------
```

![](./8.PNG?raw=true)
* 디버깅 중 Key 바이트를 조작하여 정상적으로 난독화를 해제하였다.
* Check 버튼을 눌렀을 때 실행되는 함수 `&GenerateSerialByName`의 call graph를 그려보았다.
* 다음과 같이 작동한다.
	+ 함수 `&GenerateKeyByName`을 호출하여 Key 바이트를 생성한다.
	+ 이를 이용하여 16자리의 Serial을 생성한다. `[0-9A-Z]{16}`

![](./9.PNG?raw=true)
* 함수 `&GenerateKeyByName`의 call graph를 그려보았다.
* Serial을 생성하는 데 쓰이는 Key를 생성한다.
	+ `l = 0x10`
	+ `key = 0x00`
	+ `for(i=0; i<l; i++)`
		- `a = (l * l)의 결과의 상위 2 바이트와 하위 2 바이트를 더한 값.`
		- `b = Name[i]`
		- `c = (a * b)의 결과의 상위 2 바이트와 하위 2 바이트를 더한 값.`
		- `key += c (2 바이트를 넘어가는 나머지 바이트들은 무시)`
	+ 글자 수를 초과하면 그냥 `0x00` 바이트로 계산한다.

![](./10.PNG?raw=true)
* 다음과 같이 통과함을 알 수 있다.

## Review
* Keygen, UnlockCodeGen 작성 필요...