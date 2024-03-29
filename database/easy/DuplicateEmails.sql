-- 196. Delete Duplicate Emails

/*
Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.
After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
The query result format is in the following example.
*/

-- 600 ms, faster than 86.45%

SELECT
    email Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(id) > 1;