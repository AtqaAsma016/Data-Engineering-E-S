
-- INNER JOIN: Show order details with customer & product info
SELECT 
  o.order_id,
  c.customer_name,
  p.product_name,
  o.quantity,
  (o.quantity * p.price) AS total_price
FROM 
  orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;

-- LEFT JOIN: Customers with no orders
SELECT 
  c.customer_id,
  c.customer_name
FROM 
  customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- GROUP BY + SUM: Total revenue per product
SELECT 
  p.product_name,
  SUM(o.quantity * p.price) AS total_revenue
FROM 
  products p
JOIN orders o ON p.product_id = o.product_id
GROUP BY 
  p.product_id, p.product_name;

-- ORDER BY + LIMIT: Top 5 products by revenue
SELECT 
  p.product_name,
  SUM(o.quantity * p.price) AS total_revenue
FROM 
  products p
JOIN orders o ON p.product_id = o.product_id
GROUP BY 
  p.product_id, p.product_name
ORDER BY 
  total_revenue DESC
LIMIT 5;

-- WITH + Subquery: Orders with total > average order value
WITH order_totals AS (
  SELECT 
    o.order_id,
    SUM(p.price * o.quantity) AS total_value
  FROM 
    orders o
  JOIN products p ON o.product_id = p.product_id
  GROUP BY 
    o.order_id
)
SELECT 
  order_id,
  total_value
FROM 
  order_totals
WHERE 
  total_value > (SELECT AVG(total_value) FROM order_totals);

-- GROUP BY + CASE WHEN: Customer spending tiers
SELECT 
  c.customer_name,
  SUM(p.price * o.quantity) AS total_spent,
  CASE 
    WHEN SUM(p.price * o.quantity) < 500 THEN 'Low'
    WHEN SUM(p.price * o.quantity) BETWEEN 500 AND 2000 THEN 'Medium'
    ELSE 'High'
  END AS spending_tier
FROM 
  customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY 
  c.customer_id, c.customer_name;

-- HAVING Clause: Customers who spent more than 1500
SELECT 
  c.customer_name,
  SUM(p.price * o.quantity) AS total_spent
FROM 
  customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN products p ON o.product_id = p.product_id
GROUP BY 
  c.customer_id, c.customer_name
HAVING 
  SUM(p.price * o.quantity) > 1500;
