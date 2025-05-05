# Write your MySQL query statement below


WITH rank_salary AS 
(SELECT 
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) as dept_rank_salary
FROM 
    Employee e
    INNER JOIN 
    Department d on e.departmentId = d.id)


SELECT 
    Department,
    Employee,
    Salary
FROM    
    rank_salary
WHERE 
    dept_rank_salary<4