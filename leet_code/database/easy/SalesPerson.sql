-- 607. Sales Person

/*
Write an SQL query to report the names of all the salespersons who did not have
any orders related to the company with the name "RED".
Return the result table in any order.
*/

-- 910 ms, faster than 83.45%

SELECT
    SP.name 
FROM
    SalesPerson SP
WHERE
    SP.sales_id NOT IN
        (
        SELECT
            O.sales_id -- get sales_id for gettign name
        FROM
            Orders O
        WHERE
            O.com_id = (SELECT C.com_id FROM Company C WHERE name = 'RED') -- get com_id of "RED" for getting sales_id
        );