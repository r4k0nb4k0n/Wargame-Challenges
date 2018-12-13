# 31

### First impression
```php
$port=rand(10000,10100);
$socket=fsockopen("$_GET[server]","$port",$errno,$errstr,3) or die("error : $errstr");
```
```
Warning: fsockopen() [function.fsockopen]: unable to connect to xxx.xxx.xxx.xxx:10034 (Connection timed out) in /home/hosting_users/webhacking/www/challenge/web/web-16/index.php on line 24
error : Connection timed out
```

### Inspection
* php 스크립트 분석.
	- `10000`~`10100` 사이 숫자로 포트 넘버를 정한 후, `?server=` 파라미터로 넘기는 곳으로 소켓을 연다.
	- `?server=` 파라미터에는 처음에는 현재 자신의 컴퓨터 IP가 넘어간다.
* [Well known ports, 10000 to 10999](http://www.networksorcery.com/enp/protocol/ip/ports10000.htm)

| Port | Transport | Protocol |
|:----:|:---------:|:--------:|
|10000 ||NDMP, Network Data Management Protocol.|
|10001||SCP Configuration.|
|10002|||
|10003||EMC-Documentum Content Server Product.|
|10004||EMC Replication Manager Client.|
|10005||EMC Replication Manager Server.|
|10006|||
|10007||MVS Capacity.|
|10008||Octopus Multiplexer.|
|10009||Systemwalker Desktop Patrol.|
|10010||ooRexx rxapi services.|
|10011-10049|||
|10050||Zabbix Agent.|
|10051||Zabbix Trapper.|
|10052-10054|||
|10055||Quantapoint FLEXlm Licensing Service.|
|10056-10079|||
|10080||Amanda.|
|10081||FAM Archive Server.|
|10082-10099|||
|10100||VERITAS ITAP DDTP.|

* `10000`~`10100`의 포트가 열린 서버 IP를 `?server=` 파라미터로 넘겨준다면 통과할 것 같다.

### Trial and error
* `localhost`, `127.0.0.1` 안된다.
