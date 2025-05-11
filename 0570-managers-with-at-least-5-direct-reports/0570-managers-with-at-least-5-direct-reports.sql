# Write your MySQL query statement below
SELECT 
    e.name as name
FROM 
    (SELECT 
        COUNT(id) as employee_count,
        managerId
    FROM 
        Employee
    GROUP BY managerId) AS a
    INNER JOIN 
    Employee e on a.managerId = e.id
WHERE a.employee_count>=5
