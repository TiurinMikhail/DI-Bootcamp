-- 1. Get a list of all the languages, from the language table.
select*
from language;

-- 2. Get a list of all films joined with their languages – select the following details : film title, description, and language name.
select t1.title, t1.description, t2.name
from film as t1 left join language as t2 on t1.language_id = t2.language_id;

-- 3. Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
select t2.title, t2.description, t1.name
from  language as t1 left join film as t2 on t1.language_id = t2.language_id;

-- 4. Create a new table called new_film with the following columns : id, name. Add some new films to the table.
create table new_film(
film_id serial primary key,
film_name varchar(100)
);

insert into new_film(film_name)
VALUES ('Segun'),
       ('Thor 4'),
       ('The Dark Knight'),
       ('Pulp Fiction');	   

select*
from new_film;


--5.  Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.


create table customer_review(
review_id serial primary key,
film_id integer references new_film (film_id) ON DELETE CASCADE,
language_id int references language (language_id),
title varchar(200),
score int CHECK (score BETWEEN 1 AND 10),
review_text text,
last_update timestamp default CURRENT_TIMESTAMP
);



-- 6. Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review (film_id,language_id,title,score,review_text)
values((select film_id from new_film where film_name = 'Segun'),(select language_id from language where name = 'English'),'The game of throwns in Japan!',8,
'"Segun" is a captivating TV series that kept me on the edge of my seat from start to finish. The storyline is engaging, 
filled with unexpected twists and turns that leave you wanting more after each episode. The characters are well-developed, and the acting is top-notch, 
making it easy to become emotionally invested in their journeys. The production quality is impressive, with stunning cinematography and a memorable soundtrack
that enhances the viewing experience. Overall, "Segun" is a must-watch for anyone looking for a thrilling and immersive television experience. 
Highly recommended!');

insert into customer_review (film_id,language_id,title,score,review_text)
values((select film_id from new_film where film_name = 'Pulp Fiction'),(select language_id from language where name = 'English'),'Best movie ever!',10,
'Pulp Fiction is a masterpiece that stands the test of time. Directed by Quentin Tarantino, this film is a captivating journey through the criminal underworld,
filled with memorable characters and iconic scenes. One of the most striking aspects of "Pulp Fiction" is its non-linear narrative structure,
which keeps the audience engaged and constantly guessing. The film weaves together multiple storylines, all interconnected in unexpected ways,
creating a rich tapestry of crime, violence, humor, and redemption. The performances in "Pulp Fiction" are outstanding across the board. From John Travoltas 
charismatic turn as Vincent Vega to Uma Thurmans enigmatic portrayal of Mia Wallace, each actor brings their character to life with depth and nuance. 
The chemistry between the cast members is palpable, adding an extra layer of authenticity to the film.');


select *
from customer_review;



-- 7. Delete a film that has a review from the new_film table, what happens to the customer_review table?-- It will delete the review fro this film!
DELETE FROM new_film WHERE film_id = 1;


--Exercise 2 : DVD Rental--

--Use UPDATE to change the language of some films. Make sure that you use valid languages.--

update film
SET language_id = 2
WHERE film_id = 17;

select*
from film
where film_id = 17;

--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?--
--address_id and store_id are foreign keys for customer table. when we want to insert the new line in customer we need to find store_id in table
-- store because ids must be the same (customer.store_id=store.store_id). The same for address_id

--We created a new table called customer_review. Drop this table. Is this an easy step,
-- or does it need extra checking?
drop table customer_review;
-- there is no need to extra check, because it is a child table

--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
select count(*) as number_outstanding
from rental
where return_date is null;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select film.title, film.rental_rate
from film  join inventory on  film.film_id = inventory.film_id
           join rental on inventory.inventory_id = rental.inventory_id
where rental.return_date is null
order by rental_rate desc, title
fetch first 30 rows  only;


--Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies,
-- but he can’t remember their names. Can you help him find which movies he wants to rent?

--The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select *
from film as t1 left join film_actor as t2 on t1.film_id=t2.film_id
where t1.description ilike '%sumo wrestler%' and t2.actor_id
in (select actor_id from actor where first_name = 'Penelope' and last_name = 'Monroe');

--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select*
from film
where length < 60 and rating = 'R' and description ilike'%documentary%';

--The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental,
-- and he returned it between the 28th of July and the 1st of August, 2005.

select title
from film join inventory on film.film_id = inventory.film_id
          join rental on inventory.inventory_id = rental.inventory_id
          join customer on rental.customer_id = customer.customer_id
where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.rental_rate > 4.00
and rental.return_date between '28-07-2005' and '01-08-2005';

--The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title
-- or description, and it looked like it was a very expensive DVD to replace.
select
from film;

select title, description, replacement_cost
from film join inventory on film.film_id = inventory.film_id
          join rental on inventory.inventory_id = rental.inventory_id
          join customer on rental.customer_id = customer.customer_id
where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and (film.title ilike '%boat%' or film.description ilike '%boat%')
and film.replacement_cost > (select avg(replacement_cost) from film)
order by replacement_cost desc;

