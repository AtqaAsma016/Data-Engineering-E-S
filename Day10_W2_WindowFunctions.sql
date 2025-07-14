-- 1. Create the 'orders' table and inserting data
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    region VARCHAR(20),
    amount DECIMAL(10, 2)
);


INSERT INTO orders (order_id, customer_id, order_date, region, amount) VALUES
(1, 101, '2025-01-10', 'East', 500.00),
(2, 102, '2025-01-15', 'West', 600.00),
(3, 101, '2025-01-20', 'East', 700.00),
(4, 103, '2025-02-01', 'West', 400.00),
(5, 104, '2025-02-05', 'East', 1000.00),
(6, 101, '2025-02-10', 'East', 300.00),
(7, 102, '2025-02-12', 'West', 450.00),
(8, 103, '2025-03-01', 'West', 800.00),
(9, 104, '2025-03-02', 'East', 1200.00),
(10, 101, '2025-03-10', 'East', 400.00),
(11, 105, '2025-03-12', 'South', 900.00),
(12, 106, '2025-03-15', 'South', 1100.00),
(13, 105, '2025-04-01', 'South', 600.00),
(14, 106, '2025-04-03', 'South', 700.00),
(15, 101, '2025-04-05', 'East', 550.00);

-- TASK 1: Rank Customers by Monthly Spending

WITH monthly_spending AS (
    SELECT 
        customer_id,
        DATE_FORMAT(order_date, '%Y-%m') AS order_month,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id, DATE_FORMAT(order_date, '%Y-%m')
)

SELECT 
    customer_id,
    order_month,
    total_spent,
    RANK() OVER (
        PARTITION BY order_month
        ORDER BY total_spent DESC
    ) AS spending_rank
FROM monthly_spending
ORDER BY order_month, spending_rank;


-- Task 2: Get Previous Order Value for Each Customer (LAG)
SELECT 
    customer_id,
    order_id,
    order_date,
    amount,
    LAG(amount) OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS previous_order_amount
FROM orders
ORDER BY customer_id, order_date;



-- Task 3: Flag Top N Spenders Per Region Using NTILE
WITH region_spending AS (
    SELECT 
        customer_id,
        region,
        SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id, region
),

quartiles AS (
    SELECT 
        customer_id,
        region,
        total_spent,
        NTILE(4) OVER (
            PARTITION BY region 
            ORDER BY total_spent DESC
        ) AS quartile
    FROM region_spending
)

SELECT *
FROM quartiles
WHERE quartile = 1;
