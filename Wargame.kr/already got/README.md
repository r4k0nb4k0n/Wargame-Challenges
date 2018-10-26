# already got
### First impressions
```
can you see HTTP Response header?
```
말 그대로 HTTP Response header에서 FLAG 값을 찾으라는 것 같다.

### Trial and error
* Nothing.  

### Solution
* Chrome browser - DevTools(개발자 도구) - Network
* Response Headers 확인.
```
HTTP/1.1 200 OK
Date: Fri, 26 Oct 2018 07:32:51 GMT
Server: Apache/2.4.18 (Ubuntu)
FLAG: (HIDE)
Content-Length: 27
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
```
* FLAG 값이 나온다.