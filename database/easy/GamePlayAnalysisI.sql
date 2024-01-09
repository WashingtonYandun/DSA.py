-- 511. Game Play Analysis I

/*
Write an SQL query to report the first login date for each player.
Return the result table in any order.
*/

-- 2364 ms, faster than 62.65%

SELECT
    A.player_id,
    MIN(A.event_date) first_login
FROM
    Activity A
GROUP BY
    A.player_id
