# 22

### First impression
* `index.php`

```
username	
password	
login join

HINT

echo("hi! $id");
echo("your password is $pw");

if($id=="admin") echo("good! Password is $solution");
```

### Trial and error
* `id`가 `admin`이어야 통과할 것 같다.
* `join`으로 기존 `admin` 레코드의 비밀번호를 원하는 것으로 덮어씌워 로그인해야 통과할 것 같다.
* `join` 버튼을 눌러 ` `index.php?mode=join`로 이동했다.
* `admin`, `(아무런 pw)`로 가입 시도했으나 `Username already exists`라고 뜬다.
* `admin`의 양옆에 띄어쓰기를 추가해도 `admin`과 똑같다고 인식한다.
* `AdMiN`과 같이 대소문자 구분을 해도 `admin`과 똑같다고 인식한다.
* 다음과 같이 입력했을 때 `No!`가 뜬다.
	- `admin+`
	- `admin%00`

* (2018-12-06) `if($id=="admin")` 을 보니 PHP의 Loose comparision이 생각났다.
	- [PHP.net manual typs.comparisons](http://php.net/manual/en/types.comparisons.php)
	- Loose comparison에서 `"php"` 와 같은 것은 `"php"`와 `TRUE`, 그리고 숫자 `0`이다.
	- 문자열 `"TRUE"`가 아니라 정말 `TRUE`값이다.
	- 숫자 `0`도 있다.
* `<input name="uuid" type="text" value=true>` 실패. 이름이 `true`로 들어간다.
* `<input name="uuid" type="checkbox">`로 체크하고 시도했으나 실패. 이름이 `on`으로 들어간다.
* `<input name="uuid" type="number">`로 값 `0`주고 시도했으나 실패. 가입은 성공함. 로그인이 안된다.
* Python requests 모듈을 이용해서 `0`, `true` 시도해봤으나 로그인 실패.
* 양 옆에 공백을 썼을 때 기존 아이디가 있다고 뜨는 걸 봐서는 MySQL을 쓰는 것 같다. [Link](http://woowabros.github.io/study/2018/02/26/mysql-char-comparison.html#%EB%A7%88%EC%A7%80%EB%A7%89-%ED%85%8C%EC%8A%A4%ED%8A%B8---%EA%B3%B5%EB%B0%B1%EC%9D%84-%EC%9D%B4%EC%96%B4%EB%B6%99%EC%9D%B4%EB%A9%B4-%EC%96%B4%EB%96%A8%EA%B9%8C)

* `user key`가 뭐길래 계속 뜨는거지?
	- `test`로 가입해서 로그인했을 때 나오는 md5 값을 [여기](https://www.md5online.org/md5-decrypt.html)에서 깨보니 `testzombie`가 뜬다.
	- `ad?min`, `ad@min`로 가입해서 로그인했을 때 나오는 md5 값을 깨보니 `adminzombie`가 뜬다.

### Solution