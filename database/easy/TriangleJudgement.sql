-- 610. Triangle Judgement

/*
Write an SQL query to report for every three line segments whether they can form a triangle.
Return the result table in any order.
*/

-- 382 ms, faster than 91.10%

SELECT
    *,
    CASE
        WHEN
            T.x + T.y <= T.z OR
            T.x + T.z <= T.y OR
            T.y + T.z <= T.x
        THEN
            'No'
        ELSE
            'Yes'
    END triangle 
FROM
    Triangle T