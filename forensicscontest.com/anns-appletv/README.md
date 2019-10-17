# [Puzzle #3: Ann’s AppleTV](http://forensicscontest.com/2009/12/28/anns-appletv)

## Description
```
Ann and Mr. X have set up their new base of operations. While waiting for the extradition paperwork to go through, 

you and your team of investigators covertly monitor her activity. Recently, Ann got a brand new AppleTV, and 

configured it with the static IP address 192.168.1.10. Here is the packet capture with her latest activity.

You are the forensic investigator. Your mission is to find out what Ann searched for, build a profile of her 

interests, and recover evidence including:

1. What is the MAC address of Ann’s AppleTV?
-> Source: Apple_fe:07:c4 (00:25:00:fe:07:c4)
2. What User-Agent string did Ann’s AppleTV use in HTTP requests?
-> User-Agent: AppleTV/2.4\r\n
3. What were Ann’s first four search terms on the AppleTV (all incremental searches count)?
-> hack(h, ha, hac, hack)
4. What was the title of the first movie Ann clicked on?
-> Hackers
5. What was the full URL to the movie trailer (defined by “preview-url”)?
-> http://a227.v.phobos.apple.com/us/r1000/008/Video/62/bd/1b/mzm.plqacyqb..640x278.h264lc.d2.p.m4v
6. What was the title of the second movie Ann clicked on?
-> Sneakers
7. What was the price to buy it (defined by “price-display”)?
-> $9.99
8. What was the last full term Ann searched for?
-> iknowyourewatchingme

Prize: Ann’s AppleTV (of course!)

Deadline is 2/01/10 (11:59:59PM UTC-11) (In other words, if it’s still 2/01/10 anywhere in the world, you can 

submit your entry.)

Please use the Official Submission form to submit your answers. Here is your evidence file:
http://forensicscontest.com/contest03/evidence03.pcap
MD5 (evidence03.pcap) = f8a01fbe84ef960d7cbd793e0c52a6c9

The MOST ELEGANT solution wins. In the event of a tie, the entry submitted first will receive the prize. Coding is 

always encouraged. We love to see well-written, easy-to-use tools which automate even small sections of the 

evidence recovery. Graphical and command-line tools are all eligible. You are welcome to build upon the work of 

others, as long as their work has been released under a GPL license. (If it has been released under another free-

software license, email us to confirm eligibility.) All responses should be submitted as plain text. Microsoft Word 

documents, PDFs, etc will NOT be reviewed.

Feel free to collaborate with other people and discuss ideas back and forth. You can even submit as a team (there 

will be only one prize). However, please do not publish the answers before the deadline, or you (and your team) 

will be automatically disqualified. Also, please understand that the contest materials are copyrighted and that we’

re offering them publicly for the community to enjoy. You are welcome to publish full solutions after the deadline, 

but please use proper attributions and link back. If you are interested in using the contest materials for other 

purposes, just ask first.

Exceptional solutions may be incorporated into the SANS Network Forensics Toolkit. Authors agree that their code 

submissions will be freely published under the GPL license, in order to further the state of network forensics 

knowledge. Exceptional submissions may also be used as examples and tools in the Network Forensics class. All 

authors will receive full credit for their work.

Deadline is 2/01/10 (11:59:59PM UTC-11). Here’s the Official Submission form. Good luck!!

Copyright 2009, Lake Missoula Group, LLC. All rights reserved.

Share and Enjoy:
```
* Ann과 Mr. X는 새로운 작전기반을 마련했다. 범죄인 인도 서류 작업이 끝나기를 기다리는 동안, 당신과 팀원들은 그녀의 활동을 은밀하게 감시했다. 최근에, Ann은 새로 출시된 AppleTV를 구매했고, 이를 정적 IP 주소 `192.168.1.10`으로 설정했다. 여기에 그녀의 최근 활동이 담긴 패킷 캡처가 있다.
* 당신은 포렌식 수사관이다. 당신의 임무는 Ann이 무엇을 검색했는지 찾고, 그녀의 관심사에 대한 프로필을 작성하며, 다음을 포함한 증거들을 복구하는 것이다:
	1. Ann의 AppleTV의 MAC 주소는 무엇인가?
	2. Ann의 AppleTV가 HTTP 요청에서 사용하는 User-Agent 스트링은 무엇인가?
	3. Ann이 AppleTV에서 처음 검색한 네 개의 검색어는 무엇인가 (증분 검색 포함)?
	4. Ann이 클릭한 첫번째 영화의 제목은 무엇인가?
	5. 그 영화의 트레일러의 완전한 URL은 무엇인가 ("preview-url"로 정의된 것)?
	6. Ann이 클릭한 두번째 영화의 제목은 무엇인가?
	7. 그 영화의 구매 가격은 얼마인가 ("price-display"로 정의된 것)?
	8. Ann이 마지막으로 검색한 검색어는 무엇인가?

