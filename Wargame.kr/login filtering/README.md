# login filtering
### First impressions
```
I have accounts. but, it's blocked.

can you login bypass filtering?
```
필터링을 통과하여 로그인을 하라는 말인 것 같다.
```
<?php

if (isset($_GET['view-source'])) {
    show_source(__FILE__);
    exit();
}

/*
create table user(
 idx int auto_increment primary key,
 id char(32),
 ps char(32)
);
*/

 if(isset($_POST['id']) && isset($_POST['ps'])){
  include("../lib.php"); # include for auth_code function.

  mysql_connect("localhost","login_filtering","login_filtering_pz");
  mysql_select_db ("login_filtering");
  mysql_query("set names utf8");

  $key = auth_code("login filtering");

  $id = mysql_real_escape_string(trim($_POST['id']));
  $ps = mysql_real_escape_string(trim($_POST['ps']));

  $row=mysql_fetch_array(mysql_query("select * from user where id='$id' and ps=md5('$ps')"));

  if(isset($row['id'])){
   if($id=='guest' || $id=='blueh4g'){
    echo "your account is blocked";
   }else{
    echo "login ok"."<br />";
    echo "Password : ".$key;
   }
  }else{
   echo "wrong..";
  }
 }
?>
<!DOCTYPE html>
<style>
 * {margin:0; padding:0;}
 body {background-color:#ddd;}
 #mdiv {width:200px; text-align:center; margin:50px auto;}
 input[type=text],input[type=[password] {width:100px;}
 td {text-align:center;}
</style>
<body>
<form method="post" action="./">
<div id="mdiv">
<table>
<tr><td>ID</td><td><input type="text" name="id" /></td></tr>
<tr><td>PW</td><td><input type="password" name="ps" /></td></tr>
<tr><td colspan="2"><input type="submit" value="login" /></td></tr>
</table>
 <div><a href='?view-source'>get source</a></div>
</form>
</div>
</body>
<!--

you have blocked accounts.

guest / guest
blueh4g / blueh4g1234ps

-->
```
맨 밑에 주석으로 막힌 계정들 정보가 있다.
### Trial and error
* 처음엔 SQL Injection인 줄 알고 엄청나게 삽질을 했지만,
* `mysql_real_escape_string()` 때문에 막힘.
* 유니코드를 활용한 취약점을 써봤으나, 인코딩 방식때문인지 먹히지 않음.
* `guest / guest`, `blueh4g / blueh4g1234ps` 로그인 시도, 막힘.
* `isset($row['id'])를 통과했다는 것은 DB에는 계정 정보가 반드시 있다는 것.
* `if($id=='guest' || $id=='blueh4g')` 조건문만 회피하면 될 것 같다.
* **DB User 테이블의 ID 열은 char이므로 대소문자를 구분하지 않는다.**
### Solution
* `GuEsT / guest` 로그인 시도.
* FLAG 가 나온다.