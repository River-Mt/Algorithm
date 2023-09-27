SET @HOUR := -1; # 변수선언

SELECT 
    (@HOUR := @HOUR +1) AS HOUR,
    (SELECT COUNT(*) 
     FROM ANIMAL_OUTS 
     WHERE HOUR(DATETIME) = @HOUR
    ) AS COUNT 
FROM ANIMAL_OUTS
WHERE @HOUR < 23