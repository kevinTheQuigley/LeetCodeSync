# Write your MySQL query statement below
SELECT B.product_name,A.year,A.price
FROM Sales AS A
LEFT JOIN Product AS B
ON A.product_id = B.product_id

