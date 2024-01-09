-- 577. Employee Bonus

/*
Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
Return the result table in any order.
*/

-- 1174 ms, faster than 53.80%

SELECT
    E.name,
    B.bonus
FROM
    Bonus B
RIGHT JOIN
    Employee E ON B.empId = E.empId
WHERE
    B.bonus < 1000 OR B.bonus IS NULL;