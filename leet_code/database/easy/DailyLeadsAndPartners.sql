-- 1693. Daily Leads and Partners

/*
Write an SQL query that will, for each date_id and make_name,
return the number of distinct lead_id's and distinct partner_id's.
Return the result table in any order.
*/

-- 827 ms, faster than 50.65%

SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) as unique_leads,
    COUNT(DISTINCT partner_id) as unique_partners
FROM DailySales
GROUP BY
    date_id,
    make_name