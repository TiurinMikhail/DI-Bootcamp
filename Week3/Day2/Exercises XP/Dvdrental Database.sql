-- We will use the newly installed dvdrental database.

-- In the dvdrental database write a query to select all the columns from the “customer” table.
select*
from customer;

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.

select (first_name, last_name) as full_name
from customer;

select first_name|| ' ' ||last_name as full_name
from customer;


-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
select distinct create_date
from customer;

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
select *
from customer
order by first_name desc;


-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

select film_id, title, description,release_year, rental_rate
from film
order by rental_rate asc;


-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
select t2.address,t2.phone
from customer as t1 left join address as t2 on t1.address_id = t2.address_id
where t2.district = 'Texas';


-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
select *
from film
where film_id in (15,150)
order by rental_rate asc;


-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, 
-- these details can be found in the “film” table.
select film_id, title, description, length, rental_rate
from film
where title = 'Lord of the rings';


-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all
-- the movies starting with the two first letters of your favorite movie.

select film_id, title, description, length, rental_rate
from film
where title = 'Lo%';

-- Write a query which will find the 10 cheapest movies.
select *
from film
order by rental_rate asc, title asc
limit 10;
--or
select *
from film
order by rental_rate asc, title asc
fetch first 10 rows only;


-- select *
-- from film
-- order by rental_rate asc
-- fetch first 20 rows only
-- ---
-- select *
-- from film
-- order by rental_rate asc
-- limit 20;
---

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
-- select *
-- from film
-- where title in (select title
-- from film
-- order by rental_rate asc
-- limit 20)
-- offset 10
;
--Bonus: Try to not use LIMIT. This one
select *
from film
order by rental_rate asc, title asc
offset 10
fetch first 10 rows only;

-- Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, 
-- as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select t1.customer_id,t1.first_name,t1.last_name , t2.amount, t2.payment_date
from customer as t1 inner join payment as t2 on t1.customer_id = t2.customer_id
order by customer_id asc;


-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
select t1.film_id,t1.title,t2.inventory_id
from film as t1 left join inventory as t2 on t1.film_id = t2.film_id
where t2.inventory_id is NULL;

-- Write a query to find which city is in which country.
select*
from city as t1 left join country as t2 on t1.country_id=t2.country_id
order by t1.city_id
---
select*
from country as t1 left join city as t2 on t1.country_id=t2.country_id
order by t1.country_id


-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment
-- ordered by the id of the staff member who sold them the dvd.
select t3.staff_id,t1.customer_id,t2.first_name,t2.last_name , t1.amount, t1.payment_date
from payment as t1 inner join customer as t2 on t1.customer_id = t2.customer_id
				   inner join staff as t3 on t1.staff_id=t3.staff_id
order by t3.staff_id asc;

---Bonus
select t3.staff_id, sum(t1.amount)
from payment as t1 inner join customer as t2 on t1.customer_id = t2.customer_id
				   inner join staff as t3 on t1.staff_id=t3.staff_id
group by t3.staff_id
order by t3.staff_id asc;


