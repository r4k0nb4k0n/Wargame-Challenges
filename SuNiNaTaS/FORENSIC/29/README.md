# 29

## Problem
```
Brothers - Download

 
 
유준혁은 PC가 고장나서 형 유성준에게 PC를 고쳐 달라고 했다.
그런데, 유성준은 동생의 PC를 고치면서 몇 가지 장난을 했다.
당신은 이 PC를 정상으로 돌려 놓아야 한다.

1. 웹 서핑은 잘 되는데, 네이버에만 들어가면 사이버 경찰청 차단 화면으로 넘어간다. 원인을 찾으면 Key가 보인다.
2. 유성준이 설치 해 놓은 키로거의 절대경로 및 파일명은?(모두 소문자)
- ex) c:\windows\notepad.exe
3. 키로거가 다운로드 된 시간은?
- ex) 2016-05-27_22:00:00 (yyyy-mm-dd_hh:mm:ss)
4. 키로거를 통해서 알아내고자 했던 내용은 무엇인가? 내용을 찾으면 Key가 보인다.

인증키 형식 : lowercase(MD5(1번키+2번답+3번답+4번키))

======================================================================================

Joon-hyeok asked Seong-joon to repair PC
After repairing, Seong-joon did something to PC
You should fix this PC.

Q1 : When you surf "www.naver.com", Web browser shows something wrong. Fix it and you can find a Key
Q2 : Installed Keylogger's location & filename(All character is lower case)
- ex) c:\windows\notepad.exe
Q3 : Download time of Keylogger
- ex) 2016-05-27_22:00:00 (yyyy-mm-dd_hh:mm:ss)
Q4 : What did Keylogger detect and save? There is a Key

Auth Key = lowercase(MD5(Key of Q1+Answer of Q2+Answer of Q3+Key of Q4))
```

