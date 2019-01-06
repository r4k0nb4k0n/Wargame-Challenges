# 28

## Problem
```
Do you have a password?

암호를 풀어야 뭘 볼수 있지! 암호가 있기나 한건가!
이 문제를 낸 사람은 너무 쉬워서 사람들이 빨리 풀지
않을까 걱정하다가 시름시름 앓고 있다는 전설이 있다.
Does it have a real password?
I am afraid that this challenge is very esay.
You need not do brute-force

down

Thanks to : heizelnet
```

## Background Knowledge
* [Zip 압축파일 Header 분석](http://downrg.com/403)
    - ![](./1.PNG?raw=true)
    - `50 4B 03 04` -> .ZIP 헤더
    - Offset 6, 2 Bytes -> general purpose bit flag
* [ZIP File Format Specification](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)
    -  4.4.4 general purpose bit flag: (2 bytes)
        + Bit `0`: If set, indicates that the file is encrypted.
        
## Tool
* HxD

## Inspection and Solution
* **Big-endian 기준으로 읽어야 한다.**
* HxD에서 해당 압축 파일을 불러와 헤더(`50 4B`)를 검색해보니 Offset 6 지점에 2바이트만큼 bit flag가 있다.
    - ![](./2.PNG?raw=true)
    - Local Header(`50 4B 03 04`)에선 Offset 6 지점이다.
    - Central Header(`50 4B 01 02`)에선 Offset 8 지점이다.
* 해당 ZIP 파일의 bit flag의 LSB(Least Significant Big)를 0으로 설정한다.
    - ![](./3.PNG?raw=true)
    - `09 08`은 Big-endian 기준의 Hex값이다. 
    - 이를 Little-endian 기준의 Binary로 보면 다음과 같다.
        + `00001000 00001001` : Bit `0`, 즉 LSB가 1로 설정되어있고, 이는 파일이 암호화되었다고 나타낸다.
    - LSB를 0으로 설정하고 Big-endian 기준의 Hex값으로 나타내면 다음과 같다.
        + `08 08`
* 이를 저장하고 압축을 풀면 다음과 같은 파일들이 있다.
    - `So_Simple_Touched.zip`
        + `Am_I_key.zip`
        + `Am_I_key2.txt`
        + `Am_I_key3.txt`
* 텍스트 파일들은 `Dummy` 문자열이 반복되면서 채워져있다.
* `Am_I_key.zip`의 압축을 풀면 `There_is_key.txt`가 있고, 내용은 다음과 같다.

```
Isn't it so easy?

Take it.

dGE1dHlfSDR6M2xudXRfY29mZmVl
```

* `dGE1dHlfSDR6M2xudXRfY29mZmVl`를 Base64 디코드하면 Authkey가 나온다.