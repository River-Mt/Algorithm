SELECT 
   (SELECT MEMBER_NAME FROM MEMBER_PROFILE WHERE r.MEMBER_ID = MEMBER_ID) MEMBER_NAME
 , REVIEW_TEXT
 , TO_CHAR(r.REVIEW_DATE, 'YYYY-MM-DD') REVIEW_DATE
FROM REST_REVIEW r
WHERE MEMBER_ID IN (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    HAVING COUNT(1) = (SELECT MAX(COUNT(1)) FROM REST_REVIEW GROUP BY MEMBER_ID)
)
ORDER BY 
   REVIEW_DATE
 , REVIEW_TEXT


