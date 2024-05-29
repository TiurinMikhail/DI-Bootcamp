--Task 2: Determine The Most Consistently High-Rated Actor
--Identify the actor who has appeared in the most movies that are rated above the average rating of all movies.
--Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

with avg_rating_all as( select avg(vote_average) as avg_rating_all
						from movies.movie	
),
relevant_movies as(
					select movie_id, title, vote_average, avg_rating_all
					from movies.movie cross join avg_rating_all
where vote_average > avg_rating_all),
actors_personal_info as(
					select person_id,movie_id, person_name
					from movies.movie_cast left join movies.person using(person_id)),
higth_rated_actor as(
					select person_name,count(distinct movie_id) as number_of_appearance
					from relevant_movies join actors_personal_info using(movie_id)
					group by person_id,person_name
					order by count(movie_id) desc)
select *, rank() over (ORDER BY number_of_appearance DESC) AS rank_by_appearance
from higth_rated_actor
limit 10;
