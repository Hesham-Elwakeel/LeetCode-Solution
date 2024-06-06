# Write your MySQL query statement below

select name, bonus
from Employee E
left join Bonus B
on B.empid = E.empid
where bonus < 1000 or bonus is Null