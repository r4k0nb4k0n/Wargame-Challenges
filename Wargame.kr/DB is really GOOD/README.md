# DB is really GOOD
### First impressions
```
What kind of this Database?

you have to find correlation between user name and database.
```
사용자 이름과 데이터베이스의 연관성을 찾아야 한다고 나온다.
### Trial and error
* DevTools로 뜯어보니 admin으로 들어가는 것을 막아놓았다. 아무래도 admin에 답이 있는 듯 싶다.
* ` admin` 등 앞뒤 공백 다 넣어보고 해봤는데 `admin`이 나타나지 않는다.
* 다양한 입력을 시도해보았다.

### Solution
* form에 `/`를 입력하여 오류 메시지를 출력하게 한다.
* sqlite3을 이용한다는 것을 알 수 있고, `./db/wkrm_[user name].db`으로 db 파일이 존재한다는 것을 알 수 있다.
* `wget http://wargame.kr:8080/db_is_really_good/db/wkrm_admin.db`
* `xxd wkrm_admin.db`
* `./??????????.php` url이 나타난다.
* 해당 url로 접속 시 FLAG가 나타난다.
