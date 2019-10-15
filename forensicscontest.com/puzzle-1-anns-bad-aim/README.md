# [Puzzle #1: Ann’s Bad AIM](http://forensicscontest.com/2009/09/25/puzzle-1-anns-bad-aim)

## Description
```
Anarchy-R-Us, Inc. suspects that one of their employees, Ann Dercover, is really a secret agent working for their competitor. Ann has access to the company’s prize asset, the secret recipe. Security staff are worried that Ann may try to leak the company’s secret recipe.

Security staff have been monitoring Ann’s activity for some time, but haven’t found anything suspicious– until now. Today an unexpected laptop briefly appeared on the company wireless network. Staff hypothesize it may have been someone in the parking lot, because no strangers were seen in the building. Ann’s computer, (192.168.1.158) sent IMs over the wireless network to this computer. The rogue laptop disappeared shortly thereafter.

“We have a packet capture of the activity,” said security staff, “but we can’t figure out what’s going on. Can you help?”

You are the forensic investigator. Your mission is to figure out who Ann was IM-ing, what she sent, and recover evidence including:

1. What is the name of Ann’s IM buddy?
2. What was the first comment in the captured IM conversation?
3. What is the name of the file Ann transferred?
4. What is the magic number of the file you want to extract (first four bytes)?
5. What was the MD5sum of the file?
6. What is the secret recipe?

Here is your evidence file:

http://forensicscontest.com/contest01/evidence01.pcap
MD5 (evidence.pcap) = d187d77e18c84f6d72f5845edca833f5

The MOST ELEGANT solution wins. In the event of a tie, the entry submitted first will receive the prize. Scripting is always encouraged. All responses should be submitted as plain text files.

Exceptional solutions may be incorporated into the SANS Network Forensics Toolkit. Authors agree that their code submissions will be freely published under the GPL license, in order to further the state of network forensics knowledge. Exceptional submissions may also be used as examples and tools in the Network Forensics class. All authors will receive full credit for their work.

Email submissions to answers@lakemissoulagroup.com. Deadline is 9/10/09. Good luck!!
```

* Anarchy-R-Us 유한회사는 직원 중 한 명인 Ann Dercover가 경쟁사의 비밀 요원이라고 의심한다. Ann은 회사의 값진 자산인 비밀 요리법에 접근할 수 있다. 보안 담당은 Ann이 회사의 비밀 요리법을 유출할 거라고 걱정한다.
* 보안 담당은 그동안 Ann의 활동을 지켜보았지만, 의심스러운 것을 찾을 수 없없다-지금까지는 말이다. 오늘 회사 무선 네트워크에 예상하지 못한 노트북이 나타났다. 보안 담당은 건물 내부에서 이상한 사람을 발견하지 못했기 때문에, 누군가 주차장에 있었다고 가설을 세웠다. Ann의 컴퓨터 (`192.168.1.158`)에서 이 컴퓨터로 인스턴트 메시지들을 보냈다. 그 노트북은 그 이후로 갑자기 사라졌다. 
* "우리는 그 활동의 패킷 캡처를 가지고 있어,", 보안 담당이 말했다, "하지만 도대체 무슨 일이 벌어졌는 지 알아내지 못하겠어. 도와줄래?"
* 당신은 포렌식 수사관이다. 당신의 임무는 Ann이 IM을 보낸 사람, 그녀가 보낸 것, 그리고 다음을 포함한 증거들을 복구하는 것이다:
	1. Ann의 IM 친구의 이름은 무엇인가?
	2. 캡처된 IM 대화의 첫 시작은 무엇이었는가?
	3. Ann이 전송한 파일의 이름은 무엇인가?
	4. 당신이 추출하고 싶은 파일의 매직 넘버는 무엇인가? (첫 네 개의 바이트들)
	5. 그 파일의 MD5sum은 무엇이었는가?
	6. 비밀 레시피는 무엇인가?

## Explanation
![](./1.PNG?raw=true)
* Wireshark에서 Statistics - Conversations로 들어간 다음 `192.168.1.158`로부터 나온 것들을 찾아보았다.
* 다음과 같이 IM 대화 내용과 상대방 ID, 전송한 파일 이름으로 추정되는 것들이 보인다.

![](./2.PNG?raw=true)
* `OFT2`, `Cool FileXfer`, `recipe.docx`가 보인다.
* `OFT2 packet`으로 검색하면 AOL Instant Messenger 관련 내용이 나온다. 해당 프로그램에서 파일을 전송할 때 쓰는 프로토콜로 추정된다. 
* `PK..|504b0304`는 .docx 파일의 헤더로 보인다.

![](./3.PNG?raw=true)
* 위 패킷 데이터를 Raw로 덤프하여 OFT2 관련 헤더를 삭제하고 열어보았다. 다음과 같이 레시피가 드러난다.

* 찾아낸 것들
	1. Ann의 IM 친구의 이름은 무엇인가?
		- `Sec558user1`
	2. 캡처된 IM 대화의 첫 시작은 무엇이었는가?
		- `Here's the secret recipe... I just downloaded it from the file server. Just copy to a thumb drive and you're good to go &gt;:-)`
	3. Ann이 전송한 파일의 이름은 무엇인가?
		- `recipe.docx`
	4. 당신이 추출하고 싶은 파일의 매직 넘버는 무엇인가? (첫 네 개의 바이트들)
		- `50 4b 03 04`
	5. 그 파일의 MD5sum은 무엇이었는가?
		- `8350582774E1D4DBE1D61D64C89E0EA1`
	6. 비밀 레시피는 무엇인가?
		```
Recipe for Disaster:
1 serving
Ingredients:
4 cups sugar
2 cups water
In a medium saucepan, bring the water to a boil. Add sugar. Stir gently over low heat until sugar is fully dissolved. Remove  the  saucepan from heat.  Allow to cool completely. Pour into gas tank. Repeat as necessary. 
		```
