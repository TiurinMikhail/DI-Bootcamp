--Task 4: Identify The Highest-Grossing Movie Series
--Identify the movie series (based on shared keywords) with the highest total revenue.
--Use window functions and CTEs to group movies by their series and calculate the total revenue.


--v1
-- WITH keywords AS (
--     SELECT 
-- 		movie_id, 
-- 		keyword_name
--     FROM 
--         movies.movie_keywords 
--     LEFT JOIN 
--         movies.keyword
--     USING (keyword_id)
-- ),
-- movie_revenue as (
--  	SELECT 
-- 		title,
-- 		revenue,
-- 		keyword_name
--     FROM 
--         movies.movie 
--     LEFT JOIN 
--         keywords
--     USING (movie_id)
-- )
-- select keyword_name,title,max(revenue)
-- from movie_revenue
-- where keyword_name is not null
-- group by 1,2
-- order by 3 desc,1;


--final_version

WITH keywords AS (
    SELECT 
        movie_id, 
        keyword_name
    FROM 
        movies.movie_keywords 
    LEFT JOIN 
        movies.keyword
    USING (keyword_id)
),
movie_revenue AS (
    SELECT 
        movie_id,
        title,
        revenue,
        keyword_name
    FROM 
        movies.movie 
    LEFT JOIN 
        keywords
    USING (movie_id)
),
series_revenue AS (
    SELECT 
        keyword_name,
        SUM(revenue) AS total_revenue
    FROM 
        movie_revenue
    WHERE 
        keyword_name IS NOT NULL
    GROUP BY 
        keyword_name
),
highest_grossing_series AS (
    SELECT 
        keyword_name,
        total_revenue,
        RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
    FROM 
        series_revenue
)
SELECT 
    keyword_name AS series_name,
    total_revenue
FROM 
    highest_grossing_series
WHERE 
    revenue_rank <= 5;


