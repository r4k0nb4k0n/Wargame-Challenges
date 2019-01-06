# 21

## Problem
```
What is a Solution Key?
Is it a Puzzle?
```

![](./monitor.jpg?raw=true)

## Background Knowledge
* [JPEG File Interchange Format - Wikipedia](https://en.wikipedia.org/wiki/JPEG_File_Interchange_Format)
	- SOI. Start of Image. `FF D8`.
	- JFIF-APP0 APP0 marker. `FF E0`.
	- EOI. End of Image. `FF D9`.
- [JPEG 파일 구조](http://cometkorea.tistory.com/56)
	- DQT Marker. `FF DB`.

## Tool
* HxD

## Inspection and Solution
* `monitor.jpg`에서 알아낸 것은 다음과 같다.
	- `H4??????N_TH3_MIDD33_4TT4CK`
	- 화질이나 해상도도 안좋은게 1.40MB씩이나 나간다. 틀림없이 무언가 숨겨져 있는 것이 틀림없다.
* HxD로 열어서 SOI + APP0 marker(`FF D8 FF E0`)와 EOI(`FF D9`)를 찾아보았다.
	- ![](./1.PNG?raw=true)
		+ SOI + APP0 marker(`FF D8 FF E0`)
		+ 15개.
	- ![](./2.PNG?raw=true)
		+ EOI(`FF D9`)
		+ 16개.
		+ 맨 마지막을 제외하곤 3번씩 패턴이 동일하다.
* 맨 마지막 `FF D9`에서 마지막에서 두번째 `FF D9` 전까지의 데이터를 살리기 위해 `15번째 EOI + 2 bytes` ~ `16번째 EOI`(`151C10`~`1670CA`)를 복사하고 새 파일에 붙여넣는다.
* 정상적으로 만들어진 JPG 파일과 복사한 내용을 비교한다.
	- ![](./3.PNG?raw=true)
		+ DQT Marker(`FF DB`)부터는 비슷해보인다.
		+ 정상 파일에서 선택한 부분을 붙여넣어본다.
* 정상 파일에서 선택한 부분을 DQT Marker(`FF DB`) 전까지 덮어씌우고 저장하면 다음과 같은 사진이 나타난다.
	- ![](./hidden.jpg?raw=true)
* `H4CC3R_IN_TH3_MIDD33_4TT4CK` 임을 유추할 수 있다.

## Review
* 혹시 몰라서 다른 풀이를 살펴보니 툴을 이용해서 좀더 쉽게 풀 수 있다는 것을 깨달았다.
* WinHex를 실행하고 `monitor.jpg`를 연 뒤, Tools - Disk Tools - File Recovery by Type...를 실행한다.
    - ![](./4.PNG?raw=true)
* File Header를 찾아서 이를 기준으로 파일을 복구하는 것 같다. `Pictures`에 체크하고 `Complete byte-level search` 선택 후 진행한다.
    - ![](./5.PNG?raw=true)
* 다음과 같이 숨겨진 이미지들을 찾았다. 여기서 확실하게 키를 알아낼 수 있다.
    - ![](./6.PNG?raw=true)