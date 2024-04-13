CREATE TABLE users (
    user_id serial PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE items (
    item_id serial PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

CREATE TABLE product_orders (
    order_id serial PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE product_orders_items (
    order_id int,
    item_id INT,
    quantity INT,
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES product_orders(order_id),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);

CREATE FUNCTION calculate_total_price(order_id INT)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total DECIMAL(10, 2);
BEGIN
    SELECT SUM(items.price * product_orders_items.quantity)
    INTO total
    FROM product_orders_items
    INNER JOIN items ON product_orders_items.item_id = items.item_id
    WHERE product_orders_items.order_id = order_id;
    RETURN total;
END;
$$ LANGUAGE plpgsql;





