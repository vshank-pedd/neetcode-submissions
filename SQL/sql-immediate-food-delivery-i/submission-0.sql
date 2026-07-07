select round(
  100 * sum(case when customer_pref_delivery_date = order_date then 1 else 0 end)::decimal
  / count(delivery_id)
, 2) as immediate_percentage
from delivery