-- Write your query below
select first_name, last_name, city, state
from person p
left join address a on a.person_id = p.person_id;
