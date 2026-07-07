-- Write your query below
Select name
from customers c
left join orders o on customer_id = c.id
where o.id is NULL