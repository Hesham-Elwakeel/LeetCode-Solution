# Write your MySQL query statement below
WITH CumulativeWeights AS (
    SELECT 
        person_id,
        person_name,
        weight,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
)
SELECT  person_name
   
FROM  CumulativeWeights
   
WHERE  cumulative_weight <= 1000
   
ORDER BY cumulative_weight DESC
    
LIMIT 1;