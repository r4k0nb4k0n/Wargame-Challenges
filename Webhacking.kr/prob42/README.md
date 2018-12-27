# 42

## Problem
```html
<html><head>
<title>Challenge 42</title>
</head>
<body>

<table border="1" align="center" width="300">
<tbody><tr><td width="50">no</td><td>subject</td><td>file</td></tr>
<tr><td>2</td><td>test</td><td>test.txt [<a href="?down=dGVzdC50eHQ=">download</a>]</td></tr>
<tr><td>1</td><td>read me</td><td>test.zip [<a href='javascript:alert("Access%20Denied")'>download</a>]</td></tr>
</tbody></table>

<!--

test.zip password is only numbers

-->

</body></html>
```

## Inspection
* `test.txt`의 링크는 `?down=dGVzdC50eHQ=`이고, 접속하면 `6dd75b248af291f3bf164e28e3acd811/test.txt`가 나타나며, 내용은 `test~~~`이다.
	- 파라미터 `?down=`로 넘기는 값 `dGVzdC50eHQ=`의 끝인 `=`를 보고 base64 인코딩이라는 것을 떠올렸다.
	- `test.txt`를 base64로 인코딩한 결과가 `dGVzdC50eHQ=`이다.
* 위 추측으로 `test.zip`의 링크는 `?down=dGVzdC56aXA=`임을 알아낼 수 있다.
* 주석 힌트에 따르면 `test.zip`의 패스워드는 오직 숫자로 이루어져있다.
* `fcrackzip`을 이용하여 패스워드를 알아냈다.
* 안에 들어있는 `readme.txt` 파일에 있는 링크로 접속하면 flag가 뜬다.

## Solution
* `test.zip`의 링크인 `?down=dGVzdC56aXA=`로 접속하여 `test.zip`을 다운로드 받는다.
* 패스워드는 오직 숫자로 이루어져있다는 힌트를 이용하여 패스워드를 찾는다.
    * `fcrack -b -c 1 -l 1-8 -u test.zip`
    * `-b` : 브루트-포스
    * `-c 1` : 숫자만 사용
    * `-l 1-8` : 길이 `1`부터 `8`까지
    * `-u` : 일일이 확인
* `test.zip`을 해제하여 나오는 `readme.txt`에 들어있는 링크로 접속한다.
* 나타난 flag로 인증하면 통과한다.