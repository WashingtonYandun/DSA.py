-- 584. Find Customer Referee

/*
Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.
*/

-- 759 ms, faster than 87%

SELECT
    C.name
FROM
    Customer C
Where
    C.referee_id <> 2 OR C.referee_id IS NULL