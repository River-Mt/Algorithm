-- 코드를 입력하세요
SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(BS.SALES * B.PRICE)
FROM AUTHOR A
JOIN BOOK B
    ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN BOOK_SALES BS
    ON BS.BOOK_ID = B.BOOK_ID
WHERE BS.SALES_DATE LIKE '2022-01%'
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY B.AUTHOR_ID, B.CATEGORY DESC

