/*
Enter your query here.
*/
SET @R_IDX := -1;
SELECT ROUND(AVG(TMP.LAT_N),4)
FROM
   (SELECT @R_IDX:=@R_IDX + 1 row_, S.LAT_N LAT_N
    FROM STATION S
    ORDER BY S.LAT_N) TMP
WHERE TMP.row_ IN (FLOOR(@R_IDX / 2) , CEIL(@R_IDX / 2));