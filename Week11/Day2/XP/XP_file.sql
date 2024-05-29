--Task 1: Rank Movies by Popularity within Each Genre

--Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, 
--and their rank based on popularity.

---Tables
-- select * 
-- from movies.movie_genres

-- select*
-- from movies.genre


with movie_genre_names as (
					select *
					from movies.movie_genres mg left join movies.genre g using(genre_id)
),
movie_by_popularity as(
select movie_id, title, genre_name,genre_id, rank() over (partition by genre_name order by popularity desc) as popularity_rank
from movies.movie m left join movie_genre_names mgn using(movie_id))
select *
from movie_by_popularity
where popularity_rank<=3;



--Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

--Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue.
--Display the company name, movie title, revenue, and quartile.

-- select movie_id,title,company_id, revenue,
-- 		NTILE(4) OVER (PARTITION BY company_id ORDER BY revenue desc) AS quartile
-- from movies.movie as m left join movies.movie_company as mc using(movie_id)


with company_info as (
select * 
from movies.movie_company left join movies.production_company using (company_id)
),
movie_by_revenue as (
	select title,company_name, revenue,
			NTILE(4) OVER (PARTITION BY company_id ORDER BY revenue desc) AS quartile,
			rank() over (PARTITION BY company_id ORDER BY revenue desc) AS revenue_rank
	from movies.movie as m left join company_info ci using(movie_id)
)
select*
from movie_by_revenue
where revenue_rank <= 3; 


--Task 3: Calculate the Running Total of Movie Budgets for Each Genre

--Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each
--genre. Display the genre name, movie title, budget, and running total budget.


with movie_genre_names as (
					select *
					from movies.movie_genres mg left join movies.genre g using(genre_id)
),
running_total as(
SELECT *,
       SUM(budget) OVER (partition by genre_name ORDER BY budget RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM movies.movie left join movie_genre_names using(movie_id))
select genre_name,title,budget, running_total
from running_total;

--Task 4: Identify the Most Recent Movie for Each Genre

--Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. -
--Display the genre name, movie title, and release date.


with movie_genre_names as (
					select *
					from movies.movie_genres mg left join movies.genre g using(genre_id)
),
movie_info as(
SELECT *, FIRST_VALUE(release_date) OVER (partition by genre_name ORDER BY release_date) AS first_release_date
FROM movies.movie left join movie_genre_names using(movie_id))
select genre_name,title,release_date
from movie_info
where release_date = first_release_date;


-- SELECT employee_id, first_name, last_name, salary,
--        FIRST_VALUE(salary) OVER (ORDER BY salary) AS first_salary
-- FROM employees;



----Excersise 2

--Task 1: Rank Actors by Their Appearance in Movies

--Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s-
--name and their rank.

with actors_personal_info as(
select person_id,movie_id,character_name,person_name
from movies.movie_cast left join movies.person using(person_id)),
numbers_of_appearance as(
select *
from actors_personal_info left join movies.movie  using(movie_id)
),
ranking_by_appearance as(
select person_id,person_name, count(distinct title) as number_of_appearance
from numbers_of_appearance
group by person_id,person_name
order by count(movie_id) desc)
select *, dense_rank() over (order by number_of_appearance desc) as rank_by_appearance
from ranking_by_appearance;


--Task 2: Identify the Top Director by Average Movie Rating

--Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director’s 
--name and their average rating.


with directors as (
select person_id, person_name, movie_id
from movies.movie_crew left join movies.person using (person_id)
where job = 'Director' 
),
max_movie_rating_by_director as (
select round(avg(vote_average),2) as avg_rating,person_name, rank() over (order by avg(vote_average) desc) as rank_by_rating
from movies.movie left join directors using(movie_id)
group by person_name
)
select *
from max_movie_rating_by_director
where rank_by_rating =1;



--Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

--Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. Display the actor’s name and 
--the cumulative revenue.







--Task 4: Identify the Director Whose Movies Have the Highest Total Budget

--Use a CTE and a window function to find the director whose movies have the highest total budget.
--Display the director’s name and the total budget.




