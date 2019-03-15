# Advanced RCE Level 12

## Problem
* Serial : `11E0-FBB4-490D` 일때 Username은 무엇인가 
* 해당 Serial에 대한 정답이 여러개 나오는 문제이며 Contact로 보내주시면 인증키를 보내드리겠습니다 
* 해당 Serial에 대해서 'Registered Successfully' 메시지가 나와야 합니다. 

## Tool
* ExeinfoPe
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* VB 5.0-6.0, Windows GUI임을 알 수 있다.
* Code Virtualizer (obfuscator) 1.3.8.0이 사용되었다고 **추측**할 수 있다.

![](./2.jpg?raw=true)
* [Code Virtualizer - Oreans Technology](https://oreans.com/codevirtualizer.php)
* 실제 코드를 가상 CPU 코드로 변경하여 난독화한다.
* 가상 머신? 코드가 변경된 가상 CPU 코드를 실행한다.
* 이는 실제 코드와 똑같은 작동을 하지만, 리버스 엔지니어링을 더욱 어렵게 만든다.

![](./3.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* 다음과 같이 버튼마다 함수들이 엮여 있다.

![](./4.PNG?raw=true)
* `&handlerOK`의 graph를 그려보았다.
* 입력한 Name 문자열을 복사한다.
* 그리고 `&VM`을 호출한다.

![](./5.PNG?raw=true)
* `&VM`의 graph를 그려보았다.
* `.SpiderZ` 구역의 코드를 fetch, decode, execute 한다. Instruction cycle.
* 코드의 양이 매우 많아 자동 진행으로도 분석하기 힘들다. 

![](./6.PNG?raw=true)
* `&VM`도 결국 VB Runtime 위에서 돌아가므로 `msvbvm60.dll`의 함수를 사용할 것이라고 추측했다.
* `msvbvm60.dll`의 함수들에 모두 중단점을 걸고 사용하는 함수들만 남겼다.
* 이를 통해 작동 내용을 추측할 수 있었다.

![](./7.PNG?raw=true)
* [`keygen.cpp`](./keygen.cpp)
* 다음은 Name에 따른 Key 생성 과정이다.
    + 첫 번째 토큰.
        - Name 한 글자씩 Ascii code 값을 알아내고 이를 하나의 문자열로 이어붙인다.
        - 첫 번째 토큰은 해당 문자열의 5번째 ~ 8번째 글자들이다.
        - 첫번째 토큰의 3번째 숫자에 14를 더한 값을 16진수로 나타내고 해당 숫자를 대체한다.
    + 두 번째 토큰.
        - 두 번째 토큰은 첫번째 토큰을 음수인 10진수로 읽었을 때, 이를 16진수로 표현하고 마지막 4글자를 사용한다.
    + 세 번째 토큰.
        - 세 번째 토큰의 첫 두 글자는 첫번째 토큰의 첫 숫자에 48을 더한 값이다.
        - 세 번째 토큰의 마지막 두 글자는 Name의 길이에 5를 더한 값을 16진수로 나타낸 것이다.

## Review
* 여태까지 리버싱하면서 가장 어려웠던 것 같다.
* 디버거 자동 진행을 하루 종일 켜놓아도 끝나지 않는 압도적인(?) 양으로 분석할 엄두도 못나게 했다.
* 이를 약 2주 동안 고민하다가 외부 모듈 함수에 중단점을 걸면 어느 정도 작동 내용을 추측할 수 있다는 생각을 하고 다시 시도하여 어느정도 파악할 수 있었다.
* `ddddh`는 통과 성공/실패 여부를 나타내는 다이얼로그가 나타날 때 스택을 확인하여 외부 함수를 실행하는 명령어를 찾아내고 그곳에 중단점을 걸면 호출 함수, 파라미터를 확인할 수 있다고 조언해주었다.
* 안티리버싱 기술에도 관심이 생긴다. 나를 이렇게 힘들게 만든 만큼...
* 다음은 고군분투한 흔적이다.

```
Serial : 11E0-FBB4-490D 일때 Username은 무엇인가 
해당 Serial에 대한 정답이 여러개 나오는 문제이며 Contact로 보내주시면 인증키를 보내드리겠습니다 
해당 Serial에 대해서 'Registered Successfully' 메시지가 나와야 합니다. 

Code Virtualizer (obfuscator) v1.3.8.0 - www.oreans.com - Compiler : MS Visual Basic 5.0-6.0   EXE

* CodeEngn 성공...

그냥 CodeEngn으로 때려맞히긴 했는데 어떻게 돌아가는질 모르겠다...
살...려...줘...

jmp <12.&handlerOK>
call &__vbaStrMove <- &L"CodeEngn" -> &L"CodeEngn"
jmp <12.&VM>
call &__vbaStrCopy <- &L"CodeEngn" -> &L"CodeEngn"
/**
 * Get the length of Name.
 */
call &__vbaLenBstr <- L"CodeEngn" -> 8
call &__vbaI2I4 <- 8 (int short integer) -> 8 (in 32-bit integer)
/**
 * Get the ascii code from Name one character by one.
 * And Concatenate them all in one.
 */
for i in range(8)
	call &rtcMidCharVar
	call &__vbaStrVarVal <- &L"CodeEngn" -> 
	call &rtcAnsiValueBstr <- &L"CodeEngn" -> 0x43 'C'
	call &__vbaStrI2 <- 0x43 'C' -> L"67"
	call &__vbaStrMove <- L"67" -> "67"
	call &__vbaStrCat <- 
	call &__vbaFreeStrList
	call &__vbaFreeVar
// "6711110010169110103110"
call &rtcMidCharVar <- "6711110010169110103110", 4, 4 -> "1100"
call &__vbaStrMove <- "1100"
call &__vbaFreeVarList
call &__vbaStrcat <- "1100", "-" -> "1100-"
call &__vbaStrMove


call &rtcHexVarFromVar <- "1100-" -> "FFFFFBB4"
// -1100 in Decimal -> FFFFFBB4 in Hex
call &rtcHexBstrFromVar
call &__vbaStrVarMove <-"FFFFFBB4"
call &__vbaStrMove <-"FFFFFBB4"
call &__vbaFreeVar
call &rtcReplace <- "FFFFFBB4", ? -> "FBB4"
call &rtcMidCharVar
call &__vbaVarCat
call &__vbaStrVarMove
call &__vbaStrMove
call &__vbaFreeVarList
call &__vbaFreeVar
call &rtcMidCharVar <- "1100-FBB4", 3 -> "0"
call &__vbaStrVarMove
call &__vbaStrMove
call &__vbaFreeVarList
call &__vbaR8Str <- "0" -> ???
		<- "2" -> ???
call &rtcHexVarFromVar <- ??? -> E
			<- ??? -> 10
call &__vbaFreeVar
call &__vbaStrVarMove
...
call &rtcReplace <- "1100-FBB4", 2, "E" -> "11E0-FBB4"
		<- "1121-FB9F", 2, "10" -> "11101-FB9F"
call &__vbaStrCat <- "11E0-FBB4" -> "11E0-FBB4-"

call &rtcAnsiValueBstr -> "1" substr(0, 1)
call &__vbaStrI2 <- "1" -> "49"
call &__vbaStrMove
call &__vbaStrCat <- "49" -> "11E0-FBB4-49"
call &__vbaLenBstr <- L"CodeEngn" -> 8
call &rtcHexVarFromVar <- 8? -> "0D"
call &__vbaStrCat
call &__vbaStrMove "11E0-FBB4-490D"


...

call &__vbaStrComp





* Breakpoint at msvbvm60.__vbaStrMove
1. Translate the username string in Ascii code.
'UserName' -> '851151011147897109101'
2. '851151011147897109101'.substr(4, 4)
-> '5101'
3. 'FFFFEC13'.substr(4, 4)
-> 'EC13'
4. '5101-EC13-530D'
5. '51E1-EC13-530D'

* Breakpoint at msvbvm60.__vbaStrComp
6. '51E1-EC13-530D'.compare('11E0-FBB4-490D')

* BreakPoint at user32.dll_GetDialogMonitor@8
7. Dialog.

'CodeEngn'	-> '11E0-FBB4-490D'
'Aod'	-> '11E0-FBB4-4908'
' od'	-> '11E0-FBB4-4908'
'AAAAAAAA'	-> '1456-E65B-490D'

첫 번째 토큰 11E0
첫 세 글자 [A-Z`abc]{1}[eoy]{1}[d]{1} 
여기서 1100이 나옴
11E0은 갑자기 왜 나오는지 모르겠음

두 번째 토큰 FBB4
FFFFFBB4 -> FBB4
두 번째 및 세 번째 글자에 영향을 받는 것으로 추정.
od -> 1100 -> FBB4
oe -> 1101 -> FBB3
pd -> 2100 -> F7CC
pe -> 2101 -> F7CB
qd -> 3100 -> F3E4
..
zz -> 2122 -> F7B6

세 번째 토큰 490D
앞 49는 첫 번째 토큰의 첫번째 숫자에 48을 더하는 것.
od -> 49
pd -> 50
qd -> 51
oe -> 49
[ABCDE]{1}d -> 49
뒤 0D는 글자 수에 영향을 받음.
8글자 0D, 3글자 08.
```