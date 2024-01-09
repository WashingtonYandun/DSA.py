-- 1581. Customer Who Visited but Did Not Make Any Transactions

/*
Write a SQL query to find the IDs of the users who visited without
making any transactions and the number of times they made these types of visits.
Return the result table sorted in any order.
*/

-- 1973 ms, faster than 89.98%

SELECT
    V.customer_id,
    COUNT(customer_id) count_no_trans
FROM
    Visits V
LEFT JOIN
    Transactions T On V.visit_id = T.visit_id
WHERE
    T.transaction_id IS NULL
GROUP BY
    V.customer_id;