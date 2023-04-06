-- 코드를 입력하세요
SELECT B.title, B.board_id, R.reply_id, R.writer_id, R.contents, DATE_FORMAT(R.created_date, "%Y-%m-%d")
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R 
ON B.board_id = R.board_id
AND B.created_date like "2022-10%"
ORDER BY R.created_date, B.title;