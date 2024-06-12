
# Write your MySQL query statement below

with first_order as (
    select delivery_id,
        customer_id,
        min(order_date) as first_order_date,
        min(customer_pref_delivery_date) as customer_pref_delivery_date
    from Delivery
    group by customer_id
)

select round(100 * sum(case when first_order_date = customer_pref_delivery_date then 1 else 0 end) / count(delivery_id),2) as immediate_percentage
from first_order
