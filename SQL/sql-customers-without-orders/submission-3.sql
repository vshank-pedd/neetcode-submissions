-- Write your query below
Select name
from customers
left join orders o on o.customer_id = customers.id
where o.id is null