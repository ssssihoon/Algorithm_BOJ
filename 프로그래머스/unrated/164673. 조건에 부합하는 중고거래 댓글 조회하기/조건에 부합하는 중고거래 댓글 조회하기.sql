-- 2022년 10월에 작성된 것을 기준? where? 댓글 작성일을 기준으로 오름차순 정렬, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순
-- 게시글 제목, 게시글ID, 댓글ID, 댓글작성자ID, 댓글 내용, 댓글 작성일 조회
SELECT 
B.TITLE, B.BOARD_ID, REPLY_ID, 
R.WRITER_ID, R.CONTENTS, date_format(R.CREATED_DATE, "%Y-%m-%d") as CREATED_DATE
from USED_GOODS_BOARD as B
join USED_GOODS_REPLY as R
on B.BOARD_ID = R.BOARD_ID
where MONTH(B.CREATED_DATE) = 10
order by R.CREATED_DATE asc,  B.TITLE asc;