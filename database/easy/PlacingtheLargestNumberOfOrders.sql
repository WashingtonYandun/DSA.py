-- 586. Customer Placing the Largest Number of Orders

/*
Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.
*/

-- 1000 ms, faster than 0%

SELECT TOP 1
    O.customer_number
FROM
    Orders O
GROUP BY
    O.customer_number
ORDER BY
    COUNT(O.order_number)
DESC