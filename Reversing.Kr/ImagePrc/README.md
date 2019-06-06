# ImagePrc

## Problem
* [`ImagePrc.exe`](./ImagePrc.exe)

## Tools
* ExeinfoPe
* PEiD
* x32dbg
* IDA 7.0
* PEStudio
* HxD
* mspaint

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe, PEiD로 해당 PE 파일을 열어보았다.
* 해당 PE 파일의 특성을 알 수 있다.
	- Win32
	- GUI
	- Microsoft Visual C++ 5.0/6.0

![](./2.PNG?raw=true)
* 해당 PE 파일을 실행해보았다.
* 창 안에 마우스를 클릭 및 드래그하여 그림을 그릴 수 있다.
* 색깔은 흰색 및 검은색만 있다.
* `Check` 버튼을 클릭했을 때 `Wrong`이라는 경고창이 뜬다.

![](./3.PNG?raw=true)
* x32dbg로 해당 PE 파일을 열어보았다.
* GUI 처리 담당 함수인 `@handlerFunc`의 call graph를 그려보았다.
* Check 버튼을 눌렀을 때
	- canvas의 내용을 불러온다.
	- canvas의 내용과 `.rsrc` 섹션에 저장된 내용을 `90000` bytes 만큼 비교한다.
		+ 완벽히 일치하지 않으면 `Wrong`이라는 경고창이 뜬다.
		+ 완벽히 일치하면 별다른 일이 없다.

![](./4.PNG?raw=true)
* IDA 7.0에서 해당 PE 파일을 열어보았다.
* canvas의 내용을 불러오는 부분을 보았다.
* canvas의 가로 길이와 세로 길이를 알 수 있다. `200 X 150`

![](./5.PNG?raw=true)
* PEStudio로 해당 PE 파일을 열어보았다.
* `.rsrc`를 덤프한다.
* 총 `90000` bytes.
* canvas의 가로 길이와 세로 길이 `200 X 150`.
* **즉 3만 개의 점인데 1개 점에 `3` bytes 씩 총 `90000` bytes 사용하므로 24비트 비트맵 파일로 바꿀 수 있을 것이다.**

![](./6.PNG?raw=true)
* 그림판을 이용하여 `200 X 150` 크기의 24비트 비트맵 파일을 생성한다.

![](./7.PNG?raw=true)
* HxD를 이용하여 `.rsrc` 덤프 내용을 비트맵 파일에 덮어쓴다.

![](./8.PNG?raw=true)
* 다음과 같이 그림 내용을 확인할 수 있다.
