/*
Enter your query here.
*/
SELECT DISTINCT(CITY)
FROM STATION
WHERE LOWER(CITY) REGEXP "^[^aeiou]|[^aeiou]$";