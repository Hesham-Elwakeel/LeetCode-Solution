select query_name,
       round(sum(rating/position) / count(query_name),2) as quality,
       round(100*sum(case when rating < 3 then 1 else 0 end) / count(query_name),2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name