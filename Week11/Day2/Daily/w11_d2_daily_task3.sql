--Task 3: Calculate The Rolling Average Revenue For Each Genre
--Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. 
--Use window functions with the ROWS frame specification to achieve this.

--Ver1 
-- with movie_genre_names as (
-- 					select *
-- 					from movies.movie_genres mg left join movies.genre g using(genre_id)
-- ),
-- movie_by_revenue as (
-- 	select title, revenue,genre_name,rank() over (partition by genre_name order by release_date) as rank_by_realese
-- 	from movies.movie left join movie_genre_names using(movie_id)
-- )
-- select*, avg(revenue) over (partition by genre_name order by revenue ROWS BETWEEN 2 PRECEDING AND CURRENT) as rolling_avg
-- from movie_by_revenue; 

WITH movie_genre_names AS (
    SELECT 
        mg.movie_id,
        g.genre_name
    FROM 
        movies.movie_genres mg 
    LEFT JOIN 
        movies.genre g 
    USING (genre_id)
),
movie_by_release AS (
    SELECT 
        m.title, 
        m.revenue,
        mgn.genre_name,
        m.release_date,
        ROW_NUMBER() OVER (PARTITION BY mgn.genre_name ORDER BY m.release_date DESC) AS rank_by_release
    FROM 
        movies.movie m
    LEFT JOIN 
        movie_genre_names mgn 
    USING (movie_id)
)
SELECT
    title,
    revenue,
    genre_name,
    release_date,
    rank_by_release,
    AVG(revenue) OVER (PARTITION BY genre_name ORDER BY release_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg
FROM 
    movie_by_release
ORDER BY
    genre_name, 
    release_date DESC;
