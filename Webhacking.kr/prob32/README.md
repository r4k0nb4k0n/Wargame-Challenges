# 32

### First impression
| RANK | NAME | HIT |
|:----:|:----:|:---:|
| .... | .... | ... |
| 731  | r4k4 | 0 / 100 |
| .... | .... | ... |

button Join

### Inspection
* 리스트 중 한 행을 클릭하면 `?hit=그 행의 ID`로 이동한다. 그리고, `no!`라는 창이 뜬다.
	- `?hit=r4k4`
* `Join` 버튼을 클릭하면 `?vote=add`로 이동하고, 내 아이디 `r4k4`가 추가된다.
* 쿠키에 `vote_check=ok` 값이 저장되어있다.

### Trial and error
* 쿠키의 `vote_check`를 삭제하고 `r4k4` 행을 클릭하니 HIT가 `1` 증가했고, 다시 `vote_check`가 생성되었다.
* HIT가 `100` 이상이면 통과하는 것 같다.

### Solution
* 먼저 `Join` 버튼을 클릭하여 자신의 ID를 목록에 추가한다.
* 쿠키에 `vote_check`가 없는 상태에서 `?hit=[자신의 ID]`를 `100`번 이상 접속하여 HIT를 `100` 이상으로 만들면 통과한다.
* [`vote.py`](./vote.py)