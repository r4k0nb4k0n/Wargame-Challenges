# 26

## Problem
```
Cipher III : Frequency analysis

This challenge is to recover the plaintext from the following ciphertext using frequency analysis:
 
szqkagczvcvyabpsyincgozdainvscbnivpnzvbpnyfkqhzmmpcqhzygzgfcxznvvzgdfnvbpnjyifxmpcqhzygbpnoyaim
ygbzgngbvmpcqhzygcbpinnbzqndicgxhiztozgcfmpcqhzygbpnjyifxeagzyimpcqhzygbpneagzyidicgxhiztozgcfm
pcqhzygcgxcoyaibzqnvyabpsyincggcbzygcfmpcqhzygszqzvbpnozivbvyabpsyincgozdainvscbnibyjzgcqnxcfcb
cgzvaeagzyiyivngzyidicgxhiztnungbzvampcqhzygvpzhcgxbpnyfkqhzmdcqnvvpnzvbpnozivbonqcfnvscbnibyjz
gbpnyfkqhzmdcqnvbpnjyifxmpcqhzygvpzhvbpnoyaimygbzgngbvmpcqhzygvpzhvcgxbpndicgxhiztozgcfvpnzvygn
yobpnqyvbpzdpfkinmydgzlnxcbpfnbnvcgxqnxzcozdainvzgvyabpsyinccvyochizfbpzvkncivpnzvicgsnxvnmygxz
gbpnjyifxrkbpnzgbnigcbzygcfvscbzgdagzygvpnzvbpnmaiingbinmyixpyfxnioyifcxznvzgbpnvpyibhiydicqbpn
oinnvscbzgdcgxbpnmyqrzgnxbybcfagxnibpnzvaeaxdzgdvkvbnqvpnzvcfvybpnozivbonqcfnvscbnibyvaihcvvbpn
bjypaxincxhyzgbqcisagxnibpnzvaeaxdzgdvkvbnqvpnpcvgnunirnnghfcmnxyoobpnhyxzaqzgpningbzinmcinni

Note that we have omitted the blank letters and punctuation marks of the plaintext.
```