## Explanation
![](./1.PNG?raw=true)
* 패킷 캡처 파일을 WireShark로 열어보았다.
* Ann의 AppleTV가 정적 IP 주소 `192.168.1.10`으로 설정되었다는 것을 이용하여 `ip.addr == 192.168.1.10` 필터를 걸어보았다.
* 필터 결과에 나온 패킷 중 하나를 보면 다음과 같이 데이터 링크 레이어의 Source MAC address가 AppleTV의 MAC address임을 알 수 있다.
	- `00:25:00:fe:07:c4`

![](./2.PNG?raw=true)
* Ann의 AppleTV에서 사용된 HTTP 요청을 살펴보기 위해 `ip.addr == 192.168.1.10 && http.request` 필터를 걸어보았다.
* 필터 결과에 나온 패킷 중 하나를 보면 User-Agent string을 확인할 수 있다.
	- `AppleTV/2.4`

![](./3.PNG?raw=true)
* Ann이 AppleTV에서 검색한 검색어를 알기 위해 `ip.addr == 192.168.1.10 && http.request.uri.path contains "incrementalSearch"` 필터를 걸어보았다.
* 첫 4개의 패킷의 HTTP GET 쿼리를 보고 Ann이 처음 검색한 네 개의 검색어를 순차적으로 확인할 수 있다.
	- `h`
	- `ha`
	- `hac`
	- `hack`

![](./4.PNG?raw=true)
* 이전과 같은 필터에서 맨 마지막 패킷을 보면 Ann이 마지막으로 검색한 검색어를 알 수 있다.
	- `iknowyourewatchingme`

![](./5.PNG?raw=true)
* Ann이 클릭한 영화들을 알아내기 위해 `http.request.uri contains "viewMovie" || http.response_for.uri contains "viewMovie""` 필터를 걸어보았다.
* 필터 결과에 나온 패킷들 중 HTTP 응답 내용이 XML인 것들에 Ann이 클릭한 영화들의 정보가 담겨 있다.
	- `Hackers`
		- `preview-url`: `http://a227.v.phobos.apple.com/us/r1000/008/Video/62/bd/1b/mzm.plqacyqb..640x278.h264lc.d2.p.m4v`
	- `Sneakers`
		- `price-display`: `$9.99`
* 다음 정보들을 알아낼 수 있었다.
	1. Ann의 AppleTV의 MAC 주소는 무엇인가?
		- `00:25:00:fe:07:c4`
	2. Ann의 AppleTV가 HTTP 요청에서 사용하는 User-Agent 스트링은 무엇인가?
		- `AppleTV/2.4`
	3. Ann이 AppleTV에서 처음 검색한 네 개의 검색어는 무엇인가 (증분 검색 포함)?
		- `h`
		- `ha`
		- `hac`
		- `hack`
	4. Ann이 클릭한 첫번째 영화의 제목은 무엇인가?
		- `Hackers`
	5. 그 영화의 트레일러의 완전한 URL은 무엇인가 ("preview-url"로 정의된 것)?
		- `http://a227.v.phobos.apple.com/us/r1000/008/Video/62/bd/1b/mzm.plqacyqb..640x278.h264lc.d2.p.m4v`
	6. Ann이 클릭한 두번째 영화의 제목은 무엇인가?
		- `Sneakers`
	7. 그 영화의 구매 가격은 얼마인가 ("price-display"로 정의된 것)?
		- `$9.99`
	8. Ann이 마지막으로 검색한 검색어는 무엇인가?
		- `iknowyourewatchingme`
