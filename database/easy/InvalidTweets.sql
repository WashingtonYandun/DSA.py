-- 1683. Invalid Tweets

/*
Write an SQL query to find the IDs of the invalid tweets. The tweet is invalid
if the number of characters used in the content of the tweet is strictly greater than 15.
*/

-- 1479 ms, faster than 74.71%

SELECT tweet_id
FROM Tweets
WHERE len(content) > 15
