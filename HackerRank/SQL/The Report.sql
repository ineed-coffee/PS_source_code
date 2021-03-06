/*
Enter your query here.
*/

SELECT T1.NAME,T1.GRADE,T1.MARKS
FROM (
        SELECT S.NAME,G.GRADE,S.MARKS
        FROM STUDENTS S, GRADES G
        WHERE S.MARKS >= G.MIN_MARK
        AND S.MARKS <= G.MAX_MARK
    ) T1
WHERE T1.GRADE>7
ORDER BY T1.GRADE DESC ,T1.NAME ASC;
SELECT "NULL",T2.GRADE,T2.MARKS
FROM (
        SELECT S.NAME,G.GRADE,S.MARKS
        FROM STUDENTS S, GRADES G
        WHERE S.MARKS >= G.MIN_MARK
        AND S.MARKS <= G.MAX_MARK
    ) T2
WHERE T2.GRADE<=7
ORDER BY T2.GRADE DESC ,T2.MARKS ASC;