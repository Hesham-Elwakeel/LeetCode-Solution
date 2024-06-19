# Write your MySQL query statement below
select id,
       case when id%2=0 then lag(student,1) over (order by id) 
            when id%2<>0 then coalesce(lead(student,1) over (order by id), student) end as student
from Seat