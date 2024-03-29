-- 595. Big Countries

/*
A country is big if:
it has an area of at least three million (i.e., 3000000 km2), or
it has a population of at least twenty-five million (i.e., 25000000).
Write an SQL query to report the name, population, and area of the big countries.
Return the result table in any order.
*/

SELECT
    W.name,
    W.population,
    W.area 
FROM
    World W
WHERE
    W.area >= 3000000
    OR W.population >= 25000000
