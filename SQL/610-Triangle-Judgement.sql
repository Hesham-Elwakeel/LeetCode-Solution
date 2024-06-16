# Write your MySQL query statement below
/*
The rule to form a triangle is the sum of any two lines is greater than the third line.
*/
select *,
       case when x+y > z and x+z > y and y+z > x
            then 'Yes' else 'No' end as triangle
from Triangle