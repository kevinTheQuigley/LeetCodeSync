# Write your MySQL query statement below
SELECT A.customer_id,COUNT(A.visit_id) AS count_no_trans
FROM Visits AS A
LEFT JOIN Transactions AS B
ON A.visit_id = B.visit_id
WHERE B.transaction_id IS null
GROUP BY A.customer_id

