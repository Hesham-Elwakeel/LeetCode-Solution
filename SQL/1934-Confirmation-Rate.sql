# Write your MySQL query statement below

with cte as ( 
select a.user_id, b.action
from Signups a
left join Confirmations b
on a.user_id = b.user_id
)

select user_id, round(sum(case when action = 'confirmed' then 1 else 0 end)/count(*),2) confirmation_rate
from cte
group by user_id
order by confirmation_rate asc