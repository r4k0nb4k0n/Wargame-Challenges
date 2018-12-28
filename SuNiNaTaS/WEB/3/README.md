# 3

## Problem
```
Write articles in Notice Board!
```

## Inspection
* `http://suninatas.com/board/list.asp?divi=notice` `NOTICE` 게시판에는 글쓰기 버튼이 없다.
* `http://suninatas.com/board/list.asp?divi=Free` `Q&A` 게시판에는 글쓰기 버튼이 있다.
    - `<input type="button" class="btnWrite gray" value="WRITE" onclick="location.href='../board/write.asp?page=1&amp;divi=Free'">`
* `GET` 파라미터 `divi`로 게시판을 구분하는 것 같다.
* 위 버튼의 `location.href`의 내용에서 `Free`를 `notice`로 바꾼 뒤 클릭하면 `NOTICE` 게시판의 글을 쓸 수 있고, 등록하면 Auth 키가 뜬다.

## Solution
* `http://suninatas.com/board/write.asp?page=1&amp;divi=notice` 접속한다.
* 글을 쓴 후 등록하면 Auth 키가 뜬다.