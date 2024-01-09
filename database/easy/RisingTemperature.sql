-- 197. Rising Temperature

/*
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
*/

-- 760 ms, faster than 65.99%

SELECT
    W_act.id
FROM
    Weather W_act
JOIN
    Weather w_prev ON W_act.recordDate = DATEADD(day, 1, w_prev.recordDate)
WHERE
    W_act.temperature > w_prev.temperature;
