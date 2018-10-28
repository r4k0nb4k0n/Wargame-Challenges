# flee button
### First impressions
```
click the button!

i can't catch it!
```
click me! 버튼이 마우스 커서에 따라 움직이기 때문에 바로 클릭할 수는 없다.

### Trial and error
* Nothing.  

### Solution
* Chrome browser - DevTools(개발자 도구) - Elements
* style attribute 삭제.
```
<div id="esc" style="position: absolute; left: 642px; top: 431px;"><input type="button" onfocus="nokp();" onclick="window.location='?key=7163';" value="click me!"></div>
```
* 버튼이 고정되고, 이를 누르면 FLAG 가 나온다.