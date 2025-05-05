# Write your MySQL query statement below

SELECT 
    d_s.Department as Department ,
    e.name as Employee,
    e.salary as Salary

FROM 
    (SELECT 
        d.id as department_id,
        d.name as Department,
        MAX(e.salary) as Salary
    FROM 
        Employee e
        INNER JOIN
        Department d ON e.departmentId = d.id
    GROUP BY d.name) AS d_s
    INNER JOIN
    employee e on d_s.department_id = e.departmentId
WHERE 
    e.salary = d_s.Salary