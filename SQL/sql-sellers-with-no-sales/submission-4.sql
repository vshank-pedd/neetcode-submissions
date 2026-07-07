-- Write your query below
select seller_name
from seller s
left join orders o on s.seller_id = o.seller_id and extract(year from sale_date)=2020
where o.order_id is null
order by seller_name