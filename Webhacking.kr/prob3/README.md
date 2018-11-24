# 3
### First impression
* [Nonogram](https://en.wikipedia.org/wiki/Nonogram)

### Trial and error
* 퍼즐을 풀고 이름까지 입력하면 풀었던 사람들의 이름과 정답, IP가 나열된다.
* 여러 탈출 문자들(`\`, `{` 등)울 입력했지만 오류를 일으키진 않는다.
* 한글을 입력하면 첫 글자만 제대로 뜨고 뒤에 `&#`이 붙는다.
* SQL Injection 구문도 통하지 않고 그대로 출력된다.
* 이름 칸 대신 숨겨진 폼 필드인 `answer`에 SQL Injection을 시도해본다.

### Solution
* 이름을 입력할 때 숨겨진 폼 필드인 `answer`의 맨 뒤에 `||TRUE`을 붙인 후 전송한다.
* 답이 나타난다.