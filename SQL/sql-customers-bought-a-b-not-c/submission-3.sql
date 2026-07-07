-- Write your query below
Select c.customer_id, c.customer_name
from customers c
where c.customer_id in (select o.customer_id from orders o where product_name ='A') and c.customer_id in (select o.customer_id from orders o where product_name = 'B') and c.customer_id not in (select o.customer_id from orders o where product_name = 'C')
order by customer_name