-- 619. Biggest Single Number

/*
A single number is a number that appeared only once in the MyNumbers table.
Write an SQL query to report the largest single number. If there is no single number, report null.
*/

-- 454 ms, faster than 88.92%

SELECT
    MAX(num) num
FROM MyNumbers
where num in (
  SELECT
    num
  FROM
    MyNumbers
  GROUP BY
    num
  HAVING
    COUNT(*) = 1
) 