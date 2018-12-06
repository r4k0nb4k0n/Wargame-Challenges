# 23

### First impression
```html
<form method="get" action="index.php">
    <table border="0" cellpadding="10">
        <tbody>
	        <tr>
		        <td><input name="code"></td>
			    <td><input type="submit"></td>
		    </tr>
        </tbody>
	</table>
</form>
Your mission is to inject <script>alert(1);</script> 
```

### Trial and error
* `code` 파라미터로 전송한 것이 그대로 작성된다.
* 숫자는 제한없이, 문자는 한 글자만 작성이 되고, HTML 태그같은 것은 한 글자를 넘어서면 `no hack`라고 뜨면서 막힌다.
* `<a> </a>`는 되길래, 여기에 `onclick` 속성을 넣으려 했으나, `no hack`이라고 막힌다.
* `PHP` 단에서 뭔가 필터링하는 함수를 쓰는 것 같다.
	* 이를 `eregi()`라고 예상하고, 이를 우회하기 위해 `%00`을 썼다.
	* 이는 해당 함수가 `NULL`(`%00`)까지만 검사한다는 것을 악용한 것이다.

### Solution
* `%00<script>alert(1);</script>` 을 전송한다.
* XSS을 차단하는 브라우저가 있을 수 있다. 이는 알아서 잘 피한다.