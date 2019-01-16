# 16

## Problem
```
Can you find the password for a member of SuNiNaTaS.com?
 
Download
```

## Tool
* [tshark](https://www.wireshark.org/docs/man-pages/tshark.html)

## Inspection and Solution
```
$ tshark -r packet_dump.pcap -Y http.request.method=="POST" -T fields -e text
Timestamps,POST /member/mem_action.asp HTTP/1.1\r\n,\r\n,Form item: "Hid" = "suninatas",Form item: "Hpw" = "suninatas"
Timestamps,POST /member/mem_action.asp HTTP/1.1\r\n,\r\n,Form item: "Hid" = "blackkey",Form item: "Hpw" = "blackkey"
Timestamps,POST /member/mem_action.asp HTTP/1.1\r\n,\r\n,Form item: "Hid" = "ultrashark",Form item: "Hpw" = "sharkpass01"
Timestamps,POST /member/mem_action.asp HTTP/1.1\r\n,\r\n,Form item: "Hid" = "ultrashark",Form item: "Hpw" = "=sharkpass01"
Timestamps,POST /member/mem_action.asp HTTP/1.1\r\n,\r\n,Form item: "Hid" = "ultrashark",Form item: "Hpw" = "=SharkPass01"
Timestamps,POST /member/mem_action.asp?licen=login_out HTTP/1.1\r\n,\r\n
$ 
```
* 일반적으로 로그인 폼을 전송할 때 `GET` 대신 `POST`를 사용한다.
* 이를 떠올려서 `POST`만 필터링해보자.
* `tshark -r packet_dump.pcap -Y http.request.method=="POST" -T fields -e text`
	- `-r packet_dump.pcap`
		+ `packet_dump.pcap` 파일로부터 패킷 데이터를 읽어온다.
	- `-Y http.request.method=="POST"`
		+ http request method가 `POST`인 것만 필터링한다.
	- `-T fields -e text`
		+ `text` 필드만 출력한다.
* 여러 번의 로그인 시도가 있었고, `Form item: "Hid" = "ultrashark",Form item: "Hpw" = "=SharkPass01"` 이후에 `login_out`을 했다.
* 따라서 `ultrashark`, `=SharkPass01`일 때 로그인을 성공했다는 것을 알 수 있다.
* SuNiNaTaS 사이트에 위 계정 정보로 로그인해보면 `Congratulation! Authkey :   ***********************`로 인증키가 뜬다.