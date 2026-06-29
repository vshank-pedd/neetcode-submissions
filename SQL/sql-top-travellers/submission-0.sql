-- Write your query below
select users.name, coalesce(sum(rides.distance),0) as travelled_distance
from users
left join rides on rides.user_id = users.id
group by users.id, users.name 
order by travelled_distance desc, name asc