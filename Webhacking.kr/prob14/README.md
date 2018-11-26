# 14

### First impression
```javascript
function ck()
{
var ul=document.URL;
ul=ul.indexOf(".kr");
ul=ul*30;
if(ul==pw.input_pwd.value) { alert("Password is "+ul*pw.input_pwd.value); }
else { alert("Wrong"); }
}
```

### Trial, Error, and Solution
* 위 코드를 분석하자면 다음과 같다.
	- 현재 접속한 사이트의 URL을 알아낸다.
	- 거기서 `.kr`가 나타나는 인덱스 값을 알아낸다.
	- 그 값에 `30`을 곱한 값을 제출해야 Auth 값을 얻는다.
* 처음에 URL에 `http://`가 없는 줄 알고 인덱스 값이 `10`인 줄 알았다.
* 하지만 이는 브라우저 UI에 의한 착각으로, 프로토콜이 보이지 않아도 `http://`가 붙어있다.
* 따라서 인덱스 값이 `17`임을 알아냈다.
* 이를 제출하여 얻은 값으로 Auth를 하여 통과한다.