/* Write your T-SQL query statement below */
 
-- 692 ms, faster than 70.52%

SELECT
    P.firstName,
    P.lastName,
    A.city,
    A.state
FROM Person P
LEFT JOIN Address A
ON P.personId = A.personId;