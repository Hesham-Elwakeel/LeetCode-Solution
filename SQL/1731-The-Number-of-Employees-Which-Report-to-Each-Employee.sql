# Write your MySQL query statement below
select distinct manager.employee_id, 
                manager.name,
                count(emp.reports_to) as reports_count,
                round(avg(emp.age),0) as average_age
from Employees emp
join Employees manager
on emp.reports_to = manager.employee_id
group by employee_id
order by employee_id