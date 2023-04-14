/* Write your T-SQL query statement below */

-- 727 ms, faster than 25.93%

SELECT 
    E.name AS Employee
FROM
    Employee E 
JOIN
    Employee M ON E.managerId = M.id 
WHERE 
    E.salary > M.salary;