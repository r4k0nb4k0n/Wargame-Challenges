# CSHOP

## Problem
* [`CSHOP.zip`](./CSHOP.zip)
    - `CSHOP.exe`

## Tools
* ExeinfoPe
* dnSpy v6.0.5 (32-bit)

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `CSHOP.exe`를 열어보았다.
* 문제 이름과 파일 이름에서도 알 수 있지만 해당 파일은 C#으로 작성된 것을 유추할 수 있다.

![](./2.PNG?raw=true)
* `CSHOP.exe`를 실행했을 때 나타나는 화면이다.
* Window만 뜨고 빈 Form만 있다.

![](./3_1.PNG?raw=true)  
![](./3_2.PNG?raw=true)  
* `CSHOP` - `FrmMain` - `InitializeComponent()`
    - 여러 개의 label과 한 개의 button을 생성한 후 2차원 좌표계로 위치를 지정한 것을 볼 수 있다.
    - button의 click 이벤트 핸들러 함수를 연결하는 것을 볼 수 있다.
* `CSHOP` - `FrmMain` - `\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD_Click()`
    - 여러 개의 label에 Text 값을 지정해주는 것을 볼 수 있다.
* 이는 Auth값으로 추측할 수 있다.

![](./4.PNG?raw=true)
* 유니코드로 작성된 변수명들을 보기 쉽게 바꾼다.
* `CSHOP` - `FrmMain` - `\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD_Click()`의 내용을 실행했을 때 바뀌는 Text 값들을 찾는다.
* 이를 label의 x 위치값으로 오름차순 정렬하여 보면 화면에서 그려지는 것과 동일한 순서대로 볼 수 있다.
* 이는 Auth값으로 추측하는 것이다.
