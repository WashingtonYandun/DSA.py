/* Write your T-SQL query statement below */

-- 727 ms, faster than 34.56%

SELECT
    MAX(E.salary) AS SecondHighestSalary
FROM 
    Employee E
WHERE
    E.salary < (SELECT MAX(E.salary) FROM Employee E)