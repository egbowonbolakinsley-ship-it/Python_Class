
-- SQL ASSIGNMENT
E-COMMERCE ORDER MANAGEMENT
DATABASE: ecommerce_oct

QUESTION 1 — CREATE THE ORDERS TABLE

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    status VARCHAR(30),
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orders_users
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE RESTRICT
);

QUESTION 2 — CREATE THE ORDER_ITEMS TABLE

CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_order_items_orders
        FOREIGN KEY (order_id)
        REFERENCES orders(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_order_items_products
        FOREIGN KEY (product_id)
        REFERENCES product(id)
        ON DELETE RESTRICT
);

QUESTION 3 — INSERT SAMPLE RECORDS

At least 10 orders.
At least 15 order items.
At least three different order statuses.
Some orders containing multiple products.
Some customers placing more than one order.

INSERT INTO orders (user_id, status, order_date)
VALUES
(1, 'Pending',   '2026-10-01 09:00:00'),
(2, 'Processing','2026-10-02 10:30:00'),
(1, 'Delivered', '2026-10-03 11:15:00'),
(3, 'Pending',   '2026-10-04 12:00:00'),
(4, 'Delivered', '2026-10-05 13:45:00'),
(2, 'Cancelled', '2026-10-06 14:20:00'),
(5, 'Processing','2026-10-07 15:00:00'),
(1, 'Delivered', '2026-10-08 16:10:00'),
(3, 'Pending',   '2026-10-09 17:30:00'),
(4, 'Delivered', '2026-10-10 18:00:00');

QUESTION 4 — RETRIEVE ORDER INFORMATION

Customer's first name.
Customer's last name.
Email address.
Order status.
Order date.

SELECT
    users.firstname,
    users.lastname,
    users.email,
    orders.status,
    orders.order_date
FROM orders
INNER JOIN users
    ON orders.user_id = users.id;

QUESTION 5 - FILTER PENDING ORDERS 

SELECT *
FROM orders
WHERE status = 'Pending'
ORDER BY order_date DESC;


QUESTION 6 - RETRIEVE ORDER ITEMS

SELECT
    order_items.order_id,
    product.title AS product_title,
    order_items.quantity,
    order_items.price AS price_per_item,
    order_items.quantity * order_items.price AS subtotal
FROM order_items
INNER JOIN product
    ON order_items.product_id = product.id
ORDER BY order_items.order_id;

QUESTION 7 CALCULATE ORDER TOTALS

SELECT
    order_id,
    SUM(quantity * price) AS total_amount
FROM order_items
GROUP BY order_id
ORDER BY order_id;

QUESTION 8  COUNT ORDERS PER CUSTOMER 

SELECT
    CONCAT(users.firstname, ' ', users.lastname) AS full_name,
    COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
GROUP BY
    users.id,
    users.firstname,
    users.lastname
ORDER BY total_orders DESC;


QUESTION 9  FIND POPULAR PRODUCTS

SELECT
    product.title AS product_title,
    COALESCE(SUM(order_items.quantity), 0) AS total_quantity_ordered
FROM product
LEFT JOIN order_items
    ON product.id = order_items.product_id
GROUP BY
    product.id,
    product.title
ORDER BY total_quantity_ordered DESC;


QUESTION 10 CUSTOMER SPENDING REPORT

SELECT
    CONCAT(users.firstname, ' ', users.lastname) AS full_name,
    COALESCE(
        SUM(order_items.quantity * order_items.price),
        0
    ) AS total_amount_spent
FROM users
LEFT JOIN orders
    ON users.id = orders.user_id
    AND orders.status = 'Delivered'
LEFT JOIN order_items
    ON orders.id = order_items.order_id
GROUP BY
    users.id,
    users.firstname,
    users.lastname
ORDER BY total_amount_spent DESC;

