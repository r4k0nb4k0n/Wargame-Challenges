# 2

## Problem
```html
<!-- ... -->
<script>
	function chk_form(){
		var id = document.web02.id.value ;
		var pw = document.web02.pw.value ;
		if ( id == pw )
		{
			alert("You can't join! Try again");
			document.web02.id.focus();
			document.web02.id.value = "";
			document.web02.pw.value = "";
		}
		else
		{
			document.web02.submit();
		}
	}
</script>
<!-- Hint : Join / id = pw -->
<!-- M@de by 2theT0P --></form></body></html>
```

## Inspection
* `function chk_form()`
	- `form`의 `id`와 `pw`가 같으면 값을 비우고 가입을 못하며, 다르면 폼을 전송한다.
* `<!-- Hint : Join / id = pw -->`
	- `id`와 `pw`가 같도록 `Join`하라.

## Solution
* `chk_form = function () { document.web02.submit(); }`
	- 콘솔로 자바스크립트 함수를 바꿔치기하여 우회한다.