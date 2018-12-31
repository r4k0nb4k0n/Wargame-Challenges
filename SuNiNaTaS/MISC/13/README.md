# 13

## Problem
```
KEY Finding
```

## Inspection
* 다음과 같은 주석 힌트가 있다.
    - `<!--	Hint : The programmer's bad habit of backup source codes -->`
* Webhacking.kr의 vi blackout과 비슷한 문제라고 생각한다.
* 다운로드받은 압축 파일의 안은 다음과 같다. `압축비번은4자리정수` 힌트를 통해 비밀번호를 brute-force로 알아낸다.
    - `whitehack1.jpg`
        + 모니터에서 사람 팔 여러개가 휘젓는다.
    - `whitehack2.jpg`
        + 컴퓨터에 자물쇠가 채워져있다.
    - `whitehack3.jpg`
        + 수화기, 통장, 수갑.
    - `whitehack4.jpg`
        + 컴퓨터, 돋보기.
    - `압축비번은4자리정수.txt`
        + `4개의 이미지를 합하여 key를 구하시오`

## Solution
* `http://suninatas.com/Part_one/web13/web13.***` 을 다운로드받는다. 압축파일이고 확장자는 누구나 맞출 수 있다.
* `fcrackzip -b -c 1 -l 4 -u web13.zip`를 통해 비밀번호를 알아내고 압축을 푼다.
* 각 이미지를 hexdump로 떠보면 key가 4개가 나오고 이를 조합하여 제출하면 성공한다.
* `3nda....` 총 32바이트.