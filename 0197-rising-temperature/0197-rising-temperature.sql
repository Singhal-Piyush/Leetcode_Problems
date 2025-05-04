# Write your MySQL query statement below

SELECT 
    id
FROM 
(SELECT 
    *,
    LAG(temperature,1) OVER (ORDER BY recordDate) as yesterday_temp,
    DATEDIFF(recordDate, LAG(recordDate) OVER(ORDER BY recordDate)) as diff_in_days
FROM 
    Weather ) as a
WHERE 
    yesterday_temp<temperature AND diff_in_days=1