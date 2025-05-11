# Write your MySQL query statement below
SELECT 
    actor_id,
    director_id
FROM 
    (SELECT 
        actor_id,
        director_id,
        CONCAT(actor_id,",",director_id) AS pair
    FROM 
        ActorDirector) as a
GROUP BY a.pair
HAVING COUNT(a.pair)>2

