# Advanced RCE Level 07

## Problem
* Name이 CodeEngn일때 Serial은 `28BF522F-A5BE61D1-XXXXXXXX` 이다. 
* `XXXXXXXX` 를 구하시오 

## Tool and ...
* ExeinfoPe
* dnSpy
* Monodevelop

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* 닷넷 언어 C#로 작성되었음을 알 수 있다.

![](./2.PNG?raw=true)
* dnSpy로 해당 PE 파일을 열어보았다.
* `textBox1`이 Name, `textBox2`가 Serial을 입력하는 곳이다.
* `button1`이 Check, Serial 확인 코드를 실행하는 버튼이다.
* Name의 길이는 5 이상 27 이하이고, Serial의 길이는 26이며, `/^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{8}-[A-Fa-f0-9]{8}$/` 형식이어야 한다.
* 다음 5개의 값을 이용한다.
	+ `num = Convert.ToUInt32('Serial의 첫번째 토큰', 16)` -> `28BF522F`
	+ `num2 = Convert.ToUInt32('Serial의 두번째 토큰', 16)` -> `A5BE61D1`
	+ `num3 = Convert.ToUInt32('Serial의 세번째 토큰', 16)` -> `알아내야 할 값`
	+ `num4 = ytrewq.qwerty(Form.dfgsf(this.TextBox1.Text))` -> `CodeEngn`의 변형
	+ `hashCode = (uint)this.TextBox1.Text.GetHashCode()` -> `"CodeEngn"`의 해시값.

![](./3.PNG?raw=true)
* [`decrypt.cs`](./decrypt.cs)
* dnSpy에서 디컴파일하여 얻은 코드들을 최대한 그대로 활용하여, 세번째 코드를 얻을 수 있는 브루트포싱 작업을 진행했다.
* `vxzzz()`안의 `uint num = pgdsfa % 57u - 1u;`는 `0xFFFFFFFF`가 되어 루프에 빠질 수 있다. 이는 `num`이 `1` 이상 `56` 미만일 경우만 연산하도록 설정했다.
* **아키텍처 등 환경에 따라 해시값이 달라지는 것을 알게 되었다.**
* 따라서 x86일 때 나온 값으로 진행한다.

![](./4.PNG?raw=true)
* `07.exe` 을 x86으로 실행하기 위해 다음과 같이 설정한다.
* 저장한다.

![](./5.PNG?raw=true)
* `07.exe` 을 x86으로 실행하기 위해 다음과 같이 설정한다.
* 저장한다.

![](./6.PNG?raw=true)
* 다음과 같이 x86으로 실행된 파일에서 x86일때 나온 값으로 진행했더니 통과함을 알 수 있다.

## Why?

| Image | Architecture | Description |
|:-----:|:------------:|:------------|
|![](./x86_on_x64.PNG?raw=true)|x86|`"CodeEngn"`의 해시값 `9E1E73D5`. 세번째 토큰 `11E051D1` 찾음.|
|![](./x64_on_x64.PNG?raw=true)|x64|`"CodeEngn"`의 해시값 `82AD30CB`. 세번째 토큰 찾지 못함.|
* x86으로 컴파일한 `decrypt_x86.exe`를 통해 찾은 `11E051D1`을 이용하여 통과 여부를 확인해보았으나, 통과가 되지 않는 것을 알 수 있다.
* 이는 `07.exe`가 x64로 작동하여 `"CodeEngn"`의 해시값이 `9E1E73D5`가 아닌 `82AD30CB`로 나왔기 때문이다.
* 아키텍처 등 환경에 따라 해시값이 달라지는 이유.
	* [String.GetHashCode Method (String) | Microsoft Docs](https://docs.microsoft.com/ko-kr/dotnet/api/system.string.gethashcode?view=netframework-4.7.2#System_String_GetHashCode)
		+ The value returned by GetHashCode() is **platform-dependent**. It differs on the 32-bit and 64-bit versions of the .NET Framework. It also can differ between versions of the .NET Framework and .NET Core.
	* [C# GetHashCode (String Method) - Dot Net Perls](https://www.dotnetperls.com/gethashcode)
		+ It uses several magic constants and **low-level pointer arithmetic** to achieve its performance requirement.
		+ GetHashCode is called when we use a Hashtable or Dictionary with string keys. It has unsafe code that uses **pointer arithmetic**, bit shifting and an unwound loop.
	* 중간 언어로 구현된 내용을 보니, 포인터 연산을 사용하는 것을 알 수 있다.
	* x86, x64에 따라 포인터 크기가 4바이트, 8바이트로 달라진다.
	* **아키텍처에 따라 달라진 포인터 크기로 인해 포인터 연산 결과가 상이하고, 이는 곧 해시값이 달라지는 이유중 하나로 추측할 수 있다.**


## Reference
* [String.GetHashCode Method (String) | Microsoft Docs](https://docs.microsoft.com/ko-kr/dotnet/api/system.string.gethashcode?view=netframework-4.7.2#System_String_GetHashCode)
* [C# GetHashCode (String Method) - Dot Net Perls](https://www.dotnetperls.com/gethashcode)