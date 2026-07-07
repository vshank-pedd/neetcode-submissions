-- Write your query below
select name as warehouse_name, sum(case when p.product_id = warehouse.product_id then width * length * height * units end) as volume
from warehouse
join products p on p.product_id = warehouse.product_id
group by warehouse.name