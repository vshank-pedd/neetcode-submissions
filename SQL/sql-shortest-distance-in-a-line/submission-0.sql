-- Write your query below
select abs(min(next_x-x)) as shortest
from (
    select x, lead(x) over(order by x asc) as next_x
    from point
) t
