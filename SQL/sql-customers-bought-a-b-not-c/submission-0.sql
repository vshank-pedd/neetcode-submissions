-- Write your query below
Select c.customer_id, c.customer_name
From customers c
Where customer_id in (Select customer_id from orders Where product_name = 'A') and customer_id in (Select customer_id from orders where product_name = 'B') and customer_id not in (Select customer_id from orders where product_name = 'C')
Order by customer_name