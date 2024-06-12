# Write your MySQL query statement below
with login as (
    select player_id,
        device_id,
        min(event_date) over (partition by player_id) as first_log,
        event_date,
        games_played
    from Activity
)

select round(sum(case when datediff(event_date,first_log) = 1 then 1 else 0 end)/
       count(distinct player_id),2) as fraction
from login
