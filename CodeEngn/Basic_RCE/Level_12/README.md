# Basic RCE 12

## Problem
* Korean : 
	- Key를 구한 후 입력하게 되면 성공메시지를 볼 수 있다 
	- 이때 성공메시지 대신 Key 값이 MessageBox에 출력 되도록 하려면 파일을 HexEdit로 오픈 한 다음 `0x????` ~ `0x????` 영역에 Key 값을 overwrite 하면 된다. 
	- 문제 : Key값과 + 주소영역을 찾으시오 
	- Ex) `7777777????????`
* English : 
	- You will see a success message after finding the key. 
	- If you would want the Key itself to replace the success message in the MessageBox, open up a Hex Editor and overwrite the key value in the offset range `0x????` ~ `0x????`. 
	- Q : find the key value and the offset range and write the solution in this format : `key????????` 
(first `????` for the start and the next 4 `?`s for the end). 

## Tool
* ExeinfoPe
* x32dbg
* HxD

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 열어보았다.
* 패킹되진 않았다.

![](./2.PNG?raw=true)
* x32dbg에서 열고 EntryPoint에 진입한 후 그래프를 그려보았다.
* `cmp eax, 7A2896BF`를 통과해야 통과 메시지가 나타난다.
* `7A2896BF`는 10진수로 `2049480383`이다.

![](./3.PNG?raw=true)
* HxD에서 `12.exe`를 연다.
* initialized data 영역에서 통과 메시지의 문자열들을 찾아본다.
	- `In the Bin` -> `0x0D30` ~ `0x0D39`
	- `Congratulation, you found the right key` -> `0x0D3B` ~ `0x0D61`
* 해당 문자열에 덮어씌우면 된다.

![](./4.PNG?raw=true)
* 다음과 같이 통과 메시지에 Key가 나타나는 것을 볼 수 있다.