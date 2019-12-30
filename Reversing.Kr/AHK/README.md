# AHK

## Problem
* [`AHK.zip`](./AHK.zip)
    - `ahk.exe`
    - `readme.txt`
```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

AuthKey = un_md5(DecryptKey) + " " + un_md5(EXE's Key)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

Ex:)
 DecryptKey = 1dfb6b98aef3416e03d50fd2fb525600
 EXE's  Key = c944634550c698febdd9c868db908d9d
 => AuthKey = visual studio

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

By Pyutic
```

## Tools
* ExeinfoPe
* [Kalamity/Exe2AhkPatched](https://github.com/Kalamity/Exe2AhkPatched)
    - `.\Exe2AhkAReturnPassword.exe`
    - `.\Exe2AhkAnyPassword.exe`

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `ahk.exe`을 열어보았다.
* AutoHotKey로 제작된 PE 파일임을 알 수 있다.
* [AutoHotKey](https://www.autohotkey.com/)
    - 특징
        - Windows 기반 자동화 스크립트 언어.
        - GUI 쉽게 제작 가능.
    - 디컴파일([오토핫키 버전 별 디컴파일](https://sanseolab.tistory.com/61))
        - 여러 버전이 있다.
            - 1.0 버전 B
                - 2009년 안정화 이후 추가 개발 없음
            - 1.1 버전 L
                - 다른 개발자가 기능 추가하여 공식 버전으로 올라감
* `ahk.exe`는 1.0 버전 B이다. 따라서 위 언급한 포스팅과 같이 디컴파일을 시도한다.

![](./2.PNG?raw=true)
* [Kalamity/Exe2AhkPatched](https://github.com/Kalamity/Exe2AhkPatched)을 `git clone`한다.
* 다음과 같이 Decrypt key를 먼저 알아낸 후 스크립트 안 key를 알아낸다.
    - DecrptKey: `220226394582d7117410e3c021748c2a`
    - Exe's Key: `54593f6b9413fc4ff2b4dec2da337806`

![](./3.PNG?raw=true)
* 다음과 같이 md5와 상응하는 문자열을 찾는다.
* AuthKey는 `isolated pawn`이다.
