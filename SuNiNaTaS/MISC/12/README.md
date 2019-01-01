# 12

## Problem
```
[Mission!]
suninatas.com에 관리자로 로그인 하세요!
Login as Admin at suninatas.com!
```
## Inspection
* http://suninatas.com/admin/ 가 존재하고, 다음과 같은 QR Code가 있다.
	- ![](./qrcode.jpg?raw=true)

```
Python 2.7.6 (default, Nov 13 2018, 12:45:42)
[GCC 4.8.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import qrtools
>>> qr = qrtools.QR()
>>> qr.decode('qrcode.jpg')
True
>>> print qr.data
MECARD:N:;TEL:;EMAIL:;NOTE:;URL:http://suninatas.com/admin/admlogin.asp;ADR:;
>>>
```
* QR Code를 decode한 결과는 `MECARD:N:;TEL:;EMAIL:;NOTE:;URL:http://suninatas.com/admin/admlogin.asp;ADR:;`이다.

* http://suninatas.com/admin/admlogin.asp 에 [`admlogin.swf`](./admlogin.swf.original)이 있다. 로그인 폼처럼 생겼다.

```
$ flasm -x admlogin.swf.original
...
$ flasm -d admlogin.swf.decompressed > admlogin.flm
```
* [`flasm`](http://flasm.sourceforge.net/)을 사용하여 `admlogin.swf`를 disassemble한다.

* [`admlogin.flm`](./admlogin.flm)을 살펴보니 올바른 ID,PW 및 Auth 값이 나온다.

## Solution
* http://suninatas.com/admin/ 에 접속한다. (guessing)
* 여기서 나오는 [qrcode.jpg](./qrcode.jpg)를 디코드한다.
* 디코딩 결과에서 나온 http://suninatas.com/admin/admlogin.asp 로 접속한다.
* 여기서 나오는 [admlogin.swf](./admlogin.swf.original)을 디스어셈블한다.
* [디스어셈블 결과](./admlogin.flm)에서 나오는 ID, PW, Auth값을 얻고 통과한다.