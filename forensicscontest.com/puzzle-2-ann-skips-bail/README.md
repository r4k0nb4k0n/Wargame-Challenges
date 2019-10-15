# [Puzzle #2: Ann Skips Bail](http://forensicscontest.com/2009/10/10/puzzle-2-ann-skips-bail)

## Description
```
After being released on bail, Ann Dercover disappears! Fortunately, investigators were carefully monitoring her network activity before she skipped town.

“We believe Ann may have communicated with her secret lover, Mr. X, before she left,” says the police chief. “The packet capture may contain clues to her whereabouts.”

You are the forensic investigator. Your mission is to figure out what Ann emailed, where she went, and recover evidence including:

1. What is Ann’s email address?
2. What is Ann’s email password?
3. What is Ann’s secret lover’s email address?
4. What two items did Ann tell her secret lover to bring?
5. What is the NAME of the attachment Ann sent to her secret lover?
6. What is the MD5sum of the attachment Ann sent to her secret lover?
7. In what CITY and COUNTRY is their rendez-vous point?
8. What is the MD5sum of the image embedded in the document?

Please use the Official Submission form to submit your answers. Prize TBD. Prize will be a Lenovo IdeaPad S10-2 – just like the free netbooks Sec558 students will get in Orlando.

Here is your evidence file:

http://forensicscontest.com/contest02/evidence02.pcap
MD5 (evidence02.pcap) = cfac149a49175ac8e89d5b5b5d69bad3

The MOST ELEGANT solution wins. In the event of a tie, the entry submitted first will receive the prize. Scripting is always encouraged. We love to see well-written, easy-to-use tools which automate even small sections of the evidence recovery. You are welcome to build upon the work of others, as long as their work has been released under a GPL license. (If it has been released under another free-software license, email us to confirm eligibility.) All responses should be submitted as plain text. Microsoft Word documents, PDFs, etc will NOT be reviewed.

Exceptional solutions may be incorporated into the SANS Network Forensics Toolkit. Authors agree that their code submissions will be freely published under the GPL license, in order to further the state of network forensics knowledge. Exceptional submissions may also be used as examples and tools in the Network Forensics class. All authors will receive full credit for their work.

Deadline is 11/15/09 11/22/09. Here’s the Official Submission form. Good luck!!

Share and Enjoy:
```
* 보석으로 풀려난 Ann Dercover가 사라졌다! 운이 좋게도, 수사관들은 특별히 그녀가 도시를 떠나기 전에 그녀의 네트워크 활동을 지켜보고 있었다. 
* "우리는 Ann이 떠나기 전 그녀의 비밀 애인 Mr. X와 접촉했을 거라 믿는다,"라고 경찰 서장은 말했다. "패킷 캡처가 그녀의 행방에 대한 단서를 담고 있을 지도 모른다."
* 당신은 포렌식 수사관이다. 당신의 임무는 Ann이 이메일로 보낸 것, 그녀가 간 장소, 그리고 다음을 포함한 증거를 복구하는 것이다:
	1. Ann의 이메일 주소는 무엇인가?
	2. Ann의 이메일 비밀번호는 무엇인가?
	3. Ann의 비밀 애인의 이메일 주소는 무엇인가?
	4. Ann이 비밀 애인더러 가져오라고 한 두 개의 물건은 무엇인가?
	5. Ann이 비밀 애인에게 보낸 첨부 파일의 이름은 무엇인가?
	6. Ann이 비밀 애인에게 보낸 첨부 파일의 MD5sum은 무엇인가?
	7. 그들이 만나기로 한 장소의 도시와 국가는 어디인가?
	8. 문서에 포함된 이미지의 MD5sum은 무엇인가?

## Explanation
![](./1.PNG?raw=true)
* Wireshark에서 해당 패킷 파일을 열고 Statistics - Conversations를 살펴보았다.
* 다음과 같이 Ann이 비밀 애인에게 보낸 이메일 내용을 볼 수 있다.

