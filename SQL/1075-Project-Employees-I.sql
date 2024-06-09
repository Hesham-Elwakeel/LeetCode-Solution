# Write your MySQL query statement below
Select Project_id, round(avg(experience_years),2) as average_years 
from Project a
left join Employee b
on a.employee_id = b.employee_id
group by project_id