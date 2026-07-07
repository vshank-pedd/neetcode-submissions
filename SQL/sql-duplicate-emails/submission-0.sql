-- Write your query below
select email
from person
where email in (
    select email
    from person
    group by email
    having count(id)>1
    order by count(id)
)
group by email