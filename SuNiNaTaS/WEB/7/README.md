# 7

## Inspection
* `<!-- Hint : Faster and Faster -->`
* 두 개의 사람 사진 사이에 `YES` 버튼이 있다. 이를 클릭하면 `Fail... You too slow`라는 창이 뜬다.

```html
<form method="post" action="./web07_1.asp" name="frm">
<div align="center"><input type="button" name="main_btn" value="main" style="width:60" onclick="location.href='/main/main.asp'">&nbsp;&nbsp;&nbsp;
<input type="button" name="main_btn" value="Back" style="width:60" onclick="history.back()"></div>
	<div align="center"><input type="hidden" name="web07" value="Do U Like girls?"></div>
	<div align="center"><img src="./iu.gif" width="700" height="1000" name="iu"></div>
	<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
	<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
	<div align="center"><input type="submit" value="YES"></div>
	<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
	<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
	<div align="center"><img src="./yoona.gif" width="700" height="1000" name="yoona"></div>
</form>
```
* `http://suninatas.com/Part_one/web07/web07_1.asp`로 `POST` 파라미터 `web07`에 `Do U Like girls?` 값을 전송해야 한다.

## Solution
* [`post_faster.py`](./post_faster.py)
	- `./web07.asp`에 먼저 접속한다.
	- 이후 `./web07_1.asp`에 `POST` 파라미터 `web07`에 `Do U Like girls?` 전송하면 `Auth key`가 뜬다.