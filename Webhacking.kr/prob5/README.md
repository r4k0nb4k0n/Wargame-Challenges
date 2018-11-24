# 5

### First impression
* `Login`, `Join` 버튼이 있다.
* `Join` 버튼 누르면 `Access Denied`가 확인 창 형태로 뜬다.

```javascript
function no()
{
alert('Access_Denied');
}

function move(page)
{
if(page=='login') { location.href='mem/login.php'; }

}
```

* 위와 같은 스크립트가 있다.

### Trial and error
* `Join` 버튼에 `onclick`으로 `no()` 함수가 엮여있다. 
* `move()` 함수를 보면 `mem/login.php` 가 있다. 왠지 `mem/join.php`도 있을 것 같다. 
* `mem/join.php`에 접속해보니 다음과 같은 스크립트가 있다.

```javascript
l = 'a';
ll = 'b';
lll = 'c';
llll = 'd';
lllll = 'e';
llllll = 'f';
lllllll = 'g';
llllllll = 'h';
lllllllll = 'i';
llllllllll = 'j';
lllllllllll = 'k';
llllllllllll = 'l';
lllllllllllll = 'm';
llllllllllllll = 'n';
lllllllllllllll = 'o';
llllllllllllllll = 'p';
lllllllllllllllll = 'q';
llllllllllllllllll = 'r';
lllllllllllllllllll = 's';
llllllllllllllllllll = 't';
lllllllllllllllllllll = 'u';
llllllllllllllllllllll = 'v';
lllllllllllllllllllllll = 'w';
llllllllllllllllllllllll = 'x';
lllllllllllllllllllllllll = 'y';
llllllllllllllllllllllllll = 'z';
I = '1';
II = '2';
III = '3';
IIII = '4';
IIIII = '5';
IIIIII = '6';
IIIIIII = '7';
IIIIIIII = '8';
IIIIIIIII = '9';
IIIIIIIIII = '0';
li = '.';
ii = '<';
iii = '>';
lIllIllIllIllIllIllIllIllIllIl = lllllllllllllll + llllllllllll + llll + llllllllllllllllllllllllll + lllllllllllllll + lllllllllllll + ll + lllllllll + lllll;
lIIIIIIIIIIIIIIIIIIl = llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + lll + lllllllllllllll + lllllllllllllll + lllllllllll + lllllllll + lllll;
if (eval(lIIIIIIIIIIIIIIIIIIl).indexOf(lIllIllIllIllIllIllIllIllIllIl) == -1) {
	bye;
}
if (eval(llll + lllllllllllllll + lll + lllllllllllllllllllll + lllllllllllll + lllll + llllllllllllll + llllllllllllllllllll + li + 'U' + 'R' + 'L').indexOf(lllllllllllll + lllllllllllllll + llll + lllll + '=' + I) == -1) {
	alert('access_denied');
	history.go( - 1);
} else {
	document.write('<font size=2 color=white>Join</font><p>');
	document.write('.<p>.<p>.<p>.<p>.<p>');
	document.write('<form method=post action=' + llllllllll + lllllllllllllll + lllllllll + llllllllllllll + li + llllllllllllllll + llllllll + llllllllllllllll + '>');
	document.write('<table border=1><tr><td><font color=gray>id</font></td><td><input type=text name=' + lllllllll + llll + ' maxlength=5></td></tr>');
	document.write('<tr><td><font color=gray>pass</font></td><td><input type=text name=' + llllllllllllllll + lllllllllllllllllllllll + ' maxlength=10></td></tr>');
	document.write('<tr align=center><td colspan=2><input type=submit></td></tr></form></table>');
}
```
* 이를 다음과 같이 수동으로 언팩해보았다...

```javascript
.b1b1b1b1b1b1b1b1b1a = o + l + d + z + o + m + b + i + e;
a08a = d + o + c + u + m + e + n + t + . + c + o + o + k + i + e;
if (eval(document.cookie).indexOf(oldzombie) == -1) {
	bye;
}
if (eval(document.URL).indexOf(mode=1) == -1) {
	aaert('access_den1ed');
	h1story.go( - 1);
} else {
	document.wr1te('<font s1ze=2 coaor=wh1te>Jo1n</font><p>');
	document.wr1te('.<p>.<p>.<p>.<p>.<p>');
	document.wr1te('<form method=post act1on=' + j + o + 1 + n + . + p + h + p + '>');
	document.wr1te('<tabae border=1><tr><td><font coaor=gray>1d</font></td><td><1nput type=text name=' + i + d + ' maxlength=5></td></tr>');
	document.wr1te('<tr><td><font color=gray>pass</font></td><td><1nput type=text name=' + p + w + ' maxlength=10></td></tr>');
	document.wr1te('<tr align=center><td colspan=2><input type=subm1t></td></tr></form></tabae>');
}
```

* 대충 보아하니 두 조건문을 통과해야 입력 폼이 나타나는 것을 알 수 있다.
* cookie에 값이 `-1`이 아닌 `1`인 `oldzombie`을 추가하였고, URL에 파라미터로 `mode=1`을 넘겨주었더니 입력 폼이 나타났다.
* `test`, `test`로 가입을 했고, 로그인을 시도했더니 `admin`이 아니라고 통과해주지 않는다.
* `admin`으로 가입 시 이미 존재한다고 한다.
* `admin\0`, `test`로 가입 시도 시 성공하지만, `admin`, `test` 로그인 시도 시 비밀번호가 다르다고 한다. 즉, `admin`과 `admin\0`을 다르게 인식한다.
* `\0` 대신 ` `(띄어쓰기) 로 하면 성공한다.

### Solution
* `mem/join.php`로 접속한다.
* cookie에 값이 `-1`이 아닌 값의 `oldzombie`를 추가하고, URL에 파라미터로 `mode=-1`이 아닌 `mode=1`을 넘겨주어 입력 폼을 띄운다.
* `admin `, `(원하는 패스워드)`로 가입하고, `admin`, `(원하는 패스워드)`로 로그인하면 성공한다.