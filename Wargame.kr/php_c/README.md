# php? c?
### First impressions
```
do you know "integer type" of 32bit application?
```
* 32 bit 어플리케이션의 정수형 타입을 아느냐고 묻는다. 아무래도 오버플로우 문제같다.

```php
<?php
 if (isset($_GET['view-source'])) {
     show_source(__FILE__);
    exit();
 }
 require("../lib.php"); // include for auth_code function.
 if(isset($_POST['d1']) && isset($_POST['d2'])){
  $input1=(int)$_POST['d1'];
  $input2=(int)$_POST['d2'];
  if(!is_file("/tmp/p7")){exec("gcc -o /tmp/p7 ./p7.c");}
  $result=exec("/tmp/p7 ".$input1);
  if($result!=1 && $result==$input2){echo auth_code("php? c?");}else{echo "try again!";}
 }else{echo ":p";}
?>
<style>
 table {background-color:#000; color:#fff;}
 td {background-color:#444;}
</style>
<hr />
 <center>
  <form method='post'>
  <table>
  <tr><td>D1:</td><td><input type='text' id="firstf" style="width:75px;" maxlength="9" name='d1'></td></tr>
  <tr><td>D2:</td><td><input type='text' style="width:75px;" name='d2'></td></tr>
  <tr><td colspan="2" style="text-align:center;"><input type='submit' value='try'></td></tr>
  </table>
  </form>
 <div><a href='?view-source'>get source</a></div>
 </center>
 <script>
  document.getElementById("firstf").focus();
 </script>
```
* `d1`, `d2`를 POST를 통해 받은 후 정수형으로 캐스팅한다.
* `./p7.c`를 컴파일하여 생성된 프로그램에게 `d1`을 넘겨주어 실행한 결과값(`$result`)과 `d2`가 같아야 FLAG가 나타난다.
* `$result!=1`을 보아 특정 조건문에 의해 대부분의 입력이 걸러지는 것 같다.

```c
#include <stdio.h>
#include <stdlib.h>
void nono();
int main(int argc,char **argv){
 int i;
 if(argc!=2){nono();}
 i=atoi(argv[1]);
 if(i<0){nono();}
 i=i+5;
 if(i>4){nono();}
 if(i<5){printf("%d",i);}
 return 0;
}
void nono(){
  printf("%d",1);
  exit(1);
}
```
* 첫번째 조건문에 의해 음수일 경우 걸러진다.
* `i=i+5;`가 실행된다.
* 두번째 조건문에 의해 4보다 큰 양수일 경우 걸러진다.
* 세번째 조건문에 의해 5보다 작은 정수일 경우 `i`가 그대로 출력된다.

### Trial and error
* `i=i+5;` 코드 이전에는 `i`는 양수여야 한다.
* `i=i+5;` 코드 이후에는 `i`는 5보다 작은 정수여야 한다.
* 즉 `i=i+5;` 코드가 실행되면 오버플로우가 발생하여 양수가 음수로 바뀌어야 한다.
* 32-bit signed integer range -> `-2,147,483,648` ~ `2,147,483,647`
* `INT_MAX` 값을 넣는다면 조건문들을 통과할 것이다.

### Solution
* DevTools를 이용하여 D1 input의 `maxlength="9"` 속성을 제거한다.
* D1에 `INT_MAX`를, D2에 `INT_MAX+5`가 오버플로우된 값을 입력한 후 전송한다.
* FLAG가 나타난다.
