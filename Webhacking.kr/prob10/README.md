# 10

### First impression
```html
<a 
	id="hackme" 
	style="position:relative;left:0;top:0" 
	onclick="this.style.posLeft+=1;if(this.style.posLeft==800)this.href='?go='+this.style.posLeft" 
	onmouseover="this.innerHTML='yOu'" 	
	onmouseout="this.innerHTML='O'"
>O
</a>
```

### Trial and error
* `onclick`의 스크립트가 잘못 짜여있다.
	- `this.style.posLeft` -> `this.style.left`
	- 단위가 `px`이므로 증감식이 적용되지 않고 문자열 합침으로 돌아갔다.
* `this.style.left`가 `800`일 때 `'?go='+this.style.left` 링크를 걸어준다. 이는 `?go=800px`이다.
* 해당 링크 접속하면 풀린다.

### Solution
* `?go=800px`로 접속한다.