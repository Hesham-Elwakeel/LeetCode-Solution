The idea is to arrange people according to their turn in ascending, and then gradually add up their weights until we find a person who, 
if he or anyone after him ascends, will exceed the maximum weight.

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
