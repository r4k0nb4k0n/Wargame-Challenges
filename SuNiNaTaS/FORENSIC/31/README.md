# 31

## Problem
```
PDF Analysis

 
 
* 안내 : 본 PDF 파일은 PC에 유해한 작업을 하지 않습니다. 단순 문제 풀이용입니다.
악성코드가 첨부된 PDF를 분석하여 Flag를 찾으세요.
인증키 형식 : lowercase(MD5(Flag))

* Info : This PDF file don't attack your PC. Just using for study.
Analyze this PDF and Find a Flag.
Auth Key = lowercase(MD5(Flag))

down

Thanks to : dongbo
```

## Background Knowledge
* [Github zbetcheckin PDf_analysis](https://github.com/zbetcheckin/PDF_analysis)
    - ![](https://github.com/zbetcheckin/PDF_analysis/raw/master/pdf_ange_albertini.png?raw=true)

## Tool
* ParanoiDF
* pdf-parser.py

## Solution
![](./1.PNG?raw=true)
* ParanoiDF의 info 기능으로 살펴보니 의심스러운 object가 보인다.
* 39번이 여러번 보일 뿐더러, `/OpenAction`, `/Javascript`, `/JS`등을 달고 있다.

![](./2.PNG?raw=true)
* object 39번에 stream이 있길래 이를 살펴보았다.
* PDF 헤더와 푸터가 보인다. -> 숨겨진 파일이 있다.

![](./3.PNG?raw=true)
* pdf-parser.py를 사용하여 stream 39를 FlateDecode를 거친 결과를 `extracted.pdf`로 덤프한다.

![](./4.PNG?raw=true)
* 의심스러운 object를 열어보고 reference를 따라가보니 다음과 같이 FLAG가 나타난다.

![](./5.PNG?raw=true)
* `lowercase(MD5(Flag))`를 제출하면 된다.

## Review
* 이 문제 덕분에 악성코드가 들어있는 PDF를 어떻게 분석하는지 알게 되었다.
* PDF Steganography...?
* 숨겨진 PDF 파일을 잘못 덤프해서 파일 자체가 손상되어 플래그가 안보였다. 여기서 삽질을 3일 동안 했었다.

```
$ python2 paranoiDF.py -i Hello_SuNiNaTaS.pdf
File: Hello_SuNiNaTaS.pdf
MD5: 2a7a558ca100a0d9b9cf8973a0ad8424
SHA1: 8ed5e1da7f1021860ae56008788dd5892ce5b58c
Size: 25232 bytes
Version: 1.4
Binary: True
Linearized: False
Encrypted: False
Updates: 1
Objects: 40
Streams: 11
Comments: 0
Errors: 0

Version 0:
        Catalog: 2
        Info: 4
        Objects (29): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        Streams (8): [14, 13, 6, 18, 19, 20, 22, 23]
                Encoded (6): [14, 13, 6, 19, 20, 22]
                Decoding errors (1): [13]

Version 1:
        Catalog: 2
        Info: 4
        Objects (11): [2, 4, 23, 30, 31, 35, 36, 37, 38, 39, 40]
        Streams (3): [23, 37, 39]
                Encoded (1): [39]
        Suspicious elements:
                /OpenAction: [39]
                /Names: [2, 31, 38]
                /JavaScript: [30, 36, 39]
                /JS: [35, 39]
                /EmbeddedFiles: [30]
ParanoiDF> extractJS ./Hello_SuNiNaTaS.pdf
parsing ./Hello_SuNiNaTaS.pdf
Wrote JavaScript (5520 bytes -- 2911 headers / 2609 code) to file ./Hello_SuNiNaTaS.pdf.out
ParanoiDF>
```
* 의심스러운 요소에 Javascript가 있길래, `extractJS`를 이용하여 추출했다.

```javascript
info.title = String('find\x20the\x20key');
this.title = info.title;
info.Title = info.title;
app.doc.title = info.title;
app.doc.Title = info.title;
info.author = String('capcorps');
this.author = info.author;
info.Author = info.author;
app.doc.author = info.author;
app.doc.Author = info.author;
info.creator = String('Hancom\x20PDF\x201\x2e3\x2e0\x2e480');
this.creator = info.creator;
info.Creator = info.creator;
app.doc.creator = info.creator;
app.doc.Creator = info.creator;
info.producer = String('Hancom\x20PDF\x201\x2e3\x2e0\x2e480');
this.producer = info.producer;
info.Producer = info.producer;
app.doc.producer = info.producer;
app.doc.Producer = info.producer;
info.creationdate = String('D\x3a20160526050544\x2b09\x5cx2700\x5cx27');
this.creationdate = info.creationdate;
info.CreationDate = info.creationdate;
app.doc.creationdate = info.creationdate;
app.doc.CreationDate = info.creationdate;
app.doc.creationDate = info.creationdate;
info.creationDate = info.creationdate;
info.moddate = String('D\x3a20160526050544\x2b09\x5cx2700\x5cx27');
this.moddate = info.moddate;
info.ModDate = info.moddate;
app.doc.moddate = info.moddate;
app.doc.ModDate = info.moddate;
info.title = String('find\x20the\x20key');
this.title = info.title;
info.Title = info.title;
app.doc.title = info.title;
app.doc.Title = info.title;
info.author = String('capcorps');
this.author = info.author;
info.Author = info.author;
app.doc.author = info.author;
app.doc.Author = info.author;
info.creator = String('Hancom\x20PDF\x201\x2e3\x2e0\x2e480');
this.creator = info.creator;
info.Creator = info.creator;
app.doc.creator = info.creator;
app.doc.Creator = info.creator;
info.producer = String('Hancom\x20PDF\x201\x2e3\x2e0\x2e480');
this.producer = info.producer;
info.Producer = info.producer;
app.doc.producer = info.producer;
app.doc.Producer = info.producer;
info.creationdate = String('D\x3a20160526050544\x2b09\x5cx2700\x5cx27');
this.creationdate = info.creationdate;
info.CreationDate = info.creationdate;
app.doc.creationdate = info.creationdate;
app.doc.CreationDate = info.creationdate;
app.doc.creationDate = info.creationdate;
info.creationDate = info.creationdate;
info.moddate = String('D\x3a20160526070004\x2b09\x5cx2700\x5cx27');
this.moddate = info.moddate;
info.ModDate = info.moddate;
app.doc.moddate = info.moddate;
app.doc.ModDate = info.moddate;
info.moddate = String('D\x3a20160525212830Z');
this.moddate = info.moddate;
info.ModDate = info.moddate;
app.doc.moddate = info.moddate;
app.doc.ModDate = info.moddate;
info.creationdate = String('D\x3a20160525213559Z');
this.creationdate = info.creationdate;
info.CreationDate = info.creationdate;
app.doc.creationdate = info.creationdate;
app.doc.CreationDate = info.creationdate;
app.doc.creationDate = info.creationdate;
info.creationDate = info.creationdate;
c = []; zzzpages.push(c); this.numPages = zzzpages.length;

//jsunpack End PDF headers
Cvar Base64 = {
	_keyStr : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
	decode : function (input) {
		for (var ah = 0; ah < (input.length); ah++){
			input=input.replace("'+'", "");
		}
		var rlLwarzv = "";
		var chr1, chr2, chr3;
		var enc1, enc2, enc3, enc4;
		var i = 0;
		input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
		while (i < input.length) {
			enc1 = this._keyStr.indexOf(input.charAt(i++));
			enc2 = this._keyStr.indexOf(input.charAt(i++));
			enc3 = this._keyStr.indexOf(input.charAt(i++));
			enc4 = this._keyStr.indexOf(input.charAt(i++));
			chr1 = (enc1 << 2) | (enc2 >> 4);
			chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
			chr3 = ((enc3 & 3) << 6) | enc4;
			rlLwarzv = rlLwarzv + String.fromCharCode(chr1);
			if (enc3 != 64) {
				rlLwarzv = rlLwarzv + String.fromCharCode(chr2);
			}
			if (enc4 != 64) {
				rlLwarzv = rlLwarzv + String.fromCharCode(chr3);
			}
		}
		eval(rlLwarzv);
	}
}
Base64.decode("'Vm0'+'wd2Qy'+'UXlW'+'a1pP'+'VldS'+'WFYw'+'ZG9WV'+'ll3W'+'kc5V'+'01Wb'+'DNXa2'+'M1VjF'+'Kc2JET'+'lhhMU'+'pUV'+'mpGS'+'2RHVk'+'dX'+'bFpOY'+'WtFe'+'FZtc'+'EdZV'+'1JIV'+'mtsa'+'QpSb'+'VJPW'+'W14R'+'00x'+'WnR'+'NWH'+'BsU'+'m1S'+'SVZ'+'tdF'+'dVZ'+'3Bp'+'Umx'+'wd1'+'ZXM'+'TRkM'+'VZX'+'WkZ'+'kYV'+'JGS'+'lVU'+'V3N'+'4Tk'+'ZaS'+'E5V'+'OVhR'+'WEJ'+'wVW'+'01Q'+'1dW'+'ZHNa'+'RFJa'+'ClYx'+'WlhWM'+'jVLVm1'+'FeVVtR'+'ldh'+'a1p'+'MVj'+'BaV'+'2RF'+'NVZ'+'PV2'+'hSV'+'0VK'+'VVd'+'XeG'+'FTM'+'VpX'+'V2t'+'kVm'+'EwN'+'VVD'+'azF'+'XV2'+'xoV'+'01X'+'aHZ'+'WMG'+'RLU'+'jJO'+'SVR'+'sWm'+'kKV'+'0do'+'NlZ'+'HeG'+'FZV'+'k5I'+'VWt'+'oU2'+'JXa'+'FdW'+'MFZ'+'LVl'+'ZkW'+'E1U'+'QlR'+'NV1'+'JYV'+'jI1'+'U2Fs'+'SllV'+'bkJEY'+'XpGV1'+'kwWm'+'9XR0'+'V4Y'+'0hK'+'V01'+'uTjN'+'aVmR'+'HUjJ'+'GRwp'+'WbGN'+'LWW'+'toQm'+'VsZH'+'NaR'+'FJa'+'Vms1'+'R1R'+'sWm'+'tZV'+'kp1U'+'WxkV'+'01GW'+'kxWb'+'FprV'+'0Ux'+'VVF'+'sUk'+'5WbH'+'BJVm'+'pKMG'+'ExZH'+'RWbk'+'pYYm'+'tKRV'+'lYcE'+'dWMW'+'t3Cl'+'dtOV'+'hSMF'+'Y1WV'+'VWN'+'FYw'+'MUh'+'Va3'+'hXT'+'VZw'+'WFl'+'6Rm'+'Fjd3'+'BqUj'+'J0T'+'FZXM'+'DFRM'+'kl4W'+'khOY'+'VJGS'+'mFWa'+'kZLU'+'1ZadG'+'RHOV'+'ZSbH'+'AxV'+'Vd4'+'a1Y'+'wMU'+'cKV'+'2t4'+'V2J'+'GcH'+'JWMG'+'RTU'+'jFw'+'SGR'+'FNV'+'diS'+'EJK'+'Vmp'+'KMF'+'lXS'+'XlS'+'WGh'+'UV0'+'dSW'+'Vlt'+'dGF'+'SVm'+'xzV'+'m5k'+'WFJ'+'sbD'+'VDb'+'VJI'+'T1Z'+'oU0'+'1GW'+'TFX'+'VlZ'+'hVT'+'FZeA'+'pTWH'+'BoU0'+'VwV1'+'lsaE'+'5lRl'+'pxUm'+'xkam'+'QzQn'+'FVak'+'owVE'+'ZaWE'+'1UUm'+'tNa'+'2w0'+'VjJ'+'4a1'+'ZtR'+'XlV'+'bGh'+'VVm'+'xae'+'lRr'+'WmF'+'kR1'+'ZJV'+'Gxw'+'V2E'+'zQj'+'VWa'+'ko0'+'CmE'+'xWX'+'lTb'+'lVL'+'VVc'+'1V1'+'ZXS'+'kZW'+'VFZ'+'WUm'+'tVN'+'VVG'+'RTl'+'QUT'+'09'");
```
* 여기서 `Base64.decode`의 입력값에 눈길이 간다. 저 입력값을 `Base64.decode`로 여러번 처리해본다.

```
$ cat suspicious.js
...
var a = Base64.decode("'Vm0'+'wd2Qy'+'UXlW'+'a1pP'+'VldS'+'WFYw'+'ZG9WV'+'ll3W'+'kc5V'+'01Wb'+'DNXa2'+'M1VjF'+'Kc2JET'+'lhhMU'+'pUV'+'mpGS'+'2RHVk'+'dX'+'bFpOY'+'WtFe'+'FZtc'+'EdZV'+'1JIV'+'mtsa'+'QpSb'+'VJPW'+'W14R'+'00x'+'WnR'+'NWH'+'BsU'+'m1S'+'SVZ'+'tdF'+'dVZ'+'3Bp'+'Umx'+'wd1'+'ZXM'+'TRkM'+'VZX'+'WkZ'+'kYV'+'JGS'+'lVU'+'V3N'+'4Tk'+'ZaS'+'E5V'+'OVhR'+'WEJ'+'wVW'+'01Q'+'1dW'+'ZHNa'+'RFJa'+'ClYx'+'WlhWM'+'jVLVm1'+'FeVVtR'+'ldh'+'a1p'+'MVj'+'BaV'+'2RF'+'NVZ'+'PV2'+'hSV'+'0VK'+'VVd'+'XeG'+'FTM'+'VpX'+'V2t'+'kVm'+'EwN'+'VVD'+'azF'+'XV2'+'xoV'+'01X'+'aHZ'+'WMG'+'RLU'+'jJO'+'SVR'+'sWm'+'kKV'+'0do'+'NlZ'+'HeG'+'FZV'+'k5I'+'VWt'+'oU2'+'JXa'+'FdW'+'MFZ'+'LVl'+'ZkW'+'E1U'+'QlR'+'NV1'+'JYV'+'jI1'+'U2Fs'+'SllV'+'bkJEY'+'XpGV1'+'kwWm'+'9XR0'+'V4Y'+'0hK'+'V01'+'uTjN'+'aVmR'+'HUjJ'+'GRwp'+'WbGN'+'LWW'+'toQm'+'VsZH'+'NaR'+'FJa'+'Vms1'+'R1R'+'sWm'+'tZV'+'kp1U'+'WxkV'+'01GW'+'kxWb'+'FprV'+'0Ux'+'VVF'+'sUk'+'5WbH'+'BJVm'+'pKMG'+'ExZH'+'RWbk'+'pYYm'+'tKRV'+'lYcE'+'dWMW'+'t3Cl'+'dtOV'+'hSMF'+'Y1WV'+'VWN'+'FYw'+'MUh'+'Va3'+'hXT'+'VZw'+'WFl'+'6Rm'+'Fjd3'+'BqUj'+'J0T'+'FZXM'+'DFRM'+'kl4W'+'khOY'+'VJGS'+'mFWa'+'kZLU'+'1ZadG'+'RHOV'+'ZSbH'+'AxV'+'Vd4'+'a1Y'+'wMU'+'cKV'+'2t4'+'V2J'+'GcH'+'JWMG'+'RTU'+'jFw'+'SGR'+'FNV'+'diS'+'EJK'+'Vmp'+'KMF'+'lXS'+'XlS'+'WGh'+'UV0'+'dSW'+'Vlt'+'dGF'+'SVm'+'xzV'+'m5k'+'WFJ'+'sbD'+'VDb'+'VJI'+'T1Z'+'oU0'+'1GW'+'TFX'+'VlZ'+'hVT'+'FZeA'+'pTWH'+'BoU0'+'VwV1'+'lsaE'+'5lRl'+'pxUm'+'xkam'+'QzQn'+'FVak'+'owVE'+'ZaWE'+'1UUm'+'tNa'+'2w0'+'VjJ'+'4a1'+'ZtR'+'XlV'+'bGh'+'VVm'+'xae'+'lRr'+'WmF'+'kR1'+'ZJV'+'Gxw'+'V2E'+'zQj'+'VWa'+'ko0'+'CmE'+'xWX'+'lTb'+'lVL'+'VVc'+'1V1'+'ZXS'+'kZW'+'VFZ'+'WUm'+'tVN'+'VVG'+'RTl'+'QUT'+'09'");

for (var ah = 0; ah < 10; ah++){

    a = Base64.decode(a);
	console.log(a);
}
$ node suspicious.js
Vm0wd2VFNUdWWGhUV0doV1YwZG9WRll3WkRSV1JteFZVMjA1VjFadGVIbFdNblF3Vm1zeFdHVkVR
bFZpUmxwUVdWZDRTMk14VG5OWApiRnBYWld4YWVWWnJVa2RaVjFKWFVtNU9hQXBTYlZKVVZGUkNT
MVZXV1hoWGJGcHNVbXhzTlZaSGRHRmhVWEJUWW10S1dWWnRjRXRpCk1VcFhXa1prV2sweWFGaFVW
bHAzWld4YVNFNVdaRnBWV0VKVVdXMTBTMVZHV2tkWmVrWnBDazFWY0ZoWGEyaExWMGRLV1ZWc1Zs
cGkKUm5Cb1dsZDRZV1JIVmtoUFZuQldWMFZLVlZkWGRGZGtNVlpIV2tab2ExSXdXbkZEYlVwWFYy
dG9XR0V5YUZSV1IzaHJVbXMxVjFWcwpjR2tLVW14d2IxWldVa2RXTVVsNFZteHNZVkpyV2xkV2Ju
QnVUbEU5UFE9PQ==
Vm0weE5GVXhTWGhWV0doVFYwZDRWRmxVU205V1ZteHlWMnQwVmsxWGVEQlViRlpQWVd4S2MxTnNX
bFpXZWxaeVZrUkdZV1JXUm5OaApSbVJUVFRCS1VWWXhXbFpsUmxsNVZHdGFhUXBTYmtKWVZtcEti
MUpXWkZkWk0yaFhUVlp3ZWxaSE5WZFpVWEJUWW10S1VGWkdZekZpCk1VcFhXa2hLV0dKWVVsVlpi
RnBoWld4YWRHVkhPVnBWV0VKVVdXdFdkMVZHWkZoa1IwWnFDbUpXV2toWGEyaFRWR3hrUms1V1Vs
cGkKUmxwb1ZWUkdWMUl4VmxsYVJrWldWbnBuTlE9PQ==
Vm0xNFUxSXhVWGhTV0d4VFlUSm9WVmxyV2t0Vk1XeDBUbFZPYWxKc1NsWlZWelZyVkRGYWRWRnNh
RmRTTTBKUVYxWlZlRll5VGtaaQpSbkJYVmpKb1JWZFdZM2hXTVZwelZHNVdZUXBTYmtKUFZGYzFi
MUpXWkhKWGJYUlVZbFphZWxadGVHOVpVWEJUWWtWd1VGZFhkR0ZqCmJWWkhXa2hTVGxkRk5WUlpi
RlpoVVRGV1IxVllaRkZWVnpnNQ==
Vm14U1IxUXhSWGxTYTJoVVlrWktVMWx0TlVOalJsSlZVVzVrVDFadVFsaFdSM0JQV1ZVeFYyTkZi
RnBXVjJoRVdWY3hWMVpzVG5WYQpSbkJPVFc1b1JWZHJXbXRUYlZaelZteG9ZUXBTYkVwUFdXdGFj
bVZHWkhSTldFNVRZbFZhUTFWR1VYZFFVVzg5
VmxSR1QxRXlSa2hUYkZKU1ltNUNjRlJVUW5kT1ZuQlhWR3BPWVUxV2NFbFpWV2hEWVcxV1ZsTnVa
RnBOTW5oRVdrWmtTbVZzVmxoYQpSbEpPWWtacmVGZHRNWE5TYlVaQ1VGUXdQUW89
VlRGT1EyRkhTbFJSYm5CcFRUQndOVnBXVGpOYU1WcElZVWhDYW1WVlNuZFpNMnhEWkZkSmVsVlha
RlJOYkZreFdtMXNSbUZCUFQwPQo=
VTFOQ2FHSlRRbnBpTTBwNVpWTjNaMVpIYUhCamVVSndZM2xDZFdJelVXZFRNbFkxWm1sRmFBPT0=

U1NCaGJTQnpiM0p5ZVN3Z1ZHaHBjeUJwY3lCdWIzUWdTMlY1ZmlFaA==
SSBhbSBzb3JyeSwgVGhpcyBpcyBub3QgS2V5fiEh
I am sorry, This is not Key~!!
```
* 낚였다.