/* Problem 2 Store inventory and order system */

/* Drop existing tables to prevent errors, just in case */

    DROP TABLE IF EXISTS products;
    DROP TABLE IF EXISTS customers;
    DROP TABLE IF EXISTS orders;
    DROP TABLE IF EXISTS order_items;

/* products table */

    CREATE TABLE products (
	    id SERIAL PRIMARY KEY,
	    product_name VARCHAR(50),
	    price NUMERIC(10,2),
	    stock_quantity INT
    );

/* customers table */

    CREATE TABLE customers (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100)
    );

/* orders table */

    CREATE TABLE orders (
        id SERIAL PRIMARY KEY,
        customer_id INT REFERENCES customers(id),
        order_date DATE
    );

/* order items table */

    CREATE TABLE order_items (
        order_id INT REFERENCES orders(id),
        product_id INT REFERENCES products(id),
        quantity INT,
        PRIMARY KEY (order_id, product_id)
    );

/* Insert data */

    /* insert products */

        INSERT INTO products (product_name, price, stock_quantity)
        VALUES
        ('Laptop', 1200.00, 10),
        ('Smartphone', 800.00, 20),
        ('Headphones', 150.00, 50),
        ('Monitor', 300.00, 15),
        ('Keyboard', 75.00, 30);

    /* insert customers */

        INSERT INTO customers (first_name, last_name, email)
        VALUES
        ('Alice', 'Johnson', 'alice.johnson@gmail.com'),
        ('Bob', 'Smith', 'bsmith@outlook.com'),
        ('Charlie', 'Brown', 'charlieb@bing.com'),
        ('Diana', 'Prince', 'diana.prince@example.com');

    /* insert orders */

        INSERT INTO orders (customer_id, order_date)
        VALUES
        ((SELECT id FROM customers WHERE first_name = 'Alice' AND last_name = 'Johnson'), '2025-10-01'),
        ((SELECT id FROM customers WHERE first_name = 'Bob' AND last_name = 'Smith'), '2025-10-02'),
        ((SELECT id FROM customers WHERE first_name = 'Charlie' AND last_name = 'Brown'), '2025-10-03'),
        ((SELECT id FROM customers WHERE first_name = 'Diana' AND last_name = 'Prince'), '2025-10-04'),
        ((SELECT id FROM customers WHERE first_name = 'Alice' AND last_name = 'Johnson'), '2025-10-05');

    /* insert order items */

        /* Alice first order */

            INSERT INTO order_items (order_id, product_id, quantity)
            SELECT orders.id AS order_id, products.id AS product_id, items.quantity
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            CROSS JOIN (VALUES 
                ('Laptop', 1),
                ('Keyboard', 2)
            ) AS items(product_name, quantity)
            JOIN products ON products.product_name = items.product_name
            WHERE customers.first_name = 'Alice'
            AND customers.last_name = 'Johnson'
            AND orders.order_date = '2025-10-01';

        /* Bob's first order */

            INSERT INTO order_items (order_id, product_id, quantity)
            SELECT orders.id AS order_id, products.id AS product_id, items.quantity
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            CROSS JOIN (VALUES 
                ('Smartphone', 1),
                ('Headphones', 2)
            ) AS items(product_name, quantity)
            JOIN products ON products.product_name = items.product_name
            WHERE customers.first_name = 'Bob'
            AND customers.last_name = 'Smith'
            AND orders.order_date = '2025-10-02';

        /* Charlie's first order */

            INSERT INTO order_items (order_id, product_id, quantity)
            SELECT orders.id AS order_id, products.id AS product_id, items.quantity
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            CROSS JOIN (VALUES 
                ('Monitor', 1),
                ('Keyboard', 1)
            ) AS items(product_name, quantity)
            JOIN products ON products.product_name = items.product_name
            WHERE customers.first_name = 'Charlie'
            AND customers.last_name = 'Brown'
            AND orders.order_date = '2025-10-03';

        /* Diana's first order */

            INSERT INTO order_items (order_id, product_id, quantity)
            SELECT orders.id AS order_id, products.id AS product_id, items.quantity
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            CROSS JOIN (VALUES 
                ('Laptop', 1),
                ('Headphones', 1)
            ) AS items(product_name, quantity)
            JOIN products ON products.product_name = items.product_name
            WHERE customers.first_name = 'Diana'
            AND customers.last_name = 'Prince'
            AND orders.order_date = '2025-10-04';

        /* Alice second order */

            INSERT INTO order_items (order_id, product_id, quantity)
            SELECT orders.id AS order_id, products.id AS product_id, items.quantity
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            CROSS JOIN (VALUES 
                ('Monitor', 1),
                ('Smartphone', 1)
            ) AS items(product_name, quantity)
            JOIN products ON products.product_name = items.product_name
            WHERE customers.first_name = 'Alice'
            AND customers.last_name = 'Johnson'
            AND orders.order_date = '2025-10-05';

/* Queries */

    /* retrieve names and sock quantities */

        SELECT products.product_name, products.stock_quantity
        FROM products;

    /* retrieve product names and quantities for an order */

        SELECT products.product_name, order_items.quantity
        FROM order_items
        JOIN products ON order_items.product_id = products.id
        JOIN orders ON order_items.order_id = orders.id
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.first_name = 'Alice'
        AND customers.last_name = 'Johnson'
        AND orders.order_date = '2025-10-01';

    /* retrieve all orders */

        SELECT orders.id AS order_id, products.id AS product_id, products.product_name, order_items.quantity, orders.order_date
        FROM order_items
        JOIN orders ON order_items.order_id = orders.id
        JOIN products ON order_items.product_id = products.id
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.first_name = 'Alice'
        AND customers.last_name = 'Johnson';

/* update product data */

    UPDATE products
    SET stock_quantity = stock_quantity - sub.quantity
    FROM (
        SELECT products.id AS product_id, order_items.quantity
        FROM order_items
        JOIN products ON order_items.product_id = products.id
        JOIN orders ON order_items.order_id = orders.id
        JOIN customers ON orders.customer_id = customers.id
        WHERE customers.first_name = 'Bob'
        AND customers.last_name = 'Smith'
        AND orders.order_date = '2025-10-02'
    ) AS sub
    WHERE products.id = sub.product_id;

/* Delete data */

    /* delete order items */

        DELETE FROM order_items
        WHERE order_id = (
            SELECT orders.id
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            WHERE customers.first_name = 'Alice'
            AND customers.last_name = 'Johnson'
            AND orders.order_date = '2025-10-05'
        );

    /* delete order itself */

        DELETE FROM orders
        WHERE customer_id = (
            SELECT id FROM customers WHERE first_name = 'Alice' AND last_name = 'Johnson'
        )
        AND order_date = '2025-10-05';