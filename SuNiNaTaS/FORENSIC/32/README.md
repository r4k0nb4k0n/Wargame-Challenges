# 32

## Problem
```
Terrorist - Download

 
 
경찰청으로 부터 연쇄 테러 용의자로 부터 압수한 USB 이미지 분석을 의뢰 받았다.
최초 분석을 신입 직원에게 맡겼으나 Hex Editor로 여기 저기 둘러 보다 실수로 특정 부분이 손상되고 이미지가 인식되지 않는다.

당신은 포렌식 전문가의 자존심을 걸고 이미지를 살려 내고 다음 테러를 예방하는데 기여를 해야 한다.
1. 다음 테러 계획이 들어있는 문서의 수정 일시는? (UTC+9)
2. 다음 테러 장소는?

인증키 형식 : lowercase(MD5(YYYY-MM-DD_HH:MM:SS_장소)

예) lowercase(MD5(2016-03-28_13:00:00_Pink Lake)

======================================================================================

You got a USB image of terrorist from the National Police Agency.
A beginner made a USB image wrong, So your PC couldn't recognize it.

You should fix a USB image and prevent next terror.
Q1 : What is modified date/time of the file which contains next terror plan. (UTC+9)
Q2 : Where is the next terror target.

Auth Key = lowercase(MD5(YYYY-MM-DD_HH:MM:SS_place)

example) lowercase(MD5(2016-03-28_13:00:00_Pink Lake)

Thanks to : zulu093
```

## Background Knowledge
* [Design of the FAT file system - Wikipedia](https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system)
	- Layout
		+ Reserved sectors
			- Boot Sector
            - Magic code `0x55 0xAA` at the end of all boot sectors.
			- etc..
		+ FAT Region
			- Multiple File Allocation Tables...
		+ Root Directory Region
		+ Data Region
	- Directory table
		+ A directory table is a special type of file that represents a directory.
		+ Directory entry
			- 32 bytes.
			- Offset `0x0E`. 
				+ Bits 15-11 : Hour(0-23)
				+ Bits 10-5 : Minutes(0-59)
				+ Bits 4-0 : Seconds/2(0-59)
            - Offset `0x10`.
                + Bits 15-9 : Year(0 = 1980, 119 = 2099)
                + Bits 8-5 : Month (1-12)
                + Bits 4-0 : Day (1-31)
* [The FAT File System - TechNet](https://social.technet.microsoft.com/wiki/contents/articles/6771.the-fat-file-system.aspx)
	- ![](./0.PNG?raw=true)

## Tool
* WinHex

## Inspection and Solution
* 다운로드한 파일은 USB 이동식 디스크를 본뜬 931MB의 `IMG` 파일이다.
* 이를 WinHex에서 열어 보면 FAT32의 Magic code인 `0x55 0xAA`를 발견할 수 있다.
    - ![](./1.PNG?raw=true)
* 일단 [SuNiNaTaS FORENSIC 21](../21)의 Review에서 했던 것처럼 알려진 파일 헤더를 조사하여 파일들을 카빙?해본다.
    - ![](./2.PNG?raw=true)
        + Tools - Disk Tools - File Recovery by Type...
    - ![](./3.PNG?raw=true)
        + `Documents` 선택, `Complete byte-level search` 선택 후 확인.
* 꽤 많은 파일들이 나온 것을 볼 수 있다.
	 - ![](./4.PNG?raw=true)
		+ `000007.hwp`
			- 2차 테러 계획
		+ `000008.pdf`
			- Country Reports on Terrorism 2013
			- DPRK
		+ `000009.pdf`
			- Country Reports on Terrorism 2013
			- ROK
		+ `000010.hwp`
			- Operation K
			- SuNiNaTaS
			- Congratulation!
			- Auth key is "F1l3syst3m, 4lw4ys b3 r34dy"
* `000007.hwp`가 **다음 테러 계획이 들어있는 문서**임을 알 수 있다.
	 - ![](./5.PNG?raw=true)
	 	+ 장소 : **Rose Park**
* 파일 이름이 길다고 가정하고, `~1HWP`, `~1PDF` 등 확장자를 붙여 검색해보았다.
	 - ![](./6.PNG?raw=true)
	 - 위 4개의 파일들이 오프셋 기준으로 순차적으로 카빙되었다는 것을 볼 때, 먼저 나온 Directory entry가 `000007.hwp`임을 알 수 있다.
* `000007.hwp`의 Short entry를 따로 보자.
	- ![](./7.PNG?raw=true)
		- Offset `0x16`. Last Modified Time.
			+ `0x81 0x15`.
			+ Big-endian 기준으로는 `0x15 0x81`.
			+ Big-endian 기준의 Binary는 `00010101 10000001`.
				+ Bits 15-11 : Hour(0-23) -> `00010` -> `2`
				+ Bits 10-5 : Minutes(0-59) -> `101100` -> `44`
				+ Bits 4-0 : Seconds/2(0-59) -> `00001` -> `1`
			+ UTC+0 기준 `02:44:02`.
			+ **UTC+9 기준 `11:44:02`.**
		- Offset `0x18`. Last Modified Date.
			+ `0xBE 0x48`
			+ Big-endian 기준으로는 `0x48 0xBE`.
			+ Big-endian 기준의 Binary는 `01001000 10111110`.
				+ Bits 15-9 : Year(0 = 1980) -> `0100100` -> `36` -> `2016`
				+ Bits 8-5 : Month (1-12) -> `0101` -> `5`
				+ Bits 4-0 : Day (1-31) -> `11110` -> `30`
			+ **`2016-05-30`**
* Authkey를 만들 수 있다.
	- Auth Key = lowercase(MD5(YYYY-MM-DD_HH:MM:SS_place)
	- `lowercase(MD5(2016-05-30_11:44:02_Rose Park))`
	- ![](./8.PNG?raw=true)

## Review
* @ddddhkim이 좋은 툴들을 많이 소개해줬다. 이를 이용해서 다시 한번 풀어볼까 한다.
* [AccessData FTK Imager](http://marketing.accessdata.com/ftkimager4.2.0)
	- 최초 분석을 신입 직원에게 맡겼으나 Hex Editor로 여기 저기 둘러 보다 실수로 특정 부분이 손상되고 이미지가 인식되지 않는다.
	- 문제에서 이미지가 인식되지 않는다는 것을 전제로 내걸었다. 따라서 이 툴을 사용하기는 힘들 것 같다.
* `foremost`
	- 빨라서 좋긴 한데 `HWP`를 찾아주진 않는다.
	- [`foremost_audit.txt`](./foremost_audit.txt)
* `binwalk`
	- 구름IDE에서 너무 느려서 포기함.