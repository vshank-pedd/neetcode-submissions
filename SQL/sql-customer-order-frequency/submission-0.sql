-- Write your query below
select c.customer_id, c.name
from customers c
join orders o on o.customer_id = c.customer_id
join product p on p.product_id = o.product_id
where c.customer_id in (
    select c.customer_id
    from customers c
    join orders o on o.customer_id = c.customer_id
    join product p on p.product_id = o.product_id
    WHERE order_date >= '2020-06-01' AND order_date <= '2020-06-30'
    group by c.customer_id, c.name
    having sum(quantity*price)>=100
)
and c.customer_id in (
    select c.customer_id
    from customers c
    join orders o on o.customer_id = c.customer_id
    join product p on p.product_id = o.product_id
    WHERE order_date >= '2020-07-01' AND order_date <= '2020-07-31'
    group by c.customer_id, c.name
    having sum(quantity*price)>=100
)
group by c.customer_id, c.name