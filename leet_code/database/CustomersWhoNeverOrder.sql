-- 183. Customers Who Never Order

/*
Write an SQL query to report all customers who never order anything.
Return the result table in any order.
The query result format is in the following example.
*/

-- 600 ms, faster than 86.45%

SELECT
    C.name Customers
FROM 
    Customers C
LEFT JOIN
    Orders O ON C.id = O.customerId
where
    O.customerId is null