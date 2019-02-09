# Advanced RCE Level 06

## Problem
* 남은 군생활은 몇일 인가 
* 정답인증은 MD5 해쉬값(대문자) 변환 후 인증하시오 

## Tool
* ExeinfoPe
* Exe2Aut

## Explanation
![](./1.PNG?raw=true)
* ExeinfoPe로 해당 PE 파일을 열어보았다.
* AutuIt Script로 만든 것임을 알 수 있다.

![](./2.PNG?raw=true)
* Exe2Aut로 해당 PE 파일을 열어보았다.
* `1`부터 `790`까지의 숫자를 확인창으로 반복해서 띄우는 것을 알 수 있다.