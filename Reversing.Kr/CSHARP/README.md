# CSHARP

## Problem
* [`CSharp.exe`](./CSharp.exe)

## Tools
* ExeinfoPe
* dnSpy v6.0.5
* [Cryptii](https://cryptii.com/)

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `CSharp.exe`을 열어보았다.
* C#으로 짠 PE 파일임을 알 수 있다.

![](./2-1.PNG?raw=true)
![](./2-2.PNG?raw=true)
![](./2-3.PNG?raw=true)
![](./2-4.PNG?raw=true)
* dnSpy로 해당 PE 파일을 열어보았다.
* 다음과 같이 작동한다.
    * `TextBox`에 특정 값을 입력하고 `btnCheck`를 클릭하면, `Form1.MetMetMet()` 함수에 입력한 값을 넣어주어 해당 값이 유효한지 판단해준다.
    * `Form1.MetMetMet()` 함수 내에서 `Form1.bb` 바이트들을 이용하여 새로운 동적 메소드를 생성하고, 해당 메소드를 이용해서 유효 여부를 판단한다.
    * `Form1.bb` 바이트들은 `Form1.ctor()` 생성자에서 초기화된다.
    * 이는 기존에 파싱이 되지 않는 손상된 메소드 `MetMett`에서 MethodBody를 긁어온 후 일부 바이트들을 수정한 것이다.
* 동적으로 생성된 메소드의 내용을 알 수 있다면, 어떤 값을 넣어야 유효한 지 알 수 있을 것이다.

![](./3-1.PNG?raw=true)
![](./3-2.PNG?raw=true)
![](./3-3.PNG?raw=true)
![](./3-4.PNG?raw=true)
* 동적으로 생성된 메소드에 중단점을 걸고, Step Into 계속 안으로 들어가본다.

![](./3-5.PNG?raw=true)
* 계속 안으로 들어가다보면 동적으로 생성된 메소드의 내용을 확인할 수 있다.
* 해당 코드를 이용하여 유효하게 판단될 수 있는 입력값을 생성해보았다. [`brute.py`](./brute.py)

![](./4.PNG?raw=true)
* 유효하게 판단될 수 있는 입력값이 base64 인코딩된 상태라 이를 디코딩해보았다.
* 다음과 같이 flag가 뜨는 것을 확인할 수 있다.
