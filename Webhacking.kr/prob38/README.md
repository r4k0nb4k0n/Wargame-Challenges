# 38

## Problem
* `index.php`

```html
<html><head>
<title>Challenge 38</title>
</head>
<body>
<h1>LOG INJECTION</h1>
<!-- admin.php -->

<form method="post" action="index.php">
<input type="text" name="id" size="20">
<input type="submit" value="Login"><input type="button" value="Admin" onclick="location.href='admin.php'">
</form>


</body></html>
```

* `admin.php`

```html
<html><head>
<title>log viewer</title>
</head>
<body>
<!--

hint : admin

-->
log

</body></html>
```

## Background Knowledge
* [Log injection. What? How?](https://medium.com/@shatabda/security-log-injection-what-how-a510cfc0f73b)
	- 악의적인 입력으로 로그 파일을 조작할 수 있다. 

## Inspection
* `admin.php`에 `hint : admin`이 있다.
* `index.php`에 무언가 입력하고 `Login` 버튼을 누르면 `admin.php`로 이동하는데, 여기에 입력한 무언가가 기록으로 남는다.
* 무조건 소문자로 바뀐다.
* `admin`을 보내면 `you are not admin`이라고 뜬다.

## Solution
* `admin\nadmin`