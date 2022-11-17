--
-- File generated with SQLiteStudio v3.3.3 on Wed May 25 10:23:07 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: orders
CREATE TABLE orders (orders_id INTEGER PRIMARY KEY, orders_time DATE, orders_fname TEXT);
INSERT INTO orders (orders_id, orders_time, orders_fname) VALUES (1, '2022-05-18', 'Jack');
INSERT INTO orders (orders_id, orders_time, orders_fname) VALUES (2, '2022-05-19', 'Haskins');
INSERT INTO orders (orders_id, orders_time, orders_fname) VALUES (3, '2022-05-20', 'Kenan');

-- Table: pizza
CREATE TABLE pizza (pizza_id INTEGER PRIMARY KEY, name TEXT, toppings TEXT, price NUMERIC, size TEXT);
INSERT INTO pizza (pizza_id, name, toppings, price, size) VALUES (1, 'Plain Cheese', NULL, 5, 'Medium');
INSERT INTO pizza (pizza_id, name, toppings, price, size) VALUES (2, 'Garlic', NULL, 5.5, 'Large');
INSERT INTO pizza (pizza_id, name, toppings, price, size) VALUES (3, 'Pepperoni', 'Pepperoni', 6, 'Small');
INSERT INTO pizza (pizza_id, name, toppings, price, size) VALUES (4, 'Hawaiian', 'Pineapple, Meat', 5.99, 'New York');
INSERT INTO pizza (pizza_id, name, toppings, price, size) VALUES (5, 'Meat Lovers', 'Meat, BBQ Sauce', 5.49, 'Mini');

-- Table: pizza_orders
CREATE TABLE pizza_orders (id INTEGER PRIMARY KEY, pizza_id INTEGER REFERENCES pizza (pizza_id), orders_id INTEGER REFERENCES orders (orders_id));
INSERT INTO pizza_orders (id, pizza_id, orders_id) VALUES (1, 5, 1);
INSERT INTO pizza_orders (id, pizza_id, orders_id) VALUES (2, 5, 1);
INSERT INTO pizza_orders (id, pizza_id, orders_id) VALUES (3, 5, 1);
INSERT INTO pizza_orders (id, pizza_id, orders_id) VALUES (4, 4, 2);
INSERT INTO pizza_orders (id, pizza_id, orders_id) VALUES (5, 5, 1);
INSERT INTO pizza_orders (id, pizza_id, orders_id) VALUES (6, 2, 3);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
