--Ex 3
CREATE TABLE purchases (
    id serial PRIMARY KEY,
    customer_id INT,
    item_id INT,
    quantity_purchased INT
);

--drop table purchases

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT customer_id FROM customers WHERE first_name = 'Scott' and last_name = 'Scott'),
    (SELECT item_id FROM items WHERE item_name = 'Fan'),
    1
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT customer_id FROM customers WHERE first_name = 'Melanie' and last_name = 'Johnson'),
    (SELECT item_id FROM items WHERE item_name = 'Large desk'),
    10
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT customer_id FROM customers WHERE first_name = 'Greg' and last_name = 'Jones'),
    (SELECT item_id FROM items WHERE item_name = 'Small Desk'),
    2
);


SELECT * FROM purchases;

SELECT p.*, c.first_name, c.last_name 
FROM purchases p JOIN customers c ON p.customer_id = c.customer_id;

SELECT * FROM purchases WHERE customer_id = 5;

SELECT * FROM purchases 
WHERE item_id IN (
    SELECT id FROM items WHERE item_name IN ('Large desk', 'Small Desk')
);


SELECT c.first_name, c.last_name, i.item_name 
FROM customers c
JOIN purchases p ON c.customer_id = p.customer_id
JOIN items i ON p.item_id = i.item_id;

---Adding a row that references a customer by ID but does not reference an item by ID won't work if the purchases table
--has a foreign key constraint that requires both customer_id and item_id to have valid references. 
--If such a constraint exists, the insertion will fail due to a foreign key constraint violation. If there's no such 
--constraint or it allows NULL values, the insertion will succeed but leave the item_id column blank for that row.