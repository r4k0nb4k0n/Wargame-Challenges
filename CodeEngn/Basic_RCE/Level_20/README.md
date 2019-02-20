# Basic RCE Level 20

## Problem
* 이 프로그램은 Key파일을 필요로 하는 프로그램이다. 
* 'Cracked by: CodeEngn!' 문구가 출력 되도록 하려면 crackme3.key 파일안의 데이터는 무엇이 되어야 하는가 
* Ex) 41424344454647 
* (정답이 여러개 있는 문제로 인증시 맞지 않다고 나올 경우 Contact로 연락주시면 확인 해드리겠습니다) 

## Tool
* ExeinfoPe
* PEiD
* HxD
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe와 PEiD로 열어보았다.
* 패킹되어 보이진 않았다.

![](./2.PNG?raw=true)
* x32dbg로 PE 파일을 분석해보았다.
* 다음과 같이 작동한다.
	- `CRACKME3.KEY` 파일이 PE 파일과 같은 폴더 안에 있어야 한다.
	- `CRACKME3.KEY` 파일 내용의 길이는 `0x12 bytes`이어야 한다.
	- `CRACKME3.KEY`의 앞부분 바이트들과 `ABCD...MNO`의 XOR 연산 루프를 통해 크래커의 이름을 생성한다.
		+ 한 글자씩 XOR 연산을 한다.
		+ XOR 연산의 결과가 `00`이 되면 멈춘다.
	- 생성된 크래커의 이름의 아스키코드값 합을 `0x12345678`과 XOR 연산을 한 결과값을 검증값으로 활용한다.
	- `CRACKME3.KEY`의 `0x0E ~ 0x11` 범위의 바이트들을 가져온다. 그리고 이를 위 검증값과 비교한다.
	- 같으면 `Cracked by (생성된 크래커의 이름)! ...` 내용의 창이 뜨고, 다르면 아무 변화가 없다.

![](./3.PNG?raw=true)
* HxD로 다음과 같이 작성했다.
	- 첫 8 bytes는 `CodeEngn`과 `ABCDEFGH`의 XOR 연산값인 `02 2D 27 21 00 28 20 26`을 넣었다. 그래야 `02 2D 27 21 00 28 20 26`와 `ABCDEFGH`의 XOR 연산 루프의 결과가 `CodeEngn`이 되기 때문이다.
	- `0x08`번째 바이트에 `I(0x49)`를 넣어 XOR 연산 결과가 `NULL(0x00)`이 되도록 하여 크래커 이름 생성을 거기서 멈추도록 했다.
	- `0x0E ~ 0x11` 바이트들은 `0x1234557B`이다. 이는 `CodeEngn`의 아스키코드값들 합인 `0x00000303`과 `0x12345678`의 XOR 연산값, 즉 검증값이다.
	- `0x12` 바이트는 `0x12` 바이트 길이를 맞추기 위해 `NULL(0x00)`값을 넣었다.

![](./4.PNG?raw=true)
* 다음과 같이 통과함을 알 수 있다.