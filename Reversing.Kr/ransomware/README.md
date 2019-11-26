# Ransomware

## Problem
* [`ransomware.zip`](./ransomware.zip)
    - `file`
	- `run.exe`
    - `readme.txt`

```

Decrypt File (EXE)


By Pyutic

```

## Tools
* ExeinfoPe
* UPX
* x32dbg
* HxD
* Cryptii

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 `run.exe`을 열어보았더니 **UPX로 패킹**된 것을 확인했다.
* 이를 **언패킹**한 `run.unpacked.exe`을 ExeinfoPe로 열어보았더니 다음과 같은 특징을 알 수 있다.
	- Windows Console
	- Microsoft Visual C++
	- 32bit

![](./2.PNG?raw=true)
* `run.unpacked.exe`를 x32dbg로 열어서 분석 및 주석 작업을 마치고 다음과 같이 그래프로 나타내보았다.
* 작동 흐름을 요약하자면 다음과 같다.
    1. Key를 문자열로 입력받는다.
    2. `file`을 열고 내용을 메모리에 저장한다.
    3. 메모리에 저장된 `file`의 내용을 입력받은 `Key`를 이용하여 복호화한다.
        - **`Encrypted ^ Key(Repeated) ^ 0xff(Repeated) = Decrypted`**
    4. 복호화한 내용을 `file`에 그대로 덮어쓴다.
        - `Key`가 정상이라면 `file`은 성공적으로 복호화된다.
        - `Key`가 정상이 아니면 `file`은 오히려 망가진다.
* `Key`를 구해야 한다.

![](./3.PNG?raw=true)
* `readme.txt`의 내용에 따르면 `file`은 EXE 파일임을 알 수 있다.
    - `Decrypt File (EXE)`
* **XOR 연산으로 암복호화가 되므로, 정상 EXE 파일의 내용과 비교하여 `Key`를 유추할 수 있다**.
    - File signature `MZ`
    - DOS Stub message `This program cannot be run in DOS mode`

![](./4.PNG?raw=true)
* `run.unpacked.exe`를 이용하여 `file`을 복호화하여 `file.decrypted` 파일을 생성했다.
* `file.decrypted`는 UPX로 패킹된 것을 알 수 있다.
* 이를 언패킹하여 `file.decrypted.unpacked` 파일을 생성했다.

![](./5.PNG?raw=true)
* `file.decrypted.unpacked` 파일에서 문자열을 탐색해보면 다음과 같이 키를 알아낼 수 있다.
