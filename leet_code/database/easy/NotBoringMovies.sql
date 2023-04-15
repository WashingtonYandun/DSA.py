-- 620. Not Boring Movies

/*
Write an SQL query to report the movies with an odd-numbered ID and a description that is not "boring".
Return the result table ordered by rating in descending order.
*/

-- 321 ms, faster than 94.40%

SELECT
    *
FROM
    Cinema C
WHERE
    C.id % 2 <> 0 AND C.description <> 'Boring'
ORDER BY
    C.rating DESC