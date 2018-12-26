# Basic RCE Level 01

## Problem
* Korean : 
HDD를 CD-Rom으로 인식시키기 위해서는 `GetDriveTypeA`의 리턴값이 무엇이 되어야 하는가 
* English : 
What value must `GetDriveTypeA` return in order to make the computer recognize the HDD as a CD-Rom 

## Tool
* x32dbg

## Explanation
![](./1.png)  
* 흐름
	- `c:\` 인자를 넣고 `GetDriveTypeA` 함수를 실행한 후, 리턴값이 `eax`에 저장된다.
	- `eax`를 `2`만큼 빼고, `0`이었던 `esi`에는 `3`을 더한다.
	- `eax`와 `esi`를 서로 비교한다.
		+ 서로 같으면, `I really think that your HD is a CD-ROM!`을 띄운다.
		+ 서로 다르면, `This is not a CD-ROM Drive!`를 띄운다.
* 리턴값이 2를 빼는 연산을 거친 후 `esi`의 `3`과 같으려면 `?`이어야 한다.
* [`GetDriveTypeA` function | Microsoft Docs](https://docs.microsoft.com/en-us/windows/desktop/api/fileapi/nf-fileapi-getdrivetypea)
	- Return Value
		+ `DRIVE_FIXED` `3`
		+ `DRIVE_CDROM` `?`