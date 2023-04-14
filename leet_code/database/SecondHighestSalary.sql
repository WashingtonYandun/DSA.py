-- 176. Second Highest Salary

/*
Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary,
the query should report null.
*/

-- 727 ms, faster than 34.56%

SELECT
    MAX(E.salary) AS SecondHighestSalary
FROM 
    Employee E
WHERE
    E.salary < (SELECT MAX(E.salary) FROM Employee E)