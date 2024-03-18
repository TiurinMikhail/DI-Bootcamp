-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
select*
from items 
order by item_price asc;
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
select*
from items 
where item_price >= 80
order by item_price asc;

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
select*
from customers
order by first_name asc
limit 3;

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select last_name 
from customers 
order by last_name desc;


