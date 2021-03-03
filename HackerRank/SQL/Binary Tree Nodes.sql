/*
Enter your query here.
*/
SELECT N,
    CASE
        WHEN P IS NULL THEN "Root"
        WHEN N NOT IN
            (SELECT DISTINCT(P) FROM BST WHERE P IS NOT NULL) THEN "Leaf"
        ELSE "Inner"
    END
FROM BST
ORDER BY N;


SELECT N,
    CASE
        WHEN P IS NULL THEN "Root"
        WHEN N IN (SELECT DISTINCT(P) FROM BST) THEN "Inner"
        ELSE "Leaf"
    END
FROM BST
ORDER BY N;