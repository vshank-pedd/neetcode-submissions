-- Write your query below
select s.name
from sales_person s
where s.sales_id not in (select o.sales_id from orders o left join company c on c.com_id = o.com_id group by o.sales_id, c.name having c.name = 'CRIMSON' )