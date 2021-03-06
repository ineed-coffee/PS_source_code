/*
Enter your query here.
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE LOWER(SUBSTR(CITY,1,1)) IN ("a","e","i","o","u");

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP "^[aeiou]";