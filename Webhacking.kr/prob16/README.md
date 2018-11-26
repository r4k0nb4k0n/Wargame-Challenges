# 16

### First impression
```html
<body bgcolor="black" onload="kk(1,1)" onkeypress="mv(event.keyCode)">
```

```javascript
document.body.innerHTML+="<font color=yellow id=aa style=position:relative;left:0;top:0>*</font>";

function mv(cd)
{
kk(star.style.posLeft-50,star.style.posTop-50);
// 4 (Num Lock)
if(cd==100) star.style.posLeft=star.style.posLeft+50;
// 1 (Num Lock)
if(cd==97) star.style.posLeft=star.style.posLeft-50;
// F8
if(cd==119) star.style.posTop=star.style.posTop-50;
// F4
if(cd==115) star.style.posTop=star.style.posTop+50;
// Nothing
if(cd==124) location.href=String.fromCharCode(cd);
}

function kk(x,y)
{
rndc=Math.floor(Math.random()*9000000);
document.body.innerHTML+="<font color=#"+rndc+" id=aa style=position:relative;left:"+x+";top:"+y+" onmouseover=this.innerHTML=''>*</font>";
}
```

### Trial and error
* 뭔가 많아보이지만 별 거 없다.
* `if(cd==124) location.href=String.fromCharCode(cd);` 뭔가 다른 라인들과는 다른 코드다.

### Solution
* 자바스크립트 콘솔에서 `mv(124)`를 호출하여 나타난 값으로 Auth한다.