# 54

## Problem
```javascript
function run(){
  if(window.ActiveXObject){
   try {
    return new ActiveXObject('Msxml2.XMLHTTP');
   } catch (e) {
    try {
     return new ActiveXObject('Microsoft.XMLHTTP');
    } catch (e) {
     return null;
    }
   }
  }else if(window.XMLHttpRequest){
   return new XMLHttpRequest();
 
  }else{
   return null;
  }
 }

x=run();

function answer(i)
{
x.open('GET','?m='+i,false);
x.send(null);
aview.innerHTML=x.responseText;
i++;
if(x.responseText) setTimeout("answer("+i+")",100);
if(x.responseText=="") aview.innerHTML="?";
}

setTimeout("answer(0)",10000);
```

## Background Knowledges
* [Ajax 시작하기 | MDN](https://developer.mozilla.org/ko/docs/Web/Guide/AJAX/Getting_Started)
    - AJAX
        + 비동기 자바스크립트와 XML (Asynchronous JavaScript And XML)을 말합니다. 
        + 간단히 말하면, 서버와 통신하기 위해 `XMLHttpRequest` 객체를 사용하는 것을 말합니다.
        + AJAX의 강력한 특징은 페이지 전체를 리프레쉬 하지 않고서도 수행 되는 "비동기성"입니다.
        + 이를 이용해 페이지의 일부분만을 업데이트할 수 있다.

## Inspection
* `function run()`
    - XHR(XMLHttpRequest) 객체 생성하는 함수이다.
    - 먼저 `ActiveXObject`를 지원하는지 확인하고, 그렇지 않으면 native javascript 객체가 할당된다.
* `x=run();`
    - `x`에 XHR 객체를 생성후 할당한다.
* `function answer(i)`
    - `x.open('GET','?m='+i,false);`
        + `index.php?m=(i)`를 `GET` 방식으로 **동기적으로** 요청한다. 
    - `x.send(null);`
        + `false`로 설정된 경우 동기적으로 작동합니다. (`send()` 함수에서 서버로부터 응답이 올 때까지 기다림)
    - `aview.innerHTML=x.responseText;`
        + 페이지의 내용을 응답받은 내용으로 수정한다.
    - `i++;`
    - `if(x.responseText) setTimeout("answer("+i+")",100);`
    - `if(x.responseText=="") aview.innerHTML="?";`
        + 응답내용이 있으면 `100`ms 이후 `answer(i)`를 실행한다.
        + 응답내용이 없으면 페이지의 내용을 `?`로 수정한다.
* `setTimeout("answer(0)",10000);`
    - `10000`ms 이후 `answer(0)`을 실행한다.
* `index.php?m=(X)` `(0 ≤ X ≤ 31)`의 응답으로 한 글자씩 flag가 온다.
* 크롬 개발자 도구의 Network 탭에서 확인할 수 있다.
* 이는 HTML 상에서도 한 글자씩 flag가 뜨는 것을 확인할 수 있다.

## Solution
* 개발자 도구 `Network` 탭에서 한 글자씩 차례대로 붙이면 Flag가 된다.
* [`get_answer.py`](./get_answer.py) 작성중...