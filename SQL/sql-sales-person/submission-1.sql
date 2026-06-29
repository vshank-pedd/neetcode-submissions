-- Write your query below
select distinct sales_person.name
from sales_person
left join  orders on sales_person.sales_id = orders.sales_id
where sales_person.sales_id not in (
    select orders.sales_id
    from orders
    where orders.com_id = 1
)
group by orders.com_id, sales_person.name 