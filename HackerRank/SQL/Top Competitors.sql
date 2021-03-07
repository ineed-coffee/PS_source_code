/*
Enter your query here.
*/

SELECT H.HACKER_ID, H.NAME
FROM HACKERS H
LEFT JOIN
    (SELECT S.HACKER_ID HACKER_ID,
        SUM(CASE
            WHEN S.SCORE=CD.FULL_SCORE THEN 1
            ELSE 0
        END) FULLED
    FROM SUBMISSIONS S
    LEFT JOIN
        (SELECT C.CHALLENGE_ID CHALLENGE_ID,D.SCORE FULL_SCORE
        FROM CHALLENGES C
        LEFT JOIN DIFFICULTY D
        ON C.DIFFICULTY_LEVEL=D.DIFFICULTY_LEVEL)CD
    ON S.CHALLENGE_ID=CD.CHALLENGE_ID
    GROUP BY S.HACKER_ID)SCD
ON H.HACKER_ID=SCD.HACKER_ID
WHERE SCD.FULLED>1
ORDER BY SCD.FULLED DESC,H.HACKER_ID ASC;


--OPTIMIZED SOL

select h.hacker_id, h.name
FROM HACKERS H
INNER JOIN SUBMISSIONS S
ON H.HACKER_ID=S.HACKER_ID
inner join challenges c
on s.challenge_id = c.challenge_id
inner join difficulty d
on c.difficulty_level = d.difficulty_level 
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id,H.NAME
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id asc;