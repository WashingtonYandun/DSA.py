-- 196. Delete Duplicate Emails

/*
Write an SQL query to delete all the duplicate emails,
keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.
After running your script, the answer shown is the Person table.
The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.
*/

-- 823 ms, faster than 48.25%

DELETE FROM Person
WHERE
    id NOT IN (
    SELECT
        MIN(id) id
    FROM
        Person
    GROUP BY
        email
    )
