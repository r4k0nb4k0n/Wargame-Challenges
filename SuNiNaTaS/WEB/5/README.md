# 5

## Problem
```html
<!--Hint : 12342046413275659 -->
<!-- M@de by 2theT0P -->
```
* 주석 힌트.

```javascript
<script>
eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('g l=m o(\'0\',\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'a\',\'b\',\'c\',\'d\',\'e\',\'f\');p q(n){g h=\'\';g j=r;s(g i=t;i>0;){i-=4;g k=(n>>i)&u;v(!j||k!=0){j=w;h+=l[k]}}x(h==\'\'?\'0\':h)}',34,34,'||||||||||||||||var|result||start|digit|digitArray|new||Array|function|PASS|true|for|32|0xf|if|false|return'.split('|'),0,{}))
</script>
```
* 폼에 숨겨진 스크립트.

## Inspection
```javascript
var digitArray=new Array('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f');
function PASS(n)
	{
	var result='';
	var start=true;
	for(var i=32;
	i>0;
	)
		{
		i-=4;
		var digit=(n>>i)&0xf;
		if(!start||digit!=0)
			{
			start=false;
			result+=digitArray[digit]
		}
	}
	return(result==''?'0':result)
}

```
* [UnPacker](http://matthewfl.com/unPacker.html)에서 언팩해보았다.
* `function PASS(n)`
    - `10`진수 `n`의 맨 뒤부터 8자리 수를 `8`자리 16진수로 바꿔준다.
* 주석 힌트에 있던 수 `12342046413275659`를 `PASS`에 넣어본다.

## Solution
* `PASS(12342046413275659)`를 콘솔에서 돌려본다.
* Auth 키가 나온다.