-- Write your query below
Select seller_name
from seller
where seller_id not in (
    select seller_id
    from orders
    WHERE EXTRACT(YEAR FROM sale_date) = 2020
)
order by seller_name