```
220 cia-mc07.mx.aol.com ESMTP mail_cia-mc07.1; Sat, 10 Oct 2009 15:37:56 -0400
EHLO annlaptop
250-cia-mc07.mx.aol.com host-69-140-19-190.static.comcast.net
250-AUTH=LOGIN PLAIN XAOL-UAS-MB 
250-AUTH LOGIN PLAIN XAOL-UAS-MB 
250-STARTTLS
250-CHUNKING
250-BINARYMIME
250-X-AOL-FWD-BY-REF
250-X-AOL-DIV_TAG
250-X-AOL-OUTBOX-COPY
250 HELP
AUTH LOGIN
334 VXNlcm5hbWU6
c25lYWt5ZzMza0Bhb2wuY29t
334 UGFzc3dvcmQ6
NTU4cjAwbHo=
235 AUTHENTICATION SUCCESSFUL
MAIL FROM: <sneakyg33k@aol.com>
250 OK
RCPT TO: <mistersecretx@aol.com>
250 OK
DATA
354 START MAIL INPUT, END WITH "." ON A LINE BY ITSELF
Message-ID: <001101ca49ae$e93e45b0$9f01a8c0@annlaptop>
From: "Ann Dercover" <sneakyg33k@aol.com>
To: <mistersecretx@aol.com>
Subject: rendezvous
Date: Sat, 10 Oct 2009 07:38:10 -0600
MIME-Version: 1.0
Content-Type: multipart/mixed;
	boundary="----=_NextPart_000_000D_01CA497C.9DEC1E70"
X-Priority: 3
X-MSMail-Priority: Normal
X-Mailer: Microsoft Outlook Express 6.00.2900.2180
X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2900.2180

This is a multi-part message in MIME format.

------=_NextPart_000_000D_01CA497C.9DEC1E70
Content-Type: multipart/alternative;
	boundary="----=_NextPart_001_000E_01CA497C.9DEC1E70"


------=_NextPart_001_000E_01CA497C.9DEC1E70
Content-Type: text/plain;
	charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

Hi sweetheart! Bring your fake passport and a bathing suit. Address =
attached. love, Ann
------=_NextPart_001_000E_01CA497C.9DEC1E70
Content-Type: text/html;
	charset="iso-8859-1"
Content-Transfer-Encoding: quoted-printable

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD>
<META http-equiv=3DContent-Type content=3D"text/html; =
charset=3Diso-8859-1">
<META content=3D"MSHTML 6.00.2900.2853" name=3DGENERATOR>
<STYLE></STYLE>
</HEAD>
<BODY bgColor=3D#ffffff>
<DIV><FONT face=3DArial size=3D2>Hi sweetheart! Bring your fake passport =
and a=20
bathing suit. Address attached. love, Ann</FONT></DIV></BODY></HTML>

------=_NextPart_001_000E_01CA497C.9DEC1E70--

------=_NextPart_000_000D_01CA497C.9DEC1E70
Content-Type: application/octet-stream;
	name="secretrendezvous.docx"
Content-Transfer-Encoding: base64
Content-Disposition: attachment;
	filename="secretrendezvous.docx"

UEsDBBQABgAIAAAAIQDleUAGfwEAANcFAAATAAgCW0NvbnRlbnRfVHlwZXNdLnhtbCCiBAIooAAC
```
* `AUTH LOGIN`과 `235 AUTHENTICATION SUCCESSFUL` 사이에 계정 정보가 드러난다.
	- `c25lYWt5ZzMza0Bhb2wuY29t` -> `sneakyg33k@aol.com`
	- `NTU4cjAwbHo=` -> `558r00lz`
* 메일 헤더에 비밀 애인의 메일 주소가 드러난다.
	- `To: <mistersecretx@aol.com>`
* 메일 본문에 비밀 애인더러 가져오라고 한 두 개의 물건이 나타난다.
	- `Bring your fake passport and a bathing suit`
* 메일 후반부에 첨부파일의 이름이 드러난다.
	- `name="secretrendezvous.docx"`

![](./2.PNG?raw=true)
* 패킷에 드러난 첨부파일은 base64 인코딩이 되어 있는 상태다. 이를 추출하여 디코딩하고 raw bytes 그대로 저장하면 .docx 파일이 보인다.
* 열어 보면 다음과 같이 영어 문장 두 개와 이미지 파일이 보인다.
* 이미지에 드러난 그들이 만나기로 한 장소의 도시와 국가는 Playa del Carmen, Mexico다.
* Office Word로도 이미지 파일을 추출할 수 있지만, 확장자를 `.zip`으로 바꿔서 열어보면 이미지 파일을 손쉽게 추출할 수 있다.
* 알아낸 정보들은 다음과 같다.
	1. What is Ann’s email address?
		- `sneakyg33k@aol.com`
	2. What is Ann’s email password?
		- `558r00lz`
	3. What is Ann’s secret lover’s email address?
		- `mistersecretx@aol.com`
	4. What two items did Ann tell her secret lover to bring?
		- His/her fake passport and a bathing suit
	5. What is the NAME of the attachment Ann sent to her secret lover?
		- `secretrendezvous.docx`
	6. What is the MD5sum of the attachment Ann sent to her secret lover?
		- `9E423E11DB88F01BBFF81172839E1923`
	7. In what CITY and COUNTRY is their rendez-vous point?
		- Playa del Carmen, Mexico
	8. What is the MD5sum of the image embedded in the document?
		- `AADEACE50997B1BA24B09AC2EF1940B7`