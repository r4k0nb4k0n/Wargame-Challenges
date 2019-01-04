# 14

## Problem
```
Do you know password of suninatas?
```
http://suninatas.com/Part_one/web14/evidence.tar

## Background Knowledge
* Reference.
    - [제타위키](https://zetawiki.com/)
    - [Understanding `/etc/shadow` file](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)
* 리눅스 패스워드 파일 `/etc/passwd`
    - 리눅스 계정 정보를 담고 있는 파일이다.
    - 이름과는 달리 패스워드 정보를 가지고 있지 않다.
    - 원래 패스워드 해시값을 가지고 있었지만, `/etc/shadow` 로 분리되고 해당 자리에 `x`가 들어간다.
    - `(a):(b):(c):(d):(e):(f):(g)`
        1. Username
        2. Password
        3. UID
        4. GID
        5. Description
        6. Home Directory
        7. Shell Environment
    - 예시
        + `root:x:0:0:root:/root:/bin/bash`
        + `gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh`
* 리눅스 쉐도우 파일 `/etc/shadow`
    - `/etc/passwd` 에 있는 계정들의 패스워드 부분을 암호화하여 저장한 파일이다.
    - `root`만 읽을 수 있는 권한(`400`)으로 설정 되어 있다.
    - `(a):(b):(c):(d):(e):(f):(g):(h):`
        1. Username
        2. Password : 암호화된 패스워드이다. 이는 최소 `8`-`12`글자 이상이면서 특수문자, 숫자, 알파벳 소문자 등을 포함해야 한다. 일반적으로 패스워드 포맷은 `$id$salt$hashed`로 설정되는데, `$id`는 GNU/Linux에서 사용된 알고리즘이다:
            + `$1$` is MD5
            + `$2a$` is Blowfish
            + `$2y$` is Blowfish
            + `$5$` is SHA-256
            + `$6$` is SHA-512
        3. Last password change (lastchanged) : Days since Jan 1, 1970 that password was last changed
        4. Minimum : The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
        5. Maximum : The maximum number of days the password is valid (after that user is forced to change his/her password)
        6. Warn : The number of days before password is to expire that user is warned that his/her password must be changed
        7. Inactive : The number of days after password expires that account is disabled
        8. Expire : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.

## Inspection
```
$ cat passwd | grep suninatas
suninatas:x:1001:1001::/home/suninatas:/bin/sh
$ cat shadow | grep suninatas
cat shadow | grep suninatas
suninatas:$6$QlRlqGhj$BZoS9PuMMRHZZXz1Gde99W01u3kD9nP/zYtl8O2dsshdnwsJT/1lZXsLar8asQZpqTAioiey4rKVpsLm/bqrX/:15427:0:99999:7:
::
```
* `shadow` 파일에서 `suninatas` 행의 `Password` column을 보니 `$6$`, 즉 SHA-512 알고리즘으로 암호화했다는 것을 알 수 있다.
* `$6$QlRlqGhj$BZoS9PuMMRHZZXz1Gde99W01u3kD9nP/zYtl8O2dsshdnwsJT/1lZXsLar8asQZpqTAioiey4rKVpsLm/bqrX/`
    - `$id` : `$6`
    - `$salt` : `$QlRlqGhj`
    - `$hashed` : `$BZoS9PuMMRHZZXz1Gde99W01u3kD9nP/zYtl8O2dsshdnwsJT/1lZXsLar8asQZpqTAioiey4rKVpsLm/bqrX/`

```
$ cat shadow | grep suninatas > shadow.suninatas
$ john shadow.suninatas
Loaded 1 password hash (crypt, generic crypt(3) [?/64])
Press 'q' or Ctrl-C to abort, almost any other key for status
iloveu1          (suninatas)
1g 0:00:01:29 100% 2/3 0.01111g/s 159.6p/s 159.6c/s 159.6C/s helene1..loren1
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
* `johntheripper` 툴로 1분 30초만에 깰 수 있다.