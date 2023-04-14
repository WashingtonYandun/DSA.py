-- 181. Employees Earning More Than Their Managers

/*
Write an SQL query to find the employees who earn more than their managers.
Return the result table in any order.
The query result format is in the following example.
*/

-- 727 ms, faster than 25.93%

SELECT 
    E.name AS Employee
FROM
    Employee E 
JOIN
    Employee M ON E.managerId = M.id 
WHERE 
    E.salary > M.salary;