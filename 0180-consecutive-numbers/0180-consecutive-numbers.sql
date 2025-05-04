# Write your MySQL query statement below
SELECT 
 DISTINCT num as ConsecutiveNums
FROM 
(SELECT 
    *,
    LAG(num,1,0) OVER (ORDER BY id) AS pervious_1,
    LAG(num,2,0) OVER (ORDER BY id) AS pervious_2
FROM 
    Logs) as q

WHERE 
    num=pervious_1 AND num=pervious_2
