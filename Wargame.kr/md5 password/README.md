# md5 password
### First impressions
```
md5('value', true);
```
패스워드를 입력하는 form이 있다.  
view-source 하면 다음 주요 코드가 있다.  
```php
$key=auth_code("md5 password");
$ps = mysql_real_escape_string($_POST['ps']);
$row=@mysql_fetch_array(mysql_query("select * from admin_password where password='".md5($ps,true)."'"));
if(isset($row[0])){
    echo "hello admin!"."<br />";
    echo "Password : ".$key;
}
```
### Trial and error
* `md5($ps, true)`는 16자리 2진수 값의 md5를 의미한다.
* 이를 이용하여 sql injection이 가능하다고 판단했다.
* `select * from admin_password where password='[output of md5($ps, true)]'`
* [md5 raw hash를 이용한 sql injection](http://bbolmin.tistory.com/77)
* `1' or '1` 따위를 삽입한다.

### Solution
* `[output of md5($ps, true)] => 1' or '1`이 나오는 $ps를 넣는다.
* FLAG 값이 나온다.
