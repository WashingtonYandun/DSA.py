/* Write your T-SQL query statement below */

-- 600 ms, faster than 86.45%

SELECT
    email Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(id) > 1;