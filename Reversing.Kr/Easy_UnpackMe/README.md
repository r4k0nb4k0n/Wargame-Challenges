# Easy Unpack

## Problem
* [Easy_UnpackMe.zip](./Easy_UnpackMe.zip)
	- Easy_UnpackMe.exe
	- ReadMe.txt
		+ ReversingKr UnpackMe
		+ Find the OEP
		+ ex) `00401000`

## Background Knowledge
* [Packing/Unpacking/Patching](https://resources.infosecinstitute.com/unpacking-reversing-patching/)
	- Packing is the process of compressing an exe,including the data and decompressing function with the compressed exe itself.
	- Unpacking is the reverse of this; it’s a process of identifying the decompressing function and extracts the original data out of exe.
	- Goals of packing:
		+ To reduce the size of exe
		+ To obfuscate the data, in case of malwares
* [What's the differences between Address of Entry Point and Original Entry Point? - Stack Overflow](https://stackoverflow.com/questions/46108236/whats-the-differences-between-address-of-entry-point-and-original-entry-point)
	- once the stub runs, it will transfer control to the address of the original entry point so the modified program still works (or appears) to work as normal.
	- OEP

## Tools
* PEStudio
* x32dbg

## Explanation
![](./1.PNG?raw=true)
* PEStudio로 해당 PE 파일을 열어보았다.
* 특이한 섹션들을 볼 수 있다.
	- `.Gogi`
		+ Start from `0x00409000`.
	- `.GWan`
		+ Start from `0x0040A000`.

![](./2.PNG?raw=true)
* 노란색은 모듈에서 함수를 직접 불러오는 곳을 나타낸다.
* 빨간색은 XOR 연산을 이용해 원래 코드를 복구하는 곳을 나타낸다.
* 하늘색은 원상 복구된 코드를 나타낸다.
* 모듈에서 함수를 직접 불러오는 것과 XOR 연산을 이용해 원래 코드를 복구하는 작업을 마친(Unpacking) 이후인 `0x00401150`이 OEP이다.

## Review
* 길어도 쫄지 말고 차근차근 찾아보자.
* OEP를 찾는 것도 좋지만 PE 파일 구조에 대해서 더 공부하자.
	- [연구실 :: Unpacking 관련 - PE 내용 정리 #1](https://procdiaru.tistory.com/52)
	- [연구실 :: Unpacking 관련 - PE 내용 정리 #2](https://procdiaru.tistory.com/53)
