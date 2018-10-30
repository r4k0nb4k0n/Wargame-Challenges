# tmitter
### First impressions
```
you need login with "admin"s id!

===========================

create table tmitter_user(
 idx int auto_increment primary key,
 id char(32),
 ps char(32)
);
```
사이트에는 Sign up과 Sign in 버튼이 있다.  
Sign up 페이지 소스를 보면 주석으로 admin으로 가입을 해야 한다는 말이 적혀 있다.  
### Trial and error
* 아이디를 `admin`과 비슷하게 넣어서 가입을 시도해봤다.
* `\0admin`으로 가입은 성공했고 로그인해서 글을 올려보니 실제 admin과 이름은 똑같다. 
* 즉 앞뒤 공백같은 문자를 잘라내는 `trim()`같은 함수가 있을 거라고 생각한다.
* 근데 여기서 더이상 할 게 생각이 안났다.
* 그래서 글자수를 넘겨보기로 했다.
### Solution
* Sign in 페이지에 접속한다.
* 개발자 도구에서 ID 칸의 글자 수 제한을 풀어준다. (`maxlength=32` 속성 삭제)
* `admin                                \0`이란 아이디와 원하는 패스워드로 가입. (사이 공백이 32개다. 어떻게든 32글자만 넘겨보자.)
* `admin`, 원하는 패스워드로 로그인 시도 성공. FLAG 출력.