## Background Knowledge
* [EGG Format Specification](./EGG_Specification.pdf) ~ [Link](http://sdn.altools.co.kr/etc/EGG_Specification.zip)
	- 알집을 개발한 이스트소프트의 압축 파일 포맷이다. 
	- Signature
		- EGG Header : `0x41474745` -> `EGGA` in Big-endian Ascii.
* [hosts (file) - Wikipedia](https://en.wikipedia.org/wiki/Hosts_%28file%29)
	- 컴퓨터 파일 **hosts**는 호스트 이름과 IP 주소를 연결해주는 운영체제 파일이다.
	- 최근 Windows에서의 위치는 `%SystemRoot%\System32\drivers\etc\hosts`이다. 
	- 애드웨어나 컴퓨터 바이러스, 트로이 목마같은 악성 소프트웨어에 의해 수정되어 의도한 곳으로 가야할 트래픽을 차단하거나 악의적인 콘텐츠를 호스팅하는 사이트로 우회시킬 수 있다.
* [What Files Make Up a Virtual Machine?](https://www.vmware.com/support/ws55/doc/ws_learning_files_in_a_vm.html)
	- `.log` 확장자는 VMware Workstation의 활동을 기록하는 파일의 것이다.
	- `.nvram` 확장자는 가상 머신의 상태를 저장하는 BIOS 파일의 것이다.
	- `.vmdk` 확장자는 가상 머신의 디스크 파일이다.
	- `.vmem` 확장자는 가상 머신의 페이징 파일의 것으로, 가상 머신의 메인 메모리를 호스트 머신의 파일로서 저장하는 것이다.
	- `.vmsd` 확장자는 스냅샷에 관한 정보와 메타데이터를 저장하는 파일의 것이다.
	- `.vmsn` 확장자는 스냅샷 당시 가상 머신의 작동 상황 정보를 저장하는 파일의 것이다.
	- `.vmx`, `.vmxf` 확장자는 가상 머신 설정 파일의 것이다.
* Web browser Forensic
	- [Web Browser Forensics: Part 1 by blueangel](./INSIGHT_Web-Browser-Forensics_Part1.pdf) ~ [Link](http://forensicinsight.org/wp-content/uploads/2012/03/INSIGHT_Web-Browser-Forensics_Part1.pdf)
		+ Internet Explorer의 기록들은 `index.dat` 파일로 여러 경로에 남아있다.
	- [An Overview of Web Browser Forensics](https://www.digitalforensics.com/blog/an-overview-of-web-browser-forensics/)


## Tool
* [HxD](https://mh-nexus.de/en/hxd/)
* [반디집](https://www.bandisoft.com/bandizip/)
* [AccessData FTK Imager](https://accessdata.com/product-download/ftk-imager-version-4.2.0)
* [Index.dat Analyzer](http://www.systenance.com/download/indexdat-setup.exe)

## Inspection and Solution
![](./1.PNG?raw=true)
* 문제 내용의 링크를 통해 `Windows7(SuNiNaTaS)` 파일을 받았다.
* 어떤 형식의 파일인지 잘 몰라서 HxD로 열어보니 헤더가 `EGGA`이다.
* `EGGA`는 `0x41474745`를 Big-endian의 순서로 ASCII 디코드한 것이다.
* 이는 알집을 개발한 이스트소프트의 압축 파일 포맷인 `EGG`의 Signature이다.

![](./2.PNG?raw=true)
* `.egg` 확장자를 붙여 `Windows7(SuNiNaTaS).egg`로 만들었다.
* 해당 파일의 압축을 해제한 후 살펴보니, 가상 머신 관련 파일들이 있다.

![](./3.PNG?raw=true)
* 문제에서 1번 항목인 `1. 웹 서핑은 잘 되는데, 네이버에만 들어가면 사이버 경찰청 차단 화면으로 넘어간다. 원인을 찾으면 Key가 보인다.`를 보고, 호스트 이름과 IP 주소를 연결해주는 운영체제 파일인 `hosts`가 떠올랐다.
* AccessData FTK Imager로 `Windows 7.vmdk` 이미지 파일을 열어 `C:\Windows\System32\drivers\etc\hosts` 파일의 내용을 살펴보니 1번 키가 나타났다.
* Key of Q1 is `what_the_he11_1s_keey`.

![](./4.PNG?raw=true)
* `C:\`에서 살펴보니 `v196vv8`이라는 매우 의심스러운 이름의 폴더를 발견했다.
* `C:\v196vv8\v1valv\Computer\24052016 #training\ss`에 수많은 스크린샷들을 발견했다.
* 스크린샷 내용 상 해당 폴더가 키로거와 관련되어 있음을 알 수 있다.
* Answer of Q2 is `c:\v196vv8\v1tvr0.exe`.

![](./5.PNG?raw=true)
* `C:\v196vv8\v1valv\Computer\24052016 #training\ss`를 좀더 뒤져보니 Internet Explorer에서 키로거 설치파일을 다운로드받는 스크린샷이 있다.
* 해당 파일 이름은 `pc-spy-2010-keylogger-surveillance-spy-3.exe`이다.
* IE 관련 로그들을 볼 필요가 있다.

![](./6.PNG?raw=true)
* `C:\Users\training\AppData\Local\Microsoft\Windows\History\History.IE5\index.dat`
* 브라우저 방문기록이 나타난다.
* `pc-spy-...` 파일 다운로드 경로 접속 시간이 나타난다.
* Answer of Q3 is `2016-05-24_04:25:06`.

![](./7.PNG?raw=true)
* `C:\v196vv8\v1valv\Computer\24052016 #training\z1.dat`에 키로깅 내용들이 기록되어있다.
* Key of Q4 is `blackkey is a Good man`.


* `lowercase(MD5("what_the_he11_1s_keey"+"c:\v196vv8\v1tvr0.exe"+"2016-05-24_04:25:06"+"blackkey is a Good man"))`를 제출하면 통과한다.

## Review
* 다른 사람들의 풀이을 보니 VMware에서 돌려보면서 이것저것 재미있게 푼 것 같다.