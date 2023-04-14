-- 596. Classes More Than 5 Students

/*
Write an SQL query to report all the classes that have at least five students.
Return the result table in any order.
*/

-- 1044 ms, faster than 64.75%

SELECT
    C.class
FROM
    Courses C
GROUP BY
    C.class
Having
    COUNT(*) >= 5 