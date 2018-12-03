# collision

### Problem
```
Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw:guest)
```

### Background Knowledge
* [RFC 1321](https://tools.ietf.org/html/rfc1321)
	- The algorithm takes as input a message of arbitrary length and produces as output a 128-bit "fingerprint" or "message digest" of the input.
* [MD5 - Wikipedia](https://en.wikipedia.org/wiki/MD5)
	- It can still be used as a checksum to verify data integrity, but only against **unintentional corruption**.
	- One basic requirement of any cryptographic hash function is that it should be **computationally infeasible** to find two distinct messages which hash to the same value. MD5 fails this requirement catastrophically; such collisions can be found in seconds on an ordinary home computer.
* [Collision attack - Wikipedia](https://en.wikipedia.org/wiki/Collision_attack)
	- Find two different messages `m1` and `m2` such that `hash(m1) = hash(m2)`.

### Inspection
```
col@ubuntu:~$ ls -l
total 16
-r-sr-x--- 1 col_pwn col     7341 Jun 11  2014 col
-rw-r--r-- 1 root    root     555 Jun 12  2014 col.c
-r--r----- 1 col_pwn col_pwn   52 Jun 11  2014 flag
```
* `ls -l`의 결과이다. `flag`는 읽기 권한이 `col` 계정으로서는 없다.

```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```
* [`col.c`](./col.c)
	- `passcode`는 반드시 `20 bytes` 이어야 한다.
	- `hashcode = 0x21DD09EC = 568134124`
	- `unsigned long check_password(const char* p)`는 `p`를 `int*`로 캐스팅하여 `4 bytes`씩 읽어들인 값들의 합을 돌려준다.
	- `hashcode`와 `check_password(passcode)`가 서로 같아야 `flag`을 알 수 있다.
	
### Trial and error
* `hashcode = 0x21DD09EC = 568134124`
	- `= 113626824.8 × 5`
	- `= (113626824 × 5) + (0.8 × 5)`
	- `= (113626824 × 5) + 4`
	- `= (113626824 × 4) + 113626828`
		+ `113626824 = 00000110 11000101 11001110 11001000`
		+ 1바이트씩 끊어서 ASCII 코드로 해석하면 `ÅÎÈ`.
		+ `113626828 = 00000110 11000101 11001110 11001100`
		+ 1바이트씩 끊어서 ASCII 코드로 해석하면 `ÅÎÌ`.
* `ÅÎÈÅÎÈÅÎÈÅÎÈÅÎÌ`로 해보자.
	- `./col ÅÎÈÅÎÈÅÎÈÅÎÈÅÎÌ`
		+ 터미널 상으로는 직접 입력이 안되어서 쉘 스크립트로 실행했다.
		+ `passcode length should be 20 bytes`
	- ``./col `printf '%b' '\006\305\316\310\006\305\316\310\006\305\316\310\006\305\316\310\006\305\316\314'` ``
		+ 쉘 상에서 8진수를 문자로 출력하여 `passcode`를 넘겨주었다.
		+ `wrong passcode.`
* 혹시 Big-endian과 Little-endian을 고려하지 않아서 이런 것일까?
	- `ÅÎÈ ÅÎÈ ÅÎÈ ÅÎÈ ÅÎÌ`
		+ `06 C5 CE C8 06 C5 CE C8 06 C5 CE C8 06 C5 CE C8 06 C5 CE CC`
		+ 이를 Big-endian으로 `4 bytes`씩 읽은 값의 합이 `hashcode`와 같다.
	- `ÈÎÅ ÈÎÅ ÈÎÅ ÈÎÅ ÌÎÅ`
		+ `C8 CE C5 06 C8 CE C5 06 C8 CE C5 06 C8 CE C5 06 CC CE C5 06`
		+ 이를 Little-endian으로 `4 bytes`씩 읽은 값의 합이 `hashcode`와 같다.
* Little-endian을 고려하여 `passcode`를 생성해야 한다.

### Solution
* `x + y + z + u + v = hashcode = 0x21DD09EC = 568134124`
	- `x`, `y`, `z`, `u`, `v`는 `4 bytes integer` 범위 안의 수이다.
* `x = y = z = u = 113626824`, `v = 113626828`이라고 하자.
	- `x = y = z = u = 0x06C5CEC8`
	- `v = 0x06C5CECC`
* 이들을 이어붙이되, `./col`이 실행되는 시스템 환경에 맞는 Little-endian을 고려한다.
	- `xyzuv`(Big-endian)
		+ `06C5CEC8 06C5CEC8 06C5CEC8 06C5CEC8 06C5CECC`(가독성을 위해 `4 bytes` 마다 띄어쓰기를 넣었다.)
	- `xyzuv`(Little-endian)
		+ `C8CEC506 C8CEC506 C8CEC506 C8CEC506 CCCEC506`
		+ 이는 Big-endian인 위 바이트들을 Little-endian으로 바꾼 것이다. 쉽게 말해서 `4 bytes`마다 바이트들의 순서를 거꾸로 했다.
* `passcode_in_hex = C8CEC506C8CEC506C8CEC506C8CEC506CCCEC506` 라고 하자.
* `` ./col `echo passcode_in_hex | xxd -r -p` ``를 실행한다.
* `flag`를 뱉는다.

### Review
* 알게 된 것.
    - MD5가 데이터 무결성을 검증하기 위한 해시 함수로서 만들어졌지만, collision attack이 일반 컴퓨터에서 수 초 내에 가능하다는 것을 알았다.
    - [Big-endian과 Little-endian의 차이점](http://www.ktword.co.kr/abbr_view.php?m_temp1=2353)을 알았다.
        + Big-endian : 큰 단위의 바이트가 앞에 온다.
        + Little-endian : 작은 단위의 바이트가 앞에 온다.
    - x86은 Little-endian이다.
    - 쉘에서 `` ` ` ``은 해당 명령의 결과를 가져다 쓸 수 있는 표시이다.
    - [`xxd`](https://www.systutorials.com/docs/linux/man/1-xxd/)
        + `xxd -r -p` : Hex값을 받아서 이를 Ascii 문자로 출력해준다.
* 궁금한 것.
    - Solution을 Python 스크립트로 작성하고 싶다.
        + `x + y + z + u + v = hashcode = 0x21DD09EC = 568134124` 이고, `x`, `y`, `z`, `u`, `v`는 `4 bytes integer` 범위 안의 수일 때, `x`, `y`, `z`, `u`, `v`의 조합?의 경우들을 구하고 싶다. 그냥 반복문으로 하면 `(10^31)^5`만큼의 반복문이 돌아간다. 이를 좀더 효율적으로 계산해보고 싶다.