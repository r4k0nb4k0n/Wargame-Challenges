# 20

### First impression
* `id`, `cmt`, `hack` 을 전송하는 폼이 있다.
* `time limit : 2`라고 적혀있다.

### Trial and error

* 해당 폼에 다음과 같은 자바스크립트 체크 함수가 적용되어있다.

```javascript
<script>
function ck()
{

if(lv5frm.id.value=="") { lv5frm.id.focus(); return; }
if(lv5frm.cmt.value=="") { lv5frm.cmt.focus(); return; }
if(lv5frm.hack.value=="") { lv5frm.hack.focus(); return; }
if(lv5frm.hack.value!=lv5frm.attackme.value) { lv5frm.hack.focus(); return; }

lv5frm.submit();

}
</script>
```
	- 값이 비어있는 필드에 포커스를 주어서 입력을 요구한다.
	- `hack`의 값이 `attackme`의 값과 같도록 포커스를 주어서 입력을 요구한다.
	- 모든 필드가 다 채워져있고, `hack`의 값과 `attackme`의 값이 같다면 해당 폼을 전송한다.
	
* 2초 안에 위 조건을 만족시켜서 전송해야 통과할 것 같다.

### Solution
* 콘솔에 다음 자바스크립트를 입력한다.

```javascript
ck = function()
{
lv5frm.id.value="r4k4"
lv5frm.cmt.value="r4k4"
lv5frm.hack.value=lv5frm.attackme.value
lv5frm.submit();
};

ck();
```

* 안된다면 다시 2초 안에 위 스크립트를 입력하여 실행한다.