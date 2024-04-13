SELECT first_name, last_name 
FROM customers 
ORDER BY last_name DESC 
LIMIT 2;

DELETE FROM purchases 
WHERE customer_id = (
    SELECT customer_id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'
);


SELECT * FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott';

SELECT *
FROM purchases as p right JOIN customers as c ON p.customer_id = c.customer_id;


SELECT *
FROM purchases as p LEFT JOIN customers as c ON p.customer_id = c.customer_id;

