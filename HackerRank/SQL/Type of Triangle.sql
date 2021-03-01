/*
Enter your query here.
*/
SELECT
    CASE
        WHEN 2*GREATEST(A,B,C)>=(A+B+C) THEN "Not A Triangle"
        WHEN A=B AND B=C THEN "Equilateral"
        WHEN A=B OR B=C OR C=A THEN "Isosceles"
        ELSE "Scalene"
    END AS TYPES
FROM TRIANGLES;