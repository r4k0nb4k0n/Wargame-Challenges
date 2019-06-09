# Music Player

## Problem
* [Music_Player.zip](./Music_Player.zip)
	- `msvbvm60.dll`
	- `Music_Player.exe`
	- `ReadMe.txt`
		+ This MP3 Player is limited to 1 minutes.
		+ You have to play more than one minute.
		+ There are exist several 1-minute-check-routine.
		+ After bypassing every check routine, you will see the perfect flag.

## Tools
* PEStudio
* [e2eSoft VSC](https://www.e2esoft.com/vsc/)
	- Emulates Audio Device.
* VB Decompiler
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* PEStudio로 해당 PE 파일을 열어보았다.
* 다음과 같은 특성을 알 수 있다.
	- 32-bit
	- GUI
	- Microsoft Visual Basic
	- use Korean
	- use Unicode UTF-16, Little Endian

![](./2.PNG?raw=true)
* `A problem occurred in initializing MCI.`/`MCI를 초기화하는 데 문제가 발생했습니다.` 라는 오류가 뜬다.
* ** 아무래도 리버싱을 하는 환경이 VM이라 오디오 장치가 없는 것이 원인일 것이다. **

![](./3.PNG?raw=true)
* e2eSoft의 VSC를 설치하여 가상 오디오 장치를 설치하였다.
* 다음과 같이 재생 장치가 추가되어 있으면 MCI 초기화 오류는 뜨지 않는다.

![](./4.PNG?raw=true)
* PEStudio에서 해당 PE 파일이 Visual Basic으로 만들어진 Signature가 있다는 것을 알아냈으므로, 해당 PE 파일을 VB Decompiler로 열어보았다.
* 다음과 같이 Form과 Procedure들을 볼 수 있다.
* 문제 요약인 **1분 미리듣기 해제**와 관련된 것들은 다음 Procedure들로 유추할 수 있다.
	- `CMD_PLAY_Click_4038D0`
	- `TMR_POS_Timer_4044C0`
	- `TMR_Timer_404800`

![](./5.PNG?raw=true)
* x32dbg에서 해당 PE파일을 열어보았다.
* `CMD_PLAY_Click_4038D0`의 call graph를 그려보았다.
* 오류 시 알림창을 띄우는 것을 제외하고는, 음악 파일을 불러와서 재생하는 것이 끝이다.

![](./6.PNG?raw=true)
* `TMR_POS_Timer_4044C0`의 call graph를 그려보았다.
* 첫번째 노란색 칸.
	- `0xEA60`(`60000 ms`)와 비교.
* 빨간색 칸.
	- 1분 이상이면 `1분 미리듣기만 가능합니다`라는 알림창을 띄운다.
* 첫번째 파란색 칸.
	- 특정 조건 시 `LI`라는 문자열을 어디엔가 복사한다.
	- flag에 관련된 문자열로 추측해본다.
* 두번째 노란색 칸.
	- `0xEA6A`(`60010 ms`)와 비교.
* 두번째 파란색 칸.
	- 1분 하고도 10ms 이상이면 `are`라는 문자열을 생성하고 이를 어디엔가 복사한다.
	- flag에 관련된 문자열로 추측해본다.

![](./7.PNG?raw=true)
* `TMR_Timer_404800`의 call graph를 그려보았다.
* 재생 시간 문자열(`00:?? / 01:00`)의 앞부분을 떼어와 실제 재생 시간이 1분을 초과하였는지 따져보고, 1분을 초과했다면 Window의 Title에 Flag가 나타난다.

![](./8.PNG?raw=true)
* 일부 `jmp` 분기문에서 점프하지 않고 `EIP`를 조작하여 특정 코드를 실행하였다.
	- ![](./8_1.PNG?raw=true)
	- ![](./8_2.PNG?raw=true)
	- ![](./8_3.PNG?raw=true)
* 다음과 같이 Window의 Title에 Flag가 나타나는 것을 볼 수 있다.

## Review
* 다른 분들의 풀이를 보니, 대부분 재생 시간 상수(1분, `0xEA60`, `0xEA6A`)를 수정하고 이후에 나타나는 예외 오류를 안뜨게 만들어 Flag를 찾았다.
* `LI`와 `are`가 Flag에 관련된 문자열이라고 추측한 게 뽀록인 것 같긴 하다.
