# QR CODE PUZZLE
### First impressions
```
javascript puzzle challenge

just enjoy!
```
QR Code 이미지가 6X6 퍼즐로 섞여 있고 진정 이걸 다 맞춰야 원래 이미지를 보여줄 것 같다.
### Trial and error
* DevTools 콘솔에서 정렬 함수를 이용하여 `jqp-puzzle`들을 `current`를 기준으로 정렬을 시도했지만, DOM에 정렬 결과가 적용되지 않아서(퍼즐이 맞춰지지 않아서) 실패했다.
* 근데 `jqp-puzzle`의 `background-image`을 보니 이미지 URL에 그대로 노출되어 이를 그대로 사용했다.

### Solution
* Chrome browser - DevTools(개발자 도구) - Elements
* `jqp-puzzle`의 `background-image` 확인하여 이미지 URL 획득.
```
<div class="jqp-piece" style="width: 81px; height: 81px; background-image: url(&quot;./img/qr.png&quot;); border-width: 0px; margin: 0px; padding: 0px; position: absolute; overflow: hidden; display: block; visibility: inherit; cursor: default; left: 332px; top: 415px; background-position: 0px 0px;" current="34"><span style="display: none;">1</span></div>
```
* 이미지를 QR CODE Decode한다.
* FLAG 값이 나온다.