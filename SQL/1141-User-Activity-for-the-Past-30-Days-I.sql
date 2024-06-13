# Write your MySQL query statement below
/*
We subtracted 30 days from the date 2019-07-27, resulting in the new date 2019-06-28.
*/
select activity_date as day,
    count(distinct user_id) as active_users
from Activity
where activity_date between '2019-06-28' and '2019-07-27'
group by activity_date