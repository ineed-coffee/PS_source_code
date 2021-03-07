SELECT CONTINENT,FLOOR(AVG(CITY.POPULATION))
FROM COUNTRY,CITY
WHERE COUNTRY.CODE=CITY.COUNTRYCODE
GROUP BY CONTINENT;

SELECT CONTINENT,FLOOR(AVG(CITY.POPULATION))
FROM COUNTRY
INNER JOIN CITY ON COUNTRY.CODE=CITY.COUNTRYCODE
GROUP BY CONTINENT;