# 24

## Problem
```
http://suninatas.com/Part_one/web24/Suninatas24.zip
```

## Tool
* [`file`](https://linux.die.net/man/1/file)
* [`tree`]()https://linux.die.net/man/1/tree
* [jadx](https://github.com/skylot/jadx)

## Inspection and Solution
```
$ wget http://suninatas.com/Part_one/web24/Suninatas24.zip
--2019-01-18 00:16:42--  http://suninatas.com/Part_one/web24/Suninatas24.zip
Resolving suninatas.com (suninatas.com)... 222.122.213.219
접속 suninatas.com (suninatas.com)|222.122.213.219|:80... 접속됨.
HTTP request sent, awaiting response... 200 OK
Length: 166454 (163K) [application/x-zip-compressed]
Saving to: ‘Suninatas24.zip’

100%[===============================================================>] 166,454     --.-K/s   in 0.01s

2019-01-18 00:16:42 (13.2 MB/s) - ‘Suninatas24.zip’ saved [166454/166454]

$ unzip Suninatas24.zip
Archive:  Suninatas24.zip
  inflating: suninatas

$ file suninatas
suninatas: Java Jar file data (zip)

$ unzip suninatas -d suninatas.extracted
...

$ tree suninatas.extracted
suninatas.extracted
├── AndroidManifest.xml
├── META-INF
│   ├── CERT.RSA
│   ├── CERT.SF
│   └── MANIFEST.MF
├── classes.dex
├── res
│   ├── drawable-hdpi
│   │   ├── darkness.png
│   │   ├── ic_action_search.png
│   │   └── ic_launcher.png
│   ├── drawable-ldpi
│   │   ├── darkness.png
│   │   └── ic_launcher.png
│   ├── drawable-mdpi
│   │   ├── darkness.png
│   │   ├── ic_action_search.png
│   │   └── ic_launcher.png
│   ├── drawable-xhdpi
│   │   ├── darkness.png
│   │   ├── ic_action_search.png
│   │   └── ic_launcher.png
│   ├── layout
│   │   └── main.xml
│   └── menu
│       └── main.xml
└── resources.arsc

8 directories, 19 files
```
* `file` 명령어로 확인해보니 Java Jar 파일임을 알 수 있다. 
* 압축을 풀고 안을 들여다보니 Android apk를 빌드하기 전의 jar 파일인 것 같다.

![](./1.PNG?raw=true)
* jadx를 이용하여 `suninatas` 파일을 열어보았다.
* `suninatas.project->Suninatas->OnCreate(Bundle)`을 보면 다음 정보들을 알 수 있다.
	- `id`, `pw`, `key`를 입력하는 필드가 있다.
	- 만약 `key`가 `WE1C0mEToandr01d`와 같다면, `http://www.suninatas.com/Part_one/web24/chk_key.asp`에 파라미터로 `id`, `pw`, `key`를 넘긴다. 이를 브라우저에 연결되도록 해놨다.

![](./2.PNG?raw=true)
* 컴퓨터 브라우저로 해보니 되지 않는다.
* 분명 모바일이 아니면 Flag를 뱉지 않도록 짜놨을 것이다.

![](./3.PNG?raw=true)
* 이를 직접 `.apk`로 싸서 폰에 깔 환경도 시간도 안되기 때문에, Chrome browser의 Device mode로 모바일을 흉내내보았다.
* 플래그가 뜬다. 이를 Auth에 제출하면 통과한다.