## Background Knowledge
* [Frequency analysis - Wikipedia](https://en.wikipedia.org/wiki/Frequency_analysis)
    - 암호학에서의 빈도분석은 평문과 암호문에 사용되는 문자 또는 문자열의 출현빈도를 이용하는 암호해독법이다.
    - 평문 언어의 통계적 특징을 전제로 하여, 암호문만을 사용해서 해독을 진행하기 때문에, 암호문 단독공격으로 분류된다.
* 가장 많이 나오는 것
    - Single character -> `E`
    - Trigram -> `THE`

## Inspection
* 가독성을 위해 암호문을 소문자로, **복호문을 대문자로** 표시한다.

| Character | Counts | Frequency | Bigram | Counts | Frequency | Trigram | Counts | Frequency |
|:---------:|-------:|:---------:|:------:|-------:|:---------:|:-------:|-------:|:---------:|
|**n**|**92**|**10.79%**|**pn**|**19**|**4.46%**|**bpn**|**8**|**2.82%**|
|z|78|9.14%|**bp**|**16**|**3.76%**|qhz|6|2.11%|
|g|69|8.09%|in|11|2.58%|cgx|4|1.41%|
|b|65|7.62%|yg|10|2.35%|hzy|4|1.41%|
|c|65|7.62%|zg|10|2.35%|pcq|4|1.41%|
|v|62|7.27%|gb|9|2.11%|mpc|4|1.41%|
|i|60|7.03%|cq|9|2.11%|vpn|4|1.41%|
|y|59|6.92%|yi|8|1.88%|qnv|3|1.06%|
|p|58|6.8%|hz|8|1.88%|hiz|3|1.06%|
* 단일 글자에서 `n`이 제일 많으므로 통계상 이를 `E`로 치환한다.
* Bigram에서 `pn`이 제일 많으므로 통계상 이를 `HE`로 치환한다.
* Trigram에서 `bpn`이 제일 많으므로 통계상 이를 `THE`로 치환한다.

```
szqkagc zv c vyaTHsyiEc g ozdaiEv scTEi vHE zv THE yfkqhzm mHcqhzyg 
zgfcxzEvvzgdfEv THE jyifx mHcqhzyg  THE oyaimygTzgEgTv mHcqhzyg 
cTHiEETzqE di cgx hiztozgcf mHcqhzyg THE jyifx eagzyi mHcqhzyg THE 
eagzyi di cgx hiztozgcf mHcqhzyg cgx coyaiTzqE vyaTHsyiEc ggcTzygcf 
mHcqhzyg szq zv THE ozivT vyaTHsyiEc g ozdaiEv scTEi Tyjzg cqExcfcTcg zv 
aeagzyiyivEgzyidi cgx hiztEuEgT zv a mHcqhzyg vHzh cgx THE yfkqhzm dcqEv 
vHE zv THE ozivT oEqcfEv scTEi Tyjzg THE yfkqhzm dcqEv THE jyifx 
mHcqhzyg vHzhv THE oyaimygTzgEgTv mHcqhzyg vHzhv cgx THE di cgx 
hiztozgcf vHE zv ygEyo THE qyvTHzdHfkiEmydgzlExcTHfETEv cgx qExzc 
ozdaiEv zg vyaTHsyiEc cvyochizfTH zv kEci vHE zv icgsExvEmygxzg THE 
jyifx rk THE zgTEigcTzygcfvscTzgdagzyg vHE zv THE 
maiiEgTiEmyixHyfxEioyifcxzEvzg THE vHyiThiydicq THE oiEEvscTzgd cgx THE 
myqrzgExTyTcf agxEi THE zv aeaxdzgdvkvTEq vHE zv cfvy THE ozivT oEqcfEv 
scTEi Tyvaihcvv THE TjyHaxiEcxhyzgTqcis agxEi THE zv aeaxdzgdvkvTEq vHE 
HcvgEuEirEEghfcmExyoo THE hyxzaqzgHEiEgTziEmciEEi
```
* `b`, `p`, `n`을 각각 `T`, `H`, `E`로 치환한 후, `THE`의 앞뒤에 공백을 삽입한다.
* 그리고 일치하는 토큰들을 기준으로 앞뒤에 공백을 넣는다.
* `vHE`, `zv`, `cgx`가 꽤 반복되는 것을 알 수 있다.

```
sIqkaNA IS A SyaTHsyiEA N oIdaiES sATEi SHE IS THE yfkqhIm mHAqhIyN 
INfADIESSINdfES THE jyifD mHAqhIyN THE oyaimyNTINENTS mHAqhIyN 
ATHiEETIqE di AND hiItoINAf mHAqhIyN THE jyifD eaNIyi mHAqhIyN THE 
eaNIyi di AND hiItoINAf mHAqhIyN AND AoyaiTIqE SyaTHsyiEA NNATIyNAf 
mHAqhIyN sIq IS THE oIiST SyaTHsyiEA N oIdaiES sATEi TyjIN AqEDAfATAN IS 
aeaNIyiyiSENIyidi AND hiItEuENT IS a mHAqhIyN SHIh AND THE yfkqhIm dAqES 
SHE IS THE oIiST oEqAfES sATEi TyjIN THE yfkqhIm dAqES THE jyifD 
mHAqhIyN SHIhS THE oyaimyNTINENTS mHAqhIyN SHIhS AND THE di AND 
hiItoINAf SHE IS yNEyo THE qySTHIdHfkiEmydNIlEDATHfETES AND qEDIA 
oIdaiES IN SyaTHsyiEA ASyoAhiIfTH IS kEAi SHE IS iANsEDSEmyNDIN THE 
jyifD rk THE INTEiNATIyNAfSsATINdaNIyN SHE IS THE 
maiiENTiEmyiDHyfDEioyifADIESIN THE SHyiThiydiAq THE oiEESsATINd AND THE 
myqrINEDTyTAf aNDEi THE IS aeaDdINdSkSTEq SHE IS AfSy THE oIiST oEqAfES 
sATEi TySaihASS THE TjyHaDiEADhyINTqAis aNDEi THE IS aeaDdINdSkSTEq SHE 
HASNEuEirEENhfAmEDyoo THE hyDIaqINHEiENTIiEmAiEEi
```
* `vHE`, `zv`, `cgx`를 각각 `SHE`, `IS`, `AND`로 치환한 후(글자마다 각각 적용) 각각 단어의 앞뒤에 공백을 삽입한다.
* `myNTINENTS`는 `CONTINENTS`, `INTEiNATIyNAf`은 `INTERNATIONAL`이 적합해 보인다.

```
sIqkaNA IS A SOaTHsOREA N oIdaRES sATER SHE IS THE OLkqhIC CHAqhION 
INLADIESSINdLES THE jORLD CHAqhION THE oOaR CONTINENTS CHAqhION 
ATHREETIqE dR AND hRItoINAL CHAqhION THE jORLD eaNIOR CHAqhION THE 
eaNIOR dR AND hRItoINAL CHAqhION AND AoOaRTIqE SOaTHsOREA NNATIONAL 
CHAqhION sIq IS THE oIRST SOaTHsOREA N oIdaRES sATER TOjIN AqEDALATAN IS 
aeaNIORORSENIORdR AND hRItEuENT IS a CHAqhION SHIh AND THE OLkqhIC dAqES 
SHE IS THE oIRST oEqALES sATER TOjIN THE OLkqhIC dAqES THE jORLD 
CHAqhION SHIhS THE oOaR CONTINENTS CHAqhION SHIhS AND THE dR AND 
hRItoINAL SHE IS ONEOo THE qOSTHIdHLkRECOdNIlEDATHLETES AND qEDIA 
oIdaRES IN SOaTHsOREA ASOoAhRILTH IS kEAR SHE IS RANsEDSECONDIN THE 
jORLD rk THE INTERNATIONALSsATINdaNION SHE IS THE 
CaRRENTRECORDHOLDERoORLADIESIN THE SHORThROdRAq THE oREESsATINd AND THE 
COqrINEDTOTAL aNDER THE IS aeaDdINdSkSTEq SHE IS ALSO THE oIRST oEqALES 
sATER TOSaRhASS THE TjOHaDREADhOINTqARs aNDER THE IS aeaDdINdSkSTEq SHE 
HASNEuERrEENhLACEDOoo THE hODIaqINHERENTIRECAREER
```
* `myNTINENTS`는 `CONTINENTS`, `INTEiNATIyNAf`은 `INTERNATIONAL`로 치환한 후(글자마다 각각 적용) 공백을 적절히 삽입한다.
* `SOaTHsOREA`, `OLkqhIC`, `CHAqhION`은 각각 `SOUTHKOREA`, `OLYMPIC`, `CHAMPION`이 적합해 보인다.

```
KIMYUNA IS A SOUTH KOREAN oIdURES KATER SHE IS THE OLYMPIC CHAMPION 
INLADIESSINdLES THE jORLD CHAMPION THE oOUR CONTINENTS CHAMPION 
ATHREETIME dR AND PRItoINAL CHAMPION THE jORLD eUNIOR CHAMPION THE 
eUNIOR dR AND PRItoINAL CHAMPION AND AoOURTIME SOUTH KOREAN NATIONAL 
CHAMPION KIM IS THE oIRST SOUTH KOREAN oIdURES KATER TOjIN AMEDALATAN 
IS UeUNIORORSENIORdR AND PRItEuENT IS U CHAMPION SHIP AND THE OLYMPIC 
dAMES SHE IS THE oIRST oEMALES KATER TOjIN THE OLYMPIC dAMES THE jORLD 
CHAMPION SHIPS THE oOUR CONTINENTS CHAMPION SHIPS AND THE dR AND 
PRItoINAL SHE IS ONEOo THE MOSTHIdHLYRECOdNIlEDATHLETES AND MEDIA 
oIdURES IN SOUTH KOREA ASOoAPRILTH IS YEAR SHE IS RANKEDSECONDIN THE 
jORLD rY THE INTERNATIONALSKATINdUNION SHE IS THE 
CURRENTRECORDHOLDERoORLADIESIN THE SHORTPROdRAM THE oREESKATINd AND THE 
COMrINEDTOTAL UNDER THE IS UeUDdINdSYSTEM SHE IS ALSO THE oIRST oEMALES 
KATER TOSURPASS THE TjOHUDREADPOINTMARK UNDER THE IS UeUDdINdSYSTEM SHE 
HASNEuERrEENPLACEDOoo THE PODIUMINHERENTIRECAREER
```
* `SOaTHsOREA`, `OLkqhIC`, `CHAqhION`은 각각 `SOUTHKOREA`, `OLYMPIC`, `CHAMPION`로 치환한 후(글자마다 각각 적용) 공백을 적절히 삽입/제거한다.
* 여기까지만 해도 대한민국의 피겨스케이팅 선수 김연아임을 알 수 있고, Auth도 김연아를 영어로 적어서 내면 통과한다.

|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|U|T|A|G|J|L|N|P|R|W|Y|Z|C|E|F|H|M|B|K|X|V|S|?|D|O|I|

```
Kim Yuna is A South Korean Figure Skater. 
She is The Olympic Champion In Ladies Singles, The World Champion, The Four Continents Champion A Three Time, Grand Prix Final Champion, The World Junior Champion, The Junior Grand Prix Final Champion And A Four Time South Korean National Champion. 
Kim is The First South Korean Figure Skater To Win A Medal At An ISU Junior Or Senior Grand Prix Event ISU Championship And The Olympic Games. 
She is The First Female Skater To Win The Olympic Games The World Championships The Four Continents Championships And The Grandprix Final. 
She is One Of The Most Highly Recognized Athletes And Media Figures In South Korea. 
As Of April This Year, She is Ranked Second In The World By The International Skating Union. 
She is The Current Record Holder For Ladies In The Short Program The Freeskating And The Combined Total Under The ISU Judging System. 
She is Also The First Female Skater To Surpass The Two Hudread Point Mark Under The ISU Judging System. 
She Has Never Been Placed Off The Podium In Her Entire Career.
```
* 치환 표와 최종적으로 다듬은 문장이다.