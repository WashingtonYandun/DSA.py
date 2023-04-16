-- 1873. Calculate Special Bonus

/*
Write an SQL query to calculate the bonus of each employee.
The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee
name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
Return the result table ordered by employee_id.
*/

-- 1060 ms, faster than 67.13%

SELECT
    E.employee_id,
    CASE
        WHEN
            E.employee_id % 2 <> 0 AND
            E.name not like 'M%'
        THEN
            E.salary
        ELSE
            0
    END bonus 
FROM
    Employees E
ORDER BY
    employee_id ASC