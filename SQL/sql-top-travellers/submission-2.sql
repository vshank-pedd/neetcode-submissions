-- Write your query below
select name, coalesce(sum(distance), 0) as travelled_distance
from users u
left join rides r on r.user_id = u.id
group by name
order by travelled_distance desc