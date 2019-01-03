# 10

## Problem
http://suninatas.com/Part_one/web10/reversing.zip

## Tool
* CFF Explorer
* IDA 32bit

## Explanation
![](./1.PNG?raw=true)
* CFF Explorer에서 열어보니 32비트 GUI Application이고, .NET을 사용했다는 것을 알 수 있다.

![](./2.PNG?raw=true)
* IDA 32bit에서 Microsoft.Net assembly로 열어보니 여러 함수들이 있었고, 이 중 `OK` 버튼에 엮인 함수를 보니 통과할 수 있는 문자열과 Auth key를 알 수 있었다.

## Review
* Auth key에 peid를 사용했냐고 물어보는 의미의 문장이 있길래, 이게 무엇인지 찾아봤다.
* [PEiD](https://www.aldeid.com/wiki/PEiD)
	- PEiD detects most common packers, cryptors and compilers for PE files.
	- It can currently detect more than 470 different signatures in PE files.
	- It seems that the official website (www.peid.info) has been discontinued. Hence, the tool is no longer available from the official website but it still hosted on other sites.
	
![](./3.PNG?raw=true)
* PEiD로 해당 파일을 열어보았다. C#, .NET이 뜬다.

![](./4.PNG?raw=true)
* 패킹이 되어있지 않다는 것을 알 수 있다.
* 이 툴을 사용하진 않았지만, 괜찮은 툴을 하나 더 알아낸 것 같다.
* IDA가 너무 사기가 아닌가 생각이 들기도 한다.

* 다른 풀이들을 보니, C#이어서 디컴파일러로 쉽게 읽을 수 있는 코드로 볼 수 있다고 한다.

![](./5.PNG?raw=true)
* 괜찮은 C# 디컴파일러인 JETBRAINS dotPeek으로 보았다. C#으로 쉽게 읽을 수 있다.

* C#은 프로그래밍 언어이고, 이를 이용해 만든 프로그램은 .NET Framework라는 가상머신에서 작동한다. 이는 Java와 JVM의 관계와 같다.