# 9

### First impression
```
1 2 3 
Password : 
```
* 숫자에 링크가 걸려있고, 다음과 같은 결과가 나타난다.
	- `?no=1` -> `Apple`
	- `?no=2` -> `Banana`
	- `?no=3` -> 
	```
	Secret
	
	hint : length = 11
	column : id,no
	```

### Trial and error
* `?no=3`의 결과에서 `column : id,no`를 고려하여, 다음과 같은 테이블을 생각해보았다.

| id     | no |
|:-------|:--:|
| Apple  | 1  |
| Banana | 2  |
| Secret | 3  |

* 다음과 같은 SQLi를 시도하였지만, 아무런 반응이 없었다.
	- `'%0aOR%0ano=3#`