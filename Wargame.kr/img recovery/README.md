# img recovery
### First impressions
```
Recovery the PNG image file!

but.. is this really "PNG" file?
(NO STEGANOGRAPHY. THIS IS FORENSIC CHALLENGE)
```
![](./pattern.png?raw=true)
### Trial and error
* `file` 말로는 PNG image라고 한다.
```shell
$ file pattern.png
pattern.png: PNG image data, 105 x 105, 8-bit/color RGBA, non-interlaced
```
* 하지만 [`xxd`](./xxd.out?raw=true)로 보면 `tEXtSoftware.Japng r119`이 수상하다.
* 이를 구글링해보니 [APNG](https://wiki.mozilla.org/APNG_Specification) 포맷이 나온다.
* 청크를 참고하여 파일 내용을 다시 보니 두 장의 사진이 있는 것 같다.
* `apngdis pattern.png` -> `apngframe0.png`, `apngframe1.png` 2개의 사진 나타남.
* 이 둘을 합치면 QR 코드가 나타날 듯 하다.

### Solution
* `pattern.png`을 받는다.
* 해당 파일은 APNG(Animated PNG)이고 두 장의 그림이 들어있다.
* 따라서 `apngdis pattern.png` 명령을 통해 `apngframe0.png`, `apngframe1.png`을 얻는다.
* 둘을 포개 하나의 QR CODE 그림을 얻는다.
* 이를 위해 한 그림의 하얀 픽셀을 투명하게 바꾼다. [solution.py](./solution.py)
* 얻은 QR CODE를 Decode하여 얻은 code를 전송한다.
* FLAG가 나타난다.
