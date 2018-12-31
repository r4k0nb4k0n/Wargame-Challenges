# 17

## Problem
```
Ummm... QR Code is broken!
Fix it!
```

## Background Knowledge
* [QR Code - Wikipedia](https://en.wikipedia.org/wiki/QR_code)
    - ![](./QR_Code_Structure.png?raw=true)

## Inspection
![](./qrmaster.jpg?raw=true)
* QR Code는 다음과 같다.
* Position Pattern 3군데가 모두 빨갛게 칠해져있다.
* 색깔이 물빠진 것 마냥 회색이다.

## Solution
* 그림판으로 QR Code를 복구했다.
* ![](./pos.jpg?raw=true)
* 배경은 `(0, 0, 0)`으로, 정보가 담긴 픽셀은 `(255, 255, 255)`로 색깔을 바꿨다.
* Position pattern을 우상, 좌상, 좌하 세 군데에 붙여넣고, 그 주변의 빨간색을 대충 지운다.
* 다음과 같은 모습으로 QR Code를 읽을 수 있었다. [Web QR](https://webqr.com/)
* ![](./touched.jpg?raw=true)
