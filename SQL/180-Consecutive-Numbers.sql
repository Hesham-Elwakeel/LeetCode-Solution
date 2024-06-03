# Write your MySQL query statement below
SELECT DISTINCT a.Num AS ConsecutiveNums FROM Logs a
JOIN Logs b ON a.ID = b.ID +1 AND a.Num = b.Num
JOIN Logs c ON a.ID = c.ID +2 AND a.Num = c.Num