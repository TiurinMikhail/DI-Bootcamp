
-- -- counting actors
-- select count(*) as actors_number
-- from actors

-- it will raise an error because we had an option (not null) in creating table actors!!

-- In the table actors, write the following commands:

-- Get the average number of oscars in the table
-- Get distinct actors depending on their number of oscars
-- Get the actors born after 01/01/1970
-- Get the actors which names are 'David', 'Morgan' or 'Will'

-- select avg(number_oscars) as avererage_oscars
-- from actors;

-- select  DISTINCT number_oscars, first_name, last_name
-- from actors;

-- select *
-- from actors
-- where birthdate > '01/01/1970';

-- select *
-- from actors
-- where first_name in ('David','Morgan','Will');
